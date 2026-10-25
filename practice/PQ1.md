# Practice question 1: a district clinic's appointment system

This practice question applies the Day 1 ideas, the five security properties, risk and controls, to a small health clinic. Attempt it in writing before you read the answer guidance. It carries 20 marks.

## The setting

A district clinic runs a small online system for booking appointments. Patients book a time with a doctor on a web page. The clinic's three staff manage the bookings from one shared computer at the front desk, using one shared account. The system stores each patient's name, phone number, national identity card number and the reason for the visit.

Last month, one incident had four effects:

1. A list of patients' names and phone numbers appeared in a public messaging group.
2. Several appointment times were changed, so patients arrived at the wrong hour.
3. On the busiest morning, the booking page stopped responding for two hours.
4. A nurse says she did not cancel twelve bookings. The system shows they were cancelled, but not by whom.

## The question

**(a)** Explain the difference between integrity and availability, and the difference between authenticity and accountability. Give one example of each property from a clinic. **(6 marks)**

**(b)** For each of the four effects above, name the security property that was lost, and say why in one sentence. Then choose the effect you think is most serious, and write one complete risk row for it. The row needs the asset, the threat and the vulnerability; a likelihood and an impact, each from 1 to 5; the risk score; and the property most at stake. **(8 marks)**

**(c)** The clinic's owner says: "We lock every door at night, so we are secure." Evaluate this claim. Use the three functions of controls and the idea of defence in depth. Propose one detective control and one corrective control for the clinic, and say what each adds that the locks do not. **(6 marks)**

## Answer guidance

Read this only after you have written your own answer.

**Part (a).** Integrity means the data has not been changed without permission; availability means the data and the service are there when they are needed. The difference: with lost integrity, the data is there but wrong; with lost availability, the data may be correct but cannot be reached. Authenticity asks whether something really comes from who it claims to come from; accountability asks whether you can prove who did what. A strong answer gives a clinic example for each, such as a changed prescription note (integrity) or a booking page that will not load (availability).

**Part (b).** Effect 1 is a loss of confidentiality: personal data was read by people with no right to read it. Effect 2 is a loss of integrity: booking data was changed without permission. Effect 3 is a loss of availability: the service was not there when needed. Effect 4 is a loss of accountability: the cancellations happened, but nobody can prove who made them, so the nurse's denial cannot be checked. A good risk row names a real asset, such as patients' phone numbers and identity card numbers. It names a threat that could use the weakness, such as anyone who can sit at the front desk. And it names the weakness itself: one shared account, so any person at the desk can do anything. The scores should be argued, not just stated, and the score must equal likelihood times impact. Do not name a process such as "authentication" where a property is asked for: the properties and the processes are different lists.

**Part (c).** Locks are preventive and physical. They do nothing once someone is inside during the day, and they cannot notice or repair anything. The claim is weak because one control, of one kind, is not defence in depth. A detective control would notice changes and name who made them. One example is a separate account for each person, with a record of who changed or cancelled each booking; this also answers effect 4. A corrective control, such as a regular backup of the bookings and a written plan to restore them, would repair the damage after effect 2 or effect 3. The best answers say why each layer is independent of the locks: it still works when the locks have done their job, or when someone is already inside.
