# Lab 9: Complete the risk register and write a continuity plan

**Day 9, afternoon session. Duration 3 hours. Adds items 2 and 19 to Taxila's security register.**

This lab sheet takes you through three jobs a security team does on paper before anything goes wrong. First you finish Taxila's risk register: a treatment, an owner and a residual risk for every row. Then you judge what an outage of the fee payment page and of the Student Information System (SIS) would cost over time. Last, you write the continuity plan that brings both back, with backups that match how much data the college can afford to lose.

| | |
|---|---|
| Learning outcomes | LO5, LO6 |
| You need | your Day 1 file `risk-register.csv`; this morning's four treatments; the recovery time objective and the recovery point objective |
| Tiers | Floor tier: every step, with a spreadsheet program or a text editor. There is no full-tier work today |
| Evidence pack | none today; the five evidence packs ended with the pack after Day 6 |

## Before you start

1. Open this page and the day's notes side by side. Keep the notes open at sections 4 and 5.
2. Find your Day 1 file `risk-register.csv`, with your ten rows R01 to R10.
3. Download the provided files and save them in your module folder: [`risk-register-day-9.csv`](files/risk-register-day-9.csv), [`bia-facts.txt`](files/bia-facts.txt), [`bia-worksheet.csv`](files/bia-worksheet.csv) and [`continuity-plan.txt`](files/continuity-plan.txt).
4. You need no virtual machine today. If you use one for your files, take no snapshot: this lab changes no system.

### The idea behind today's lab

> **Recall.** Risk combines how likely a harm is and how much it would cost.

> **Recall.** The recovery time objective is tolerable downtime; the recovery point objective is tolerable data loss.

On Day 1 you wrote ten risks. Since then you have learnt many more threats, and the controls that answer them. Today the register becomes a plan: for every risk, what Taxila will do, who owns it, and what is left. Then you look at the two services whose failure hurt Taxila most last semester, and plan how to bring them back.

> **Common mistake.** "The recovery time and the recovery point are the same number." One is how long the service may be down. The other is how much data, measured in time, can be lost. They answer different questions, so they are set separately and are often different.

> **Common mistake.** "A risk register is written once and filed away." It is reviewed and updated as threats and systems change. Today you change rows you wrote eight days ago, because you now know more.

> **Quick check.** Your register has a row: "SIS database port open to the student Wi-Fi; likelihood 4, impact 5". The Head of IT (information technology) closes the port at the firewall. What should change in the row?
>
> - [ ] Nothing, because the risk is on the register already
> - [x] The treatment becomes mitigate, the action names the firewall rule, and the residual likelihood is rated again, lower
> - [ ] The row is deleted, because the risk is gone
>
> **Why:** A control lowers a risk; it rarely removes it. The row stays, with its treatment and a new residual score, so the next review can see what was done. Deleting it would lose that record.

> **Quick check.** The fee payment page needs a recovery point of one hour. Which backup plan meets it?
>
> - [ ] A full copy once a week to an external disk
> - [ ] A full copy every night to a server in Kandy
> - [x] A copy every hour to a second disk, with a nightly copy sent to Kandy
>
> **Why:** The recovery point sets the backup frequency: at least every hour. Only the third plan copies that often. Its nightly copy to Kandy also keeps one copy off-site, as the three-two-one rule asks.

## Objective

You will show a risk register in which every risk has a treatment, an owner and a residual score. You will show a continuity plan whose recovery times and recovery points are argued from Taxila's own facts, with a backup plan that follows from them. These are register items 2 and 19, and the inputs your group uses on Day 10.

## Timed segments

| Segment | Minutes | Tier |
|---|---|---|
| Complete Taxila's risk register | 50 | floor |
| A business impact analysis for the fee page and the Student Information System | 45 | floor |
| A continuity plan with recovery objectives and the three-two-one rule | 35 | floor |
| Check it and hand to your group | 20 | floor |

## Steps

Each step states what to do and what you should see. If you do not see it, stop and work out why before moving on.

> **Floor path.** The whole lab is floor tier. Every step is the same on every laptop: a spreadsheet program, or a text editor for the `.csv` and `.txt` files.

*Segment 1: Complete Taxila's risk register*

1. **Copy your rows across.** Open `risk-register-day-9.csv`. Read the example row first, then copy your ten rows from `risk-register.csv` into it. Your Day 1 treatment idea goes in the **Action** column. *Expected:* ten rows, R01 to R10, each with an asset, a threat, a vulnerability, a likelihood, an impact, a score from 1 to 25 and the property most at stake. The five new columns are still empty.

2. **Bring the register up to date.** Keep at least ten rows. Replace your weakest rows, or add rows, so that at least three risks use a threat you learnt on Days 5 to 8. Examples are credential stuffing against staff accounts, an injection flaw in the portal, or a database account with too many rights. A look-alike domain, or the SIS database port open to the student Wi-Fi, would also do. *Expected:* at least ten rows, at least three of them from Days 5 to 8. Every row names a real Taxila asset and one of the five properties.

3. **Choose a treatment and an action.** For each row, write mitigate, avoid, transfer or accept in the **Treatment** column, and the control or step in the **Action** column. *Expected:* most rows are mitigate, with a named control from this module. At least one row is transfer or accept. Card numbers held by the bank's gateway are a transfer. A public page that is fixed when it is defaced can be an accept.

4. **Name an owner for every row.** Write the role that answers for the risk: the Registrar, the Head of IT or the Data Protection Officer. *Expected:* grade and exam rows are owned by the Registrar; system rows by the Head of IT; personal data rows by the Data Protection Officer. Every accept row has an owner and a reason in its Action column.

5. **Rate what remains.** Fill in the residual likelihood and impact, with the action in place, and the residual score. Then sort by residual score, highest first. *Expected:* each mitigate or avoid row has a lower residual score than its first score. An accept row keeps its score. The top rows after sorting are the ones the Head of IT should review first.

*Segment 2: A business impact analysis for the fee page and the Student Information System*

6. **Read the facts.** Open `bia-facts.txt` and read all four parts. Mark every fact that changes how much an outage would hurt. *Expected:* you have marked the deadline-evening figure of about 600 payments an hour against 20 on an ordinary evening, and the late fee. You have marked that the fee page cannot take payments without the SIS, and the 1,200 grades a day in marking weeks. You have also marked the release day, and that the only backup is a weekly disk in the server room that nobody has restored.

7. **Rate the harm over time.** In `bia-worksheet.csv`, rate the harm after one hour, one day and one week for each service. Use 1 for small and 5 for severe, and give one reason each. *Expected:* the fee page's harm rises steeply. One hour on an ordinary evening is small, but one hour on a deadline evening already stops about 600 payments, so it rates 4 or 5. The SIS is critical to the whole college. Even one hour stops lecturers, the Registrar's office and the fee page at once. One week would miss the release day, so it rates 5.

8. **Set the recovery priority.** Fill in the last column: which service comes back first, and why. *Expected:* the SIS comes first. The fee page depends on it, so restoring the page alone would not let anyone pay. Your reason names that dependency.

*Segment 3: A continuity plan with recovery objectives and the three-two-one rule*

9. **Set the two objectives for each service.** In `continuity-plan.txt`, write a recovery time objective (RTO) and a recovery point objective (RPO) for each service. Argue each one from the facts. *Expected:* for the fee page, an RTO of about one hour on a deadline evening. Its RPO can be about one hour too, because a lost hour of payments can be rebuilt from the bank's own statement. For the SIS, an RTO of a few hours, within one working day, and an RPO of about one hour in marking weeks. Your reasons quote the facts, not a guess.

10. **Write the backup strategy.** For each service, write three copies on two kinds of storage with one off-site, and say how often each is made. *Expected:* the backup frequency follows from the recovery point. A recovery point of one hour needs a copy at least every hour, for example to a second disk in the server room. A daily copy to the rack in Kandy gives the off-site copy. A regular restore test on the spare server proves it all.

11. **Write the recovery steps.** For each service, list the steps that bring it back, in order, and who must be told. *Expected:* a workable order for the SIS. First confirm the failure and tell the Registrar. If malware is suspected, cut the server off the network and tell the Data Protection Officer. Then restore the last good backup to the spare server, and check a sample of grades against the lecturers' marking sheets. Only then switch users over, and re-enter the grades made since the backup.

*Segment 4: Check it and hand to your group*

12. **Check each other's work.** Swap files with a partner and use this list. Every register row names its property, a treatment, an action and an owner. Every accept row gives a reason. Each RTO and RPO is argued from a fact. Each backup frequency is at least as often as its RPO. One copy is off-site. The restore is tested. The recovery steps check the data before users return. *Expected:* each item is ticked, or you fix it before you hand in.

13. **Hand it to your group.** Give your register, your worksheet and your continuity plan to your group for the Day 10 exercise. Your group keeps one register and one controls map. *Expected:* your group has at least ten risks with treatments, and one plan for both services.

## Prove it

Every row in your register names its property and a treatment. Your recovery time and recovery point for the fee page are argued from the deadline-night story, not guessed. You can point to the line in `bia-facts.txt` behind each number. They are the 600 payments an hour, the late fee, and the bank's own statement, from which a lost hour of payments can be rebuilt.

## Break it

**Fault:** a backup that is far rarer than the recovery point.

1. In a copy of your plan, set the SIS backup to once a week, as it is today, and keep its recovery point at one hour.
2. **Symptom:** follow the consequence. In a marking week, a failure just before the weekend backup loses almost five working days of grades. That is about 6,000 grades to find on lecturers' sheets and type again, with mistakes.
3. **Evidence:** compare the two numbers. The gap between backups, one week, is far longer than the recovery point, one hour. The data lost in a failure can be as large as the gap between backups.
4. **Fix:** set the backup to at least every hour, as step 10 says, and check that the off-site copy and the restore test are still in the plan.

## Reset

Nothing to reset; this lab changes no system. Keep your three files. Delete the broken copy of your plan from the Break it section, so that only the corrected plan reaches your group.

## Rules of engagement

No tool in this lab can affect anyone else's system. You work only with your own files and the provided worksheets, and you change no system of any kind.

## Evidence required

There is no evidence pack today. Keep these, because your group uses them on Day 10:

1. **Your risk register.** At least ten rows, each with a treatment, an action, an owner and a residual score.
2. **Your business impact analysis.** The completed `bia-worksheet.csv`, with a reason for every rating and the recovery priority.
3. **Your continuity plan.** The completed `continuity-plan.txt` for both services.

## Taxila connection

Item 2 on Taxila's security register is the risk register, a living list of risks, each with an owner. You started it on Day 1, and today it says what the college will do about each risk. Item 19 is the continuity plan and backups. It answers the dead deadline night, and the weekly disk that nobody has restored. The Head of IT will ask which risks to work on first, and what each fix will break. The Registrar will ask how many grades could be lost. The Data Protection Officer will ask who is told when personal data may be affected.
