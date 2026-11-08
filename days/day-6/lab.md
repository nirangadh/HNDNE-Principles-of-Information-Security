# Lab 6: Find the flawed lines, fix them, and prove the fix

**Day 6, afternoon session. Duration 3 hours. Adds items 11 and 12 to Taxila's security register.**

This lab sheet takes you through the work a defender does on a web application. You read the code, find the line that trusts what a user typed, apply the fix, and prove it with a provided test. You do it twice, once for the login and once for a note the portal shows back. By the end you can say where each flaw was, what the fix was, and how you know it worked.

| | |
|---|---|
| Learning outcomes | LO4 |
| You need | this morning's ideas: injection is input read as a command; a parameterised query treats input only as data; output encoding makes input display as plain text |
| Tiers | Floor tier: every step, in the browser with the portal's demos. Full tier: the same work in the provided `taxila-portal` code on your Kali virtual machine |
| Evidence pack | Pack 6, due before the next teaching day. This is the last pack |

## Before you start

1. Open this page and the day's notes side by side. Keep the notes open at sections 1 to 3.
2. Write down your personal value: your index number without spaces or hyphens (the example in this sheet, `COHNDNE999X000`, belongs to nobody). The test seeds a practice record from it, so your result is your own.
3. Floor tier: open the two demos this lab uses, [`sqli-login`](artefacts/sqli-login.html) and [`output-encoding`](artefacts/output-encoding.html).
4. Full tier: start your Kali virtual machine and take a snapshot named `day-6-start`, so Reset can bring it back. Then download the provided [`taxila-portal.py`](files/taxila-portal.py) into your module folder.

### The idea behind today's lab

> **Recall.** Injection is input read as a command.

> **Recall.** A parameterised query treats input only as data.

Both halves of today ask the same question: did the application keep what the user typed as data, or let it become part of a command? For the login, the command is a database query, and the fix is a parameterised query. For the note, the command is the markup of a page, and the fix is output encoding. You never craft an attack and you never type one. A prepared test does the probing; you read what it reports, find the flawed line, fix it, and run the test again.

> **Common mistake.** "Passing one test proves the application is secure." A test proves one case is fixed. Secure coding applies the same fix everywhere input is used: every query parameterised, every output encoded. Today you fix two lines; a real application has many.

> **Common mistake.** "Fixing the browser fixes the vulnerability." The fix belongs on the server, in the query and in the output. A check in the browser helps honest users, but it runs on the user's own machine and can be skipped.

> **Quick check.** You run the login test against the unfixed portal and it returns every record in the table. Your partner says: "The database is broken, raise it with the database team." What is the better reading?
>
> - [ ] The database is faulty and should be reinstalled
> - [x] The application built its query by joining input, so the database did what the changed query said; the fix is a parameterised query in the application
> - [ ] The test is wrong, because a login should return one record
>
> **Why:** The database answered the question it was given. The application changed that question by joining input into it. The fix is in the application, by sending the input as data beside the query.

> **Quick check.** After you set the login to a parameterised query, the test returns zero records for its probe but one for a normal sign-in. Is this the result you want?
>
> - [x] Yes: the probe now matches nothing, and a real sign-in still works
> - [ ] No: a secure login should return zero records for everyone
> - [ ] No: the test should still return every record, to prove it ran
>
> **Why:** The fix must stop the injection and keep the portal working. Zero for the probe shows the flaw is closed; one for a normal sign-in shows an ordinary login still succeeds.

## Objective

You will show the login leaking every record before your fix and leaking none after it, while a normal sign-in still works. You will show a note changing a page before your fix and shown as plain text after it. That is how Taxila closes register item 11, the portal's input handling, and confirms register item 12, the portal's session cookie from this morning.

## Timed segments

| Segment | Minutes | Tier |
|---|---|---|
| Read the login code and find the injection flaw | 40 | both |
| Fix the query and prove it with the test | 45 | both |
| Find and fix the echo flaw | 40 | both |
| Prove it, break it, reset and write up | 25 | both |

## Steps

Each step states what to do and what you should see. If you do not see it, stop and work out why before moving on.

*Segment 1: Read the login code and find the injection flaw*

1. **Run the provided test against the unfixed login.** Run the test with your own index number and read its report. *Expected:* the prepared login probe returns every record in your practice table, including your seeded record, where a normal sign-in returns 1. The table's size is set by your index; the report and the recompute tool give the number. The login is injectable.

```bash
python3 taxila-portal.py --test --index COHNDNE999X000
```

Use your own index number, not the example. Note the name and identifier of your seeded record, and that the probe returned every record where a login should return one.

2. **Find the flawed line.** Open `taxila-portal.py` and read the login. *Expected:* you find the line marked as the flawed line inside `flawed_login`, where the username and password are joined straight into the query text. That joining is why input can become part of the query.

```bash
nano taxila-portal.py
```

> **Floor path.** Open the `sqli-login` demo. Choose "Joined: input put into the query text" and step the prepared test value through: part of it becomes a condition that is always true, so every record matches. Then enter your index and run the login test: it returns every record, including your seeded record. Write down your seeded record and the count.

*Segment 2: Fix the query and prove it with the test*

3. **Apply the parameterised query and run the test again.** In `taxila-portal.py`, set the marked line `SAFE_LOGIN = False` to `SAFE_LOGIN = True`, which switches the login to the parameterised query shown in the notes. Save the file and run the test again. *Expected:* the prepared probe now returns 0 records; a normal sign-in still returns 1.

```bash
python3 taxila-portal.py --test --index COHNDNE999X000
```

> **Floor path.** In the `sqli-login` demo, choose "Parameterised: input kept as data" and run the login test again with your index. *Expected:* the probe returns 0 records, and a normal sign-in returns 1.

*Segment 3: Find and fix the echo flaw*

4. **Run the note test, find the echo flaw, and apply output encoding.** The same test reports a second page: a note the portal shows back. *Expected:* before the fix, the report shows that the prepared bold note reached the page as markup, so the browser would read it as part of the page. Find the marked flawed line inside `flawed_echo`, where the note is placed into the page as it arrived. Set `SAFE_ECHO = False` to `SAFE_ECHO = True`, which switches the page to output encoding. Save and run the test again. *Expected:* the note is now shown as plain text, with your index, and none of it is read as markup.

```bash
python3 taxila-portal.py --test --index COHNDNE999X000
```

> **Floor path.** Open the `output-encoding` demo and enter your index. With encoding off, the prepared bold note changes the page. Switch output encoding on: the same note shows as plain text, with your index.

*Segment 4: Prove it, break it, reset and write up*

5. **Write up the two register items.** In your notes, write one line for each item, in Taxila's words. *Expected:* item 11, the portal keeps what a user types as data, using a parameterised query for every database query and output encoding for everything it shows back. Item 12, the portal's session cookie carries HttpOnly, Secure and SameSite, from this morning.

## Prove it

You can show the login test returning every record before your fix, including your seeded record. After the fix it returns zero, while a normal sign-in still returns one. You can show the note test reporting that the page changed before output encoding and shows plain text after it. On the full tier, that is the two test reports, before and after each fix. On the floor tier, it is the same two results from the `sqli-login` and `output-encoding` demos, seeded from your index. The recompute tool derives your seeded record and both row counts, so your pack can be checked against it.

## Break it

**Fault:** the login is left joined, not parameterised.

1. Full tier: set `SAFE_LOGIN = True` back to `SAFE_LOGIN = False`, save, and run the test again.
2. **Symptom:** the prepared probe returns every record again, including your seeded record.
3. **Evidence:** the report line reads `OPEN`, and names every record it returned where a login should return one. The flawed line is the one inside `flawed_login` that joins input into the query text.
4. **Fix:** set `SAFE_LOGIN` back to `True`, save, and run the test once more. *Expected:* the probe returns zero records again.

> **Floor path.** In the `sqli-login` demo, switch back to the joined query and run the login test: the leak returns. Then switch to the parameterised query: the leak is closed. Name the difference in one line.

## Reset

1. Keep your two test reports, or your demo results, and your register lines from step 5, first.
2. Floor tier: reload the demos to clear them.
3. Full tier: restore the `day-6-start` snapshot, which returns `taxila-portal.py` to its unfixed form. If you did not take a snapshot, set both `SAFE_LOGIN` and `SAFE_ECHO` back to `False` and save.

## Rules of engagement

No tool in this lab can affect anyone else's system. The prepared test inputs run only against the provided application on your own machine, or inside the demo on your own browser. You read a report, find a line, and apply a fix; you never craft an attack and you never type one.

## Evidence required

Pack 6 is the last evidence pack. Put in it:

1. **Personal values.** Your seeded record, its name and identifier, and the two login counts: the records returned before your fix and zero after it. The recompute tool derives all three from your index.
2. **The flawed line and your fix.** For the login, the line that joined input into the query, and the parameterised query that replaced it. For the note, the line that placed the note as it arrived, and the output encoding that replaced it.
3. **The note result.** The note test before and after output encoding: the page changed, then shown as plain text with your index.
4. **Concept sketch.** Draw by hand the boundary between code and data: where input should stop being treated as a command, and label the parameterised-query fix. Photograph it.
5. **Explanation.** In no more than 120 words: why does a parameterised query stop the injection that joining strings allowed?

## Taxila connection

Item 11 on Taxila's register is the portal's input handling. It means a parameterised query for every database query, and output encoding for everything shown back, so what a user types stays data. Item 12 is the portal's session cookie, carrying HttpOnly, Secure and SameSite, which you met this morning. Together they answer the question the Head of IT (information technology) asked: can a crafted login read every student's record, and can a note run in another student's browser? After today, for the portal, the answer to both is no.
