# Lab 5: Audit a baseline, fix your findings, and design least-privilege roles

**Day 5, afternoon session. Duration 3 hours. Adds items 9 and 10 to Taxila's security register.**

This lab sheet takes you from a weak server baseline, keyed to your index number, to a hardened one. Then you design a role table for the Student Information System (SIS). You will see your own findings clear one by one, and you will see what goes wrong when one role is given too much.

| | |
|---|---|
| Learning outcomes | LO4 |
| You need | this morning's ideas: [least privilege](../../glossary.md#least-privilege) is the minimum access an account needs; [accounting](../../glossary.md#accounting) is the record of what was done; [hardening](../../glossary.md#hardening) turns off what nobody needs |
| Tiers | Floor tier: every step, in the browser. Full tier: segments 1 and 2 can also run on your Kali virtual machine; segment 3 is a design task on any laptop |
| Evidence pack | Pack 5, due before the next teaching day |

## Before you start

1. Open this page and the day's notes side by side.
2. Write down your personal value: your index number without spaces or hyphens, with its letters in capitals exactly as issued (the example in this sheet, `COHNDNE999X000`, belongs to nobody).
3. Full tier: start your Kali virtual machine and take a snapshot named `day-5-start`, so Reset can bring it back. Take it before you run anything else today.
4. Floor tier: open the demos this lab uses: `hardening-checklist` (its "Your baseline report" panel) and `access-models`.
5. Download the provided files and save them in your module folder: [`seed-baseline.py`](files/seed-baseline.py) (full tier only) and [`role-table.csv`](files/role-table.csv) (both tiers).

### The idea behind today's lab

> **Recall.** Least privilege is the minimum access an account needs.

> **Recall.** Accounting is the record of what was done.

A baseline is the agreed starting state of a server: which accounts exist, which services run, which files each account may change, and what is recorded. An audit compares the server with a good baseline and lists the differences as findings. Today your own server starts weak on purpose. The weaknesses are chosen from your index number, so your findings differ from your neighbour's.

![A server before and after hardening. Before: three running services with open ports, a file every account can change, and a log that records nothing. After: only the needed service runs, the file is closed to other accounts, and the log records every action.](img/attack-surface.svg "Hardening shrinks the attack surface: fewer open doors, tighter files, and a log that records")

> **Common mistake.** "Turning on logging fixes a weakness." Logging detects; it does not prevent. A log that records every grade change does not stop a change. It lets the college see who made it, and when. You still need roles and permissions to stop the change in the first place.

> **Common mistake.** "A role is just a group of users." A role is a set of permissions that users are assigned to. You design the permissions first, from the job. Then you put people into the role. If a person changes job, you move them to another role; you do not edit the permissions.

> **Quick check.** Your report says that `/etc/group` has mode `666`. Which of these is the real risk?
>
> - [ ] Anyone can read the list of groups
> - [x] Any account can add itself to a group, including the administrators' group
> - [ ] The file will be deleted at the next restart
>
> **Why:** The last `6` gives every account read and write. Reading the list of groups is normal and harmless, which is why `644` is the safe mode. Writing it lets an ordinary account make itself an administrator.

> **Quick check.** After your fixes, the Head of IT (information technology) asks: "Logging is on now, so is the grade problem solved?" What is the best answer?
>
> - [ ] Yes: nobody can change a grade once it is logged
> - [ ] No: logging only matters on the web portal, not on the server
> - [x] Partly: the log now shows who changed a grade, but roles must still stop the wrong person changing it
>
> **Why:** Logging is accounting. It detects and records, so the college can hold a named person to account. It does not prevent the change. Prevention is the job of authorisation: roles, permissions and a second approver.

## Objective

You will show that each finding keyed to your index is fixed, with the command or setting that fixed it. Your server then runs only what it needs and records what happens. You will also design SIS roles where neither the lecturer nor the student role can do more than its job. That is how Taxila makes every grade change belong to a named person.

## Timed segments

| Segment | Minutes | Tier |
|---|---|---|
| Read the baseline audit | 40 | both |
| Fix your personal findings | 55 | both |
| Account and role design | 30 | both |
| Prove it, break it, reset and write up | 25 | both |

## Steps

Each step states what to do and what you should see. If you do not see it, stop and work out why before moving on.

*Segment 1: Read the baseline audit*

1. **Make your baseline.** Build the weak starting state for your own index number. *Expected:* a report with five findings. F1 names one running service and its port. F2 names one file with mode `666` and its safe mode. F3 says logging is off. F4 says some packages may need updates. F5 names your lecturer account. For the example index the report names `apache2` on port `80`, `/etc/crontab` with safe mode `600`, and the account `lecb99b`.

> **Floor path.** Open the `hardening-checklist` demo and scroll to "Your baseline report". Type your index number in capitals and choose **Build my report**. The page accepts letters and digits only, and it never sends your index anywhere. It shows the same five findings as the full tier, and a report score of 52 out of 100.

Full tier, in a terminal on your Kali virtual machine, in the folder where you saved the script. Use your own index:

```bash
sudo python3 seed-baseline.py COHNDNE999X000
```

The script changes only the machine it runs on. It starts and enables your service, makes your file writable by every account, tells the journal to keep nothing, and creates your lecturer account. It refuses to run on anything but Kali.

2. **Run the audit.** Audit the whole server with Lynis, then find your file and your service in the result. *Expected:* a long list of tests. In the file permissions section, your file shows `[ SUGGESTION ]`. Near the end, a line reads `Hardening index` with a number out of 100. Your service also shows up, with its own suggestions.

```bash
sudo lynis audit system
```

The audit takes a few minutes. Lynis checks many files against the modes it expects. Some files that the script did not touch may also show `[ SUGGESTION ]`; that is normal on a fresh machine. Your file is the one your report names.

> **Floor path.** The report panel shows an excerpt of the same audit, with your file's line marked. Read it, and find the hardening index line.

3. **Sort the findings.** For F1 to F4, write down which of the morning's five hardening areas it belongs to, and which property is most at stake. *Expected:* F1 is services and open ports; F2 is file permissions; F3 is logging; F4 is patching; F5 is users and groups. An open service and a writable file threaten confidentiality and integrity. A silent log loses accountability.

Full tier, to read the patching finding without installing anything:

```bash
apt list --upgradable
```

If your machine has not fetched the package lists recently, the list may be short or empty. You read F4 today; you do not install the updates, which would take far too long in the lab.

*Segment 2: Fix your personal findings*

4. **Disable your service.** Stop it now and stop it starting at boot. *Expected:* `systemctl is-enabled` prints `disabled`, and its port no longer appears in the list of listening ports.

```bash
sudo ss -tlnp
sudo systemctl disable --now apache2
systemctl is-enabled apache2
sudo ss -tlnp
```

Use the service your report names. In the first `ss` list, find your port; in the second, it is gone. A service that does not run cannot be reached.

5. **Tighten your file.** Give your file its safe mode. *Expected:* `stat` prints the safe mode and the file name.

```bash
stat -c '%a %n' /etc/crontab
sudo chmod 600 /etc/crontab
stat -c '%a %n' /etc/crontab
```

Use your own file and safe mode. The first `stat` prints `666`; the second prints `600` or `644`, as your report says.

6. **Turn logging on.** Remove the setting that tells the journal to keep nothing, then restart the journal. *Expected:* the newest journal lines are from the moment you restarted it, and they say the journal started.

```bash
sudo rm /etc/systemd/journald.conf.d/50-day5-baseline.conf
sudo systemctl restart systemd-journald
sudo journalctl -n 3 --no-pager
```

Before the fix, the same restart adds no new lines, because the journal throws everything away.

> **Floor path.** In the report panel, choose the right fix for F1, F2 and F3 from the three offered for each. A wrong choice says why it is wrong. Write each fix's command in your notes, exactly as the full tier above shows it, using your own service and file.

7. **Re-audit and check.** Run the audit again and the script's check. *Expected:* your file's line now shows `[ OK ]`. The check prints `FIXED` for F1, F2 and F3. The hardening index may move a few points either way: fixing a file adds no points, and a stopped service drops its own tests. The proof is the lines that cleared, not the number.

```bash
sudo lynis audit system
sudo python3 seed-baseline.py --check COHNDNE999X000
```

> **Floor path.** When all three findings are fixed, the panel shows F1, F2 and F3 as fixed and the score rises from 52 to 83. F4 stays open, because you only read it today.

*Segment 3: Account and role design*

8. **Design the roles.** Open `role-table.csv` and fill in the lecturer role and the student role, row by row: yes or no for each action, and why. Put your own lecturer account from F5 and `lecturer01` in the lecturer role, and `student01` in the student role. *Expected:* a [role-based access control](../../glossary.md#role-based-access-control) table where neither role can do more than its job. The student role reads only its own record.

On the full tier, you can also check that your lecturer account holds no administrator rights. It should belong only to its own group:

```bash
id lecb99b
groups lecb99b
```

9. **Name the action that needs a second approver.** Mark the one action that one person must never do alone. *Expected:* changing a grade after results are released needs a second approver. The lecturer asks for the change and the Registrar approves it. Neither role can approve its own request. That is [separation of duties](../../glossary.md#separation-of-duties).

*Segment 4: Prove it, break it, reset and write up*

10. **Collect your evidence.** Fill in the evidence pack from steps 1 to 9. *Expected:* your three fixed findings, each with its fix, and your role table.

11. **Draw and explain.** Draw the sketch and write the explanation listed under Evidence required. *Expected:* a labelled sketch and at most 120 words.

## Prove it

The findings keyed to your index are addressed, each with its fix named. On the full tier, the script's check, `sudo python3 seed-baseline.py --check`, prints `FIXED` for F1, F2 and F3, and your file's line in the audit shows `[ OK ]`. On the floor tier, the report panel shows the same three findings fixed. Your role table gives the student role no access to another student's record. Your lecturer derives the same findings from your index with the module's own tool, so a report copied from someone else shows the wrong service, file or account.

## Break it

**Fault:** the student role is given read access to all records.

1. Open the `access-models` demo, choose the role-based model, and switch on **Student role: read all records**. Choose `student01` and look at what opens. **Symptom:** `student01` can now read every student's record and grades, not only its own.
2. **Evidence:** the role carries the permission, and every account assigned to the role receives it at once. One wrong line in the role table reaches every student, which is why permissions are designed per role and checked.
3. **Fix:** switch the permission off and check that `student01` again sees only its own record. In your role table, write the symptom, the cause and the fix in the "why" column of that row.

## Reset

1. Copy your evidence into your evidence pack first.
2. Floor tier: keep your marked report and your role table. Reload the demos to clear them.
3. Full tier: restore the `day-5-start` snapshot. If you did not take one, run `sudo python3 seed-baseline.py --undo` with your index: it disables your service, sets your file to its safe mode, turns logging on and removes your lecturer account.

## Rules of engagement

No tool in this lab can affect anyone else's system. You harden only your own virtual machine, or mark up the provided report. The script weakens the machine it runs on, so never run it on a computer you do not own.

## Evidence required

Submit evidence pack 5 before the next teaching day, using the [evidence pack template](../../templates/evidence-pack.md).

1. **Personal values.** In the template's table, with the step each comes from:
   - your service from F1 and the command that disabled it (steps 1 and 4);
   - your file from F2, its safe mode and the command that set it (steps 1 and 5);
   - the logging fix, and the newest journal line after it, or the panel's fixed mark (step 6);
   - the check's output, or the panel's summary, showing F1 to F3 fixed (step 7);
   - your role table, with your lecturer account from F5 and the action that needs a second approver (steps 8 and 9).
2. **Concept sketch.** Draw by hand, on paper, the three gates of authentication, authorisation and accounting (AAA) for a user signing in to the SIS, and label each gate. Photograph it.
3. **Explanation.** In no more than 120 words: why does least privilege limit the damage when a password is stolen?

## Taxila connection

This lab adds two items to Taxila's security register. Item 9 is accounts, roles and multi-factor sign-in. Every SIS account sits in a role whose permissions match its job, and a released grade changes only with a second approver. Item 10 is the hardened server baseline. The SIS server runs only what it needs, its files are closed to other accounts, and it records what happens. The Head of IT will ask what each fix could break: a stopped service that nobody used breaks nothing, which is why it was safe to stop. The Registrar will ask whether a changed grade can now be traced. Yes: the role says who may change it, the second approver must agree, and the log records who did. Before you leave, form your group of four for the group exercise and agree its four roles, as the [tabletop brief](../../coursework/tabletop-brief.md) describes.
