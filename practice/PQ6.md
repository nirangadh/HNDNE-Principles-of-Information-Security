# Practice question 6: a doctor-channelling booking platform

This practice question applies the Day 6 ideas to a public web platform. It covers the boundary between code and data, injection into a database, cross-site scripting, and the session cookie. Attempt it in writing before you read the answer guidance. It carries 20 marks.

## The setting

A company runs a website where the public book evening appointments with doctors. Patients create an account, sign in, search for a doctor, and leave a short note for the clinic with each booking. On busy evenings thousands of people use the site at once. The site keeps each patient's name, telephone number, national identity card number, and booking history in one database.

A new developer looks over the site and finds three things.

First, the sign-in builds its database question by joining the username and password straight into the text of the query. Second, the note a patient leaves is shown back on the clinic's own page exactly as it was typed, with nothing changed. Third, the cookie that keeps a patient signed in is sent with no extra settings on it.

The developer writes a short report:

1. The sign-in should use a parameterised query, so a patient's input can never change the question the database is asked.
2. The note should be encoded before any page shows it, so it is always shown as plain text.
3. The session cookie should carry three settings, so a script cannot read it, it never travels over a plain connection, and another site cannot make the browser send it.

The site owner replies: "The sign-in is the way in, so fix that. The note is just a message a patient types, and the cookie is only a small file. Fix the sign-in and we are safe."

## The question

**(a)** Explain the boundary between data and command that these flaws share. Then explain what SQL (Structured Query Language) injection is, what reflected cross-site scripting is, and what each of the three session-cookie settings (HttpOnly, Secure and SameSite) does. **(6 marks)**

**(b)** Apply these ideas to the platform. Take the three things the developer found: the sign-in query, the note shown on the page, and the session cookie. For each one, name the fix and say what it protects. Say where each fix belongs, on the server or in the browser. **(7 marks)**

**(c)** Evaluate the owner's view. Discuss whether fixing only the sign-in would make the platform safe, using the note and the cookie to argue your case. Explain why a check added in the browser is not a security control. Then recommend what the platform should do, naming the idea that several independent layers protect better than one, and give one cost of your recommendation. **(7 marks)**

## Answer guidance

Read this only after you have written your own answer.

**Part (a).** All three flaws share one boundary: what a user types should stay data, a value the application reads, and never cross into the command the application runs. SQL injection happens when input is joined into a database query, so part of the input is read as part of the query. A carefully shaped value can add a condition that is always true, so a question meant to return one record returns every record. Reflected cross-site scripting happens when a page shows a user's input as live markup, not as plain text. A script carried in the input, often through a link, then runs in the browser of whoever views the page. The three cookie settings each close a different gap. HttpOnly keeps a script on the page from reading the cookie. Secure keeps the cookie off plain connections, where it could be read in transit. SameSite keeps the browser from sending the cookie on a request that another site started. A strong answer keeps injection and scripting apart, and does not say that encoding or a cookie setting encrypts anything.

**Part (b).** The sign-in: use a parameterised query, which sends the question and the input separately, so input can never change the question. It protects against a crafted sign-in that reads every patient's record, and it belongs on the server. The note: encode the output before any page shows it, so the note is shown as plain text and a script in it can never run. It protects the patients who view the clinic page, and it belongs on the server, where the page is built. The session cookie: set HttpOnly, Secure and SameSite. It protects the token that stands in for the patient after sign-in. The three settings stop a script reading it, a plain connection carrying it, and another site making the browser send it. The settings are placed by the server when it sends the cookie. A strong answer names a fix for each flaw and says what each protects, not only "make it more secure".

**Part (c).** Fixing only the sign-in is not enough. The sign-in fix closes injection into the database. But the note still runs a script in any patient's browser that opens the clinic page. The bare cookie can still be read by such a script, or carried on a forged request. So a patient's session can be taken even with a safe sign-in. A check added in the browser is not a control. The browser runs on the user's own machine, where the check can be skipped. Validation that counts runs on the server. The platform should take all three fixes together. This is defence in depth: several independent layers, each catching what another misses, so one flaw does not open the whole site. As the holder of patients' identity numbers and booking history, the platform has a duty to keep that data secure. One cost of the recommendation is the developer's time to parameterise every query, encode every output, and set the cookie, and to test that ordinary use still works. That cost is small against one patient's records or session being taken. A strong answer rejects "fix the sign-in and we are safe" with reasons drawn from the note and the cookie. It does not treat the sign-in as the only way in.
