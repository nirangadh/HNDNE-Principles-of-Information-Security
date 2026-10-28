# Glossary

The words this module teaches, filed under the day that first teaches each one. Each word has a meaning in at most 40 words and an example at Taxila College. Each teaching day adds its words here.

## Day 1

### Data classification
Sorting data into classes by the harm its leak would cause, so that each class gets the protection it needs. Taxila uses four classes: public, internal, confidential and restricted.

*Taxila example:* the course catalogue is public, while exam papers before the exam are restricted.

### Confidentiality
The security property that only authorised people can read the data. It is lost when someone reads what they have no right to read, even if nothing is changed.

*Taxila example:* the draft exam paper read by students before the exam was a loss of confidentiality.

### Integrity
The security property that the data has not been changed without permission. It is lost when data is altered, even if nobody reads it.

*Taxila example:* the final grade that was raised in the student records was a loss of integrity.

### Availability
The security property that the data and the service are there when they are needed. It is lost when people cannot reach them, even if nothing is read or changed.

*Taxila example:* the fee payment page that stopped responding on the last evening for fees was a loss of availability.

### Authenticity
The security property that something really comes from who it claims to come from. A message can be private, unchanged and on time, and still fail authenticity.

*Taxila example:* the email that seemed to come from the Registrar, but did not, failed authenticity.

### Accountability
The security property that you can prove who did what, and when. It needs a record that names the person behind each action.

*Taxila example:* the changed grade failed accountability, because nothing recorded who changed it.

### Non-repudiation
The strong form of accountability: a person cannot later deny an action they took, because the record proves it.

*Taxila example:* if each grade change were recorded against the lecturer's own sign-in, a lecturer could not simply deny making it.

### Asset
Anything worth protecting: data, a system, a service, or the organisation's good name. An asset may or may not have been bought.

*Taxila example:* the grades in the student records are an asset; so is the college's reputation with employers.

### Threat
Anything that could cause harm to an asset: a person, a group, or an event. A threat needs a weakness to use before it becomes a risk.

*Taxila example:* a curious student near the exam paper folder is a threat to the exam papers.

### Vulnerability
A weakness that lets a threat cause harm. A vulnerability is not a person; it is the gap the person could use.

*Taxila example:* a shared folder that anyone at the college can open is a vulnerability for the exam papers.

### Risk
How likely a harm is, combined with how much it would cost. Taxila scores likelihood and impact from 1 to 5 each and multiplies them. With no threat or no weakness, there is no risk.

*Taxila example:* exam papers in a folder anyone can open, with a curious student nearby: likelihood 3, impact 5, risk 15.

### Control
Anything that lowers a risk by preventing, detecting or correcting harm. Several independent controls in layers, so that one failing does not leave the asset open, is called defence in depth.

*Taxila example:* a locked server-room door prevents, a camera at the door detects, and a weekly backup corrects.

## Day 2

### Plaintext
The readable form of a message, before it is encrypted or after it is decrypted. Anyone who sees plaintext can read it.

*Taxila example:* the draft exam paper, as the lecturer wrote it, is plaintext.

### Ciphertext
The scrambled form of a message after encryption. Without the key it cannot be read, even by someone who knows the method used.

*Taxila example:* in the encrypted exam paper store, every paper is kept as ciphertext.

### Key
The secret value that turns plaintext into ciphertext and back. All the possible keys make the key space; trying every one is brute force, so the key space must be too large to try.

*Taxila example:* a Caesar shift's twenty-five keys fall at once; a 256-bit key for the Advanced Encryption Standard (AES) does not.

### Cipher
The method, or algorithm, that uses a key to encrypt and decrypt. The Caesar shift is a hand cipher; the Advanced Encryption Standard (AES) is a modern one.

*Taxila example:* the exam paper store uses a standard, public cipher with a secret key.

### Kerckhoffs's principle
The rule that a cipher must stay secure even when everything about it, except the key, is public. Security rests in the key, not in keeping the method secret.

*Taxila example:* anyone may know that the exam paper store uses the Advanced Encryption Standard (AES); only its key must stay secret.

### Frequency analysis
Breaking a hand cipher by counting how often each symbol appears, and matching the counts to the language. In English the commonest letter is usually e.

*Taxila example:* a home-made letter-swap code for passing answers would fall to one evening of counting.

### Encoding
Changing the form of data so that it can be stored or sent, with no key. Base64 is an example. Anyone who knows the encoding can reverse it, so it protects nothing.

*Taxila example:* a password written in Base64 in a configuration file is as readable as plain text.

### Steganography
Hiding the fact that a message exists, for example in tiny changes to a picture's colours. It needs no key, so the message can be read once someone knows where to look.

*Taxila example:* a note hidden inside a campus photograph stays secret only while nobody looks for it.

### Symmetric encryption
Encryption that uses one shared key both to encrypt and to decrypt. It is fast, so it suits large data. The Advanced Encryption Standard (AES) is the modern choice.

*Taxila example:* Colombo and Kandy can both open a paper encrypted with the one AES key they share.

### Key distribution problem
The difficulty of getting one shared symmetric key to the other side without anyone intercepting it on the way.

*Taxila example:* Kandy needs the key to tonight's paper, but posting, emailing or phoning it could let someone else read it.

### Asymmetric encryption
Encryption that uses a pair of keys: anyone may encrypt with the public key, and only the matching private key decrypts. Rivest, Shamir and Adleman (RSA) is the best-known method.

*Taxila example:* Kandy locks a message with Colombo's public key, and only Colombo can open it.

### Hybrid encryption
Using both families together. Asymmetric methods set up a fast symmetric key, by carrying it or agreeing it, and the symmetric key then encrypts the data.

*Taxila example:* Kandy encrypts the paper with a fresh key for the Advanced Encryption Standard (AES), then locks that key with Colombo's public key.

## Day 3

### Hash function
A method that takes an input of any size and returns a short value of fixed length, the digest. The same input always gives the same digest, and the digest cannot be turned back into the input.

*Taxila example:* the Registrar runs each results file through a hash function before publishing it.

### Digest
The fixed-length value a hash function returns. It identifies the data like a fingerprint, but does not hide it. Any change to the data, even one character, gives a completely different digest.

*Taxila example:* the digest published beside a results file lets anyone check that the file is unchanged.

### SHA-256
The Secure Hash Algorithm at 256 bits (SHA-256): the hash function in current use. Its digest is sixty-four hexadecimal characters. Older ones, MD5 (Message Digest 5) and SHA-1 (Secure Hash Algorithm 1), are deprecated.

*Taxila example:* the lab fingerprints each student's results line with SHA-256.

### Avalanche effect
The property that changing one character of the input changes the digest completely: about half of its bits flip, with no visible link between the old digest and the new one.

*Taxila example:* a results file changed by one mark has a digest that differs in almost every character.

### Preimage resistance
The property that, given a digest, nobody can find an input that made it. A hash function can only be run forwards; there is no key and no way back.

*Taxila example:* a stolen file of password digests does not give back the passwords themselves.

### Collision resistance
The property that nobody can find two different inputs with the same digest. A hash function is retired once such pairs, called collisions, can be found.

*Taxila example:* nobody can make a second results file with the same digest as the real one.

### Lookup table
A table of digests computed in advance, each beside the input that made it, such as common passwords. A dictionary is the word list; a rainbow table is a large, compact table. It matches digests; it never reverses one.

*Taxila example:* an unsalted digest of `password123` from the SIS (Student Information System) store is found in such a table at once.

### Salt
A value, different for every user, added to a password before hashing. It is stored in plain sight beside the digest and need not be secret. It makes identical passwords store differently.

*Taxila example:* two lecturers who chose the same password have different salts, so different stored digests.

### Slow password hash
A hash made slow on purpose for storing passwords, by repeating its work many times. bcrypt, Argon2 and the Password-Based Key Derivation Function 2 (PBKDF2) are examples. Each guess then costs a guesser the same delay.

*Taxila example:* the Student Information System stores each salted password with PBKDF2 at hundreds of thousands of rounds.

### Pepper
One further secret value, the same for every user, added to each password before hashing. Unlike a salt, it is kept apart from the database, so a stolen database alone is not enough.

*Taxila example:* the Student Information System keeps its pepper in the server's own settings, not in the password store.

### HMAC
A hash-based message authentication code: a keyed hash that mixes a shared secret key with a message. Only key-holders can make or check its seal. It shows the message is unchanged, not which key-holder sent it.

*Taxila example:* the examinations offices in Colombo and Kandy share a key and seal each results file with it.
