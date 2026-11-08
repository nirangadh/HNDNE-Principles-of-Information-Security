# Day 7

## Materials

- [Morning slides: Email and databases](slides/day-7-morning.pdf) (PDF)
- [Afternoon slides: Reading headers and locking down a database](slides/day-7-afternoon.pdf) (PDF)
- [Notes](notes.md): read before the lab
- [Lab sheet](lab.md): steps, prove it, break it, reset and rules of engagement
- Demos, in teaching order. They run in the browser: open them from the [course website](https://nirangadh.github.io/HNDNE-Principles-of-Information-Security/days/day-7/), because GitHub shows them as code.
  1. [The postcard through the relays: how email travels](artefacts/smtp-postcard.html)
  2. [Three checks that fight spoofing](artefacts/spf-dkim-dmarc.html)
  3. [The header trail: reading a message&#x27;s header](artefacts/header-trail.html)
  4. [Two accounts, one leaked password: least privilege for a database](artefacts/least-privilege-db.html)
  5. [Where encryption protects: at rest, in transit and in a live query](artefacts/at-rest-vs-in-transit.html)
- Provided files: [`grants.txt`](files/grants.txt), [`query-log.txt`](files/query-log.txt), [`suspect-header.txt`](files/suspect-header.txt), [`taxila-db.sql`](files/taxila-db.sql)

## Morning: Email and databases

**Ideas covered:** How email travels; Three checks that fight spoofing; Reading a header; Least privilege for a database; At rest, in transit, and a controller's duty.

## Afternoon: Reading headers and locking down a database

**Lab:** Trace a suspect header and scope a database account.

**Adds to the register:** item 13, Email authentication for taxila.example; item 14, Student Information System (SIS) database accounts and audit log.

**Tiers:** Floor tier: every step. Full tier: recommended.

## After this day

**Read:**

- Pfleeger and Pfleeger, email and database security; the Personal Data Protection Act, No. 9 of 2022
- Pfleeger and Pfleeger, email headers and database auditing

**Practice question:** [Practice question 7](../../practice/PQ7.md), posted in [practice](../../practice/).

**Tasks:**

- Add email and database controls to your group's register and controls map
- Bring your email and database controls to your group's controls map
