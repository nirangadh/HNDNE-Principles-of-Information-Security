# Day 6

## Materials

- [Morning slides: Web application flaws and their fixes](slides/day-6-morning.pdf) (PDF)
- [Afternoon slides: Find and fix injection and scripting flaws](slides/day-6-afternoon.pdf) (PDF)
- [Notes](notes.md): read before the lab
- [Lab sheet](lab.md): steps, prove it, break it, reset and rules of engagement
- Demos, in teaching order. They run in the browser: open them from the [course website](https://nirangadh.github.io/HNDNE-Principles-of-Information-Security/days/day-6/), because GitHub shows them as code.
  1. [Data or command: the boundary in a form letter](artefacts/code-vs-data.html)
  2. [A login query, built two ways](artefacts/sqli-login.html)
  3. [Output encoding: markup or plain text](artefacts/output-encoding.html)
  4. [Cookie guards: three settings, three gaps](artefacts/cookie-attributes.html)
  5. [The Open Worldwide Application Security Project (OWASP) map: ten web risks, three for today](artefacts/owasp-map.html)
- Provided files: [`taxila-portal.py`](files/taxila-portal.py)

## Morning: Web application flaws and their fixes

**Ideas covered:** The boundary between code and data; Injection into a database; Scripts in another user's browser; Sessions, cookies and forged requests; Misconfiguration and secure development.

## Afternoon: Find and fix injection and scripting flaws

**Lab:** Find the flawed lines, fix them, and prove the fix.

**Adds to the register:** item 11, Portal input handling; item 12, Portal sessions and cookies.

**Tiers:** Floor tier: every step. Full tier: recommended.

## After this day

**Read:**

- Pfleeger and Pfleeger, program and web security; the OWASP Top 10 on the portal
- Pfleeger and Pfleeger, injection and cross-site scripting defences

**Practice question:** [Practice question 6](../../practice/PQ6.md), posted in [practice](../../practice/).

**Tasks:**

- Add web risks to your group's register

**Evidence pack 6** is due before the next teaching day, on the date announced for your cohort. See the [evidence packs brief](../../coursework/evidence-packs-brief.md).
