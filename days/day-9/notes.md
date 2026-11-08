# Day 9: Attacks, people, risk and continuity

These notes cover the Day 9 morning. They give you three questions that describe any attack, and show how the main kinds of harmful software differ. They show how attackers use people instead of systems, and where the law draws its lines. Then they turn from single threats to the whole picture: how an organisation chooses what to do about each risk, and how it keeps working when something fails anyway.

> **Recall.** A threat exploits a vulnerability to put an asset at risk.

> **Recall.** Availability is the property that keeps a service answering.

It is results week. The Registrar stands at the server room door and remembers the night the fee payment page stopped. "If the Student Information System (SIS) stopped tonight, how long could we wait before students were hurt? And if we restored from last week's disk, how many grades would we lose?" Nobody in the room has a number yet. By the end of today, you will.

Item 18 on Taxila's security register is the staff awareness programme, taught today as a concept. This afternoon you return to item 2, the risk register you started on Day 1, and choose how to treat each risk. You also write item 19, the continuity plan and backups.

## 1. Classifying an attack

Try the demo first: [Three questions for any attack](artefacts/attack-axes.html). Read six things that went wrong, set three switches for each, and read the profile.

> **Recall.** Sniffing only receives and leaves no trace; a flood sends traffic to stop a service.

You have met many attacks in this module. Three questions describe any of them. Each question has two answers, so we call them the three axes.

| Axis | One answer | The other answer |
|---|---|---|
| What does the attacker do? | **Passive**: only watches or reads, and changes nothing | **Active**: sends, changes, blocks or deletes something |
| Where does the attacker start? | **Insider**: already has access, such as a member of staff or a student | **Outsider**: starts with no access of their own |
| Who was chosen? | **Targeted**: aimed at this organisation or this person | **Opportunistic**: aimed at anyone who happens to be open |

Together the three answers give the attack's profile. The profile helps you judge how likely the attack is and which controls fit it. A passive attack leaves no trace, so encryption is the answer, not watching for it. An insider already holds a password, so a firewall does not stop them, but [least privilege](../../glossary.md#least-privilege) and a record of who did what do. An opportunistic attack hits whoever is weakest, so ordinary good practice, such as patching, removes most of it. A targeted attacker keeps trying, so the controls must be in layers.

![Two rows, one per event, answered on three questions. The changed grade in the SIS is marked active, insider and targeted. A mass phishing run, one message to thousands, is marked active, outsider and opportunistic. Below, the controls that fit each: least privilege and a second approver for the changed grade; awareness and email checks for the phishing run.](img/attack-axes.svg "Two events on three axes: the profile points to the controls")

An insider is not always dishonest. A lecturer who emails a spreadsheet of grades to the wrong person is an insider too, acting by mistake.

> **You already know this.** You describe a burglary in three ways. Did the burglar only look through the window, or break in? Was it someone who works in the house, or a stranger? Did they choose your house, or try every door in the street until one opened?
>
> *Mapping:* watching against breaking in = passive against active; a staff member against a stranger = insider against outsider; chosen against first-unlocked = targeted against opportunistic.

> **Taxila.** The changed grade was likely an insider: someone with access to the SIS. A mass phishing run is opportunistic.

> **Common mistake.** "An attacker is always an outsider." Insiders already have accounts and know where the data is. By malice or by mistake, they are among the hardest to catch. This is why Taxila's grade changes now need a named person and a second approver.

> **Quick check.** A student on the college Wi-Fi quietly records other students' traffic to find passwords sent without encryption. They do not mind whose passwords they get. What is the profile?
>
> - [ ] Active, outsider, targeted
> - [x] Passive, insider, opportunistic
> - [ ] Passive, outsider, targeted
>
> **Why:** Recording traffic only receives, so it is passive. The student is already on the college's own network with their own access, so they are an insider. They take whatever passes, so it is opportunistic. "Outsider" is the tempting wrong answer, because people picture attackers as strangers.

## 2. Malware

Try the demo first: [How malware spreads](artefacts/malware-spread.html). Start each animation and watch how each kind moves from one college computer to the next.

> **Recall.** Hardening means removing what a system does not need and keeping it patched.

[Malware](../../glossary.md#malware), short for malicious software, is any program written to harm a computer or its owner. Its kinds differ in how they spread and in what they do.

| Kind | How it spreads or hides | What it does |
|---|---|---|
| Virus | attaches itself to a host file, and runs when a person opens that file | copies itself into other files; may damage data |
| [Worm](../../glossary.md#worm) | moves across the network by itself, through a weakness such as a missing patch | spreads to every reachable machine, with no click needed |
| Trojan | hides inside something the user wants, such as a free program | does something harmful behind the wanted part, such as opening a hidden way in |
| [Ransomware](../../glossary.md#ransomware) | arrives as any of the above | encrypts the victim's files and demands payment for the key |
| Spyware | runs quietly in the background | watches the user, such as recording the keys they press, and reports back |
| Rootkit | hides itself, and other malware, from the operating system and its tools | keeps an attacker in control without being seen |

The first difference matters most. A virus needs a human action: someone must open the infected file. A worm needs none. It finds the next machine with the same weakness, and copies itself there. That is why one unpatched server can infect a whole network in minutes.

Ransomware turns Day 2's encryption against its victim. The files are still there, but nobody can read them without a key the attacker holds. Many ransomware groups also copy the files out first and threaten to publish them, so confidentiality is lost as well.

No single product stops all of these. Each layer meets a different kind:

- **Patching**, from Day 5, closes the weaknesses that worms use.
- **Least privilege** limits what any malware can reach from one account.
- **Anti-malware software** on each computer recognises known malware and blocks it.
- **Awareness** stops a person opening the infected file or the trojan.
- **Backups** that the malware cannot reach let you restore after ransomware.

> **You already know this.** Picture a printed flyer. It travels only when someone picks it up and hands it on. Now picture a rumour. It spreads from person to person by itself, and nobody has to decide to pass it on.
>
> *Mapping:* a flyer someone must pass on by hand = a virus needing a host and a click; a rumour that spreads by itself = a worm moving across the network.

> **Taxila.** Ransomware on the Student Information System would hold grades hostage, hurting availability and integrity.

> **Common mistake.** "A virus and a worm are the same thing." A virus needs a host file and a person to run it. A worm moves across the network on its own. The difference changes the defence: awareness slows a virus, but only patching stops a worm.

> **Quick check.** A district clinic's appointment computers stop one evening. By morning every computer on the clinic's network shows the same message, and nobody had opened any attachment. Which kind of malware spread this way?
>
> - [ ] A virus, because it damaged files
> - [x] A worm, because it reached every machine with no human action
> - [ ] A trojan, because it was hidden
>
> **Why:** Nobody opened anything, so the malware moved by itself: that is a worm. The message on every screen suggests ransomware was its payload. A virus needs a person to open the host file, which did not happen here.

## 3. Social engineering, the law and privacy

Try the demo first: [Which button does it press?](artefacts/social-triggers.html). Read six prepared messages and name the trigger each one pulls.

> **Recall.** Phishing is a message that tricks people into giving away a password, money or data.

[Social engineering](../../glossary.md#social-engineering) attacks people instead of systems. It persuades someone to do what the attacker wants: give a password, open a file, or hold a door. Four forms are common.

- **[Phishing](../../glossary.md#phishing)** sends a message, as on Day 7. Spear-phishing aims it at one person.
- **Pretexting** invents a story, the pretext, to make a request seem normal. "I am from the bank's security team, and I need to confirm your account."
- **Baiting** leaves something tempting, such as a memory stick marked "Salaries", for someone to pick up and plug in.
- **Tailgating** follows a person with access through a locked door, perhaps carrying boxes so that they hold it open.

Each one pulls on a human trigger. Six are common:

| Trigger | What the message makes you feel | Example |
|---|---|---|
| Authority | an important person is asking | "This is the Registrar." |
| Urgency | there is no time to check | "Reply within one hour." |
| Fear | something bad will happen if you do not act | "Your account will be closed." |
| Reward | you will gain something | "You have won a free laptop." |
| Curiosity | you want to see what it is | "Exam results leaked: see the list." |
| Helpfulness | a polite person needs your help | "I left my card at home, could you hold the door?" |

The control is people who recognise the triggers, which is item 18 on Taxila's security register, the staff awareness programme. It teaches staff to stop and check through a second channel, such as phoning the Registrar's office on the number they already know. It gives them one easy way to report a suspicious message. Practice phishing messages show staff, safely, what a real one looks like.

The law sets the boundary for all security work. Under Sri Lanka's Computer Crime Act, No. 24 of 2007, gaining access to a computer, or to its information, without lawful authority is an offence. So is making a computer do something without lawful authority. Attacking any system without written permission is a crime, even with no damage. A practice phishing exercise is no exception: Taxila runs one only with the college management's written approval.

The same exercise produces a list of who clicked. That list is personal data, and the law protects personal data too. Under Sri Lanka's Personal Data Protection Act, No. 9 of 2022, as amended, Taxila is the [data controller](../../glossary.md#data-controller) for its students' and staff's personal data. It must use that data only for a stated purpose, keep it safe and correct, and keep it no longer than needed. At the time of writing, the Act's Data Protection Authority is set up, and a government order has fixed the date from which the duties on organisations apply. The Authority's own site gives the current position. The European Union's General Data Protection Regulation (GDPR) is the best-known law of the same kind, and many of its ideas appear in the Sri Lankan Act.

> **You already know this.** A man in a smart uniform knocks at the door. "Electricity board. Your supply will be cut in ten minutes unless I check the meter now." You let him in without asking to see his card.
>
> *Mapping:* the uniform that makes you comply = authority; the act-now demand = urgency.

> **Taxila.** Two staff followed the fake Registrar link. An awareness programme and the Data Protection Officer's duties are the answer.

> **Common mistake.** "Good technical controls stop social engineering." Social engineering attacks people, not systems. A firewall cannot stop a member of staff who reads a password out over the phone. The main control is people who recognise the triggers and check through a second channel.

> **Quick check.** A microfinance cooperative's field agent gets a call: "Head office here. The system is down and the auditors arrive at noon. Read me your login code now, or your village's loans will be stopped." Which triggers does the caller pull?
>
> - [ ] Reward and curiosity
> - [ ] Helpfulness only
> - [x] Authority, urgency and fear
>
> **Why:** "Head office" is authority. "Auditors arrive at noon" and "now" are urgency. "Loans will be stopped" is fear. The agent's defence is to hang up and call head office on the number they already know.

## 4. Managing risk

Try the demo first: [Four ways to treat a risk](artefacts/risk-treatment.html). Choose a treatment for each of four Taxila risks and watch what remains.

> **Recall.** Risk combines how likely a harm is and how much it would cost.

The Head of IT (information technology) cannot fix everything at once. Managing risk is how an organisation decides what to do first, and what to do about each risk. It is a cycle, not a single task.

1. **Identify** the assets, the threats and the vulnerabilities, as you did on Day 1.
2. **Rate** each risk: likelihood from 1 to 5, impact from 1 to 5, and the score, which is the two multiplied.
3. **Treat** each risk, starting with the highest scores.
4. **Record** the treatment and the person who owns the risk.
5. **Review** the register when threats or systems change, and start again.

There are four ways to treat a risk. Together they are called [risk treatment](../../glossary.md#risk-treatment).

| Treatment | What you do | Taxila example |
|---|---|---|
| Mitigate | add a control that lowers the likelihood or the impact | encrypt the exam paper store, so a leaked file cannot be read |
| Avoid | stop the activity that creates the risk | switch off the old test web server that nobody uses |
| Transfer | let another party carry the cost | the bank's payment gateway holds card numbers, so Taxila never does |
| Accept | live with the risk, as a recorded choice | the course catalogue on the website is public data; a defaced page is fixed when it happens |

![One risk at the top, exam papers in a folder anyone can open, scored 3 times 5, which is 15. Four treatments below, each with a residual risk bar out of 25. Mitigate, encrypt and limit the folder: 1 times 5, which is 5. Avoid, write papers on paper only: the folder risk is gone. Transfer, insurance pays for a rewrite: 15 stays, because the leak still happens. Accept: 15 stays, too high here.](img/treatments.svg "One risk, four treatments, and what each leaves behind")

Treatment rarely removes a risk. What is left after treatment is the [residual risk](../../glossary.md#residual-risk). You rate it again, with the control in place. The owner then judges whether that remaining score is low enough.

To find threats you might miss, analysts use a structured list. [STRIDE](../../glossary.md#stride) (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege) names six kinds of threat. Five of them attack one of the five properties. The sixth defeats authorisation, the process from Day 5 that decides what each account may do.

| STRIDE threat | What it attacks | Taxila example |
|---|---|---|
| Spoofing | authenticity | the email that pretended to come from the Registrar |
| Tampering | integrity | the changed grade |
| Repudiation | accountability | nobody could prove who changed the grade |
| Information disclosure | confidentiality | the leaked exam paper |
| Denial of service | availability | the fee payment page that stopped responding |
| Elevation of privilege | authorisation (a process, not a property) | a student account that gains a lecturer's rights |

Organisations write the results down as security policies: short rules that everyone must follow, such as "exam papers are stored only in the examinations office's encrypted folder".

### Two frameworks: the NIST Cybersecurity Framework and ISO/IEC 27001

Two well-known frameworks give the whole process a common shape. The first is the Cybersecurity Framework of the National Institute of Standards and Technology (NIST), at version 2.0 at the time of writing. It sorts security work into six functions: govern, identify, protect, detect, respond and recover. The second is an international standard, numbered 27001, published jointly by two international standards bodies. It sets out what an organisation's information security management system must contain, and organisations can be certified against it.

> **You already know this.** Your roof leaks over one room. You can fix the roof. You can stop using that room. You can pay for insurance that covers the damage. Or, if the leak is small, you can put a bucket under it and decide to live with it.
>
> *Mapping:* fix the roof = mitigate; stop using the room = avoid; insure it = transfer; live with it = accept.

> **Taxila.** The Head of IT cannot fix everything at once, so the register is prioritised.

> **Common mistake.** "Accepting a risk means ignoring it." An accepted risk is a recorded, owned choice to live with a measured risk. It has an owner, a reason and a point at which it is looked at again. A risk nobody wrote down was not accepted: it was missed.

> **Quick check.** A doctor-channelling booking platform buys insurance against losses from an outage on busy evenings. Which treatment is this, and what is still the platform's job?
>
> - [x] Transfer; it must still bring the service back itself
> - [ ] Accept; the insurer now handles the outage
> - [ ] Mitigate; insurance makes an outage less likely
>
> **Why:** Insurance moves the cost to another party, so it is transfer. It does not make an outage less likely, so it is not mitigation. Patients still cannot book until the service returns, so a continuity plan is still needed.

## 5. Keeping the college running

Try the demo first: [Two windows on one timeline](artefacts/rto-rpo-timeline.html). Slide the last backup and the moment of recovery, and read both windows.

> **Recall.** A denial of service floods a service so real users cannot reach it.

Some failures will happen whatever you do: a disk dies, a power cut lasts all night, or ransomware gets through. [Business continuity planning](../../glossary.md#business-continuity-planning) keeps the organisation's critical work going during a failure, and brings it back afterwards.

It starts with a [business impact analysis](../../glossary.md#business-impact-analysis). For each important service, you ask three questions. What depends on it? What happens if it stops for one hour, one day, one week? So which service must come back first? The answers give two numbers for each service:

- The [recovery time objective](../../glossary.md#recovery-time-objective) (RTO) is the longest the service may be down before the harm becomes unacceptable.
- The [recovery point objective](../../glossary.md#recovery-point-objective) (RPO) is the most data, measured in time, that you can afford to lose. It is the gap between the last good backup and the failure.

![A timeline. The last good backup on the left, the failure in the middle, and the service back on the right. From the last backup to the failure is the data lost, which must not exceed the recovery point objective. From the failure to recovery is the time down, which must not exceed the recovery time objective.](img/rto-rpo.svg "One failure, two windows: data lost before it, time down after it")

The two are set separately. A service can need a short recovery time and still tolerate a day of lost data, or the other way round. The recovery point sets how often you back up: an RPO of one hour needs a backup at least every hour.

Several tools meet these numbers:

- **Recovery sites.** A hot site is a second copy of the systems, running all the time, ready in minutes. A warm site has the equipment but needs the latest data loaded, which takes hours. A cold site is a room with power and network, and takes days. Faster costs more.
- **The [three-two-one backup rule](../../glossary.md#three-two-one-backup-rule).** Keep three copies of the data, on two kinds of storage, with one copy off-site. A fire or ransomware that reaches one place cannot reach all three.
- **Failover.** A standby server takes over automatically when the main one fails.
- **Plan testing.** Walk through the plan on paper, run a tabletop exercise as your group will on Day 10, and restore a real backup to a spare machine.
- **Incident response**, at overview. When something goes wrong, a team detects and reports it, contains it so that it stops spreading, recovers the service, and learns what to change. These steps belong to the respond and recover functions of the NIST framework.

> **You already know this.** A small shop plans for a power cut. How long can it stay closed before customers go elsewhere? And if the till loses its memory, how many of today's sales can the owner afford to forget? The owner writes the day's sales in a notebook every hour, just in case.
>
> *Mapping:* how long before you must reopen = the recovery time objective; how many sales records you can afford to lose = the recovery point objective; the hourly notebook = the backup.

> **Taxila.** The dead fee-payment night needed a continuity plan with a stated recovery time. Today Taxila backs up to one external disk once a week, so a failure just before the next backup could lose almost a week of grades.

> **Common mistake.** "A backup you have never restored is a working backup." Only a tested restore proves a backup. A disk can fail, a copy can be incomplete, and ransomware may have encrypted the backup too. Test by restoring to a spare machine and checking the data.

> **Common mistake.** "The recovery time and the recovery point are the same number." One is tolerable downtime, the other tolerable data loss, and they are set separately. The fee page may need to return within an hour, yet the SIS may need to lose no more than an hour of grades.

> **Quick check.** A school examinations board says its results database may lose at most one hour of entries. It backs up every night. What is wrong?
>
> - [ ] Nothing, because nightly backups are normal
> - [ ] The recovery time is too long
> - [x] The backup is too rare: a failure just before the nightly backup loses almost a day of entries, far more than one hour
>
> **Why:** The recovery point of one hour sets the backup frequency: at least every hour. A nightly backup gives a recovery point of up to a day. The recovery time is a separate number, and the question does not give it.

## Before the lab

This afternoon you open your own risk register from Day 1, choose a treatment and an owner for each risk, and rate what remains. Then you judge what an outage of the fee payment page and of the SIS would cost over an hour, a day and a week. Last, you write a continuity plan with a recovery time and a recovery point for each. Bring these notes, open at sections 4 and 5, and your Day 1 file `risk-register.csv`. You need no virtual machine today.

## Reading

- Pfleeger, C. P., Pfleeger, S. L. and Coles-Kemp, L., *Security in Computing*, 6th ed., chapter 3, section 3.2, on malware. Then chapter 10, sections 10.2 to 10.4, on business continuity planning, handling incidents and risk analysis.
- Pfleeger, C. P., Pfleeger, S. L. and Coles-Kemp, L., *Security in Computing*, 6th ed., chapter 11, section 11.5, on computer crime; and chapter 9, sections 9.1 and 9.2, on privacy.
- Computer Crime Act, No. 24 of 2007, Sri Lanka, sections 3 to 5, on access without lawful authority.
- Personal Data Protection Act, No. 9 of 2022, Sri Lanka, as amended by Act No. 22 of 2025: the duties of a controller.

Next: Day 10, the group exercise, synthesis and exam preparation. Your group runs a live incident at Taxila with the register, the controls map and the continuity plan you finish today.
