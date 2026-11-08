# Practice question 8: a courier company's tracking site

This practice question applies the Day 8 ideas to a courier company. It covers what a shared network shows, address poisoning, the three kinds of firewall, a demilitarised zone, and where a private tunnel helps. Attempt it in writing before you read the answer guidance. It carries 20 marks.

## The setting

A courier company delivers parcels across the Western Province. Customers type a tracking number into the company's public website to see where their parcel is. Forty drivers carry company phones. At each delivery, the driver's phone sends the parcel's status and a photo to the company over mobile data.

All the company's servers sit in one room at the main depot: the tracking website, the delivery database behind it, and the payroll computer. The depot also has one Wi-Fi network. Office staff use it, and so do visiting drivers from partner companies, who join it to send their own paperwork. The office computers, the servers and the Wi-Fi are all on the same network. One router joins it to the internet, and it lets in only connections to the website's secure web port.

Last month the company's IT (information technology) contractor reviewed the network. Two findings worried them most:

| Finding | What the contractor saw |
|---|---|
| A capture on the depot Wi-Fi | the office computers' address caches showed the router's address with two different hardware addresses during one afternoon |
| The payroll computer | its file-sharing port answered from every device on the Wi-Fi |

The contractor proposes four changes:

1. Split the network into zones: one for the servers, one for office computers, and a separate one for visitors' Wi-Fi.
2. Put the tracking website in a demilitarised zone, between two firewalls, with the database behind the inner one.
3. Replace the router's simple filter with a stateful firewall, and add an intrusion detection system that watches the servers' zone.
4. Give every driver's phone a virtual private network (VPN) back to the depot.

The operations manager agrees with the first two changes but not the last two. "Our website already uses secure web, so nobody can read our traffic. A VPN for the drivers is a waste of money. And instead of a new firewall and an intrusion system, let us buy one web application firewall: it reads everything, so it will stop everything."

## The question

**(a)** Explain what someone sniffing a shared network can learn from unencrypted traffic, and what they can still learn from encrypted traffic. Then explain how address poisoning puts a machine in the middle, and what the first finding suggests. **(6 marks)**

**(b)** Apply these ideas to the company. Describe the zones and firewalls you would set up, and say where each server and each kind of device goes. Say which traffic each firewall should allow between the zones. Then say where the intrusion detection system should watch, and what it could notice that a firewall would not. **(7 marks)**

**(c)** Evaluate the operations manager's view. Discuss whether secure web on the website makes the drivers' VPN unnecessary, and whether one web application firewall could replace a stateful firewall and an intrusion system. Recommend what the company should do, with one cost of your recommendation. **(7 marks)**

## Answer guidance

Read this only after you have written your own answer.

**Part (a).** On a shared segment every machine can receive what the others send. Sniffing is passive: it reads that traffic and leaves no trace. From unencrypted traffic a watcher reads everything: passwords typed into plain web forms, session cookies, the content of messages and files. Encryption hides the content but not the outside of each packet. The watcher still sees which machines talk, on which ports, when, how often and how much: that is traffic analysis. Address poisoning uses the Address Resolution Protocol (ARP), which maps an Internet Protocol (IP) address to a hardware address. A machine asks the whole segment who has an address, and believes any reply. A false reply that claims the router's address makes the victims send their traffic to the wrong machine. That machine can read it and pass it on, so it sits in the middle. Two hardware addresses for the router's address, in one afternoon, is the pattern of poisoning. The company should find which device on the Wi-Fi owned the second hardware address. A strong answer says that poisoning needs a machine on the same segment, which is why the open Wi-Fi matters.

**Part (b).** Visitors' Wi-Fi gets its own zone, which reaches only the internet and nothing inside. Office computers get a staff zone. The servers sit behind an inner firewall: the delivery database and the payroll computer. The tracking website sits in a demilitarised zone between the outer firewall and the inner one. The outer firewall lets the public reach only the website's secure web port. The inner firewall lets the website reach only the database's port, and lets office computers reach only the services they need. Nothing from the visitors' zone reaches the servers, so the payroll file-sharing port is no longer open to them. The drivers' phones reach the depot through the VPN, which ends at the outer firewall, and they reach only the service that takes delivery records. The intrusion detection system watches traffic into the servers' zone, out of the path. It can notice what a firewall lets through but should not happen. Examples are a signature it knows, such as an injection string in a request, or an anomaly, such as a sudden flood or a database read far larger than normal. It can also flag two hardware addresses for one IP address. A firewall only allows or drops; it does not tell anyone what it saw.

**Part (c).** Secure web protects the content of the website's traffic, so the manager is partly right. But the drivers' phones send more than web pages. Each status update and photo travels over mobile data and public networks. A VPN gives every connection from the phone one encrypted tunnel to the depot, so the company's servers need not face the internet for the drivers at all. It also hides which depot services each phone uses. If the phones' delivery app already uses secure connections for everything, a VPN adds less, so the answer depends on checking that first. On the firewall, the manager is wrong. A web application firewall reads web requests, and only those it can decrypt. It does not replace the stateful firewall that drops packets claiming to belong to connections nobody opened, as in a denial of service flood. It does not separate the zones, and it does not watch other protocols, such as the file-sharing port. Nor does it replace monitoring, which notices what is allowed but unusual. These are independent layers, and defence in depth needs them all. A reasonable recommendation: zones and the demilitarised zone first, because they close the payroll door and contain the open Wi-Fi. Then the stateful firewall, then the intrusion detection system. Then the VPN, if the drivers' app does not already encrypt everything. A web application firewall is worth adding later in front of the website, as one more layer, not instead of the others. One cost: the intrusion system's alerts need someone to read them, which takes staff time every week. A strong answer weighs that cost against the payroll data now exposed to every visitor's device.
