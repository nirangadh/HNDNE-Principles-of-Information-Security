# Practice question 3: an online bookshop

This practice question applies the Day 3 ideas, hashing, salting and slow password hashing, to an online bookshop. Attempt it in writing before you read the answer guidance. It carries 20 marks.

## The setting

A small online bookshop in Sri Lanka has about 40,000 customer accounts. Each customer signs in with an email address and a password. Many customers use the same password on other sites, such as their email and their bank.

The bookshop's developer stores the SHA-256 (Secure Hash Algorithm, 256 bits) digest of each password, with no salt. The developer chose SHA-256 "because it is fast, so logins are quick".

Last week, a backup copy of the customer table was left on a file-sharing link that anyone could open. It has been copied. The owner tells customers: "Your passwords were hashed, so nothing has been lost, and nobody needs to do anything."

Here are four rows of the copied table:

| Customer | Stored digest |
|---|---|
| Customer A | `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8` |
| Customer B | `e55d399c0939c85f98fdbaabc565a19ab1f0c3266614205da7c8a97e0f979ae8` |
| Customer C | `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8` |
| Customer D | `ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f` |

## The question

**(a)** Explain what a hash function does. Then explain two properties of a hash function that make a digest suitable for storing passwords, and say why a system should store a digest rather than the password itself. **(6 marks)**

**(b)** Using the four rows above, describe what someone who copied the table can learn, and how. Then design a better way for the bookshop to store passwords: say what each row of the table should hold, and what the system does when a customer signs in. **(7 marks)**

**(c)** Evaluate the developer's reason for choosing SHA-256, and the owner's message to customers. Recommend what the bookshop should use instead, with one cost of your recommendation. Then say why encrypting the passwords would be the wrong fix, and what customers should be told to do. **(7 marks)**

## Answer guidance

Read this only after you have written your own answer.

**Part (a).** A hash function takes an input of any size and returns a digest of fixed length; the same input always gives the same digest. Two properties make it suitable for passwords. Preimage resistance: from a digest, nobody can work back to the password, because there is no key and no reverse. The avalanche effect: a password that differs by one character gives a completely different digest, so a digest gives no clue about a nearby password. Collision resistance is also accepted: two different passwords will not share a digest. A system stores a digest because it never needs the password itself: at sign-in it hashes what the customer typed and compares the two digests. So a stolen table, or a curious member of staff, does not see the passwords. A strong answer also says that hashing is not encryption: nothing is locked, and nothing can be unlocked.

**Part (b).** Two things can be learnt. First, customers A and C have the same digest, so they have the same password, whatever it is. Second, common passwords can be found in a lookup table: a table of common passwords, hashed in advance. The digests of A and C are the SHA-256 of `password`, and D's is the SHA-256 of `password123`, so a table finds them at once. The table does not reverse the hash; it matches digests that were computed in advance. Customer B's digest matches nothing in such a table, because B chose an uncommon password; it can still be guessed, but only one try at a time. Because customers reuse passwords, the email and bank accounts of A, C and D are now at risk too. A better design gives each customer a unique, random salt. The row holds the email, the salt and the digest of the password with the salt added. The salt is stored in plain sight; it does not need to be secret. At sign-in, the system reads that customer's salt, adds it to the typed password, hashes the result, and compares it with the stored digest. With salts, the rows of A and C would differ, and no table built in advance would hold either. The best answers use a slow password hash for this step, not plain SHA-256, and may add a pepper kept apart from the database.

**Part (c).** The developer's reason is weak. Speed is good for checking files, but for passwords it helps the guesser: a fast hash lets someone try millions of guesses a second against a copied table. The owner's message is wrong. Unsalted digests of common passwords are found at once in a lookup table, and identical digests show who shares a password, so some passwords are effectively known now. The bookshop should store passwords with a slow password hash such as Argon2, bcrypt or PBKDF2 (the Password-Based Key Derivation Function 2), with a unique salt for each customer. Its cost: each sign-in takes a little longer and uses more of the server's time; for a guesser, every single guess costs the same extra time. Encrypting the passwords would be the wrong fix. Anything encrypted can be decrypted, and whoever holds the key could read every password. And the key would sit on the same server as the table. Customers should be told plainly about the leak, asked to change their bookshop password, and told to change the same password anywhere else they have used it. Strong answers weigh the trade-off: a slightly slower sign-in against a much more costly guess. They also note that a salt alone stops tables but not guessing, which is why salt and slow hashing are used together.
