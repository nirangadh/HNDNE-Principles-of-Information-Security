# Lab 1: Classify Taxila's data and start its risk register

**Day 1, afternoon session. Duration 3 hours. Adds items 1 and 2 to Taxila's security register.**

This lab sheet takes you through classifying the data Taxila College holds and writing the first ten rows of its [risk](../../glossary.md#risk) register, using only this morning's ideas.

| | |
|---|---|
| Learning outcomes | LO1, LO5 |
| You need | this morning's five properties, the four data classes, and the words [asset](../../glossary.md#asset), [threat](../../glossary.md#threat), [vulnerability](../../glossary.md#vulnerability) and risk |
| Tiers | Floor tier: every step. Full tier: not needed today, and nothing is lost on the floor tier |
| Evidence pack | none today; evidence packs start after Day 2 |

## Before you start

1. Open this page and the day's notes side by side. Keep the notes open at [Taxila's classification page](notes.md#6-taxilas-classification-page).
2. Download the provided worksheet [`data-inventory.csv`](files/data-inventory.csv) and the [risk register template](../../templates/risk-register.csv). Both open in any spreadsheet program, or in a text editor.
3. Make a folder on your laptop for this module, and save both files in it. You keep them: you use them again on Day 9 and in your group's preparation.
4. Full tier: you do not need your Kali virtual machine today.

### The idea behind today's lab

> **Recall.** [Confidentiality](../../glossary.md#confidentiality), [integrity](../../glossary.md#integrity) and [availability](../../glossary.md#availability) are the first three properties.

> **Recall.** Risk combines how likely a harm is and how much it would cost.

> **Common mistake.** "Classification is about who owns the data." Classification is about how much harm a leak would cause. The Registrar owns both the course catalogue and the exam papers, but they sit in different classes.

> **Common mistake.** "A risk row needs a tool." A risk row needs an asset, a threat, a weakness and the property at stake. You write all of today's rows with your own thinking and a spreadsheet.

> **Quick check.** A lecturer suggests classing grades as internal, to save time. What would that allow?
>
> - [ ] Nothing would change, because grades stay in the student records
> - [x] Grades could be shown to every student and member of staff
> - [ ] Grades would then need more protection than exam papers
>
> **Why:** Internal data is harmless if it leaks, so it may be shared inside the college. Grades harm one student each if they leak, so they are confidential. Where data is stored does not set its class; the harm does.

> **Quick check.** Which of these is a complete risk row?
>
> - [x] Fee balances; a staff member who misuses access; every staff account can read all balances; 2 x 4 = 8; confidentiality
> - [ ] Fee balances; every staff account can read all balances; likelihood 2, impact 4
> - [ ] Fee balances; a careless lecturer as the vulnerability; score 8; authentication
>
> **Why:** The first names an asset, a threat, the weakness it uses, scores that multiply correctly, and one property. The second has no threat. The third names a person as the vulnerability and a process, not a property.

## Objective

You will sort every kind of data on Taxila's worksheet into one of four classes, and say where each important kind is most exposed. You will then write ten risk rows for the college's information technology (IT) office to act on. This answers the Data Protection Officer's first question and starts the college's list of risks.

## Timed segments

| Segment | Minutes | Tier |
|---|---|---|
| Classify Taxila's data | 45 | floor |
| Map the lifecycle and the property at stake | 45 | floor |
| Write the first risk-register rows | 40 | floor |
| Prove it, check it, and write up | 20 | floor |

## Steps

Each step states what to do and what you should see. If you do not see it, stop and work out why before moving on.

*Segment 1: Classify Taxila's data*

1. **Open the worksheet.** Open `data-inventory.csv`. *Expected:* seventeen rows, numbered 1 to 17. Each row names a system and one kind of data it holds. The other columns are empty.

2. **Name the structure.** For each row, write structured, semi-structured or unstructured. Ask: does every value sit in a fixed column, does it carry labels but no fixed table, or is it free text? *Expected:* records in the Student Information System (SIS) are structured; mailboxes are unstructured.

3. **Give each row a class.** Write public, internal, confidential or restricted. Use one test for every row: how much harm would a leak cause? Check your answer against the classification page in the notes. *Expected:* exam papers and national identity card numbers come out restricted; the course catalogue comes out public. Every class is used at least once.

> **Floor path.** The whole lab is floor tier. Use the classification page in the day's notes, and the `data-vs-information` demo if you want to see again how a label changes what a value means.

*Segment 2: Map the lifecycle and the property at stake*

4. **Find where grades are most exposed.** Take grades (row 2). Walk it through the six stages: create, store, process, share, archive, destroy. Write the stage where it is most exposed, and the property most at stake. *Expected:* the share and store stages stand out, and integrity is the property most at stake for grades: a changed grade is the harm Taxila has already suffered.

5. **Do the same for identity numbers.** Take national identity card numbers (row 4). *Expected:* store and share stand out again, but this time confidentiality is most at stake: the harm is someone reading them.

6. **Finish the restricted and confidential rows.** Fill the stage and property columns for every row you classed restricted or confidential. Add one sentence in the last column saying why. *Expected:* confidentiality is the most common answer, but not the only one. Grades point to integrity, and coursework submissions that must be there on a deadline night can point to availability.

*Segment 3: Write the first risk-register rows*

7. **Copy the template.** Open your copy of `risk-register.csv`. Read the example row first. *Expected:* an asset (exam papers), a threat (a curious student), a vulnerability (a folder anyone can open), likelihood 3, impact 5, score 15, confidentiality, and a first treatment idea.

8. **Write ten rows.** Fill R01 to R10. Each row names one real Taxila asset from your worksheet, one threat and one vulnerability. Give a likelihood from 1 (low) to 5 (high) and an impact from 1 to 5, then the score (likelihood x impact). Finish with the one property most at stake and a first treatment idea. *Expected:* ten rows, each naming a real Taxila asset and one property, each score between 1 and 25.

9. **Check each row has both halves.** For every row, cover the threat cell and ask: is the row still a risk? Then cover the vulnerability cell. *Expected:* each row needs both. If a row has a weakness but no one who could use it, it is not a risk yet; rewrite it or replace it.

*Segment 4: Prove it, check it, and write up*

10. **Compare with a partner.** Swap worksheets with the student beside you. Find one row where you chose a different class. *Expected:* you can each give the harm your class is based on; agree which harm is larger.

11. **Sort your risks.** Sort your ten rows by score, highest first. *Expected:* the top rows are the ones the Head of IT should look at first. At least one top row touches an incident from last semester.

## Prove it

Your worksheet places the exam papers (row 10) and the national identity card numbers (row 4) in restricted. Beside each, one sentence says why, in terms of harm: what would happen if it leaked.

## Break it

**Fault:** grades classed as internal.

1. Change the class of grades (row 2) to internal. Now follow what internal allows: internal data is harmless if it leaks, so a lecturer could put every student's grade on a shared notice page. **Symptom:** every student's grade is readable by everyone.
2. **Evidence:** the classification page says confidential data is personal data whose leak harms a person. Grades belong to one student each.
3. **Fix:** change the class back to confidential. Write which property that protects (confidentiality: only the student and the staff who need the grade may read it).

## Reset

1. Nothing to reset. This lab changes no system. Keep both files; they are your work, not lab scraps.

## Rules of engagement

No tool in this lab can affect anyone else's system. You work only with the provided worksheet and your own files, on your own laptop. Taxila College is fictional, so none of its systems exist to be touched.

## Evidence required

There is no evidence pack today. Evidence packs start after Day 2. Keep two files from this lab, because later days use them:

1. **Your data inventory.** `data-inventory.csv`, every row classed, with stages and properties filled for the restricted and confidential rows.
2. **Your risk register.** Your copy of `risk-register.csv` with ten complete rows.

## Taxila connection

This lab answers the first two requirements in Taxila's story. Knowing what data the college holds and how sensitive each kind is adds item 1, the data inventory and classification, to Taxila's security register. A living list of risks, each with an owner, adds item 2, the risk register. The Data Protection Officer will ask whose personal data sits in each restricted and confidential row. The Head of IT will ask which three rows to fix first, since the team is only four people. On Day 9 you return to these rows and choose how to treat each one.
