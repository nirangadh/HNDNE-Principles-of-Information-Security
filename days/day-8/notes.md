# Day 8: Networks: threats and defences

These notes cover the Day 8 morning. They show what anyone on a shared network can learn by watching it, and how a defender finds every door a server leaves open. They explain how one false reply puts a machine in the middle of a conversation. Then they turn to the defences: three kinds of firewall, systems that notice the unusual, and separate zones with a private tunnel to Kandy.

> **Recall.** Transport security makes web traffic unreadable to anyone on the path.

> **Recall.** Defence in depth stacks independent controls so one failure is not total.

Thousands of phones and laptops join Taxila's student Wi-Fi every day, and the college manages none of them. The Head of IT (information technology) has a report of what the server room's main server shows to the student network. It was made with written permission. It shows a door that should not be open from there. "Before we buy anything," the Head of IT says, "let us see what can be seen, and what can be reached."

Item 15 on Taxila's security register is firewalls and network zones, and you build part of it this afternoon. Item 16 is intrusion detection and monitoring, which you see demonstrated today. Item 17 is the private tunnel between the campuses, taught as a concept.

## 1. Sniffing and traffic analysis

Try the demo first: [The glass wall](artefacts/sniffer-glass.html). Open a plain capture and a secure capture side by side, and compare what each one lets a watcher read.

> **Recall.** Over plain web your index number crossed the network as readable text; over secure web it did not.

On a shared network segment, such as one Wi-Fi network, every machine can receive what the others send. [Sniffing](../../glossary.md#sniffing) is reading that traffic as it passes. A program such as Wireshark, which you met on Day 4, does exactly this. Whatever is sent without encryption can be read: a password typed into a plain web form, a session cookie, the text of a message.

Encryption changes what the watcher gets, but not everything. Inside a secure connection the content is scrambled. The outside of every packet still shows who is talking to whom, on which port, when, and how much. Reading those patterns, without the content, is [traffic analysis](../../glossary.md#traffic-analysis). It can tell a watcher that a laptop talks to the Student Information System (SIS) every evening at ten.

Sniffing is passive: the watcher only receives. An attack that sends, changes or blocks something is active. A passive attack leaves nothing behind for the victim to find.

> **You already know this.** Two people talk out loud in a shared room, and anyone in the room can hear every word. If they pass a sealed note instead, nobody else can read it, although everyone can still see who passed a note to whom.
>
> *Mapping:* anyone in the room hearing the words = any machine on the segment reading unencrypted traffic; the sealed note = encrypted traffic; seeing who passed the note = traffic analysis.

> **Taxila.** The student wireless network carries readable traffic unless the service uses secure connections.

> **Common mistake.** "I would notice if someone were sniffing." Sniffing only receives. It sends nothing, changes nothing and leaves no trace on your machine. The defence is not to watch for watchers: it is to encrypt, so that what they receive is useless.

> **Quick check.** A student opens the SIS over secure web on the student Wi-Fi. Another person on the same Wi-Fi is sniffing. What can the watcher learn?
>
> - [ ] The student's password, because the Wi-Fi is shared
> - [x] That the student's laptop talked to the SIS, when, and how much, but not what was sent
> - [ ] Nothing at all, because secure web hides the whole conversation
>
> **Why:** Secure web encrypts the content, so the password stays hidden. It cannot hide the outside of each packet: the addresses, the port, the time and the size. That is traffic analysis. "Nothing at all" is the tempting wrong answer.

## 2. Scanning and reconnaissance

Try the demo first: [The corridor of doors](artefacts/service-doors.html). Read the outside view of Taxila's main server beside the server's own service list, and match each door.

> **Recall.** A hardened server runs only the services its job needs.

A program that waits for connections on a numbered port is a service, and each listening port is a door into the machine. Checking which doors a machine has, by offering a connection to each port, is a scan. A scan reports each port in one of three states:

| State | What came back | What it means |
|---|---|---|
| open | a service answered | something is listening on this door |
| closed | the machine answered "nothing here" | no service on this port, and nothing in the way |
| filtered | no answer at all | something in the path, usually a firewall, dropped the request |

Attackers scan first, to map the doors before choosing how to try them. So a defender maps them first. The defender keeps an inventory of every listening service, from the machine's own list, and compares it with what the outside actually sees. A door that is open but not on the inventory, or open to a network that should not reach it, is the finding.

The law draws the line here as it did on Day 1. Scanning a system you do not own, without written permission, is an offence under the Computer Crime Act, No. 24 of 2007. Taxila's report was made by the Head of IT, with permission, from inside the college.

> **You already know this.** Someone walks down a corridor and tries each door handle in turn. A handle that turns is an unlocked door. A handle that will not move is a locked door. A door behind a locked gate cannot even be reached.
>
> *Mapping:* a handle that turns = an open port; a handle that does not move = a closed port; a handle behind a locked gate = a filtered port.

> **Taxila.** A scan of the server room's segment shows what is exposed. The outside view of `sis.taxila.example` shows its database port, `3306`, open to the student Wi-Fi.

> **Common mistake.** "A scan is harmless, so it needs no permission." A scan touches every door of someone else's machine. Without the owner's written permission it is access without lawful authority, which the Act makes an offence. Damage is not needed.

> **Quick check.** The SIS server's own list shows a service listening on port `8080`. The outside view from the student Wi-Fi says `8080/tcp filtered`. What does this tell the Head of IT?
>
> - [ ] Nothing listens on `8080`, so there is nothing to do
> - [ ] The service is broken, because it did not answer
> - [x] The service runs, but a firewall in the path drops requests to it, so it should still be stopped if nobody needs it
>
> **Why:** The server's own list proves the service is listening. "Filtered" means no answer came back, because something in the path dropped the request. The firewall hides the door today; a hardened server would not have the door at all. That is defence in depth.

## 3. Interception and address poisoning

Try the demo first: [Trusting the first answer](artefacts/arp-trust.html). Step through a prepared capture and watch one false reply change a laptop's address table.

> **Recall.** A certificate proves which server you reached, so a server in the middle cannot pass as the real one.

A [machine in the middle](../../glossary.md#man-in-the-middle) sits between two parties who each believe they talk directly. Everything they send passes through it. It can read what is not encrypted, and it can change or drop what it relays.

On a local network one simple weakness puts a machine in the middle. Machines on a segment send each other frames using hardware addresses, called media access control (MAC) addresses. This MAC is not the access-control model of Day 5. A machine may know only the Internet Protocol (IP) address it wants, such as `10.10.0.1`. To find the hardware address that goes with it, the machine broadcasts a question to the whole segment: "Who has `10.10.0.1`?" This is the [Address Resolution Protocol](../../glossary.md#address-resolution-protocol) (ARP). The owner replies, and the asker keeps the answer in its address cache.

ARP has no check on who answers. Any machine on the segment can send a reply, even when nobody asked, and the cache simply takes it. A false reply that says "`10.10.0.1` is at my hardware address" is [address poisoning](../../glossary.md#address-poisoning). From then on the victim sends its traffic for the gateway to the wrong machine, which can pass it on unseen.

![A laptop on Taxila's staff network asks who has 10.10.0.1, and the gateway replies with its own hardware address, which the laptop stores in its cache. Later a second machine on the same network sends an unasked reply saying 10.10.0.1 is at its own hardware address. The laptop's cache entry changes, and the laptop's next request goes to the second machine, which passes it on to the gateway.](img/address-poisoning.svg "One true reply, then one false reply: the cache keeps whichever came last")

A defender sees this in a capture: one IP address answered for by two different hardware addresses. Wireshark marks such a frame with the warning `Duplicate IP address configured`. In this module address poisoning is studied by concept and from a provided capture only. It is never performed.

> **You already know this.** A messenger shouts into a crowded hall, "Who is the clerk?" The first voice to answer gets the letters. Nobody checks the voice. An impostor who answers takes each letter, reads it, and hands it on to the real clerk, who never knows.
>
> *Mapping:* trusting the first voice to answer = the address protocol trusting any reply; the impostor relaying the letters = the machine in the middle.

> **Taxila.** A poisoned cache on the staff network could intercept a login. If that login uses secure web, the certificate check from Day 4 fails, and the browser warns. Over plain web, nothing warns at all.

> **Common mistake.** "Address poisoning comes from somewhere on the internet." ARP questions and replies never leave the local segment. A false reply must come from a machine on the same network, which is one reason Taxila keeps unmanaged student devices off the staff network.

> **Quick check.** A capture from the staff network shows `10.10.0.1 is at 02:00:0a:0a:00:01` in frame 2, and `10.10.0.1 is at 02:00:0a:0a:00:42` in frame 6, which nobody asked for. What should the defender conclude?
>
> - [x] Another machine on the segment is claiming the gateway's address, so traffic may be passing through it
> - [ ] The gateway changed its network card, so the cache was right to update
> - [ ] Frame 6 is harmless, because ARP replies only answer questions
>
> **Why:** One address with two hardware addresses, the second one unasked, is the pattern of address poisoning. A replaced network card is possible, but it would not leave the old address answering, and the defender should check rather than assume. ARP replies do not have to answer a question: that is the weakness.

## 4. Firewalls and intrusion systems

Try the demo first: [Three kinds of firewall](artefacts/firewall-generations.html). Send prepared traffic through each kind of firewall, then watch what an intrusion system does with the same traffic.

> **Recall.** [Injection](../../glossary.md#injection) is typed input read as a command, and a [parameterised query](../../glossary.md#parameterised-query) is its fix.

A firewall sits between networks, or in front of one machine, and decides for each packet: let it through, or drop it. Firewalls grew in three steps.

1. **A packet filter** looks at each packet alone: its addresses, its ports and its protocol. It keeps no memory, so it cannot tell a real reply from a packet that only pretends to be one.
2. **A [stateful firewall](../../glossary.md#stateful-firewall)** remembers every connection that was opened through it. A packet that belongs to a known connection may pass; a packet that claims to be a reply, to a connection nobody opened, is dropped.
3. **An application-layer firewall** reads the content of the traffic, not just its outside. It can see an injection string inside a web request. A [web application firewall](../../glossary.md#web-application-firewall) (WAF) is this kind, built for web traffic.

![Three firewall kinds side by side: the packet filter checks addresses and ports, the stateful firewall also keeps a connection table, and the application-layer firewall also reads the content. A flood of fake replies gets through only the packet filter. An injection string over plain web gets through all but the application layer. An injection string inside encryption gets through the first two, and the application layer can read it only if it ends the encryption itself.](img/firewall-kinds.svg "Each kind adds one thing it can check; none of them can read inside encryption it does not end")

Some attacks aim only at availability. A [denial of service](../../glossary.md#denial-of-service) floods a service with traffic so real users cannot reach it. A distributed denial of service uses many machines at once, so blocking one sender does not stop it. One kind of flood sends packets that pretend to be replies. A packet filter that lets replies through lets these through too; a stateful firewall drops them, because it knows no connection was ever opened.

A firewall decides; it does not tell you what happened. That is the job of intrusion systems.

- An [intrusion detection system](../../glossary.md#intrusion-detection-system) (IDS) watches a copy of the traffic, out of its path. It raises an alert, and the traffic still flows.
- An [intrusion prevention system](../../glossary.md#intrusion-prevention-system) (IPS) sits in the path. When it recognises something, it blocks it.
- Both recognise trouble in two ways. **Signature** detection matches traffic against patterns of known attacks, such as a known injection string. **Anomaly** detection learns what normal looks like and flags what is far from it, such as ten thousand packets a second from the Wi-Fi at midnight.

> **You already know this.** Picture three door checkers. The first looks at each person's face and lets anyone with a ticket in. The second also keeps a guest list, and stops someone who says "I am coming back in" but never went out. The third also searches every bag.
>
> *Mapping:* looking at each person alone = a packet filter; the guest list = tracking connection state; searching the bag = reading the payload.

> **Taxila.** A firewall between the student wireless network and the servers; monitoring that notices the unusual (register item 16).

> **Common mistake.** "A firewall reads encrypted payloads." It reads only what it can see. Inside a secure connection the content is scrambled, unless the firewall itself ends the encryption, decrypts, checks and encrypts again. A web application firewall in front of Taxila's portal could do that only if the portal's certificate and key were placed on it.

> **Quick check.** A request to Taxila's portal carries an injection string in its login field, sent over plain web. Which firewall can stop it?
>
> - [ ] A packet filter, because the port is the web port
> - [ ] A stateful firewall, because the request is part of a real connection
> - [x] Only an application-layer firewall, such as a web application firewall, because it reads the content
>
> **Why:** The request comes to an allowed port inside a real connection, so the first two kinds let it through. Only a firewall that reads the content can see the injection string. The real fix is still in the portal's code, the parameterised query; the firewall is one more layer.

## 5. Zones, private tunnels and depth

Try the demo first: [Zones and the demilitarised zone](artefacts/zones-dmz.html). Move Taxila's servers into zones, then mark one as broken into and see how far the trouble can spread.

> **Recall.** A session key, agreed at the start, encrypts everything that follows on a secure connection.

Segmentation divides a network into zones by trust, with a firewall between them. Then a problem in one zone cannot reach everything. Three tools do this.

- **A [demilitarised zone](../../glossary.md#demilitarised-zone) (DMZ)** holds the servers the public must reach, such as the website, between two firewalls. The outer firewall lets the public in to the DMZ only. The inner firewall keeps the DMZ out of the inside networks. If a public server is broken into, the inner firewall still stands.
- **Virtual local-area networks (VLANs)** split one set of switches and cables into separate networks. Staff and student traffic can share the wiring, yet never meet without passing a firewall.
- **A [virtual private network](../../glossary.md#virtual-private-network) (VPN)** carries traffic between two places through an encrypted tunnel over the internet. The Internet Protocol Security suite (IPsec), or Transport Layer Security (TLS) from Day 4, does the encrypting. Watchers on the internet see only tunnel traffic between the two ends.

![Taxila's networks. The internet meets the outer firewall. Behind it, the demilitarised zone holds the website and the mail server. The inner firewall separates the demilitarised zone from three inside zones: the staff network, the server room with the Student Information System, and the student Wi-Fi, which reaches the servers only through the inner firewall. The Kandy campus reaches the server room through an encrypted tunnel across the internet.](img/taxila-zones.svg "Two firewalls, a demilitarised zone for public servers, separate inside zones, and a tunnel to Kandy")

Defence in depth ties the layers together. A hardened server, a firewall in front of it, a separate zone, encryption on the wire, and monitoring that notices the unusual are independent layers. Each one covers a failure in another.

> **You already know this.** A hospital has a public reception where anyone may walk in. The wards behind it have locked doors, and a visitor in reception cannot wander into them. A covered, guarded corridor joins the hospital to its second building across the road.
>
> *Mapping:* the public reception = the demilitarised zone; locked ward doors = segmentation; the secure corridor between buildings = the virtual private network.

> **Taxila.** Student wireless is kept apart from staff and servers; Kandy reaches the Student Information System through a private tunnel rather than the open internet (register items 15 and 17).

> **Common mistake.** "A server in the demilitarised zone is inside, so it can be trusted." It is the most exposed server the college has, because the public can reach it. The inner firewall treats it as untrusted, and lets it reach only the one service it needs.

> **Quick check.** Taxila's fee payment page, `pay.taxila.example`, must be reachable by students from home. Where should it sit?
>
> - [ ] In the server room, beside the SIS, so it is well protected
> - [x] In the demilitarised zone, so the public can reach it and the inner firewall still protects the inside
> - [ ] On the student Wi-Fi, because students use it
>
> **Why:** A server the public must reach belongs in the demilitarised zone. Put it beside the SIS and the outer firewall must let the public into the server room. Students at home are not on the Wi-Fi, and the Wi-Fi is the least trusted inside zone.

## Before the lab

This afternoon you list the services a server runs and match them with what the outside sees. You write firewall rules, and learn why their order decides everything. Then you capture address traffic and find the field a false reply would forge. Bring these notes, open at sections 2 and 4. Full-tier students: start your Kali virtual machine before the session.

## Reading

- Pfleeger, C. P., Pfleeger, S. L. and Coles-Kemp, L., *Security in Computing*, 6th ed., chapter 6, on networks. Read sections 6.2 on threats to network communications, and 6.4 and 6.5 on denial of service. Then read 6.6 on cryptography in networks, 6.7 on firewalls and 6.8 on intrusion detection and prevention.
- Computer Crime Act, No. 24 of 2007, Sri Lanka, sections 3 to 5, on access without lawful authority.

Next: Day 9, attacks, people, risk and continuity. You classify the attacks met so far, including today's, and plan how Taxila keeps running when something fails.
