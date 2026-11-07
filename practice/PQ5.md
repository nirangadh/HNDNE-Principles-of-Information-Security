# Practice question 5: a tea estate's payroll office

This practice question applies the Day 5 ideas to a tea estate's payroll office: the three processes, access-control models, and least privilege with separation of duties. Attempt it in writing before you read the answer guidance. It carries 20 marks.

## The setting

A tea estate in the hill country pays about 600 workers. Its payroll office has three staff: a payroll clerk, a supervisor and an accountant. They share one computer in the office. The computer has one account, `payroll`, and its password is written on a card in the desk drawer.

The clerk types in each worker's days and rates. The supervisor checks the totals. Each month the accountant prepares the bank file that tells the bank how much to pay into each worker's account, and sends it to the bank.

Last month the bank paid one worker three times the usual wage. The extra money had gone to an account number nobody recognised. The estate manager asked who had changed the bank file. The computer could show that the file was changed one weekend afternoon, by the account `payroll`. All three staff say they were not in the office.

The estate's IT (information technology) adviser proposes three changes:

1. Give each of the three staff their own account on the computer, with their own password.
2. Use role-based access control, with a clerk role, a supervisor role and an accountant role.
3. Keep a record of every change to the payroll data and the bank file.

The estate manager says: "This is too much for a team of three. We trust our staff. If we just change the shared password every month, the problem is solved."

## The question

**(a)** Explain the three processes of authentication, authorisation and accounting (AAA). Say what each one does, and explain why they are not the same as the properties of authenticity and accountability. **(6 marks)**

**(b)** Apply these ideas to the payroll office. Explain which of the three processes failed when the bank file was changed, and why the shared account makes the change impossible to trace. Then design the three roles: for each role, name what it may do and what it may not, so that each account has only what its job needs. **(7 marks)**

**(c)** Evaluate the estate manager's view. Discuss whether changing the shared password each month would solve the problem, and whether least privilege and separation of duties are worth their cost in an office of three. Recommend what the estate should do, with one cost of your recommendation. **(7 marks)**

## Answer guidance

Read this only after you have written your own answer.

**Part (a).** Authentication checks who someone is: the computer checks a claimed identity, usually with a password, and accepts or refuses it. Authorisation decides what that identity may do: which files it may open and which actions it may take. Accounting records what was done: who did what, and when. The three run in that order whenever someone uses a system, and each can fail on its own. They are processes: steps a system runs. Authenticity and accountability are properties from the five: things that should be true of information. Authenticity means the information or person is genuine. Accountability means an action can be traced to a person. Accounting is the process that produces accountability. A strong answer keeps the two lists apart and does not use "authentication" where "authenticity" is meant.

**Part (b).** Accounting failed in the sense that matters. A record existed, but it named only `payroll`, an account three people share. A record is only as good as the identity behind it. So the real failure began at authentication: the computer could not tell the three staff apart. It accepted anyone who knew a password kept in a drawer. With one shared account, every action looks the same, so nobody can be held to account. This shows that accounting depends on authentication: you can only record who did something if you first know who they are. For the roles:

- The **clerk role** may enter and correct days and rates. It may not change bank account numbers or create the bank file.
- The **supervisor role** may read the totals and approve them. It may not edit the figures it checks.
- The **accountant role** may prepare and send the bank file from approved totals. It may not change days, rates or account numbers on its own.

A change to a worker's bank account number should need two people: one asks for it and another approves it. Each person gets their own account, assigned to one role. Each role holds the least it needs.

**Part (c).** A monthly password change does not solve the problem. The account is still shared, so the record would still say only `payroll`. Anyone who learns the new password, for example from the card in the drawer, can still change anything. It changes the secret, not who can be traced or what one person can do. Least privilege is not about distrusting staff. It limits the damage when a password is stolen or misused: if only the accountant's account can send the bank file, a leaked clerk password cannot change a payment. Separation of duties means one person cannot both change an account number and send the payment. That is the very gap this incident used. In an office of three the cost is small. Three accounts and three roles cost little. A second person must approve each change to a bank account, which takes a few minutes. And someone must keep the record and read it. The estate should take all three of the adviser's changes. It should also make one change to bank account numbers need the supervisor's approval, and remove the password card. The cost is a little time each month and the work of setting up the accounts; a single overpayment like last month's costs more. A strong answer rejects the manager's view with reasons and does not treat trust as a control.
