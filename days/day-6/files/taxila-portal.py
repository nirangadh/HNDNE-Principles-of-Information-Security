#!/usr/bin/env python3
"""taxila-portal: the practice application for the Day 6 lab.

This is the Day 6 extension of the portal you first ran on Day 4. It has two
pages a defender studies today: a login page and a page that echoes a note back
to the visitor. Each page is written in two ways, a flawed way and a safe way,
and you choose which one is used by editing one marked line near the top of this
file. A built-in test then tells you whether the flaw is open or closed.

The test seeds a practice record from your index number, so your result is your
own. Everything runs on this machine, against a small practice table held in
memory only; nothing is sent anywhere, and no real record exists here.

You are the defender. The test uses a prepared, harmless probe to show whether a
page is safe. It reports only what a defender sees, the number of records a login
returned and whether a note changed the page. It never shows a ready-made attack
string, and you never type one.

Run the test, with your own index number:

    python3 taxila-portal.py --test --index COHNDNE999X000

Read the report. Then fix a flaw by editing its marked line below, save the file,
and run the test again to prove the flaw is closed.
"""
import argparse
import html
import re
import sqlite3
import sys

# ----------------------------------------------------------------------------
# THE TWO LINES YOU EDIT IN THE LAB.
# Each starts False, which means the flawed way is used. The lab asks you to
# find the flawed line (further down), understand it, then switch its page to
# the safe way by setting the matching line here to True. Break it again by
# setting it back to False.
# ----------------------------------------------------------------------------
SAFE_LOGIN = False   # segment 2: set to True once you have applied the parameterised query
SAFE_ECHO = False    # segment 3: set to True once you have applied output encoding


# ----------------------------------------------------------------------------
# The practice records, seeded from an index number. Five fixed practice
# students, plus one seeded for the index you enter, so the table holds six.
# ----------------------------------------------------------------------------
FIRST = ["Nimali", "Rukshan", "Tharindu", "Ishara", "Dilani", "Kavinda",
         "Sanduni", "Pasan", "Hiruni", "Chathura", "Amaya", "Senuri",
         "Thilina", "Oshadi", "Ravindu", "Nethmi"]
LAST = ["Perera", "Fernando", "Jayasuriya", "Bandara", "Wickramasinghe",
        "Gunawardena", "Ratnayake", "Senaratne", "Dissanayake",
        "Weerasinghe", "Herath", "Ekanayake", "Samarasinghe", "Abeywardena"]

FIXED_STUDENTS = [
    ("student01", "Chamodi Rajapaksa", "TC2001"),
    ("student02", "Lahiru Mendis", "TC2002"),
    ("student03", "Dinithi Silva", "TC2003"),
    ("student04", "Yasiru Cooray", "TC2004"),
    ("student05", "Methmi Gamage", "TC2005"),
]


def clean_index(raw):
    """Capitals, with spaces and hyphens removed, as the lab sheet asks."""
    return re.sub(r"[^A-Za-z0-9]", "", raw or "").upper()


def fnv1a(text):
    """A small, plain hash used only to seed a practice record from an index. It is
    not for security; it is here so the portal, the demos and the marking tool all
    compute the same record for the same index, in Python and in the browser alike."""
    h = 0x811c9dc5
    for b in text.encode("utf-8"):
        h ^= b
        h = (h * 0x01000193) & 0xFFFFFFFF
    return h


def seed_record(index):
    """The practice record seeded for an index: its name and its identifier.
    The same recipe is used by the demos and by the lecturer's marking tool, so
    everyone computes the same record for the same index."""
    h = fnv1a(clean_index(index))
    name = FIRST[h % len(FIRST)] + " " + LAST[(h // len(FIRST)) % len(LAST)]
    sid = "TC" + str(1000 + (h // (len(FIRST) * len(LAST))) % 9000)
    return sid, name


def practice_table(index):
    """A fresh in-memory table of six students: five fixed, plus the seeded one.
    The seeded student's username is the index you enter; its password is fixed
    for the practice, so a normal login can be shown to still work."""
    ix = clean_index(index)
    sid, name = seed_record(index)
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE students (username TEXT, name TEXT, student_id TEXT, password TEXT)")
    rows = [(u, n, i, "practice-password") for (u, n, i) in FIXED_STUDENTS]
    rows.append((ix, name, sid, "practice-password"))
    con.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", rows)
    con.commit()
    return con


# ----------------------------------------------------------------------------
# PAGE 1: THE LOGIN. Find the flawed line in flawed_login().
# ----------------------------------------------------------------------------
def flawed_login(con, username, password):
    """The flawed way. The line marked below joins the username and password
    straight into the query text, so whatever arrives is read as part of the
    command, not only as data. This is the line you find in segment 1."""
    cur = con.cursor()
    # >>> THE FLAWED LINE <<<  input is joined into the query, so input becomes command.
    query = ("SELECT name, student_id FROM students "
             "WHERE username = '" + username + "' AND password = '" + password + "'")
    return cur.execute(query).fetchall()


def safe_login(con, username, password):
    """The safe way. The query holds two placeholders, and the username and
    password are passed beside it as data, so neither can become command. This
    is the fix you apply in segment 2 by setting SAFE_LOGIN to True."""
    cur = con.cursor()
    query = "SELECT name, student_id FROM students WHERE username = ? AND password = ?"
    return cur.execute(query, (username, password)).fetchall()


def login(con, username, password):
    return safe_login(con, username, password) if SAFE_LOGIN else flawed_login(con, username, password)


# ----------------------------------------------------------------------------
# PAGE 2: THE NOTE ECHO. Find the flawed line in flawed_echo().
# ----------------------------------------------------------------------------
def flawed_echo(note):
    """The flawed way. The visitor's note is placed into the page exactly as it
    arrived, so markup in the note is read by the browser as part of the page.
    This is the line you find in segment 3."""
    # >>> THE FLAWED LINE <<<  the note is put into the page without being encoded.
    return "<p>Your note: " + note + "</p>"


def safe_echo(note):
    """The safe way. The note is encoded first, so every character is shown as
    plain text and none of it is read as markup. This is the fix you apply by
    setting SAFE_ECHO to True."""
    return "<p>Your note: " + html.escape(note) + "</p>"


def echo(note):
    return safe_echo(note) if SAFE_ECHO else flawed_echo(note)


# ----------------------------------------------------------------------------
# THE PROVIDED TEST. It builds a prepared probe from parts, so this file holds
# no ready-made attack string, and reports only the effect a defender sees.
# ----------------------------------------------------------------------------
def login_probe():
    """A prepared login value that, joined into the flawed query, would match
    every row instead of one. It is built from parts here, and never printed, so
    the file carries no ready-to-use attack string. A defender reads the effect
    below, not this value."""
    q = "'"
    always_true = " OR " + q + "1" + q + " = " + q + "1" + q
    return q + always_true + " -- ", q + always_true + " -- "


def note_probe():
    """A prepared, harmless note that is only bold text. If a page places it
    without encoding, the words show in bold, which proves the page read the
    note as markup. Nothing runs; it is display only."""
    return "<b>this note is bold</b>"


def run_test(index):
    sid, name = seed_record(index)
    con = practice_table(index)
    print("Practice record seeded for " + clean_index(index) + ":")
    print("    name " + name + ", identifier " + sid)
    print("    the table holds 6 students in all")
    print("")

    # Login test.
    u, p = login_probe()
    returned = login(con, u, p)
    normal = login(con, clean_index(index), "practice-password")
    way = "safe (parameterised query)" if SAFE_LOGIN else "flawed (query built by joining text)"
    print("Login page: " + way)
    print("    the prepared login probe returned " + str(len(returned)) + " of 6 records")
    print("    a normal sign-in returned " + str(len(normal)) + " record")
    if len(returned) > 1:
        print("    RESULT: OPEN. The probe read past one record and returned every row,")
        print("            including " + sid + " " + name + ". The login is injectable.")
    else:
        print("    RESULT: CLOSED. The probe matched no record, and a normal sign-in still works.")
    print("")

    # Echo test.
    out = echo(note_probe())
    changed = "<b>" in out  # the raw tag survived, so the browser would read it as markup
    way = "safe (output encoded)" if SAFE_ECHO else "flawed (note placed as it arrived)"
    print("Note page: " + way)
    print("    the page the browser would receive is:")
    print("    " + out)
    if changed:
        print("    RESULT: OPEN. The note's markup reached the page, so the browser would")
        print("            read it as part of the page, not as plain text.")
    else:
        print("    RESULT: CLOSED. The note is shown as plain text, with your index, and")
        print("            none of it is read as markup.")
    con.close()


def main():
    ap = argparse.ArgumentParser(description="Practice portal for the Day 6 lab (runs on this machine only).")
    ap.add_argument("--test", action="store_true", help="run the provided login and note tests and print the report")
    ap.add_argument("--index", help="your index number, which seeds your practice record")
    a = ap.parse_args()
    if not a.test:
        print("Run the provided test with your index number:")
        print("    python3 taxila-portal.py --test --index COHNDNE999X000")
        return 0
    if not a.index:
        sys.exit("The test needs your index number: --index YOURINDEX")
    run_test(a.index)
    return 0


if __name__ == "__main__":
    main()
