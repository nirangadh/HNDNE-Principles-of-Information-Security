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

## Day 4

### Digital signature
A value made by hashing a document and signing the digest with a private key. Anyone checks it with the matching public key. It proves who signed and that nothing changed, and hides nothing.

*Taxila example:* the Registrar signs each transcript, so an employer can check it without phoning the college.

### Certificate
A signed file, in the X.509 format, that says a public key belongs to a name. It holds a subject, an issuer, a validity period, the public key and the issuer's signature.

*Taxila example:* the portal's certificate says its key belongs to `sis.taxila.example`.

### Certificate authority
A certificate authority (CA) is a trusted third party that checks a key belongs to a name, then vouches for it by signing a certificate. It can also revoke a certificate, for example after a key leaks.

*Taxila example:* an authority checks that Taxila controls `sis.taxila.example` before signing the portal's certificate.

### Chain of trust
The path from a site's certificate, through the intermediate authority that signed it, to a root certificate the browser already trusts. If any link fails, the browser warns and stops.

*Taxila example:* the browser trusts the portal because its certificate chains up to a root in the trust store.

### Root certificate
The self-signed certificate of an authority at the top of a chain. Browsers and operating systems keep a list of trusted roots, called the trust store, and trust every chain that ends at one.

*Taxila example:* the portal's chain ends at a root certificate already in every student's browser.

### Self-signed certificate
A certificate signed with its own subject's key, so its issuer and subject are the same. It is valid in form, but no authority vouches for it, so browsers warn about it.

*Taxila example:* the certificate you make for `sis.taxila.example` in the lab is self-signed.

### Certificate signing request
A certificate signing request (CSR) is a message holding a public key and the name wanted, signed with the matching private key, sent to an authority to ask it to sign a certificate.

*Taxila example:* the Head of IT (information technology) sends a request for `sis.taxila.example` to an authority.

### TLS
Transport Layer Security (TLS): the protocol that secures a connection. Its handshake agrees a session key and proves the server's identity with its certificate; then everything travels encrypted. Version 1.3 is current.

*Taxila example:* the portal accepts connections only over TLS.

### HTTPS
Hypertext Transfer Protocol Secure (HTTPS): ordinary web traffic, HTTP (Hypertext Transfer Protocol), carried inside TLS (Transport Layer Security). The padlock shows an encrypted channel and a vouched name, not an honest site.

*Taxila example:* students open the portal at an address that starts `https://`.

### Session key
A fast symmetric key that both sides of a TLS (Transport Layer Security) connection agree during the handshake, without sending it. It encrypts everything that follows, and is thrown away when the connection ends.

*Taxila example:* each student's visit to the portal uses its own session key.

### HSTS
A rule in the Hypertext Transfer Protocol (HTTP) called HTTP Strict Transport Security (HSTS): a site tells the browser to connect to it only over secure web from then on, refusing plain web.

*Taxila example:* the portal sends HSTS, so a student's browser never opens it over plain web.

### Certificate pinning
Building an application so it accepts only one particular certificate or key for its own server, even if another authority vouches for a different one. Mainly used by mobile apps, such as banking apps.

*Taxila example:* a Taxila phone app could pin the portal's key, so it refuses any other.

## Day 5

### Authentication
The process that checks a claimed identity, for example by matching a password against its stored salted digest. It is the first of three processes, called AAA (authentication, authorisation and accounting). It is not authenticity, which is a property.

*Taxila example:* the SIS (Student Information System) checks `lecturer01`'s password before accepting who is signing in.

### Authorisation
The process that decides what an authenticated identity may do: which resources it may open and which actions it may take. It comes after authentication.

*Taxila example:* the SIS (Student Information System) lets `lecturer01` enter grades only for the modules `lecturer01` teaches.

### Accounting
The process that records what each identity did: who, what and when. It produces the accountability property, so an action can be traced to a person.

*Taxila example:* the SIS (Student Information System) log records "`lecturer01` changed a grade in module 2", so a changed grade can be traced.

### Authentication factor
One kind of evidence of who you are: something you know (a password), something you have (a phone or security key), or something you are (a fingerprint).

*Taxila example:* a lecturer's password is one factor, and the code on the lecturer's phone is another.

### Multi-factor authentication
Multi-factor authentication (MFA) asks for two or more factors of different kinds, so a stolen password alone is not enough. Two passwords are still one factor.

*Taxila example:* staff sign in to the SIS (Student Information System) with a password and a code from their phone.

### Credential stuffing
Replaying leaked pairs of usernames and passwords, taken from another site's leak, against a different site. It works wherever people reused a password, and fails against a second factor.

*Taxila example:* a lecturer's password leaked from a shopping site stops at the SIS (Student Information System) second factor.

### Discretionary access control
Discretionary access control (DAC) lets the owner of each resource decide who may use it. It is flexible, but access spreads as owners share freely.

*Taxila example:* a lecturer shares a folder of module marks with a colleague, with nobody else involved.

### Mandatory access control
Mandatory access control (MAC) lets the system decide access by labels and clearances that users, even owners, cannot override. It is strict and consistent, but rigid.

*Taxila example:* an exam paper labelled restricted opens only for accounts cleared for restricted, whoever wrote it.

### Role-based access control
Role-based access control (RBAC) gives permissions to roles designed from jobs, then assigns people to roles. A person changing job moves to another role.

*Taxila example:* `student01` is assigned to the student role, which may read only its own record.

### Least privilege
Giving each account the minimum access its job needs, for no longer than needed. The area a stolen credential can reach, its blast radius, then stays small.

*Taxila example:* `lecturer01` can enter grades only for the lecturer's own modules, so a leaked password reaches little.

### Separation of duties
Making a second person approve a sensitive action, so that no one person can complete it alone.

*Taxila example:* a lecturer may ask to change a released grade, but only the Registrar's approval completes it.

### Hardening
Bringing a server to a safe baseline: only needed accounts and services, tight file permissions, patches installed, and logging on. Each change shrinks the attack surface, everything an attacker could try to reach.

*Taxila example:* the Head of IT (information technology) turned off services nobody used on the SIS (Student Information System) server.

## Day 6

### Session token
A long random value the server gives your browser after you sign in. Every later request carries it, so whoever holds the token is treated as you until it expires.

*Taxila example:* the portal sends each student a session token in a cookie after sign-in, and reads it on every page instead of asking for the password again.

### Cookie attribute
A setting the server adds to a cookie that tells the browser when it may send the cookie and who may read it. HttpOnly, Secure and SameSite are the three that guard a session cookie.

*Taxila example:* the portal's session cookie carries all three attributes (register item 12).

### SameSite
A cookie attribute that tells the browser to leave the cookie off requests that another site started. Strict leaves it off even when you follow a link; Lax still allows a followed link.

*Taxila example:* with this attribute set on the portal's session cookie, a form posted to the portal from another site arrives with no session, so the portal refuses it.

### Cross-site request forgery
Cross-site request forgery (CSRF): a page on another site makes your browser send a request to a site where you are signed in. The browser adds your session cookie, so the request looks like yours.

*Taxila example:* a page elsewhere makes a signed-in lecturer's browser post a form to the portal; SameSite keeps the lecturer's cookie off that request.

### Security misconfiguration
A weakness in how a system is set up rather than how it is written, such as a default password or an admin page open to everyone. It needs no clever trick to use.

*Taxila example:* an admin page on the portal left on the login it shipped with is an open door.

### OWASP Top 10
The Open Worldwide Application Security Project's (OWASP) list of the ten most common web application risks, revised every few years. It is a map, not a checklist of every flaw.

*Taxila example:* the Head of IT (information technology) uses this list to check the portal's injection, misconfiguration and session handling.

### Injection
A flaw where input a user types is read as part of a command the application runs, instead of only as data. The fault is in how the application builds the command.

*Taxila example:* the portal must treat a login as data, never as part of the database question it builds.

### SQL injection
Injection into a database query. Input joined into the query, which is written in Structured Query Language (SQL), can add a condition that is always true, so one record asked for becomes every record.

*Taxila example:* a crafted login that returns every student's record, until the portal uses a parameterised query.

### Parameterised query
A database query written with placeholders for its values. The input travels beside the query, as data, so it can never change the question the database is asked.

*Taxila example:* the portal's login uses one, so a crafted login matches no record while a real sign-in still works.

### Cross-site scripting
A flaw where a page shows a user's input as live script, which then runs in another user's browser. It is called cross-site scripting (XSS), and output encoding stops it.

*Taxila example:* a comment left on a portal page must not run a visitor's script in another student's browser.

### Output encoding
Turning the characters of a user's input, such as the angle brackets of markup, into their plain-text form before a page shows it, so the input is only ever displayed, never run.

*Taxila example:* the portal encodes every comment it shows, so a script left in one appears as plain text.

### Input validation
Checking that input looks the way it should, and turning away what does not, before the application uses it. A useful layer, but not a replacement for a parameterised query or output encoding.

*Taxila example:* the portal turns away a login of the wrong shape early, as one layer among several.

## Day 7

### Business email compromise
A message that seems to come from a manager or a supplier and asks for a payment, or a change to the bank account a payment goes to. It needs no link or attachment, only trust.

*Taxila example:* a message "from" the Registrar asks the finance office to pay an invoice today to a new account.

### Data controller
The organisation that decides why and how personal data is processed. Under Sri Lanka's Personal Data Protection Act the controller must keep that data secure and be able to show what it does with it.

*Taxila example:* Taxila College is the controller for its students' and staff's personal data in the SIS (Student Information System).

### Data masking
Replacing real values with realistic but false ones, so that a test or training system has data of the right shape without the real people. Anonymising goes further: nobody can be identified from what is left.

*Taxila example:* the `taxila-db` copy built in the Day 7 lab holds only invented students and grades.

### DKIM
DomainKeys Identified Mail: the sending server signs each message with the domain's private key, and the receiver verifies it with the public key published in the domain's records. It is a digital signature applied to mail.

*Taxila example:* `mail.taxila.example` signs outgoing mail; the public key sits at `mail._domainkey.taxila.example`.

### DMARC
Domain-based Message Authentication, Reporting and Conformance: a domain's rule for failures. The from line's domain must match one that passed SPF (Sender Policy Framework) or DKIM (DomainKeys Identified Mail); if not, deliver, quarantine or reject.

*Taxila example:* `taxila.example` publishes `p=quarantine`, so a spoofed "Registrar" message is held, not delivered.

### Email spoofing
Sending a message whose from line names someone who did not send it. It works because the sender writes the from line, and mail servers are not required to check it.

*Taxila example:* a message with the from line `registrar@taxila.example`, sent from a server outside Taxila.

### Encryption at rest
Encrypting data where it is stored, on disks and in backups, so that a stolen disk shows only ciphertext. Encryption in transit protects the same data while it crosses a network. Neither stops an authorised query.

*Taxila example:* the SIS (Student Information System) database's files and its weekly backup disk are encrypted at rest.

### Look-alike domain
A domain name chosen to look like a real one, such as a name with one letter changed or an extra word. It can publish its own records and pass its own checks.

*Taxila example:* `sis-taxila.example`, the reply-to domain in the fake Registrar message, is not Taxila's.

### Phishing
A message that tricks people into giving away a password, money or data, often through a link to a look-alike page. Spear-phishing is phishing aimed at one person or a small group, using details about them.

*Taxila example:* last semester's message asked staff to update their bank details through a link; two people did.

### SMTP
The Simple Mail Transfer Protocol (SMTP): the way mail servers hand a message from one to the next until it reaches the recipient's server. It does not require any server to check the from line.

*Taxila example:* `mail.taxila.example` receives Taxila's mail from other servers by SMTP.

### SPF
The Sender Policy Framework: a record a domain publishes, listing the servers allowed to send mail for it. A receiving server compares the server that handed over a message with that list.

*Taxila example:* `taxila.example` lists only `192.0.2.25`, its own mail server, and ends with `-all`.

### Transparent data encryption
Transparent data encryption (TDE): encryption of a database's files on disk, done by the database itself. The database decrypts as it reads, so applications notice nothing, and a stolen disk or backup stays unreadable.

*Taxila example:* the SIS (Student Information System) database could use it, so that a stolen backup disk is useless to a thief.

## Day 8

### Address poisoning
Sending a false Address Resolution Protocol (ARP) reply that ties another machine's IP (Internet Protocol) address to your own hardware address, so traffic meant for that machine comes to you. It needs a machine on the same segment.

*Taxila example:* a false reply claiming the staff network's gateway, `10.10.0.1`, would send a lecturer's traffic for the SIS (Student Information System) through another machine.

### Address Resolution Protocol
The Address Resolution Protocol (ARP): how a machine finds the hardware address that goes with an IP (Internet Protocol) address on its own network. It asks everyone, and believes any reply, with no check on who answers.

*Taxila example:* a lecturer's laptop asks "Who has `10.10.0.1`?" before it can send anything to the SIS (Student Information System) through the gateway.

### Demilitarised zone
A demilitarised zone (DMZ): a network zone between two firewalls that holds the servers the public must reach. The outer firewall lets the public in to it; the inner firewall keeps it out of the inside networks.

*Taxila example:* `www.taxila.example`, `mail.taxila.example` and `pay.taxila.example` sit in the DMZ; the SIS (Student Information System) stays behind the inner firewall.

### Denial of service
An attack on availability that floods a service so real users cannot reach it. A distributed denial of service uses many machines at once, so blocking one sender does not stop it.

*Taxila example:* a flood aimed at the fee payment page on the last evening of payment would keep students from paying.

### Intrusion detection system
An intrusion detection system (IDS): a system that watches a copy of the traffic, out of its path, and raises an alert when it recognises trouble by a known pattern (signature) or unusual behaviour (anomaly). Traffic still flows.

*Taxila example:* an IDS watching the server room alerts the Head of IT (information technology) when one address is claimed by two hardware addresses.

### Intrusion prevention system
An intrusion prevention system (IPS): a system that sits in the path of network traffic and blocks what it recognises as trouble, by signature or by anomaly. A false alarm blocks real users too.

*Taxila example:* an IPS in front of the servers could block a flood from the student Wi-Fi before it reaches the portal.

### Man-in-the-middle
A machine in the middle sits between two parties who each believe they talk directly, and relays their traffic. It can read what is not encrypted, and change or drop what it relays.

*Taxila example:* a machine on the staff network that poisoned a laptop's address cache would sit in the middle of that laptop's traffic to the SIS (Student Information System).

### Sniffing
Reading the traffic that passes on a shared network segment. It is passive: the watcher only receives, so it leaves no trace. Unencrypted content can be read; encrypted content cannot.

*Taxila example:* on the student Wi-Fi, anyone can sniff a plain-web login, but not a secure-web one.

### Stateful firewall
A firewall that remembers every connection opened through it. It lets in packets that belong to a known connection, and drops packets that claim to be replies to connections nobody opened.

*Taxila example:* the firewall in front of the SIS (Student Information System) drops a flood of fake replies from the student Wi-Fi, because no connection in its table matches them.

### Traffic analysis
Learning from the outside of network traffic, without its content: who talks to whom, on which port, when, how often and how much. Encryption hides the content, not these patterns.

*Taxila example:* a watcher on the Wi-Fi sees that a laptop talks to the SIS (Student Information System) every evening, though not what it sends.

### Virtual private network
A virtual private network (VPN): an encrypted tunnel that carries traffic between two places across the internet, using the Internet Protocol Security suite (IPsec) or Transport Layer Security (TLS). Watchers see only tunnel packets between the two ends.

*Taxila example:* the Kandy campus reaches the SIS (Student Information System) through a VPN to Colombo instead of over the open internet.

### Web application firewall
A web application firewall (WAF): an application-layer firewall built for web traffic. It reads each web request and drops one that carries a known attack pattern. It can read encrypted requests only if it ends the encryption itself.

*Taxila example:* a WAF in front of `sis.taxila.example` could drop a login request carrying an injection string.
