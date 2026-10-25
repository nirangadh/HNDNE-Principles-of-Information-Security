# Practice question 2: a school examinations board

This practice question applies the Day 2 ideas, symmetric and asymmetric encryption and the hybrid pattern, to a school examinations board. Attempt it in writing before you read the answer guidance. It carries 20 marks.

## The setting

A provincial school examinations board sets the papers for a national examination. The board prints nothing itself. Instead, it sends each paper as a file to 25 district centres, and each centre prints its own copies on the morning of the examination.

Today, the board encrypts every paper with one symmetric key. The same key is used for all 25 centres and for every examination of the year. An officer reads the key to each centre over the phone the evening before.

Last month, an officer's laptop was stolen from a car. The laptop held the encrypted papers for the next two examinations. A sticky note with the key was found in the laptop bag. The board's director says: "Nobody outside the board knows which encryption method we use, so the papers are still safe."

## The question

**(a)** Compare symmetric and asymmetric encryption. For each, state how many keys are used and who holds them, how fast it is, what it is typically used for, and its main weakness. **(6 marks)**

**(b)** Design a better way for the board to send each paper to the 25 centres, using the hybrid pattern. Say which keys exist, who holds each one, what is encrypted with which key, and in what order the steps happen. A labelled diagram may be part of your answer. **(8 marks)**

**(c)** Evaluate the director's claim that the papers are still safe. Use Kerckhoffs's principle, and say what was actually lost when the laptop was stolen. Then say what the board must now do about the two papers on the laptop, and why your design in part (b) would have limited the harm. **(6 marks)**

## Answer guidance

Read this only after you have written your own answer.

**Part (a).** Symmetric encryption uses one shared secret key, held by every party that encrypts or decrypts. It is fast, so it is used to encrypt files, disks and network traffic. Its main weakness is the key distribution problem: the same key must reach every party without anyone intercepting it. Asymmetric encryption uses a key pair. The public key may be given to anyone; the private key is kept by its owner alone. It is much slower and can lock only short messages. So it is used to carry or agree a symmetric key, not to encrypt whole documents. A strong answer sets the two side by side, point by point.

**Part (b).** Each centre makes its own key pair and sends only its public key to the board. The private key never leaves the centre. For each paper, the board makes a fresh symmetric key, such as an Advanced Encryption Standard (AES) key, and encrypts the paper with it. The board then encrypts that symmetric key 25 times, once to each centre's public key, and sends each centre the encrypted paper and its own encrypted copy of the key. Each centre opens the key with its private key, then opens the paper with the key. Nothing secret is read over the phone. A strong answer gives the order clearly. It also says why the paper is encrypted with the symmetric key, not the public keys: the paper is long, and asymmetric encryption is slow and limited to short messages. The best answers use a fresh key for each paper, so one leaked key exposes only one paper.

**Part (c).** The claim is weak. Kerckhoffs's principle says that security must rest on the key, not on keeping the method secret. Standard methods are public anyway, and here the key was in the same bag as the ciphertext. So the thief holds both the ciphertext and the key, and both papers must be treated as read: confidentiality is lost. The board must rewrite both papers, and stop using that key everywhere, because the same key protects every examination of the year. With the design in part (b), nobody writes a key down or reads it over the phone. The board keeps each paper's key only until it has locked it to the centres' public keys. The centres' private keys never leave the centres. So a stolen laptop holds ciphertext that nobody can open, and a fresh key per paper means any one lost key would expose one paper, not the whole year. Strong answers also note that a key written beside the ciphertext defeats any method, however strong.
