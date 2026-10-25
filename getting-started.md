# Getting started

Read this guide before Day 1. It shows you how the ten days work, how to set up your laptop, and the rules for the tools you will use. Most students finish it in an evening. The full-tier set-up takes longer, because of the downloads.

**Before Day 1, do these five things.**

1. Read sections 1 to 3 of this guide, so you know how the module works.
2. Set up the floor tier (section 4). It takes about twenty minutes on any laptop.
3. If your laptop can run it, set up the full tier as well (section 5).
4. Open the [environment check page](days/prelude/artefacts/check.html) and read its result (section 6).
5. Read the rules of engagement (sections 7 and 8) and how your coursework works (sections 9 and 10).

## 1. The ten days

The module has nine teaching days and a tenth day for the group exercise and exam preparation. On each teaching day, the morning builds the ideas and the afternoon uses them in a lab or an activity.

| Day | Morning | Afternoon |
|---|---|---|
| 1 | What we protect, and from what | Mapping data, properties and risk |
| 2 | Secrecy with keys | Ciphers by hand and by machine |
| 3 | Fingerprints: hashing and integrity | Fingerprints and safe password storage |
| 4 | Signatures, certificates and Transport Layer Security (TLS) | Keys, certificates and a look inside TLS |
| 5 | Who are you, and what may you do | Accounts, permissions and a hardened baseline |
| 6 | Web application flaws and their fixes | Find and fix injection and scripting flaws |
| 7 | Email and databases | Reading headers and locking down a database |
| 8 | Networks: threats and defences | Services, firewall rules and captured traffic |
| 9 | Attacks, people, risk and continuity | Taxila's risk register and continuity plan |
| 10 | Group tabletop exercise | Synthesis and exam preparation |

Every idea is shown on a small demo before it is given its name. Each day builds only on the days before it, so a missed day leaves a gap under everything that follows. If you miss a day, read its notes and try its demos before the next one.

> **You already know this.** A building goes up one floor at a time. You cannot stand on the third floor until the second floor is built.
>
> *Mapping:* each floor = one teaching day; the floor below = the earlier days; standing on a floor before the one below exists = using an idea before the idea it needs.

**How a teaching day works.** In the morning you watch each idea work in a demo, then you name it, then you see it at Taxila College. In the afternoon you use the ideas on your own laptop. Between teaching days you read the day's notes again, answer the quick checks, try the plays, and attempt the day's practice question. After Days 2 to 6 you also submit an evidence pack (section 9).

> **Taxila.** Taxila College is a fictional private college in Sri Lanka, with campuses in Colombo and Kandy. You join its information technology (IT) office as a trainee security analyst. Each teaching day is one day of your placement, and each day adds controls to the college's security register.

## 2. How the portal works

The portal is this website. Its home page lists the ten days. Each day's page appears before that teaching day, and it holds:

- the **notes** for the morning, with links to the demos in teaching order;
- the **slides** as a PDF file;
- the **lab sheet** for the afternoon, with numbered steps;
- the **demos**: small pages that show one idea working;
- the **plays**: short practice games you can repeat;
- the **practice question**, with answer guidance.

The [glossary](glossary.md) explains every new term, filed by the day that teaches it. The [coursework pages](coursework/README.md) hold the two coursework briefs.

Some pages have a **Mark as done** button. It keeps a record for you on this device only. It never locks or unlocks anything, and your lecturer never sees it.

**Keep an offline copy.** The whole portal works without the internet. Open the [portal's repository](https://github.com/nirangadh/HNDNE-Principles-of-Information-Security), choose the green **Code** button, and download the zip file it offers. Unzip it into a folder you will keep, then open `index.html` in that folder. Download a fresh copy after each teaching day, because new days are added as the module runs.

## 3. Two ways to run every lab

Every lab can be done in two ways, called **tiers**.

- **Floor tier.** A current web browser, the portal's demos, the files each lab provides, and CyberChef, a free tool that runs inside the browser. Every laptop can do this. **Every mark in the coursework can be earned at the floor tier.**
- **Full tier.** A Kali Linux virtual machine, which is a whole Linux computer running inside a window on your laptop. It lets you run the real tools: OpenSSL, Wireshark, Lynis, iptables, MariaDB and Python. It is recommended where your laptop can run it, and it earns no extra marks.

> **You already know this.** You can cook every dish in a recipe book on a single hob. A full cooker with an oven is faster for some dishes, but it is not needed.
>
> *Mapping:* the single hob = the floor tier, enough for every lab; the full cooker = the full tier, closer to real work but not required; the recipe book = the lab sheets.

> **Common mistake.** "The floor tier earns fewer marks." It does not. Every mark can be earned in the browser. The virtual machine is optional.

**Which tier is mine?** Read down this table. Stop at the first row that matches your laptop.

| If your laptop... | Use |
|---|---|
| is a Chromebook or a tablet | the floor tier |
| has an Arm processor, such as a Mac with Apple silicon (M1 or later) or a Windows laptop with a Snapdragon chip | the floor tier: the Kali Linux virtual machine is built only for Intel and Advanced Micro Devices (AMD) processors |
| is owned by an employer and you cannot install software | the floor tier |
| has less than 8 GB of memory or less than 40 GB of free disk space | the floor tier |
| has 8 GB of memory or more, 40 GB of free disk space, and an Intel or AMD processor | both tiers: set up the floor tier first, then the full tier |

**How to read your laptop's details.** On Windows, open Task Manager, choose **Performance**, then the processor page. It shows the processor's name and a line that reads "Virtualization: Enabled" or "Disabled". The memory page shows the memory in GB. On a Mac, open the Apple menu and choose **About This Mac**: it shows the chip and the memory.

## 4. Set up the floor tier, step by step

Each step says what you should see. If you do not see it, try the step again, then use the help in section 11.

1. **Update your web browser.** Use a current version of Chrome, Edge or Firefox. Open the browser's "About" page and let it update.

   *You should see:* a message that the browser is up to date.
2. **Open the portal** and find this guide again from the home page.

   *You should see:* the home page with the ten days, and a link to this guide.
3. **Make your offline copy** of the portal, as described at the end of section 2. Open `index.html` from the unzipped folder.

   *You should see:* the same home page, with your browser's address bar starting `file://`.
4. **Open CyberChef** from its official site, [gchq.github.io/CyberChef](https://gchq.github.io/CyberChef/).

   *You should see:* four panes: **Operations**, **Recipe**, **Input** and **Output**.
5. **Run a test recipe.** Type `Taxila College` in **Input**. Find the operation **Reverse** in **Operations** and drag it into **Recipe**.

   *You should see:* `egelloC alixaT` in **Output**.
6. **Keep an offline copy of CyberChef.** Use the download link in the top left corner of CyberChef. Unzip the file into a folder you will keep, open the CyberChef page inside it, and run the test recipe again.

   *You should see:* the same result, with your address bar starting `file://`.
7. **Run the environment check** (section 6).

   *You should see:* "Floor tier ready".

## 5. Set up the full tier, step by step

Do this only if section 3 says both tiers suit your laptop. The downloads are several gigabytes, so use a good connection, and allow an evening. Version numbers are correct at the time of writing; a newer version is fine.

1. **Check the laptop.** Read your memory, free disk space and processor as section 3 shows.

   *You should see:* 8 GB of memory or more, 40 GB free or more, and an Intel or AMD processor. On Windows, "Virtualization: Enabled". If it says "Disabled", stop here and bring the laptop to Day 1: the setting is in the laptop's start-up settings, and your lecturer will help you change it.
2. **Install VirtualBox.** Open the [VirtualBox downloads page](https://www.virtualbox.org/wiki/Downloads) and choose the package for **Windows hosts**, or for **macOS / Intel hosts** on an Intel Mac. Run the installer and accept its defaults. Version 7.2.22 is current at the time of writing. Your network may drop for a moment during installation; this is normal. If the installer says that Python support is missing, continue: this module does not need it.

   *You should see:* the VirtualBox window, with no virtual machines yet.
3. **Download Kali Linux.** Open [Get Kali](https://www.kali.org/get-kali/), choose **Virtual Machines**, then the **VirtualBox** image for 64-bit processors. The file name ends in `-virtualbox-amd64.7z`.

   *You should see:* one large `.7z` file in your downloads folder.
4. **Unzip the image.** A `.7z` file needs an unzipping tool. On Windows, install 7-Zip from its official site and use it. On an Intel Mac, use an app that opens `.7z` files. Unzip into a folder on the disk with the free space, not into the downloads folder you clear out.

   *You should see:* a folder that holds a `.vbox` file and a much larger `.vdi` file.
5. **Add the virtual machine.** In VirtualBox, open the **Machine** menu, choose **Add...**, and select the `.vbox` file.

   *You should see:* a Kali Linux virtual machine in the list on the left, powered off.
6. **Start it and log in.** Select the virtual machine and choose **Start**. Wait for the login screen. The username is `kali` and the password is `kali`. If your mouse gets caught inside the window, press the right Ctrl key on Windows, or the left Command key on a Mac.

   *You should see:* the Kali desktop.
7. **Change the password at once.** Open a terminal from the Kali menu and run `passwd`. Type `kali` as the current password, then a new password twice. Nothing appears on screen while you type a password; this is normal. Write the new password somewhere safe.

   *Why:* every Kali image in the world starts with the same password, so anyone who knows Kali knows yours. You will meet this idea again on Day 5.

   *You should see:* `passwd: password updated successfully`.
8. **Update the system.** Run `sudo apt update`, then `sudo apt full-upgrade -y`. Give your new password when asked. This can take twenty minutes or more.

   *You should see:* the commands finish without the word `E:` at the start of a line. Restart the virtual machine when they finish.
9. **Install the module's tools.** Run `sudo apt install -y wireshark mariadb-server lynis`. If a screen asks whether users who are not the superuser should be able to capture packets, choose **Yes**.

   *You should see:* the command finish without the word `E:` at the start of a line. If a tool was already installed, the command says so; that is fine.
10. **Let your account capture traffic.** Run `groups`.

    *You should see:* `wireshark` in the list. If it is missing, run `sudo usermod -aG wireshark kali`, then log out and log in again.
11. **Switch the database service off until Day 7.** MariaDB starts itself after installation. A service you are not using is one more thing that could be attacked, so run `sudo systemctl disable --now mariadb`. Day 7 switches it on.

    *You should see:* `systemctl is-active mariadb` prints `inactive`.
12. **Check each tool** with the commands in section 6.
13. **Take a snapshot.** A snapshot saves the whole virtual machine as it is now, so you can go back to it later. Shut Kali down from its menu. In VirtualBox, select the virtual machine, open its **Snapshots** view, choose **Take**, and name the snapshot `prelude-ready`.

    *You should see:* `prelude-ready` in the snapshot list.

From Day 2, each full-tier lab starts by taking a snapshot named for that day, such as `day-2-start`. The lab's last step restores it, so a mistake in one lab never follows you into the next.

## 6. Check your environment

**The floor tier.** Open the [environment check page](days/prelude/artefacts/check.html). It tests your browser for what the demos need: the browser's own cryptography, the module's font, and saving on this device. It also tells you whether you opened it from the portal online or from your offline copy. Open it both ways: once from the portal, once from your offline copy.

*You should see:* "Floor tier ready" at the bottom of the page, both times. If you see "Needs attention", the page says what to do for each check that failed. Write down what it says and bring it to Day 1.

**The full tier.** Run each command in a terminal inside Kali.

| Command | You should see |
|---|---|
| `openssl version` | a line starting `OpenSSL 3` |
| `python3 --version` | a line starting `Python 3` |
| `python3 -c "print('Python is ready')"` | `Python is ready` |
| `wireshark --version` | a first line starting `Wireshark 4` |
| `mariadb --version` | a line that names MariaDB and a version starting `11` |
| `lynis --version` | a version number starting `3` |
| `iptables --version` | a line starting `iptables v1` |
| `systemctl is-active mariadb` | `inactive` |

The third command runs a one-line Python program. From Day 4 you run a provided application the same way, with `python3` and the file's name.

## 7. The defender's seat

In this module you sit in the defender's seat. You will learn how attacks work. But you see each attack the way a defender sees it: in a log, a captured conversation between two computers, a test report, or an animation. Your hands-on work is a defender's work. You **verify, configure, fix, detect and record**.

You never run an attack tool in this module, and you never type an attack into a website or an application. This is not because attacks are a secret. A principles module needs you to understand why each defence works, and attack tools teach the attacker's buttons, not the defender's reasons.

> **Taxila.** As a trainee analyst, you work only inside the IT office's own practice set-up. The college's real systems are never your lab.

## 8. Rules of engagement, and why the law cares

Every lab sheet has a section called **Rules of engagement**. It always opens with the same sentence:

> **Key idea.** No tool in this lab can affect anyone else's system.

The labs use only three things: your own machine, the files and applications the module provides, and the portal's demos. On Day 4 you also view the certificates of public websites, which is reading, not testing.

**Why the law cares.** In Sri Lanka, the Computer Crime Act, No. 24 of 2007, makes it an offence to access a computer, or the information in it, without lawful authority. It is also an offence to make a computer do something that changes or damages it without lawful authority. The penalties include fines and imprisonment of up to five years. "Lawful authority" for testing a system means written permission from its owner. Good intentions are not permission, and doing no damage is not permission.

> **You already know this.** A learner driver practises on a closed practice track. The same driving on a public road, without a licence, breaks the law even if nobody is hurt.
>
> *Mapping:* the practice track = your own machine, the provided files and applications, and the demos; the public road without a licence = someone else's system without written permission.

> **Common mistake.** "Trying a security technique on a real website is harmless if nothing breaks." Without written permission it is an offence, whatever happens. In this module you work only on your own machine and the provided material.

This means: do not try anything from this module on the college's network, on a website, on a classmate's laptop, or on a phone, even "just to see". If you are unsure whether something is allowed, ask before you do it.

## 9. How evidence packs work

The evidence packs are 25% of the module. You submit five packs, one after each of Days 2, 3, 4, 5 and 6. Each pack is due **before the next teaching day**. Submit each one through the learning management system (LMS) as one PDF file. The full rules are in the [evidence packs brief](coursework/evidence-packs-brief.md).

Every pack has three parts, and the day's lab sheet says exactly what each part holds.

1. **Your personal values.** Each lab uses your index number, written without spaces or hyphens, as its input. Your results are therefore different from every other student's, and your lecturer can work them out again to check them. The example index number in the lab sheets, `COHNDNE999X000`, belongs to nobody: results made from it score zero.
2. **A concept sketch, drawn by hand.** Draw the day's idea on paper, label its parts, and photograph it. Neat drawing is not marked; correct labels are.
3. **A short explanation.** Answer the lab sheet's one "why" question in your own words, in no more than 120 words. Simple English is fine. The ideas are marked, not the language.

| Part | Marks |
|---|---|
| Completeness | 4 |
| Personal values | 8 |
| Concept sketch | 5 |
| Explanation | 3 |

Use the [evidence pack template](templates/evidence-pack.md) for every pack. Its [PDF form](templates/evidence-pack.pdf) has boxes you can type into.

> **You already know this.** A photograph of your own handwriting is yours. Someone else's handwriting in your photograph would look wrong at once.
>
> *Mapping:* your handwriting = the values from your own index number, and your own sketch; someone else's handwriting = values or a sketch copied from another student, which are visibly wrong.

> **Taxila.** Every pack tells Taxila's story, but the numbers in it are yours alone.

## 10. How the group exercise works

The group exercise is the other 25% of the module. The full rules are in the [tabletop brief](coursework/tabletop-brief.md).

- **Groups** of four form on Day 5 (three or five where the class needs it). Each member takes one role: incident lead, technical lead, communications lead or continuity lead.
- **Preparation** runs across Days 6 to 9. Your group builds a risk register for Taxila of at least ten risks, and a controls map. You start the register in the Day 1 lab, on the [risk register template](templates/risk-register.csv), a plain `.csv` file that any spreadsheet program opens. Likelihood and impact are each scored from 1 (lowest) to 5 (highest), and the risk score is the two multiplied together. The template's first row is a worked example; replace it with your own rows.
- **The live round** is on Day 10 morning. Your lecturer runs an incident at Taxila, adding events every few minutes. Your group chooses each action and records it, with its reason, in an action log. At the end, each member answers one question about a role that was not their own.
- **After Day 10** your group submits an after-action report, an updated continuity plan and a signed contribution statement.

**How your work is marked.** Marks reward understanding that you show and explain. A partly correct answer that you explain well can earn more than a perfect answer you cannot explain. So attempt every task: partial credit is given.

**Using generative artificial intelligence (AI) tools.** You may use AI tools to help you learn. Submitting work you do not understand is not allowed, and your programme's rules on generated text apply. Your lecturer may ask you to explain any part of your coursework in a short conversation, called a viva. If you cannot explain it, it is not your work. Use AI, understand what it gives you, and own what you submit.

## 11. Where help is

- **During set-up:** read the step again, then the message on the environment check page. Then ask a classmate who has the same kind of laptop.
- **On Day 1:** the morning starts with a short set-up check. Bring your laptop charged, with its charger. Your lecturer fixes problems in the room, starting with anything that stops the floor tier.
- **During the module:** each day's notes, the [glossary](glossary.md), and your lecturer during the labs. Questions about deadlines and submissions go through the learning management system.

If the full tier still does not work after Day 1, use the floor tier. You lose no marks, and you can try the full tier again later.

## 12. Reading

| | |
|---|---|
| Core | Pfleeger, C. P., Pfleeger, S. L. and Coles-Kemp, L., *Security in Computing*, 6th ed., Addison-Wesley Professional (the 4th edition, by the first two authors, serves equally) |
| Core | Bishop, M., *Computer Security: Art and Science*, 2nd ed., Addison-Wesley Professional |
| Free | Computer Crime Act, No. 24 of 2007, Sri Lanka |
| Free | Personal Data Protection Act, No. 9 of 2022, Sri Lanka, as amended by the Personal Data Protection (Amendment) Act, No. 22 of 2025 |

Each day's notes say which chapters to read. Next: [Day 1, what we protect, and from what](days/day-1/index.html).
