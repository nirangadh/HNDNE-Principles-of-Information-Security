# Lab 7: Trace a suspect header and scope a database account

**Day 7, afternoon session. Duration 3 hours. Adds items 13 and 14 to Taxila's security register.**

This lab sheet takes you through two jobs a defender does every week. First you read the header of a message that claims to come from the Registrar, and find out where it really came from. You check what the Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) and Domain-based Message Authentication, Reporting and Conformance (DMARC) found. Then you give the Student Information System (SIS) database an account with only the rights the portal needs. Last, you turn on a log that records what every account asks the database to do.

| | |
|---|---|
| Learning outcomes | LO4 |
| You need | this morning's ideas: the received lines, read bottom-up, show a message's true path; the three checks, [SPF](../../glossary.md#spf), [DKIM](../../glossary.md#dkim) and [DMARC](../../glossary.md#dmarc); a scoped account limits what a stolen login can do |
| Tiers | Floor tier: every step, in the browser and with the provided files. Full tier: recommended for segments 2 and 3, on your Kali virtual machine with MariaDB |
| Evidence pack | none today; the five evidence packs ended with the pack after Day 6 |

## Before you start

1. Open this page and the day's notes side by side. Keep the notes open at sections 3 and 4.
2. Download the provided files and save them in your module folder: [`suspect-header.txt`](files/suspect-header.txt), [`grants.txt`](files/grants.txt) and [`query-log.txt`](files/query-log.txt) (both tiers), and [`taxila-db.sql`](files/taxila-db.sql) (full tier only).
3. Floor tier: open the `header-trail` demo. You use it on both tiers in segment 1.
4. Full tier: start your Kali virtual machine and take a snapshot named `day-7-start`, so Reset can bring it back. Take it before you run anything else today.

### The idea behind today's lab

> **Recall.** The received lines, read bottom-up, show a message's true path.

> **Recall.** A scoped account limits what a stolen login can do.

Both halves of today ask the same question: what really happened, and who did it? A mail header records which servers handled a message. A database's query log records which account asked for what. A defender reads both. Neither one stops a problem by itself. The header tells you a message is not genuine; the log tells you who did something. The control that stops harm is a different one: the published checks for email, and a scoped account for the database.

> **Common mistake.** "A passing sending-server check means the mail is genuine." A pass means only that the sending server was allowed to send for the domain in the address. A look-alike domain can publish its own records and pass its own checks. You must still read which domain passed.

> **Common mistake.** "Turning the log off is fine once it is set up." A log that is off records nothing at the moment it is needed most. Logging costs little disk space for a database of Taxila's size, and it is the only way the Data Protection Officer can show who read or changed personal data.

> **Quick check.** A header shows `dmarc=fail (p=QUARANTINE) header.from=taxila.example`. What does this line tell you?
>
> - [ ] The message really came from Taxila, but its signature broke on the way
> - [x] The from line claims Taxila, the message failed Taxila's checks, and Taxila asked receivers to quarantine such messages
> - [ ] The receiving server could not reach Taxila's records, so it guessed
>
> **Why:** DMARC compares the domain in the from line with the domains that passed SPF or DKIM. Here neither passed for `taxila.example`, so the from line is not backed by anything. `p=QUARANTINE` is the policy Taxila published: hold such messages instead of delivering them. Read alone, the line does not say where the message came from; the received lines do.

> **Quick check.** The Head of IT (information technology) finished setting up the portal's database account. A colleague says: "The account works now, so we can turn the query log off to save space." What is the best answer?
>
> - [ ] Yes: once the account is scoped, nothing can go wrong
> - [x] No: the scoped account limits what a stolen login can do, but only the log shows what was actually done
> - [ ] Yes, but only after a month
>
> **Why:** Least privilege prevents; the log detects and records. If the portal's password leaks, the scoped account stops the thief dropping tables, but the thief can still read what the portal reads. Only the log can show that this happened, and when.

## Objective

You will show where a quarantined message really came from, and which of Taxila's checks it failed. You will also show that the portal's database account can do its job, read records and enter grades, and is refused anything more, such as dropping a table. The query log records both the allowed and the refused requests. That is how Taxila meets register items 13 and 14.

## Timed segments

| Segment | Minutes | Tier |
|---|---|---|
| Analyse a suspicious header | 40 | both |
| Scope a database account | 55 | both |
| Turn on and read the audit log | 30 | both |
| Prove it, break it, reset and write up | 25 | both |

## Steps

Each step states what to do and what you should see. If you do not see it, stop and work out why before moving on.

*Segment 1: Analyse a suspicious header*

1. **Open the header and trace its path.** Open `header-trail` and choose the quarantined message. Put its received lines in order, oldest first. *Expected:* the oldest line is at the bottom. The first line written by Taxila's own server, `mail.taxila.example`, says it received the message from `203.0.113.45`, a machine outside Taxila. The line below it was written by that outside machine, so it proves nothing.

Full tier: you can also read the provided file in a terminal and pick out the lines that matter.

```bash
less suspect-header.txt
grep -E "^(Received|From|Reply-To|Authentication-Results)" -A3 suspect-header.txt
```

2. **Find the tells and write the true path.** In the demo, mark each line that shows the message is not genuine. *Expected:* three tells. The authentication results show `spf=fail` and `dkim=none`, so `dmarc=fail`, and the message was quarantined. The from line says `registrar@taxila.example`, but the reply-to is `registrar@sis-taxila.example`, a look-alike domain. And the true origin, `203.0.113.45`, is not Taxila's mail server, which the SPF record lists as `192.0.2.25`. Write the path in one line, oldest first: the sender's laptop, the outside relay at `203.0.113.45`, then `mail.taxila.example`.

> **Floor path.** Both tiers use the `header-trail` demo for this segment, and no outside service is used. Do not paste a real header into an online checker: a real header names real people and servers.

*Segment 2: Scope a database account*

3. **Start the database and build `taxila-db`.** Start MariaDB, then run the provided script. *Expected:* the script ends by printing **taxila-db is ready: 6 students, 12 grades**.

```bash
sudo systemctl start mariadb
sudo mariadb < taxila-db.sql
```

MariaDB was installed on your machine before Day 1 and left switched off. Today you start it, but do not enable it at boot: Reset turns it off again. The script makes only the database and its two tables, `students` and `grades`. Every row in it is invented.

4. **Create the portal's account with only what it needs.** Open the database as its administrator and create the account the portal uses. Give it three rights: read `students`, and read, add and change `grades`. Choose your own password. *Expected:* `SHOW GRANTS` lists exactly three lines. The first is `USAGE` on everything, which means only "may sign in". The others are `SELECT` on `students`, and `SELECT, INSERT, UPDATE` on `grades`.

```bash
sudo mariadb
```

Then, at the `MariaDB [(none)]>` prompt:

```sql
CREATE USER 'taxila-portal'@'localhost' IDENTIFIED BY 'choose-your-own-long-password';
GRANT SELECT ON `taxila-db`.students TO 'taxila-portal'@'localhost';
GRANT SELECT, INSERT, UPDATE ON `taxila-db`.grades TO 'taxila-portal'@'localhost';
SHOW GRANTS FOR 'taxila-portal'@'localhost';
```

The database name has a hyphen, so it sits inside backticks, `` ` ``, in every statement. Account names sit inside ordinary quotes. Leave this window open: you use it again in steps 6 and 8.

5. **Test the account.** In a second terminal, sign in as the portal's account and do the portal's job, then try one thing it must not do. *Expected:* the read shows `student01`'s two grades, the update says `1 row affected`, and the drop is refused with `ERROR 1142 (42000): DROP command denied to user 'taxila-portal'@'localhost'`.

```bash
mariadb -u taxila-portal -p taxila-db
```

```sql
SELECT student_id, module, mark FROM grades WHERE student_id = 'student01';
UPDATE grades SET mark = 64 WHERE student_id = 'student01' AND module = 'M2';
DROP TABLE grades;
```

You type `DROP TABLE` here as the defender testing your own control on your own database. A refusal is the result you want.

> **Floor path.** Open `grants.txt`. In Part A, mark each grant line `KEEP` or `REMOVE`, using what each account is for, and write the line that should replace it. Then read Part B, the same server after the Head of IT's fix, and check your marks against it. You should find three things to change. The portal account holds every right on every database, with the right to give rights to others. The old `lecturer01` account can still change and delete grades directly, outside the portal. And the query log is off. The `registrar` reading account and the `itadmin` administration account are what their jobs need. Part B ends with the same test as step 5, and its results.

*Segment 3: Turn on and read the audit log*

6. **Turn on the general query log.** In the administrator window, turn the log on and check it. *Expected:* `@@general_log` shows `1`, and the log file is `kali.log`.

```sql
SET GLOBAL general_log = 'ON';
SELECT @@general_log, @@general_log_file;
```

Then, in the portal account's window, run one allowed statement and one refused one: the same `SELECT` as in step 5, then `DROP TABLE grades;` again.

7. **Read the log.** In a terminal, read the end of the log file. *Expected:* a `Connect` line for `taxila-portal@localhost on taxila-db`, then two `Query` lines with the same connection number: your `SELECT`, and your `DROP TABLE grades`. The refused statement is there, because the server writes each statement to this log as it arrives, before it checks the grants. The error you saw in step 6 appears only in your terminal.

```bash
sudo tail -n 20 /var/lib/mysql/kali.log
```

Reading the file needs `sudo`, because it belongs to the database server. The log does not say which statements were refused. To find them, compare each statement with the account's grants: anything outside them was refused.

> **Floor path.** Open `query-log.txt` and answer its three questions. Join each `Query` line to its `Connect` line by the number in the Id column. The portal account asked for two things its grants do not allow: `DROP TABLE grades` and `SELECT * FROM mysql.user`.

*Segment 4: Prove it, break it, reset and write up*

8. **Write up the two register items.** In your notes, write one line for each item, in Taxila's words. *Expected:* item 13, Taxila publishes SPF, DKIM and DMARC records for `taxila.example`, with a quarantine policy, and staff check the reply-to of anything asking them to act. Item 14, the portal's database account holds only `SELECT` on `students` and `SELECT, INSERT, UPDATE` on `grades`, and the general query log is on and read.

## Prove it

You can show the suspect header's check result, `spf=fail`, `dkim=none` and `dmarc=fail`, and its true origin, `203.0.113.45`, which is not Taxila. You can also show the scoped account doing its reads and writes while being refused a table drop. On the full tier, that is your own `SHOW GRANTS` output, the `1 row affected` line and the `ERROR 1142` line, and the same statements in `kali.log`. On the floor tier, it is your marked `grants.txt`, matching Part B, and your answers to the log's questions.

## Break it

**Fault:** the portal's account is given full privileges.

1. Full tier, in the administrator window, make a throwaway database with one table, then give the portal account every right on everything.

```sql
CREATE DATABASE throwaway;
CREATE TABLE throwaway.practice (n INT);
GRANT ALL PRIVILEGES ON *.* TO 'taxila-portal'@'localhost';
```

2. **Symptom:** in the portal account's window, `DROP TABLE throwaway.practice;` now succeeds, with `Query OK`. Use only the throwaway table: never drop a table in `taxila-db`.
3. **Evidence:** `SHOW GRANTS FOR 'taxila-portal'@'localhost';` now begins `GRANT ALL PRIVILEGES ON *.*`. Anyone holding the portal's password could now drop any table, read every database and make new accounts.
4. **Fix:** take back only the rights given on everything, and check that the three scoped lines are back.

```sql
REVOKE ALL PRIVILEGES ON *.* FROM 'taxila-portal'@'localhost';
SHOW GRANTS FOR 'taxila-portal'@'localhost';
```

`REVOKE ... ON *.*` removes only what was given on `*.*`. The rights on `students` and `grades` were given table by table, so they stay. *Expected:* the same three lines as step 4.

> **Floor path.** Use Part A of `grants.txt`, where the portal account starts with `GRANT ALL PRIVILEGES ON *.* ... WITH GRANT OPTION`. Write what a thief holding the portal's password could do with that line: drop any table, read every database, and give rights to other accounts. Then write the two statements that take it back to least privilege: `REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'taxila-portal'@'localhost';` and the two `GRANT` lines from step 4.

## Reset

1. Keep your notes from steps 2, 7 and 8 first.
2. Floor tier: keep your marked `grants.txt` and your log answers. Reload the demo to clear it.
3. Full tier: restore the `day-7-start` snapshot. This removes the throwaway database, `taxila-db` and the account, and leaves MariaDB switched off. If you did not take a snapshot, run these in the administrator window, then quit and stop the database:

```sql
DROP DATABASE throwaway;
DROP USER 'taxila-portal'@'localhost';
DROP DATABASE `taxila-db`;
SET GLOBAL general_log = 'OFF';
```

```bash
sudo systemctl stop mariadb
```

## Rules of engagement

No tool in this lab can affect anyone else's system. You work only on your own machine, the `taxila-db` database you built there, and the provided files. Never paste a real email header into an online service, and never test an account on a database you do not own.

## Evidence required

There is no evidence pack today. Keep these, because your group uses them in its controls map:

1. **Your header notes.** The true path, the three tells and the check results from steps 1 and 2.
2. **Your database notes.** Your `SHOW GRANTS` output, or your marked `grants.txt`, and your two register lines from step 8.

## Taxila connection

Item 13 on Taxila's register is email authentication for `taxila.example`: the three published checks that turn last semester's fake Registrar message into one held in quarantine. Item 14 is the SIS database accounts and audit log: the portal's account can no longer drop a table or read other databases, and every request is recorded. The Data Protection Officer can now answer part of the question asked this morning: if the portal's password leaks, what could it reach, and would we know?
