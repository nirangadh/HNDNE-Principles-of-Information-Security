#!/usr/bin/env python3
"""Day 5 lab: give your own Kali virtual machine a weak baseline, keyed to your index number.

Run it only on your own Kali virtual machine, after you have taken the day-5-start snapshot.
It weakens that machine on purpose, so that you can find and fix the weaknesses with the
morning's hardening steps. It never touches another computer and never uses the network.

    sudo python3 seed-baseline.py COHNDNE999X000            make the baseline and print your report
    sudo python3 seed-baseline.py --check COHNDNE999X000    say which of your findings are still open
    sudo python3 seed-baseline.py --undo COHNDNE999X000     put everything right, if you have no snapshot

Use your own index number: letters and digits only, in capitals, exactly as issued.
The portal's hardening-checklist demo builds the same report from the same index number.
"""
import argparse
import hashlib
import os
import pathlib
import pwd
import re
import subprocess
import sys

# One service from this list is started and enabled. Kali installs all three and leaves them off.
SERVICES = [
    ("ssh", 22, "remote sign-in"),
    ("apache2", 80, "web server"),
    ("mariadb", 3306, "database server"),
]
# One file from this list is made writable by every account. The safe mode is the one Lynis expects.
FILES = [
    ("/etc/passwd", "644", "the list of accounts"),
    ("/etc/group", "644", "the list of groups"),
    ("/etc/crontab", "600", "the system's scheduled jobs"),
    ("/etc/ssh/sshd_config", "600", "the remote sign-in settings"),
]
WEAK_MODE = "666"
JOURNAL_DROPIN = pathlib.Path("/etc/systemd/journald.conf.d/50-day5-baseline.conf")
JOURNAL_TEXT = "# Day 5 lab baseline: the journal keeps nothing.\n[Journal]\nStorage=none\n"


def values(index):
    """The personal values: the same recipe as the portal's report and the lecturer's tool."""
    d = hashlib.sha256(index.encode("ascii")).digest()
    service, port, what = SERVICES[d[0] % len(SERVICES)]
    path, mode, fwhat = FILES[d[1] % len(FILES)]
    account = "lec" + d.hex()[-4:]
    return {"service": service, "port": port, "service_what": what,
            "file": path, "mode": mode, "file_what": fwhat, "account": account}


def run(*cmd):
    return subprocess.run(list(cmd), capture_output=True, text=True)


def mode_of(path):
    return oct(os.stat(path).st_mode & 0o777)[2:]


def account_exists(name):
    try:
        pwd.getpwnam(name)
        return True
    except KeyError:
        return False


def report(index, v):
    print(f"Baseline report for {index}")
    print("")
    print(f"F1  Services and open ports: {v['service']} ({v['service_what']}) is running, starts at every boot,")
    print(f"    and listens on port {v['port']}. Nobody at Taxila needs it on this server.")
    print(f"F2  File permissions: {v['file']} ({v['file_what']}) has mode {WEAK_MODE}, so every account can change it.")
    print(f"    The safe mode is {v['mode']}.")
    print("F3  Logging: the journal is set to Storage=none, so nothing that happens is recorded.")
    print("F4  Patching: some packages may have updates waiting. Read them; you do not install them today.")
    print(f"F5  Users and groups: the account {v['account']} is the lecturer account for your role table.")
    print("")
    print("Fix F1, F2 and F3. Then run this script again with --check.")


def seed(index, v):
    unit = run("systemctl", "cat", v["service"])
    if unit.returncode != 0:
        print(f"The {v['service']} service is not installed on this machine. Tell your lecturer;")
        print("the portal's report gives you the same findings, so you can carry on at the floor tier.")
        return 1
    run("systemctl", "enable", "--now", v["service"])
    os.chmod(v["file"], int(WEAK_MODE, 8))
    JOURNAL_DROPIN.parent.mkdir(parents=True, exist_ok=True)
    JOURNAL_DROPIN.write_text(JOURNAL_TEXT)
    run("systemctl", "restart", "systemd-journald")
    if not account_exists(v["account"]):
        run("useradd", "--no-create-home", "--shell", "/usr/sbin/nologin",
            "--comment", "Taxila lecturer account, Day 5 role table", v["account"])
    report(index, v)
    return 0


def check(index, v):
    enabled = run("systemctl", "is-enabled", v["service"]).stdout.strip()
    active = run("systemctl", "is-active", v["service"]).stdout.strip()
    rows = [
        ("F1", f"{v['service']} is {enabled or 'unknown'} and {active or 'unknown'}",
         enabled != "enabled" and active != "active"),
        ("F2", f"{v['file']} has mode {mode_of(v['file'])}, safe mode {v['mode']}",
         mode_of(v["file"]) == v["mode"]),
        ("F3", "the journal setting Storage=none is " + ("still there" if JOURNAL_DROPIN.exists() else "gone"),
         not JOURNAL_DROPIN.exists()),
    ]
    print(f"Check for {index}")
    for fid, text, fixed in rows:
        print(f"{fid}  {'FIXED' if fixed else 'OPEN '}  {text}")
    print(f"F5  the account {v['account']} " + ("exists" if account_exists(v["account"]) else "does not exist"))
    return 0 if all(r[2] for r in rows) else 2


def undo(index, v):
    run("systemctl", "disable", "--now", v["service"])
    os.chmod(v["file"], int(v["mode"], 8))
    if JOURNAL_DROPIN.exists():
        JOURNAL_DROPIN.unlink()
    run("systemctl", "restart", "systemd-journald")
    if account_exists(v["account"]):
        run("userdel", v["account"])
    print(f"Baseline removed for {index}.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Day 5 lab baseline for your own Kali virtual machine.")
    ap.add_argument("index", help="your index number, letters and digits only, in capitals")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true", help="say which findings are still open")
    g.add_argument("--undo", action="store_true", help="put the machine back")
    a = ap.parse_args()
    index = a.index.strip()
    if not re.fullmatch(r"[A-Z0-9]{4,32}", index):
        sys.exit("Write your index number in capitals, letters and digits only, with no spaces or hyphens.")
    if os.geteuid() != 0:
        sys.exit("Run it with sudo: sudo python3 seed-baseline.py " + index)
    osr = pathlib.Path("/etc/os-release")
    if not osr.exists() or not re.search(r"^ID=kali$", osr.read_text(), re.M):
        sys.exit("This script runs only on the module's Kali virtual machine.")
    v = values(index)
    if a.check:
        return check(index, v)
    if a.undo:
        return undo(index, v)
    return seed(index, v)


if __name__ == "__main__":
    sys.exit(main())
