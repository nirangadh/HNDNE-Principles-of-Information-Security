# Lab 4: Sign your file, inspect certificates, and see what secure web hides

**Day 4, afternoon session. Duration 3 hours. Adds items 7 and 8 to Taxila's security register.**

This lab sheet takes you from signing your own index number to reading certificates and watching what secure web hides. You will see one edit break a signature, a certificate whose issuer is its own subject, and a form that is readable on plain web but not on secure web.

| | |
|---|---|
| Learning outcomes | LO3, LO4 |
| You need | this morning's ideas: you sign with the private key and verify with the public key; a [certificate](../../glossary.md#certificate) binds a key to a name, and an authority vouches for it; the padlock proves an encrypted channel and a vouched name |
| Tiers | Floor tier: every step, in the browser. Full tier: segments 1, 2 and 4 can also run in your Kali virtual machine; segment 3 uses the browser on either tier |
| Evidence pack | Pack 4, due before the next teaching day |

## Before you start

1. Open this page and the day's notes side by side.
2. Write down your personal value: your index number without spaces or hyphens, with its letters in capitals exactly as issued (the example in this sheet, `COHNDNE999X000`, belongs to nobody).
3. Full tier: start your Kali virtual machine and take a snapshot named `day-4-start`, so Reset can bring it back.
4. Floor tier: open the demos this lab uses: `certificate-passport` and `padlock-truth`. Open CyberChef too, from its official site or your offline copy.
5. Download the provided files and save them in your module folder: [`example-private-key.txt`](files/example-private-key.txt), [`example-public-key.txt`](files/example-public-key.txt), [`portal-certificate.txt`](files/portal-certificate.txt), [`taxila-portal.py`](files/taxila-portal.py), [`plain-web.pcapng`](files/plain-web.pcapng) and [`secure-web.pcapng`](files/secure-web.pcapng).

### The idea behind today's lab

> **Recall.** You sign with the private key and verify with the public key.

> **Recall.** A certificate binds a key to a name, and an authority vouches for it.

> **Common mistake.** "The public key signs." The private key signs; the public key verifies. If the public key could sign, anyone could sign as you, because everyone may hold your public key.

> **Common mistake.** "A self-signed certificate is broken." It is a valid certificate that simply nobody vouches for. In segment 2 you make or read one, and every field is in order. The only difference is that the issuer is the subject itself.

> **Quick check.** Your lab partner says: "Send me your private key, so I can check your signature." What should you send?
>
> - [ ] Your private key, because it made the signature
> - [x] Your public key, the signed file and the signature
> - [ ] Nothing: a signature can only be checked by the person who made it
>
> **Why:** Anyone checks a signature with the public key, so your partner needs nothing secret. Sending the private key is tempting because it made the signature, but whoever holds it can sign as you.

> **Quick check.** You sign your index in CyberChef and verify it straight away, but `RSA Verify` says `Verification Failure`. You signed with `SHA-256`. What is the most likely cause?
>
> - [ ] Your private key is too short
> - [ ] Your index number has the wrong letters
> - [x] `RSA Verify` still has its default digest, `SHA-1`
>
> **Why:** Verifying recomputes the digest, so both sides must use the same hash function. A different digest never matches the one you signed, even though the file and key are right.

## Objective

You will show that a signature made with your private key verifies with your public key, and fails after a single edit. So a signed file proves who made it and that it is unchanged. You will also read a certificate, walk a chain of trust to its root, and show that secure web hides a form that plain web exposes. This is how Taxila can issue transcripts an employer can trust, and run its portal over a connection that proves it is genuine.

## Timed segments

| Segment | Minutes | Tier |
|---|---|---|
| Generate a key pair and sign your personal file | 40 | both |
| Make and read a certificate | 35 | both |
| Inspect a live certificate chain | 25 | both |
| See what secure web hides | 25 | both |
| Prove it, break it, reset and write up | 25 | both |

## Steps

Each step states what to do and what you should see. If you do not see it, stop and work out why before moving on.

*Segment 1: Generate a key pair and sign your personal file*

Your personal file holds exactly your index number, in capitals, with no space and no new line at the end. For the example, the file holds `COHNDNE999X000`, which is 14 characters.

1. **Try the example first.** Sign the example file with the provided example private key, using SHA-256 (Secure Hash Algorithm, 256 bits). Then verify it with the example public key. *Expected:* the signature, written in Base64, is 344 characters long; it starts `kGcygZsz` and ends `PRBpDQ==`. The check prints `Verified OK`. Everyone in the room gets the same signature, because everyone used the same key. That key is published, so anyone can sign as "the example": never trust a key whose private half is public.

2. **Make your own key pair.** Generate a key pair with the Rivest, Shamir and Adleman method (RSA), 2048 bits long. Save both halves in a text file in your module folder. *Expected:* two blocks of text. One starts `-----BEGIN PUBLIC KEY-----`; the other is your private key and starts `-----BEGIN RSA PRIVATE KEY-----` (floor tier) or `-----BEGIN PRIVATE KEY-----` (full tier). Your private key never leaves your laptop, and you never submit it.

3. **Sign your personal file.** Sign your own index number with your private key and SHA-256, and write the signature in Base64. *Expected:* 344 Base64 characters ending in `==`, different from your neighbour's, because your keys differ.

4. **Verify your signature with your public key.** *Expected:* `Verified OK`. Your public key alone was enough: you needed nothing secret to check it.

> **Floor path.** In CyberChef, step 1: put `COHNDNE999X000` in the input box, with nothing after it. Add `RSA Sign`. Paste the whole of `example-private-key.txt` into `RSA Private Key (PEM)`, including its first and last lines. Leave `Key Password` empty and set `Message Digest Algorithm` to `SHA-256`; the default, `SHA-1`, gives a different signature. Add `To Base64` and copy the output. To verify, start a new recipe. Put the Base64 signature in the input box, then add `From Base64` and `RSA Verify`. Paste `example-public-key.txt` into `RSA Public Key (PEM)`, type `COHNDNE999X000` into `Message`, keep `Message format` at `Raw`, and set `Message Digest Algorithm` to `SHA-256`. For step 2, use `Generate RSA Key Pair` with `RSA Key Length` set to `2048` bits (the default, `1024`, is too short) and `Output Format` `PEM`. It ignores the input box and may take a few seconds. CyberChef makes a new pair every time the recipe runs, so copy the output into your text file at once, then remove the operation. For steps 3 and 4, repeat the step 1 recipes with your own index and your own keys.

Full tier, in a terminal on your Kali virtual machine. Download the two example key files into the lab folder first. Replace the example index with your own from the sixth line on:

```bash
mkdir -p ~/lab4 && cd ~/lab4
printf '%s' COHNDNE999X000 > index.txt
openssl dgst -sha256 -sign example-private-key.txt -out example.sig index.txt
base64 -w0 example.sig; echo
openssl dgst -sha256 -verify example-public-key.txt -signature example.sig index.txt
printf '%s' COHNDNE999X000 > index.txt
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out private.pem
openssl pkey -in private.pem -pubout -out public.pem
openssl dgst -sha256 -sign private.pem -out index.sig index.txt
base64 -w0 index.sig > index.sig.b64; cat index.sig.b64; echo
openssl dgst -sha256 -verify public.pem -signature index.sig index.txt
```

The fourth command prints the example signature in Base64, and the fifth prints `Verified OK`. `openssl genpkey` may print rows of dots and plus signs while it searches for the key; that is normal. The last command checks your own signature the same way. `openssl dgst -sha256 -sign` hashes the file with SHA-256 and signs the digest: the two steps from this morning. Use `printf`, not `echo`, to write the file; `echo` adds an invisible line ending, and you would sign a different file.

*Segment 2: Make and read a certificate*

5. **Make or open a self-signed certificate for a Taxila name.** On the full tier, make one for `sis.taxila.example` with your own key pair. On the floor tier, open the provided certificate for the same name. *Expected:* a block of text that starts `-----BEGIN CERTIFICATE-----`.

6. **Read its fields against the passport.** Find the subject, the issuer, the validity period, the public key and the signature algorithm. *Expected:* the subject and the issuer are the same, both naming `sis.taxila.example` and Taxila College: the certificate is self-signed. The validity has a start and an end, the public key is RSA with 2048 bits, and the signature algorithm is SHA-256 with RSA. These are the passport fields from this morning.

7. **Take the certificate's fingerprint.** The fingerprint is the SHA-256 digest of the whole certificate. *Expected:* 64 hexadecimal characters, usually shown in pairs. For the provided certificate it starts `10:D6:56:4A` and ends `60:73:A3:81`. Write yours down: you use it in segment 4.

> **Floor path.** In CyberChef, paste the whole of `portal-certificate.txt` into the input box and add `Parse X.509 certificate`, with `Input format` `PEM`. It lists `Issuer`, `Subject`, `Validity`, `Public Key` and `Algorithm ID`, and under `Fingerprints` the `SHA256` line, in lower case and without colons. Then open the `certificate-passport` demo, which shows the same certificate beside a passport page and checks its signature. A browser cannot open a certificate file in its own viewer, so you use these two instead.

Full tier. Run these in `~/lab4`; you are signing the certificate with your own private key:

```bash
openssl req -x509 -key private.pem -sha256 -days 30 -subj "/CN=sis.taxila.example/O=Taxila College" -out portal-cert.pem
openssl x509 -in portal-cert.pem -text -noout
openssl x509 -in portal-cert.pem -noout -fingerprint -sha256
```

`openssl req` usually writes a certificate signing request, to send to an authority. With `-x509` it signs the certificate itself instead, so it is self-signed. In the output of the second command, find the `Issuer:` and `Subject:` lines, the `Validity` block, `Public-Key: (2048 bit)` and `Signature Algorithm: sha256WithRSAEncryption`.

*Segment 3: Inspect a live certificate chain*

8. **Walk a real site's chain to its root.** Open a secure website you already use for study, such as the CyberChef site, and open the browser's certificate viewer. Read the certificate for the site, then the certificate above it, then the one at the top. *Expected:* an end-entity certificate issued to the site's name, an intermediate certificate, and a root certificate, with a valid padlock. The root's issuer is the root itself: it is self-signed, and your browser trusts it because it is in the trust store. The names you see depend on the site. Write down the three subjects. You are only reading a public certificate, which every visitor receives; this is viewing a public site, not attacking it.

> **Floor path.** In Chrome or Edge, click the icon to the left of the address, then **Connection is secure**, then **Certificate is valid**. Open the **Details** tab to see the hierarchy. In Firefox, click the padlock, then **Connection secure**, **More information** and **View Certificate**; each certificate in the chain has its own tab. The menu wording can change from one browser version to the next.

*Segment 4: See what secure web hides*

![The same form sent twice. Over plain web the capture shows the line index=COHNDNE999X000 as readable text. Over secure web the capture shows only Application Data records of scrambled bytes.](img/plain-secure.svg "The same index number, on plain web and on secure web.")

9. **Capture your index number over plain web.** Start a capture on the loopback interface. Serve the provided `taxila-portal` application over plain web, that is the Hypertext Transfer Protocol (HTTP), and submit your index number in its form. *Expected:* filter the capture with `http`, and the request `POST /submit` shows the line `index=` followed by your index number, as readable text. Anyone who could see this traffic could read it.

10. **Capture it again over secure web.** Serve `taxila-portal` over secure web with the certificate you made, and submit your index again. *Expected:* filter with `tls`. You see `Client Hello`, `Server Hello` and then only `Application Data` records. Search the capture for your index number: it is not found. The handshake agreed a session key, and everything after it is encrypted.

> **Floor path.** Open the `padlock-truth` demo. Its first part shows the two provided captures, `plain-web.pcapng` and `secure-web.pcapng`, which were made in exactly this way with the example index. Read the plain request, find `index=COHNDNE999X000`, then look for it in the secure capture. If Wireshark is on your laptop, you may also open the two files in it. Write down what was readable over plain web and not over secure web.

Full tier, in `~/lab4`. Download `taxila-portal.py` into the folder first. Open Wireshark from the menu, or run `wireshark` in a second terminal, choose the interface **Loopback: lo**, and start the capture. Then:

```bash
python3 taxila-portal.py
```

Open `http://127.0.0.1:8080/` in Firefox, submit your index, and stop the server with Ctrl+C. In Wireshark, filter with `http`, right-click the `POST /submit` line, and choose **Follow** then **HTTP Stream**. Start a new capture on **Loopback: lo**, then serve secure web with your own certificate and private key:

```bash
python3 taxila-portal.py --secure --cert portal-cert.pem --key private.pem
```

Open `https://127.0.0.1:8443/`. Firefox shows **Warning: Potential Security Risk Ahead**, because your certificate is self-signed: nobody vouches for it. This warning is the lesson, and on any site you did not make yourself you would stop here. This one is different: you made the certificate on this machine, and you can check it. Click **Advanced**, then **View Certificate**, and compare its SHA-256 fingerprint with the one you wrote down in step 7. Only if the two match, go back and choose **Accept the Risk and Continue**. Submit your index, stop the server, and filter with `tls`. Use **Edit**, then **Find Packet**, choose **String** and **Packet bytes**, and search for your index.

*Segment 5: Prove it, break it, reset and write up*

11. **Collect your evidence.** Fill in the evidence pack with your values from steps 3 to 10. *Expected:* your signed file, your public key, your Base64 signature and `Verified OK`, then the certificate fields, the three subjects of the live chain, and your note on the two captures.

12. **Draw and explain.** Draw the sign-and-verify sketch and write your explanation, as listed under Evidence required. *Expected:* a labelled sketch and at most 120 words.

## Prove it

Your signature verifies with your public key and prints `Verified OK`, and it fails after one edit of the file. Your lecturer checks it the same way, with the public key you submit, because a signature is verified, not recomputed. The plain-web capture shows the index number, and the secure-web capture does not. Copy your signed file's content, your public key, your signature and the check's result into your evidence pack.

## Break it

**Fault:** the signed file is changed by a single character.

1. Change the last character of your index number in the file by one, so `0` becomes `1`, and verify again with the same signature and public key. **Symptom:** `Verification failure` on the full tier, or `Verification Failure` in CyberChef, although the key and the signature are unchanged.
2. **Evidence:** the check hashes the file it is given. One changed character gives a completely different digest, the avalanche effect from Day 3, so it no longer matches the digest you signed. Nobody can repair the signature without your private key.
3. **Fix:** put the original character back and verify again: `Verified OK`. Write down the symptom and why it happens.

> **Floor path.** In the verify recipe, change the last character of `Message` by one, read the result, then put it back.

Full tier, to make and then remove the fault:

```bash
printf '%s' COHNDNE999X001 > index.txt
openssl dgst -sha256 -verify public.pem -signature index.sig index.txt
printf '%s' COHNDNE999X000 > index.txt
openssl dgst -sha256 -verify public.pem -signature index.sig index.txt
```

## Reset

1. Copy your evidence into your evidence pack first: your public key, your signature and your notes.
2. Floor tier: clear CyberChef's recipe and input. Delete the text file that holds your private key, because nothing later needs it.
3. Full tier: stop `taxila-portal` if it is still running, delete the lab folder with `rm -r ~/lab4`, then restore the `day-4-start` snapshot. Your module folder keeps the provided files.

## Rules of engagement

No tool in this lab can affect anyone else's system. You inspect only your own certificates and public websites' certificates, and you capture only your own traffic to the provided `taxila-portal` application on your own machine.

## Evidence required

Submit evidence pack 4 before the next teaching day, using the [evidence pack template](../../templates/evidence-pack.md).

1. **Personal values.** In the template's table, with the step each comes from:
   - your signed file's content, which is your index number without spaces or hyphens (step 3);
   - your public key, the whole block, so the signature can be verified, since the marker verifies rather than recomputes a signature (step 2);
   - your signature in Base64, and the successful verification, `Verified OK` (steps 3 and 4).
   Never put your private key in the pack.
2. **Certificate and chain.** The certificate fields you read: subject, issuer, validity (step 6). The three levels of the live certificate chain, with each subject (step 8). A note of what was readable over plain web and not over secure web (steps 9 and 10).
3. **Concept sketch.** Draw by hand, on paper, signing and verifying side by side: which key is used where, and label the hash step on both sides. Photograph it.
4. **Explanation.** In no more than 120 words: why can anyone verify your signature but only you create it?

## Taxila connection

This lab answers two of Taxila's requirements. Item 7 on the security register is signed transcripts. An employer can check a transcript with the Registrar's public key, in seconds, without phoning the college, and any change breaks the signature. Item 8 is the portal certificate and TLS (Transport Layer Security): the portal is reached only over encrypted connections, and its certificate proves the key belongs to `sis.taxila.example`. The Registrar will ask whether a transcript can now prove who issued it: yes, because only the Registrar's private key could have signed it. The Head of IT (information technology) will ask what the self-signed certificate you made would do on the live portal: every visitor would see a warning. The portal needs a certificate that an authority in the trust store has signed.
