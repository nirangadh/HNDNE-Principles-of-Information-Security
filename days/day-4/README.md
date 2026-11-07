# Day 4

## Materials

- [Morning slides: Signatures, certificates and Transport Layer Security (TLS)](slides/day-4-morning.pdf) (PDF)
- [Afternoon slides: Keys, certificates and a look inside TLS](slides/day-4-afternoon.pdf) (PDF)
- [Notes](notes.md): read before the lab
- [Lab sheet](lab.md): steps, prove it, break it, reset and rules of engagement
- Demos, in teaching order. They run in the browser: open them from the [course website](https://nirangadh.github.io/HNDNE-Principles-of-Information-Security/days/day-4/), because GitHub shows them as code.
  1. [Sign, then verify](artefacts/sign-verify.html)
  2. [One edit, a broken signature](artefacts/tamper-breaks-signature.html)
  3. [A certificate is a passport](artefacts/certificate-passport.html)
  4. [Follow the chain of trust](artefacts/chain-of-trust.html)
  5. [What the padlock proves](artefacts/padlock-truth.html)
- Provided files: [`example-private-key.txt`](files/example-private-key.txt), [`example-public-key.txt`](files/example-public-key.txt), [`plain-web.pcapng`](files/plain-web.pcapng), [`portal-certificate.txt`](files/portal-certificate.txt), [`secure-web.pcapng`](files/secure-web.pcapng), [`taxila-portal.py`](files/taxila-portal.py)

## Morning: Signatures, certificates and TLS

**Ideas covered:** Signing with the private key; Tampering breaks the signature; A certificate is a signed identity; The chain of trust; Transport security and the padlock.

## Afternoon: Keys, certificates and a look inside TLS

**Lab:** Sign your file, inspect certificates, and see what secure web hides.

**Adds to the register:** item 7, Signed transcripts; item 8, Portal certificate and TLS.

**Tiers:** Floor tier: every step. Full tier: recommended.

## After this day

**Read:**

- Pfleeger and Pfleeger, public-key infrastructure and digital signatures
- Pfleeger and Pfleeger, certificates and the handshake

**Practice question:** [Practice question 4](../../practice/PQ4.md), posted in [practice](../../practice/).

**Evidence pack 4** is due before the next teaching day, on the date announced for your cohort. See the [evidence packs brief](../../coursework/evidence-packs-brief.md).
