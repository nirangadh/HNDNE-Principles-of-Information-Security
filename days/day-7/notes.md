# Day 7: Email and databases

These notes cover the Day 7 morning. They show why an email cannot prove who sent it. They show the three checks a domain publishes to fight that, and how a defender reads the truth from a message's header. Then they turn to the database behind the Student Information System (SIS). You give the portal's account only what it needs, record what each account does, and see where encryption protects personal data and where it does not.

> **Recall.** You sign with the private key and verify with the public key.

> **Recall.** Least privilege is the minimum access an account needs.

Last semester several staff received an email that seemed to come from the Registrar. It asked them to update their bank details through a link. Two people did. Nothing in the message was true, except that it reached their inboxes looking real.

The Data Protection Officer has a second question, about the SIS itself. Suppose someone does get a password, perhaps from a message like that one. What could the stolen account read or change, and would the college ever know? Item 13 on Taxila's security register is email authentication for `taxila.example`, and item 14 is the SIS database accounts and audit log. You build both this afternoon.

## 1. How email travels

Try the demo first: [The postcard through the relays](artefacts/smtp-postcard.html). Step a prepared message from server to server, and watch what each one checks.

> **Recall.** In Year 1 you learnt that data crosses a network as messages sent between devices.

An email does not travel straight from the sender to you. It is handed from one mail server to the next, each one called a relay, until it reaches the server that holds your mailbox. The servers hand it on using the Simple Mail Transfer Protocol ([SMTP](../../glossary.md#smtp)).

Each relay adds one line to the top of the message, a received line, saying where it got the message from and when. Then it passes the message on. The message also carries a from line, the name and address you see in your inbox. Here is the problem: **the sender writes the from line**, and SMTP does not require any relay to check it. Writing `registrar@taxila.example` in the from line is as easy as writing any other address.

![A message passes from a laptop outside Taxila, through a relay outside Taxila, to Taxila's mail server. Each server that receives it adds a received line at the top of the message. The from line, which says registrar@taxila.example, is carried along unchanged, and under the relay and under Taxila's server a cross says that it did not check the from line.](img/mail-relays.svg "Each relay adds a received line and passes the message on; none of them checks the from line")

Several kinds of harm use this one gap:

| Name | What it is | Example |
|---|---|---|
| [Email spoofing](../../glossary.md#email-spoofing) | a from line that names someone who did not send the message | a message "from" `registrar@taxila.example`, sent from a server outside Taxila |
| [Phishing](../../glossary.md#phishing) | a message that tricks people into giving away a password, money or data, often through a link | "Update your bank details here" |
| Spear-phishing | phishing aimed at one person or a small group, using details about them | a message to the finance office naming last week's fee deadline |
| [Business email compromise](../../glossary.md#business-email-compromise) | a message that seems to come from a manager or a supplier, asking for a payment or a change of bank account | "This is the Registrar. Please pay this invoice today, to the new account below." |

> **You already know this.** A postcard passes through several sorting offices on its way to you. Anyone can write any return address in the corner, and no sorting office checks it. Each office stamps the card and passes it on.
>
> *Mapping:* the return address anyone can write = the from line; no office checking it = the missing sender check; each office's stamp = a received line.

> **Taxila.** The fake message from the Registrar used exactly this gap.

> **Common mistake.** "The from line proves who sent the mail." Anyone can write the from line. The truth comes from the three checks in section 2, and from the header, which you read in section 3.

> **Quick check.** A lecturer at Taxila receives a message whose from line says `registrar@taxila.example`. What does that line prove about who sent it?
>
> - [ ] That the Registrar sent it, because only the Registrar has that address
> - [ ] That it was sent from inside the college
> - [x] Nothing on its own: the sender writes the from line, and no relay has to check it
>
> **Why:** The address belongs to the Registrar, but anyone can type it into a from line. SMTP passes the message on without checking. To learn the truth you need the domain's checks and the received lines.

## 2. Three checks that fight spoofing

Try the demo first: [Three checks](artefacts/spf-dkim-dmarc.html). Turn Taxila's records on one at a time, then deliver three prepared messages and watch what each check says.

If relays do not check the from line, the domain owner must give receivers a way to check it. The owner publishes three records in the domain's public DNS (Domain Name System) entries, where any receiving server can read them.

1. **Sender Policy Framework (SPF).** A list of the servers allowed to send mail for the domain. Taxila's [SPF](../../glossary.md#spf) record says that only its own mail server, `192.0.2.25`, may send for `taxila.example`. A receiver compares the server that handed it the message with the list.
2. **DomainKeys Identified Mail (DKIM).** With [DKIM](../../glossary.md#dkim), the sending server signs each message with the domain's private key. The receiver fetches the public key from the domain's records and verifies the signature. A message changed on the way, or never signed by the domain, fails.
3. **Domain-based Message Authentication, Reporting and Conformance (DMARC).** [DMARC](../../glossary.md#dmarc) is the rule for failures. The domain in the from line must match a domain that passed SPF or DKIM. When it does not, DMARC tells receivers what to do: `none` (deliver, but report), `quarantine` (hold it, for example in a junk folder) or `reject` (refuse it).

![A message arrives at a receiving server. Three checks run in turn. SPF asks whether the sending server is on the domain's list. DKIM asks whether the signature verifies with the domain's public key. DMARC asks whether the from line's domain matches a check that passed, and applies the domain's policy: none, quarantine or reject.](img/three-checks.svg "SPF and DKIM each give a result; DMARC joins them to the from line and applies the domain's policy")

> **Recall.** You sign with the private key and verify with the public key.

DKIM is the same signing you did on Day 4, applied to mail. The private key stays on Taxila's mail server. The public key is published, so anyone can verify. A spoofer outside Taxila does not hold the private key, so cannot make a valid signature for `taxila.example`.

The records look like this. You read them; you do not need to write them.

```text
taxila.example.                  TXT  "v=spf1 ip4:192.0.2.25 -all"
mail._domainkey.taxila.example.  TXT  "v=DKIM1; k=rsa; p=(the public key)"
_dmarc.taxila.example.           TXT  "v=DMARC1; p=quarantine; rua=mailto:itadmin@taxila.example"
```

`-all` means "no other server may send for us". The `rua` address receives reports from other mail servers, so the Head of IT (information technology) can see who is sending as Taxila. At the time of writing, DMARC is a full Internet standard, and records still begin `v=DMARC1`.

These three checks protect the domain, not the message's content. Two older standards protect the content from end to end, for overview only: S/MIME (Secure/Multipurpose Internet Mail Extensions) and PGP (Pretty Good Privacy). Each lets a person sign and encrypt a message with their own key pair, so only the named reader can open it. Few people use them, because both people need keys set up first.

> **You already know this.** Picture a post office with three rules. It keeps a list of who may post letters for each company. Each company seals its letters with its own wax seal, and the post office knows what every company's seal looks like. And each company leaves a rule for unsealed or unlisted letters: deliver them, hold them, or send them back.
>
> *Mapping:* the list of who may post = SPF; the wax seal = the DKIM signature; the company's rule for failures = DMARC.

> **Taxila.** The `taxila.example` domain publishes SPF, DKIM and DMARC so receiving servers can tell real mail from spoofed (register item 13).

> **Common mistake.** "SPF, DKIM and DMARC make phishing impossible." A look-alike domain can pass its own checks. Whoever registers `sis-taxila.example` can publish its own SPF, DKIM and DMARC records, and its messages pass all three, for `sis-taxila.example`. The checks prove which domain sent a message, not that the domain is honest.

> **Quick check.** A message to Taxila's finance office says it is from `registrar@sis-taxila.example`. Its header shows `spf=pass` and `dkim=pass` for `sis-taxila.example`. Is it genuine?
>
> - [ ] Yes: both checks passed
> - [x] Not proven: the checks passed for a domain that is not Taxila's
> - [ ] No: a message cannot pass both checks unless it is a test
>
> **Why:** SPF and DKIM passed for `sis-taxila.example`, which anyone could have registered. Taxila's domain is `taxila.example`. The checks only show that the message really came from the domain it names. Reading which domain passed is the defender's job.

## 3. Reading a header

Try the demo first: [The header trail](artefacts/header-trail.html). Put a quarantined message's received lines in order, then mark the lines that show it is not genuine.

> **Recall.** A padlock on a look-alike name proves an encrypted channel to the wrong place.

Every message carries a header above the text you read. Your mail program hides most of it; "show original" or "view source" shows it all. Three parts matter to a defender.

- **The received lines, read from the bottom up.** Each relay adds its line at the top, so the oldest is at the bottom. Read upwards and you follow the real path. Only the lines your own server wrote can be trusted: anything below them was written by whoever handed the message over, and could say anything. So the lowest line your own server wrote names the true origin: the machine that handed the message to Taxila.
- **The authentication results.** Your own server writes one line saying what SPF, DKIM and DMARC found, for example `spf=fail`, `dkim=none`, `dmarc=fail`.
- **The from line against the reply-to line.** The from line is where the message claims to come from. The reply-to line is where your answer would go. When they differ, especially when the reply-to is a [look-alike domain](../../glossary.md#look-alike-domain) such as `sis-taxila.example`, your reply goes to the sender, not to the person named.

A display name, the words shown before the address, such as "Registrar, Taxila College", proves nothing. The sender types it, just like the address.

> **You already know this.** A parcel gets a stamp at each depot it passes through, and each new stamp goes on top. To trace its journey, you read the stamps from the oldest, at the bottom, upwards. A return address one letter different from your bank's is not your bank.
>
> *Mapping:* the oldest stamp at the bottom = the first relay; reading upwards = reading the received lines bottom-up; a return address one letter off = a look-alike domain.

> **Taxila.** The fake message's headers would have shown an origin that was not Taxila.

> **Common mistake.** "A convincing display name proves the sender." The display name is typed by the sender, like the address. "Registrar, Taxila College" can sit in front of any address at all. Read the address, then the authentication results, then the received lines.

> **Quick check.** A header has four received lines. Which one names the machine that really handed the message to Taxila?
>
> - [ ] The top line, because it is the newest
> - [x] The lowest line written by Taxila's own server, `mail.taxila.example`
> - [ ] The bottom line, whoever wrote it
> - [ ] The line with the most familiar name
>
> **Why:** Lines below Taxila's own were written by the sender's side, so they could be false. The top line is usually Taxila's own final step. The lowest line Taxila's server wrote records who handed the message over: that is the first fact you can trust.

## 4. Least privilege for a database

Try the demo first: [Two accounts, one leaked password](artefacts/least-privilege-db.html). Suppose the password of each account leaks in turn, and compare what each one reaches.

> **Recall.** Least privilege is the minimum access an account needs.

> **Recall.** Accounting is the record of what was done.

Behind Taxila's portal sits a database, `taxila-db`, that holds student records and grades. People do not sign in to the database. The portal does, with one database account, `taxila-portal`, and it reads and writes on everyone's behalf. So whatever that account may do, anyone who gets its password may do too.

| | An over-privileged account | A scoped account |
|---|---|---|
| What it is given | every right on every database: `ALL PRIVILEGES ON *.*` | only the reads and writes the portal's job needs |
| For the portal | read, change and drop any table; read other databases; make new accounts | read `students`; read, add and change `grades` |
| If its password leaks | the thief reaches everything | the thief reaches only what the portal reaches; dropping a table is refused |

Granting is the database's form of authorisation. The administrator writes `GRANT` statements, one right at a time, and `SHOW GRANTS` lists what an account holds. A right not granted is refused, with an error.

Recording matters as much. Auditing a database means keeping a log of who read or changed what. The general query log records every statement each account sends, as it arrives. With it, the college can answer "which account read these records, and when?". Without it, nobody can.

A scoped account also limits [injection](../../glossary.md#injection), where typed input is read as a command: its fix is a [parameterised query](../../glossary.md#parameterised-query), and the database still refuses what was never granted.

> **You already know this.** In a shop, the staff at the till have a key that opens the till drawer. They do not have the key to the safe. If a till key is lost, the finder can reach one drawer, not the safe.
>
> *Mapping:* the till key = a scoped account; the master key that opens everything = full privileges; keeping the master key away from the till = least privilege.

> **Taxila.** The account the portal uses on the Student Information System must not be able to drop tables (register item 14).

> **Common mistake.** "The application needs full database rights to work." It needs only the reads and writes its job requires. Full rights are often given at setup because they are quick, and then never taken back. The portal reads records and enters grades; it never needs to drop a table or make accounts.

> **Quick check.** Taxila's portal shows students their own records and lets lecturers enter grades. Which right does the portal's database account **not** need?
>
> - [ ] `SELECT` on `students`
> - [ ] `UPDATE` on `grades`
> - [x] `DROP` on `grades`
> - [ ] `INSERT` on `grades`
>
> **Why:** Showing records needs `SELECT`; entering and correcting grades needs `INSERT` and `UPDATE`. Nothing the portal does removes a whole table. If the portal's password leaks, a refused `DROP` is the difference between a reported incident and a lost semester of grades.

## 5. At rest, in transit, and a controller's duty

Try the demo first: [Where encryption protects](artefacts/at-rest-vs-in-transit.html). Move a grade record to disk, across the network, and through a live query, with each kind of encryption on or off.

> **Recall.** Symmetric encryption shares one secret key between both sides.

Personal data sits in three places, and each needs its own protection.

1. **At rest: on the disk and in backups.** [Encryption at rest](../../glossary.md#encryption-at-rest) encrypts the stored files. A stolen disk or backup shows only ciphertext without the key. [Transparent data encryption](../../glossary.md#transparent-data-encryption) (TDE) does this for a database: it encrypts the files under the running database, and the database decrypts them as it reads, so the application notices nothing.
2. **In transit: across the network.** Encryption in transit protects data as it moves between the portal and the database, or between a browser and the portal. [TLS](../../glossary.md#tls) (Transport Layer Security) from Day 4 is one example.
3. **In use: in a live, authorised query.** When the portal's account asks for a grade, the database decrypts it and hands it over. Neither kind of encryption stops that, because the request is allowed. Only least privilege and the log protect this place.

![A grade record in three places: on the disk and its backup, on the network between the portal and the database, and in a live query by the portal's account. Encryption at rest covers the disk and the backup. Encryption in transit covers the network. Nothing in the drawing covers the live query except the account's grants and the log.](img/where-encryption-protects.svg "Each kind of encryption covers one place; a live, authorised query is covered only by least privilege and the log")

Test and training systems need realistic data too, and they are rarely guarded as well as the real system. [Data masking](../../glossary.md#data-masking) replaces real values with realistic but false ones, such as invented names and identity numbers in the right format. Anonymising goes further: it removes or changes data until nobody can be identified from it, even by joining it with other data. The `taxila-db` you build this afternoon holds only invented rows, as a masked test copy should.

The law cares about all three places. Under Sri Lanka's Personal Data Protection Act, No. 9 of 2022, as amended, an organisation that decides why and how personal data is processed is a [data controller](../../glossary.md#data-controller). Taxila is the controller for its students' and staff's personal data. A controller must keep that data secure and be able to show what it does with it. At the time of writing, the Act's Data Protection Authority is set up, and a government order has fixed the date from which the duties on organisations apply. The Authority's own site gives the current position. The European Union's General Data Protection Regulation (GDPR) is the best-known law of the same kind. Many of its ideas, such as the controller, appear in the Sri Lankan Act.

> **You already know this.** A bank keeps its files in a locked cabinet, and sends money between branches in an armoured van. But a clerk at the desk, allowed to read a customer's file, simply opens it and reads it. Neither the cabinet's lock nor the van stops the clerk.
>
> *Mapping:* the locked cabinet = encryption at rest; the armoured van = encryption in transit; a clerk reading a file at the desk = an authorised query, which neither lock stops.

> **Taxila.** The Data Protection Officer asks whose data the Student Information System holds and who can read it.

> **Common mistake.** "Encryption at rest stops someone who has the portal's password." It does not. The database decrypts data for any account allowed to read it. Encryption at rest protects a stolen disk or backup; a stolen password is stopped only by least privilege, and seen only by the log.

> **Quick check.** Taxila's SIS database uses transparent data encryption. A thief learns the portal account's password and reads every student's record through it. What would have limited the harm?
>
> - [x] An account that could read only what the portal needs, and a log that showed the reads
> - [ ] A longer key for the transparent data encryption
> - [ ] Encrypting the backups as well
>
> **Why:** Transparent data encryption protects the files on disk. The thief never touched the disk: the database decrypted each record for an account allowed to read it. A longer key, or encrypted backups, protect the same place again. Only the account's grants limit the reach, and only the log shows it happened.

## Before the lab

This afternoon you read the header of a message that was held in quarantine, and find its true origin and its tells. Then you build a copy of the SIS database and give the portal's account only what it needs. You test that a table drop is refused, then turn on the query log and read it. Bring these notes, open at sections 3 and 4. Full-tier students: start your Kali virtual machine before the session.

## Reading

- Pfleeger, C. P., Pfleeger, S. L. and Coles-Kemp, L., *Security in Computing*, 6th ed., chapter 4, section 4.5, on email and message attacks, and chapter 9, section 9.6, on email and message security. Then chapter 7, sections 7.1 to 7.4, on data and databases, for this afternoon's lab.
- Personal Data Protection Act, No. 9 of 2022, Sri Lanka, as amended by Act No. 22 of 2025: the duties of a controller.

Next: Day 8, networks: threats and defences. You see what a defender can learn by watching the traffic on Taxila's network, and how firewalls and separate zones keep it apart.
