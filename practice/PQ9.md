# Practice question 9: a ride-hailing app

This practice question applies the Day 9 ideas to a ride-hailing company. It covers the three questions that classify an attack, the four ways to treat a risk, and a backup set against a stated recovery point. Attempt it in writing before you read the answer guidance. It carries 20 marks.

## The setting

A ride-hailing company in Colombo runs a mobile app. Riders book a trip, and the app sends the nearest driver. Every trip record holds the pickup and drop-off places, the time, the fare and the rider's phone number. Drivers are paid once a week, straight into the bank account stored in their profile. About 300 trips are booked in an ordinary hour, and about 1,500 an hour on a rainy evening.

All trip records and driver profiles sit in one database, on one server in a rented server room. Every night, a copy of the database is written to a disk in the same room. Nobody has ever restored from it.

In the last three months, three things went wrong:

| Event | What happened |
|---|---|
| A changed bank account | A caller who said she was a driver told the support desk she had a new bank account and needed it changed before payday. The support worker changed it. The real driver's weekly pay went to the caller. |
| A long download | A support worker who had left the company still had a working account. Two weeks after leaving, the account downloaded the trip histories of 5,000 riders. |
| A dead evening | On a rainy evening the database server's disk failed. Bookings stopped for two hours, and the night's copy had been taken nearly a day earlier. |

After the third event, the managers agree two targets. Bookings must be back within 30 minutes on a busy evening. No more than 15 minutes of trip records may ever be lost.

The finance manager has a view on the first event. "Bank-account fraud hits only a few drivers a month. Let us accept the risk, or buy insurance for it, and spend nothing on the support desk."

## The question

**(a)** Explain the three questions that classify an attack, and the four ways an organisation can treat a risk. Use one of the company's events as an example in each explanation. **(6 marks)**

**(b)** Apply these ideas to the company. Classify the changed bank account and the long download on all three questions, and name the property each one harmed. Then compare the nightly copy with the targets the managers set. Propose a backup and recovery plan that meets both targets and follows the three-two-one rule. **(7 marks)**

**(c)** Evaluate the finance manager's view. Discuss whether accepting the bank-account risk, or transferring it with insurance, is a sound choice here. Recommend what the company should do, say what residual risk would remain, and give one cost of your recommendation. **(7 marks)**

## Answer guidance

Read this only after you have written your own answer.

**Part (a).** Three questions describe any attack. Is it passive, only watching or reading, or active, changing or sending something? Is the attacker an insider, who already has access, or an outsider, who starts with none? Is it targeted, aimed at this victim, or opportunistic, aimed at whoever is open? The answers give the attack's profile, which points to the controls that fit. The changed bank account is a good example: active, an outsider, and targeted at one driver's pay. The four treatments are these. Mitigate: add a control that lowers the likelihood or the impact. Avoid: stop the activity that creates the risk. Transfer: let another party carry the cost, as an insurer would. Accept: live with the risk as a recorded choice, with an owner. After any treatment, what remains is the residual risk. For the dead evening, mitigation would be more frequent backups and a standby server. Avoiding it would mean not running bookings at all, which makes no sense for this business.

**Part (b).** The changed bank account was active, because a record was changed. The caller was an outsider, who used social engineering to make an insider act for her. It was targeted at one driver. It harmed integrity, because the bank account in the profile was no longer correct. Authenticity was harmed too, because the caller was not who she claimed to be. The long download was passive, because data was read and nothing was changed. It came from an insider, an account the company itself had issued. It was opportunistic in reach, since it took every rider it could. A strong answer notes that it could also be read as targeted at the company. It harmed confidentiality, of personal data about where people travel. The nightly copy fails both targets. A failure just before the night's copy loses almost a day of records, far more than 15 minutes. On a day with a rainy evening, that could be more than 10,000 trips. It does not meet the 30-minute target either, because a disk in the same room must still be restored onto a working server. A plan that meets both targets has three parts. A standby database server receives every change within minutes and can take over by failover inside 30 minutes. A copy at least every 15 minutes, or continuous copying, goes to a second kind of storage. A daily copy is kept off-site, away from the server room. The restore is tested regularly.

**Part (c).** Acceptance is a recorded choice to live with a measured risk, not a way to avoid spending. A few drivers a month, each losing a week's pay, is real harm to real people. Each loss also damages trust in the company's payments. The fix is cheap, so acceptance is hard to defend here. Insurance would repay the money, so it transfers part of the cost. It does not stop the fraud, protect the drivers' trust, or close the weakness that let a phone call change a bank account. Mitigation fits better. Any change to bank details is confirmed by a call back to the number already on file, or in the app with the driver's own sign-in. A second staff member approves it. The support desk is trained to recognise urgency and authority in a request. The leavers' process should also disable accounts on the last day, which answers the long download. The trip histories are personal data, so the company has duties as a controller. The residual risk is a determined attacker who also controls the driver's phone. It is rare, and is caught when the driver reports missing pay. One cost: call-backs slow the support desk and need staff time, and some genuine drivers will wait a day for their change. A strong answer weighs that delay against a week's pay lost.
