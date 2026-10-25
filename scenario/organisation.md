# Taxila College

*A fictional organisation created for teaching. Any resemblance to a real college is coincidental.*

## 1. Profile

Taxila College is a private higher-education college in Sri Lanka. Its main campus is in Colombo and a smaller branch campus is in Kandy. About 3,200 students study for diplomas and degrees in computing, business and design, taught by about 180 staff.

The college runs a handful of systems that every student already knows from the outside:

| System | What it holds or does | Who uses it |
|---|---|---|
| Student Information System (SIS) | student records, grades, fee balances, national identity card numbers | Registrar's office, lecturers (grades only), students (their own record) |
| Learning Management System (LMS) | course pages, coursework submissions, feedback | lecturers and students |
| Fee payment page | lets students pay fees online through a bank's payment gateway; Taxila never stores card numbers | students, the finance office |
| Email | staff and student mailboxes at `taxila.example` | everyone |
| Exam paper store | a shared folder where lecturers place exam papers before an exam | lecturers, the examinations office |
| Website | the public course catalogue and news | the public |
| Campus networks | a staff network, a student Wi-Fi network, and the server room | everyone |

The servers sit in a small server room on the second floor of the Colombo building. The Kandy campus has one small rack and reaches the SIS over the internet. Backups go to an external disk once a week.

## 2. What went wrong

Last semester four things happened, and together they are the reason the college now wants a security programme.

1. **A leaked paper.** A draft exam paper appeared on a student messaging group two days before the exam. The paper had to be rewritten overnight. Nobody could say how it left the exam paper store.
2. **A changed grade.** A student's final grade in the SIS was found to be higher than the lecturer had entered. The SIS showed the new grade but not who had changed it, or when.
3. **A dead deadline night.** On the last evening of fee payment, the fee payment page stopped responding for three hours. Hundreds of students missed the deadline and the finance office spent a week sorting out late fees.
4. **A message from "the Registrar".** Several staff received an email that appeared to come from the Registrar, asking them to update their bank details through a link. Two people did.

Each of the ten teaching days adds part of the answer.

## 3. The three voices

**The Registrar** owns student records, exams and results. Wants results that are correct, released on time, and trusted by employers. Asks: "Can we prove who changed it?"

**The Head of IT** runs every system with a team of four. Wants changes that are cheap, that the team can operate, and that do not break classes during the semester. Asks: "What do we change, and what will it break?"

**The Data Protection Officer** was appointed recently under the Personal Data Protection Act. Wants to know whose personal data the college holds, who can read it, and how the college would know if someone read it who should not. Asks: "Whose data is this, and how would we know?"

**You** join the college's IT office as a trainee security analyst. Each teaching day is one day of your placement.

## 4. Requirements that drive the programme

| Requirement | Why it exists in the story | Register item(s) |
|---|---|---|
| Know what data the college holds and how sensitive each kind is | The Data Protection Officer's first question | 1 |
| A living list of risks with an owner for each | The Head of IT cannot fix everything at once | 2 |
| Exam papers unreadable to anyone without the key, even if the folder leaks | The leaked paper | 3, 4 |
| Passwords that stay safe even if the SIS database is stolen | Staff and students reuse passwords | 5 |
| Published results that cannot be altered unnoticed | The changed grade | 6, 7 |
| Transcripts an employer can verify without phoning the college | The Registrar's reputation | 7 |
| The portal and the SIS reachable only over encrypted connections that prove they are genuine | The fake Registrar email linked to a look-alike page | 8 |
| Every grade change attributable to a named person, and approved by a second person | The changed grade | 9, 14 |
| Servers that run only what they need | The Head of IT's audit found services nobody used | 10 |
| A portal that does not trust what users type | Web applications are the most attacked part of any college | 11, 12 |
| Email that receiving servers can check really came from `taxila.example` | The fake Registrar email | 13 |
| A database that each account can touch only as far as its job needs | The Data Protection Officer | 14 |
| Student Wi-Fi kept apart from staff and servers | Thousands of unmanaged devices | 15 |
| Someone notices when something unusual happens | Nobody noticed the grade change | 16 |
| The Kandy campus reaches the SIS privately | Kandy reaches the SIS over the internet today | 17 |
| Staff who recognise a phishing message | Two people followed the link | 18 |
| The fee payment page and the SIS back within a stated time after a failure, with little data lost | The dead deadline night | 19 |

## 5. Constraints

- A small budget and a team of four: controls must be ones a small team can run.
- No changes to production systems during exam weeks.
- Taxila never stores payment card numbers; the bank's gateway does.
- All lab work is done on your own laptop, on your own virtual machine and the module's provided application and files, never against Taxila's real systems (there are none) or anyone else's.

## 6. Data classification (used on Day 1)

| Class | Meaning at Taxila | Examples |
|---|---|---|
| Public | may be published | course catalogue, news, campus addresses |
| Internal | for staff and students, harmless if leaked but not for publication | timetables, staff directory, room bookings |
| Confidential | personal or business data whose leak harms a person or the college | student records, grades, fee balances, staff salaries |
| Restricted | data whose leak causes serious harm or breaks the law; the fewest people possible | exam papers before the exam, national identity card numbers, the SIS administrator credentials |

## 7. The security register you will build

Each day adds numbered items to Taxila's security register. The [register picture](architecture.svg) shows where each item sits.

| No. | Item | Kind | Mainly protects | Day |
|---|---|---|---|---|
| 1 | Data inventory and classification | governance | Confidentiality | 1 |
| 2 | Risk register | governance | Confidentiality, Integrity, Availability | 1, 9 |
| 3 | Encrypted exam paper store | control | Confidentiality | 2 |
| 4 | Key exchange with the Kandy campus | control | Confidentiality | 2 |
| 5 | SIS password store | control | Confidentiality, Authenticity | 3 |
| 6 | Results file integrity | control | Integrity | 3 |
| 7 | Signed transcripts | control | Integrity, Authenticity, Accountability | 4 |
| 8 | Portal certificate and TLS | control | Confidentiality, Authenticity | 4 |
| 9 | Accounts, roles and multi-factor sign-in | control | Authenticity, Accountability | 5 |
| 10 | Hardened server baseline | control | Confidentiality, Integrity, Availability | 5 |
| 11 | Portal input handling | control | Confidentiality, Integrity | 6 |
| 12 | Portal sessions and cookies | control | Confidentiality, Authenticity | 6 |
| 13 | Email authentication for taxila.example | control | Authenticity | 7 |
| 14 | SIS database accounts and audit log | control | Confidentiality, Accountability | 7 |
| 15 | Firewalls and network zones | control | Confidentiality, Availability | 8 |
| 16 | Intrusion detection and monitoring | control | Integrity, Accountability | 8 |
| 17 | VPN between campuses | control | Confidentiality | 8 |
| 18 | Staff awareness programme | control | Confidentiality, Authenticity | 9 |
| 19 | Continuity plan and backups | governance | Availability | 9, 10 |

## 8. Names used in labs

| Thing | Name |
|---|---|
| College domain | `taxila.example` (a reserved example domain; it never resolves on the internet) |
| Systems | `sis.taxila.example`, `lms.taxila.example`, `pay.taxila.example`, `mail.taxila.example`, `www.taxila.example` |
| Your virtual machine | `kali` (full tier) |
| Provided web application | `taxila-portal` (a small application with its own test, run with Python inside your VM, full tier) or the portal's practice-application demo (floor tier) |
| Provided database | `taxila-db` (a database you build in MariaDB on your own VM from the provided script, full tier) |
| Example accounts | `registrar`, `itadmin`, `dpo`, `lecturer01`, `student01` |
| Your personal value | your index number written without spaces or hyphens; each lab sheet says how to use it. The example used in the materials is `COHNDNE999X000`, which belongs to nobody |
