# Practice question 7: a microfinance cooperative's mobile app

This practice question applies the Day 7 ideas to a microfinance cooperative. It covers why an email cannot prove its sender, the three published checks, a scoped database account, and a controller's duty. Attempt it in writing before you read the answer guidance. It carries 20 marks.

## The setting

A microfinance cooperative lends small amounts to about 9,000 members in villages across two districts. Twenty field agents visit members, collect repayments and record them in the cooperative's mobile app. The app sends everything to one database at the head office. The database holds each member's name, national identity card number, phone number, loan balance and repayment history.

Last month three field agents received an email that seemed to come from the general manager. Its from line showed the manager's real address. It asked them to approve an urgent loan payout to a member "whose account details have changed", and gave a new bank account. One agent approved it before calling the office. The money went to an account nobody recognised.

The cooperative's IT (information technology) officer read the message's header afterwards. These are the parts that matter:

| Header part | What it showed |
|---|---|
| From | the general manager's real address, at the cooperative's own domain |
| Reply-To | an address at a domain that differs from the cooperative's by one extra letter |
| Authentication results | the sending-server check failed; there was no signature; the cooperative publishes no rule for failures |
| The lowest received line written by the cooperative's own mail server | the message was handed over by a server outside the cooperative |

The IT officer also found that the mobile app signs in to the database with one account, and that account holds every right on every database. Nothing records what the account does.

The IT officer proposes three changes:

1. Publish the three email checks for the cooperative's domain, with a policy to hold failing messages.
2. Give the app's database account only the rights the app needs, and turn on a log of every request.
3. Remind agents to check the reply-to and to confirm any payment request by phone.

The general manager says: "The email was the problem, not the database. Our database disk is already encrypted, so the members' data is safe. Publish the email checks and stop there."

## The question

**(a)** Explain why the from line of an email cannot prove who sent it. Then explain what each of the three checks adds: the Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), and Domain-based Message Authentication, Reporting and Conformance (DMARC). **(6 marks)**

**(b)** Apply these ideas to the cooperative. Use the header table to explain how the IT officer can tell the message was not from the general manager, naming each tell. Then design the app's database account: say which kinds of right it needs and which it must not have, and what the log should let the cooperative answer. **(7 marks)**

**(c)** Evaluate the general manager's view. Discuss whether publishing the email checks alone would have been enough, and whether the encrypted disk keeps the members' data safe. Then say what the cooperative owes its members as the controller of their personal data. Recommend what the cooperative should do, with one cost of your recommendation. **(7 marks)**

## Answer guidance

Read this only after you have written your own answer.

**Part (a).** Email is handed from server to server by the Simple Mail Transfer Protocol (SMTP). The sender writes the from line, and no server on the way is required to check it, so any address can be written there. The domain owner fixes this by publishing records that receiving servers can read. SPF lists the servers allowed to send mail for the domain; a receiver compares the server that handed over the message with that list. DKIM has the sending server sign each message with the domain's private key. The receiver verifies the signature with the public key the domain publishes, so a message not signed by the domain, or changed on the way, fails. DMARC is the rule for failures: the domain in the from line must match a domain that passed SPF or DKIM. The domain also tells receivers whether to deliver, quarantine or reject a message that fails. A strong answer keeps the three jobs apart and does not say that DKIM encrypts the message.

**Part (b).** There are three tells. The sending-server check failed and there was no signature, so nothing backs the from line. The lowest received line written by the cooperative's own server shows the message came from outside. Lines below it were written by the sender's side and prove nothing. And the reply-to is a look-alike domain, so any reply goes to the sender, not the manager. The message got through because the cooperative published no DMARC rule, so the receiver had no instruction to hold it. For the database account: the app needs to read members' records and loan balances, add repayment records, and perhaps update balances. It does not need to delete records, drop tables, read other databases, or create accounts and give rights to others. Each right should be granted for the specific tables the app uses. The log should let the cooperative answer which account read or changed which records, and when, including requests that were refused.

**Part (c).** Publishing the email checks is necessary but not enough. With a quarantine policy, a spoofed message from the cooperative's own domain would have been held. But a look-alike domain can publish its own SPF, DKIM and DMARC and pass all three, for its own domain. Only a person reading the address, and confirming a payment by phone, catches that. The encrypted disk protects a stolen disk or backup. It does nothing against a stolen password: the database decrypts for any account allowed to read. If an agent's or the app's password is taken by a message like this one, the app's account today reaches every member's identity number and every database. Scoping the account limits that reach. A scoped account also limits injection, where typed input is read as a command, though its real fix is a parameterised query in the app. And the log is the only way to know what was read. As the controller, the cooperative decides why and how members' personal data is processed. So it must keep that data secure and be able to show what it does with it. Under Sri Lanka's Personal Data Protection Act, No. 9 of 2022, as amended, those are duties on the organisation; at the time of writing, a government order has fixed the date from which they apply. The cooperative should take all three changes. The main cost is a few days of the IT officer's time. The records must be published and their reports watched before failures are held, and the app's account reworked and tested. The log needs disk space and someone to read it, and agents lose a minute on each payment call. One payout to an unknown account costs more. A strong answer rejects "the email was the problem" with reasons, and does not treat disk encryption as protection against a stolen login.
