# Practice question 4: a provincial land records office

This practice question applies the Day 4 ideas, digital signatures, non-repudiation and certificates, to a provincial land records office. Attempt it in writing before you read the answer guidance. It carries 20 marks.

## The setting

A provincial land records office in Sri Lanka keeps scanned copies of land deeds. Banks and buyers ask the office for certified copies before a loan or a sale. Today an officer sends each certified copy as a file by email. The officer's name is typed at the bottom, beside the words "certified true copy".

Last month a bank received a certified copy that showed a larger area of land than the deed in the office's store. The officer whose name was on the copy says: "I never issued that copy." Nobody can prove who made it, or whether it was changed after it left the office.

The office's IT (information technology) team proposes two changes:

1. Every officer gets a key pair and signs each certified copy before sending it.
2. The office's web portal, where banks will download certified copies, gets a certificate. To save money, the team will make this certificate itself, a self-signed one. It also suggests that each officer's public key should be published as a self-signed certificate.

A senior officer adds: "Once the portal shows a padlock, every copy downloaded from it is genuine."

## The question

**(a)** Explain how a digital signature is made and how it is checked. Say which key is used at each step, and what a valid signature proves and does not prove. **(6 marks)**

**(b)** Apply this to the office. Describe how a certified copy would be signed and how a bank would check it. Explain what happens if someone changes one digit of the land area after signing. Then explain why the officer's denial could be settled with a signature, but not if all officers shared one secret key to seal copies. **(7 marks)**

**(c)** Evaluate the IT team's plan to use self-signed certificates for the portal and for the officers' public keys, and the senior officer's claim about the padlock. Recommend what the office should do, with one cost of your recommendation. **(7 marks)**

## Answer guidance

Read this only after you have written your own answer.

**Part (a).** To sign, the signer's software hashes the document, for example with SHA-256 (Secure Hash Algorithm, 256 bits), and signs that digest with the signer's private key. The signature travels beside the document. To check, anyone hashes the document they received and checks the signature against that digest with the signer's public key. If it passes, two things are proved. Origin: only the holder of the private key could have made the signature. Integrity: the document is the same, byte for byte, as when it was signed. Because only one person holds the private key, the signer cannot later deny signing: non-repudiation. A signature does not hide the document; anyone can still read it. A strong answer says plainly that signing uses the signer's own private key, which is a different job from encrypting to someone's public key.

**Part (b).** Each officer keeps a private key that never leaves them, and the office publishes each officer's public key. To issue a copy, the officer signs its digest with their private key and attaches the signature. The bank hashes the copy it received and checks the signature with that officer's public key. If someone changes one digit of the area after signing, the copy's digest changes completely, by the avalanche effect. The check then fails, and the bank knows the copy is not what the officer signed, though not what changed. Nobody can repair the signature without the officer's private key. The denial can be settled because a valid signature could only have been made with that officer's private key. If the check passes, the officer signed it; if a copy carries no valid signature from them, it is not theirs. A shared secret key, used for a keyed seal such as a hash-based message authentication code (HMAC), would show only that someone holding the key made the seal. Every officer holds it, so it cannot show which one: there is no non-repudiation.

**Part (c).** A self-signed certificate is a valid certificate, but nobody else vouches for it. A bank's browser would warn on the portal, because the certificate is in no trust store. Teaching banks to click past that warning would train them to accept any warning, including one from a fake portal. For the officers' keys, a self-signed certificate lets anyone make a key and call it an officer's. A bank could not tell a real officer's key from a fake one, so the signatures would prove little. The office should get the portal's certificate from a certificate authority whose root is in browsers' trust stores. It should have the officers' public keys vouched for by an authority the banks trust, or at least publish them through a channel the banks already trust. The cost is money and work. A public certificate lasts at most a few months at the time of writing, so it must be renewed often. Keys must also be managed when officers join or leave. The senior officer's claim is wrong. A padlock proves that the connection is encrypted and that an authority vouches that the key belongs to the name in the address. It does not prove that a copy is genuine. A copy can be changed before it is placed on the portal, and a look-alike portal can have its own valid padlock. Only the officer's signature on the copy proves who issued it and that it is unchanged. Strong answers keep the two jobs apart: the certificate and padlock protect the connection and name the server, while the signature protects each copy.
