# Lab 3: Fingerprint your results file and store a password safely

**Day 3, afternoon session. Duration 3 hours. Adds items 5 and 6 to Taxila's security register.**

This lab sheet takes you from fingerprinting your own results file to storing a password the safe way. You will see one changed mark change the whole fingerprint, and a salt keep a password out of a lookup table.

| | |
|---|---|
| Learning outcomes | LO3 |
| You need | this morning's ideas: a [hash function](../../glossary.md#hash-function) gives a fixed-length [digest](../../glossary.md#digest) that changes completely on any edit; a [salt](../../glossary.md#salt) makes identical passwords store differently; a [lookup table](../../glossary.md#lookup-table) only matches digests computed in advance; a [slow password hash](../../glossary.md#slow-password-hash) makes each guess expensive |
| Tiers | Floor tier: every step, in the browser. Full tier: segments 1 to 3 can also run in your Kali virtual machine, with the same results |
| Evidence pack | Pack 3, due before the next teaching day |

## Before you start

1. Open this page and the day's notes side by side.
2. Write down your personal value: your index number without spaces or hyphens, with its letters in capitals exactly as issued (the example in this sheet, `COHNDNE999X000`, belongs to nobody).
3. Full tier: start your Kali virtual machine and take a snapshot named `day-3-start`, so Reset can bring it back.
4. Floor tier: open the demos this lab uses: `avalanche` and `salt-shaker`. Open CyberChef too, from its official site or your offline copy.
5. Download the provided file [`lookup-table.txt`](files/lookup-table.txt) and save it in your module folder. It lists common passwords beside their SHA-256 (Secure Hash Algorithm, 256 bits) digests, computed in advance.

### The idea behind today's lab

> **Recall.** A hash is a fixed-length fingerprint that changes completely on any edit.

> **Recall.** A salt makes identical passwords store differently.

> **Common mistake.** "A lookup table works the password out from its digest." It only matches the digest against digests computed in advance; it cannot reverse one. In segment 3 the table finds a common password at once, and finds nothing for your salted digest, because nobody computed that one in advance.

> **Common mistake.** "A salt must be kept secret." A salt need not be secret; it must be unique for each user. It is stored in plain sight, beside the digest. Its job is to make every stored value different, not to hide anything.

> **Quick check.** You and your lab partner both write the example line `COHNDNE999X000,50`, you with `printf` and your partner with `echo`. The two lines look the same on screen. Why do your digests differ?
>
> - [x] `echo` adds an invisible line ending, so the two files differ by one byte
> - [ ] `printf` and `echo` use different hash functions inside
> - [ ] The two terminals use different versions of SHA-256
>
> **Why:** The hash takes every byte, and one extra byte changes the whole digest: the avalanche effect. Blaming the hash function is tempting, but SHA-256 is the same everywhere; only the input differed.

> **Quick check.** In segment 2 your salt goes into your evidence pack, beside your salted digest, where anyone can read it. Is that a weakness?
>
> - [ ] Yes: a salt is a key and must be kept secret
> - [x] No: a salt only needs to be unique, and is stored beside the digest anyway
> - [ ] Yes: anyone with the salt can reverse the digest
>
> **Why:** A salt's job is to make each stored value different, so no table built in advance holds it. Treating the salt as a secret key is tempting, but the further secret, kept apart from the database, is a pepper.

## Objective

You will show that one changed mark gives your results file a completely different fingerprint, so any change can be detected. You will also show that a salt keeps a common password out of a lookup table, and that a slow password hash makes every guess cost more. This is how Taxila keeps published results honest and its password store safe, even if the store is stolen.

## Timed segments

| Segment | Minutes | Tier |
|---|---|---|
| Fingerprint your personal results file | 45 | both |
| Salt the password store | 35 | both |
| See why salt and slow hashing protect passwords | 45 | both |
| Prove it, break it, reset and write up | 25 | both |

## Steps

Each step states what to do and what you should see. If you do not see it, stop and work out why before moving on.

*Segment 1: Fingerprint your personal results file*

Your results file is one line: your index number, a comma, then a mark. The mark comes from your index number by this rule: **your mark is 50 plus the last digit of your index number**. The example index ends in 0, so its mark is 50, and its results line is `COHNDNE999X000,50`. The file holds exactly that line: no space, and no new line at the end.

1. **Try the example first.** Work through steps 2 to 4 with the example, and check that you get these values. Then repeat them with your own index number. *Expected:* the line `COHNDNE999X000,50` has the digest `84a521d52030ac8d64a96969eae32e2c4d3444d080b2d10efe7dc6bb0f4b4e3f`. The changed line `COHNDNE999X000,51` has the digest `b2d1fd0d3c53d46bbb5db46bc922600ad8229bf70cd4840dbce892f6a8e0ef8a`.

2. **Write your results line.** Take the last digit of your index number and add it to 50. Write your index number, a comma and your mark, with no space. *Expected:* a line such as `COHNDNE999X000,50`, with a two-digit mark from 50 to 59.

3. **Fingerprint it.** Take the SHA-256 digest of your results line. *Expected:* 64 hexadecimal characters. Write them down: this is the fingerprint the Registrar would publish beside the file.

4. **Change the mark by one and fingerprint it again.** Add one to your mark, so 50 becomes 51. Take the digest again and compare the two. *Expected:* a second 64-character digest that differs from the first in almost every character. You changed one character of the file; the digest changed everywhere.

> **Floor path.** In CyberChef, type your results line in the input box, with no space or new line after it. Add the operation `SHA2` and set its `Size` to `256`; the default is 512, which is wrong here. For step 4, change the mark in the input box and read the new digest. Then open the `avalanche` demo, type your two lines into its two boxes, and read how many characters of the two digests differ.

Full tier, in a terminal on your Kali virtual machine. Replace the example line with your own:

```bash
mkdir -p ~/lab3 && cd ~/lab3
printf '%s' COHNDNE999X000,50 > results.csv
sha256sum results.csv
sha256sum results.csv > results.csv.sha256
sha256sum -c results.csv.sha256
printf '%s' COHNDNE999X000,51 > results.csv
sha256sum results.csv
sha256sum -c results.csv.sha256
```

The second command prints your digest, two spaces and the file name. The fourth command keeps that digest in a file, as the Registrar would keep it. The fifth checks the file against it and prints `results.csv: OK`. After you change the mark, the same check prints `results.csv: FAILED` and a warning that one checksum did not match.

Use `printf`, not `echo`, to write the file. `echo` adds an invisible line ending, which changes the file and so the digest.

*Segment 2: Salt the password store*

Every student in this lab uses the same password: `password123`. It is a common password, and a poor one. That is the point: the whole room is now a group of staff who all chose the same password. Never type a real password of your own into any tool in this lab.

5. **Hash the password with no salt.** Take the SHA-256 digest of `password123`. *Expected:* `ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f`. Look at your neighbour's screen: they have exactly the same value. In an unsalted store, everyone with the same password has the same stored value.

6. **Find your two salts.** Take the SHA-256 digest of your index number. You made exactly this value on Day 2, where it was your Advanced Encryption Standard (AES) key. Your first salt is its first 8 characters. Your second salt is its last 8 characters. *Expected:* for the example, the digest is `5b02a8f821835e23aa2d08921e40ddb0e0e21220f3e7d4e0a979bc9e962bb99b`, so the first salt is `5b02a8f8` and the second salt is `962bb99b`.

7. **Hash the password with each salt.** Write the password, then your first salt straight after it, with no space: for the example, `password1235b02a8f8`. Take its SHA-256 digest. Then do the same with your second salt. *Expected:* for the example, `a0b12530aefa1e72505b5ef0afb82d54e8fc432477b2ade85f09d1174e42b535` with the first salt and `f7bbb48d2b7e71a3f0d6310b067b2e257c3a5528987183ef5d92bd7ab46c0e5b` with the second. The same password now gives two different stored values, and your neighbour's values differ from yours.

> **Floor path.** In CyberChef, use `SHA2` with `Size` `256` for every step. For step 6, put your index number in the input box. To read a salt exactly, add `Take bytes` after `SHA2`: `Start` `0` and `Length` `8` gives the first salt, and `Start` `56` and `Length` `8` gives the second. Then remove `Take bytes` again. For step 7, type the password and the salt together in the input box, with nothing between them and nothing after them.

Full tier. Replace the example index and the example salt with your own:

```bash
printf '%s' password123 | sha256sum
printf '%s' COHNDNE999X000 | sha256sum | cut -c1-8
printf '%s' COHNDNE999X000 | sha256sum | cut -c57-64
printf '%s' password1235b02a8f8 | sha256sum
printf '%s' password123962bb99b | sha256sum
```

The second and third commands print your two salts. `sha256sum` reads from the pipe here, so it prints a dash where a file name would be.

*Segment 3: See why salt and slow hashing protect passwords*

The provided `lookup-table.txt` is a small lookup table: about a hundred common passwords, each beside its SHA-256 digest, computed in advance. Real tables hold millions. You only search it; you never add to it.

8. **Look up the unsalted digest.** Search the table for the unsalted digest from step 5. *Expected:* found at once, on the line that ends `password123`. The table did not reverse the hash: it simply matched a digest that someone computed in advance.

9. **Look up your salted digests.** Search the table for each of your two salted digests from step 7. *Expected:* not found. Nobody computed `password123` with your salt in advance, so no table holds it. To fill a table with salted values, someone would have to compute it again for every salt, which means for every user.

10. **Time a fast hash.** Take the SHA-256 digest of your salted password from step 7 again, and note how long it took. *Expected:* a few milliseconds or less. That speed is good for checking files, and bad for passwords: it lets a guesser try millions of passwords a second.

11. **Time a slow password hash.** Run the password through the Password-Based Key Derivation Function 2 (PBKDF2), with your first salt and 600,000 iterations. *Expected:* it takes visibly longer, often a few seconds in the browser. The output is 64 hexadecimal characters; for the example it is `e6f049ab50546fe6d115431d29fb0db710debf27b76b9a6a5236e21525f9b416`. One login waits a moment, but every guess now costs the same moment, so a million guesses take far longer than before.

> **Floor path.** For steps 8 and 9, open the `salt-shaker` demo, go to its panel "Check a digest", and paste each digest in turn. It searches the same table as the provided file. For step 10, take `SHA2` with `Size` `256` of your salted password in CyberChef. Then read the bake time in the bar under the output: a clock symbol and a number of milliseconds. For step 11, remove `SHA2` and add `Derive PBKDF2 key`. It ignores the input box, so set each of its boxes. Set `Passphrase` to `password123`, with its dropdown at `UTF8`, `Key size` to `256` and `Iterations` to `600000`. Set `Hashing function` to `SHA256`, and `Salt` to your first salt, with its dropdown at `UTF8`. Type the iterations last, wait for the output, and read the bake time again. If you leave `Salt` empty, CyberChef picks a random salt and your output will not match.

Full tier. Save `lookup-table.txt` in `~/lab3` first: download it in the virtual machine's browser. Then run these commands, with your own digests and salt:

```bash
cd ~/lab3
grep ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f lookup-table.txt
grep a0b12530aefa1e72505b5ef0afb82d54e8fc432477b2ade85f09d1174e42b535 lookup-table.txt
printf '%s' password1235b02a8f8 > salted.txt
time openssl dgst -sha256 salted.txt
time openssl kdf -keylen 32 -kdfopt digest:SHA256 -kdfopt pass:password123 -kdfopt salt:5b02a8f8 -kdfopt iter:600000 PBKDF2
```

The first `grep` prints the matching line; the second prints nothing, because the table does not hold your salted digest. `time` prints how long each command took: read the line that starts `real`. Expect a few thousandths of a second for `openssl dgst`, and many times more for `openssl kdf`. OpenSSL prints the PBKDF2 output in capitals with a colon between each pair, `E6:F0:49:AB:...` for the example; it is the same value as the browser's.

*Segment 4: Prove it, break it, reset and write up*

12. **Collect your evidence.** Fill in the evidence pack table with your values from steps 2 to 9. *Expected:* every value except the unsalted digest comes from your own index number.

13. **Draw and explain.** Draw the salted-storage sketch and write your explanation, as listed under Evidence required. *Expected:* a labelled sketch and at most 120 words.

## Prove it

Your results file's two digests, before and after one change, differ in almost every character, and your salted and unsalted values for the same password differ. Both match the values your lecturer's recompute tool gives, because they come from your index number. The table finds the unsalted digest and not your salted one. Copy your results line, both digests, the unsalted digest, your two salts, your two salted digests and the two lookup results into your evidence pack.

## Break it

**Fault:** a single trailing space in the results file.

1. Add one space at the end of your results line, after the mark, and take its digest. **Symptom:** a third digest, completely different from the first, although the line looks the same on the screen. For the example, `COHNDNE999X000,50` with a space after it gives `17a67f960a43bb47094bf7a5aaeb019efa38f49d4d57846ee193600f0c3ec256`.
2. **Evidence:** the mark and the index are unchanged, so the cause must be a character you cannot see. A space is a byte like any other. The hash function takes every byte, and one changed byte changes the whole digest: the avalanche effect. On the full tier, `sha256sum -c` reports `FAILED`, and `wc -c results.csv` counts one more byte than before.
3. **Fix:** remove the space and take the digest again. It matches your first digest. Write down the symptom and why it happens.

Full tier, to make and then remove the fault:

```bash
printf '%s ' COHNDNE999X000,50 > results.csv
sha256sum results.csv
wc -c results.csv
printf '%s' COHNDNE999X000,50 > results.csv
sha256sum -c results.csv.sha256
```

## Reset

1. Copy your evidence into your evidence pack first.
2. Floor tier: clear CyberChef's recipe and input. Your module folder keeps the provided table.
3. Full tier: delete the lab folder with `rm -r ~/lab3`, then restore the `day-3-start` snapshot.

## Rules of engagement

No tool in this lab can affect anyone else's system. You hash only your own files and passwords and search only the provided table.

## Evidence required

Submit evidence pack 3 before the next teaching day, using the [evidence pack template](../../templates/evidence-pack.md).

1. **Personal values.** In the template's table, with the step each comes from:
   - the two digests of your personal results file, before and after one change, with both lines (steps 2 to 4);
   - your salted and unsalted values for one password: the unsalted digest, your two salts and your two salted digests (steps 5 to 7);
   - the table lookup result for the unsalted digest and for your salted ones (steps 8 and 9).
2. **Concept sketch.** Draw by hand, on paper, the salted-storage flow: the password, the salt, the hash function and the stored value. Label where the salt is added, and show what the store keeps for one user. Photograph it.
3. **Explanation.** In no more than 120 words: why does a salt defeat a lookup table even when two users choose the same password?

## Taxila connection

This lab answers two of Taxila's requirements. Item 6 on the security register is results file integrity: published results that cannot be altered unnoticed, because any change, even one mark, gives a different fingerprint. Item 5 is the SIS (Student Information System) password store: passwords that stay safe even if the database is stolen, because the store holds salted, slow digests rather than passwords. The Registrar will ask whether a changed grade can now be noticed: yes, if the published digest is kept where the changer cannot reach it. The Head of IT (information technology) will ask what a thief would read in a stolen password store: digests and salts, but no password, and no table that matches them.
