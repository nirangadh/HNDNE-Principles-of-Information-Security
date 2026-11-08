# Lab 8: Inventory your services, write a firewall rule, read address traffic

**Day 8, afternoon session. Duration 3 hours. Adds item 15 to Taxila's security register.**

This lab sheet takes you through three jobs a network defender does. First you list the services a server runs and match them with what the outside can see, and name the most dangerous door. Then you write firewall rules that close that door and still let your own replies back in, and you find out why their order decides everything. Last, you capture and read the Address Resolution Protocol (ARP) traffic that machines use to find each other.

| | |
|---|---|
| Learning outcomes | LO4, LO5 |
| You need | this morning's ideas: a port is open, closed or filtered; a [stateful firewall](../../glossary.md#stateful-firewall) tracks connections; address replies are trusted without a check |
| Tiers | Floor tier: every step, in the browser and with the provided files. Full tier: recommended for segments 1 to 3, on your Kali virtual machine |
| Evidence pack | none today; the five evidence packs ended with the pack after Day 6 |

## Before you start

1. Open this page and the day's notes side by side. Keep the notes open at sections 2 and 4.
2. Download the provided files and save them in your module folder: [`sis-services.txt`](files/sis-services.txt), [`sis-outside-view.txt`](files/sis-outside-view.txt), [`firewall-rules.txt`](files/firewall-rules.txt) and [`address-traffic.pcapng`](files/address-traffic.pcapng).
3. Floor tier: open the `service-doors` and `arp-trust` demos. You use them in segments 1 and 3.
4. Full tier: start your Kali virtual machine and take a snapshot named `day-8-start`, so Reset can bring it back. Take it before you run anything else today.
5. Full tier: check that the firewall tool is there. Run `sudo iptables -V`. *Expected:* a version number followed by `(nf_tables)`. If it says the command is not found, install it with `sudo apt install iptables`.

### The idea behind today's lab

> **Recall.** A port is open, closed or filtered, and every open port is a door to guard.

> **Recall.** A stateful firewall tracks connections; address replies are trusted blindly.

A defender cannot guard a door they do not know about. So the afternoon starts with a list of every door: from the server itself, and from outside. Then you close one, with a firewall rule. A firewall reads its rules from the top, and the first rule that matches a packet decides what happens to it. Last, you read the traffic a false address reply would imitate, so you would know it if you saw it.

> **Common mistake.** "The order of firewall rules does not matter." Rules are read top to bottom, and the first match wins. A rule that drops everything, placed above the rule that lets your replies in, drops your replies too. The rules below it never get a turn.

> **Common mistake.** "A filtered port is the same as a closed one." A closed port means the machine answered that nothing listens there. A filtered port means no answer came back at all, because something in the path dropped the request. A service may still be running behind a filtered port.

> **Quick check.** The outside view of `sis.taxila.example` says `3306/tcp open`, and the server's own list shows `mariadbd` listening on `0.0.0.0:3306`. The portal that uses the database runs on the same server. What is the best fix?
>
> - [x] Make the database listen only on the server itself, and drop port `3306` at the firewall, because only the portal on this machine needs it
> - [ ] Leave it open, because the database has its own passwords
> - [ ] Stop the database service, because nothing should listen on `3306`
>
> **Why:** The portal reaches the database on the same machine, so no other machine needs port `3306`. Passwords are one layer, but a database open to thousands of unmanaged devices is the door an attacker tries first. Stopping the database would stop the Student Information System (SIS) itself.

> **Quick check.** You add a firewall rule that answers "refused" instead of saying nothing. What will an outside view now report for that port?
>
> - [ ] Open, because the firewall answered
> - [ ] Filtered, because a firewall is involved
> - [x] Closed, because an answer came back saying nothing listens there
>
> **Why:** The outside view reports only what came back. A rule that refuses sends an answer, so the port looks closed. A rule that drops in silence sends nothing, so the port looks filtered. Both stop the connection; they differ only in what a watcher learns.

## Objective

You will show which services a server exposes, which one is the highest risk, and how to close it. You will show a firewall that blocks that door while your own replies still return, and explain why a rule in the wrong place breaks it. That is how Taxila starts register item 15.

## Timed segments

| Segment | Minutes | Tier |
|---|---|---|
| Inventory your own server's services | 45 | both |
| Write a firewall rule | 40 | both |
| Capture and read address traffic | 40 | both |
| Prove it, break it, reset and write up | 25 | both |

## Steps

Each step states what to do and what you should see. If you do not see it, stop and work out why before moving on.

*Segment 1: Inventory your own server's services*

1. **Read the server's own list.** Open `sis-services.txt`. It shows what the SIS server, `sis.taxila.example`, runs and listens on, printed on the server itself. *Expected:* seven listening lines. `sshd` on port `22`, `mariadbd` on `3306`, `python3` on `8080` and `apache2` on `80` and `443` listen on every address. `systemd-resolve` listens on `53`, but only on `127.0.0.53`, the server itself. The service list names eight running services, and `python3` is not among them, because it was started by hand.

2. **Match each port with the outside view.** Open `sis-outside-view.txt`, which shows what came back from each port when it was checked from the student Wi-Fi. Write a table with one row per port: the state outside, the service inside, and what Taxila should do. *Expected:* `22` open, remote login, which should be reachable from the staff network only. `25` closed: nothing listens. `80` and `443` open: the portal, which students need. `3306` open: the database, reachable from the Wi-Fi, which is the highest risk. `8080` filtered: the forgotten test copy, hidden by the firewall but still running, so stop it. Port `53` is not in the outside view at all, because it listens only on the server itself.

> **Floor path.** Use the `service-doors` demo for steps 1 and 2. It shows the same two files side by side. Choose each door to see its line in the server's own list.

3. **List the services on your own virtual machine.** Full tier. First list what listens now, then start Kali's web server, which is installed but switched off, and list again. *Expected:* before the start, almost nothing listens, because Kali starts no network services by default. After it, `sudo ss -tulpn` shows `apache2` listening on port `80` on every address. The running list shows many services, most of which listen on no port at all. Open `http://127.0.0.1/` in Firefox: you see Apache's default page.

```bash
sudo ss -tulpn
sudo systemctl start apache2
sudo ss -tulpn
systemctl list-units --type=service --state=running
```

Your machine stands in for a small server today, and `apache2` is its unneeded plain-web door. Running and listening are different questions: a service can run for hours without opening any door.

> **Floor path.** The floor tier has no virtual machine of its own. Your inventory is steps 1 and 2. Write one more line under your table: which of the SIS server's doors are needed by students, which only by staff, and which by nobody.

*Segment 2: Write a firewall rule*

4. **Write four rules.** Full tier. Add the rules in this order, then list them. *Expected:* the listing shows four numbered rules. The first rejects port 80, the second accepts the loopback interface, `lo`, the third accepts connections that are already established, and the fourth drops everything else.

```bash
sudo iptables -A INPUT -p tcp --dport 80 -j REJECT
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -j DROP
sudo iptables -L INPUT -n -v --line-numbers
```

Rule 1 closes the risky door. Rule 2 lets the machine talk to itself. Rule 3 is the stateful rule: it lets in replies to connections your machine started. Rule 4 drops everything else that arrives. Your test comes from the machine itself, so rule 1 must sit above rule 2, or rule 2 would let it through first.

5. **Test both directions.** Full tier. Reload `http://127.0.0.1/` in Firefox, then open an outside site you use for study, such as the CyberChef site. List the rules again. *Expected:* the local page fails with **Unable to connect**, because rule 1 refused it. The outside site still loads, because its replies match rule 3. In the listing, the `pkts` counter of rule 1 has gone up, and rule 3's counter climbs each time you load a page.

> **Floor path.** Open `firewall-rules.txt` and work through Part A, the first draft by the Head of IT (information technology), answering its four questions. Then write, on paper, rules for the SIS server that drop port `3306` from other machines, let replies in, allow the portal, and drop everything else. Compare yours with Part B. *Expected:* in Part A, rule 2 drops everything, so rules 3 to 6 never match: students cannot reach the portal and the server's own replies are lost. Your rules should match Part B's order, though not necessarily its wording.

*Segment 3: Capture and read address traffic*

6. **Capture an address question and its answer.** Full tier. Open Wireshark, choose your network interface, usually **eth0**, start the capture and type `arp` in the display filter. Then empty your machine's address cache, so it must ask again, and reload the outside site. *Expected:* two frames. A request, `Who has 10.0.2.2? Tell 10.0.2.15`, sent to `Broadcast`. A reply, `10.0.2.2 is at` followed by the gateway's hardware address. These are the addresses of VirtualBox's usual network; yours may differ. `ip neigh` then shows the same hardware address for the gateway.

```bash
sudo ip neigh flush dev eth0
ip neigh
```

Click the reply and open **Address Resolution Protocol (reply)**. Wireshark calls a hardware address a media access control (MAC) address. The field a poisoning attack would forge is `Sender MAC address`.

7. **Read a prepared capture of a false reply.** Both tiers. Open `address-traffic.pcapng`. It was prepared for teaching on Taxila's staff network: the false replies were written into the file and never sent on any network. Compare frame 2 with frame 6, then read frames 7 and 8. Both say who owns the Internet Protocol (IP) address `10.10.0.1`. *Expected:* frame 2 says `10.10.0.1 is at 02:00:0a:0a:00:01`, the gateway, in answer to frame 1. Frame 6 says `10.10.0.1 is at 02:00:0a:0a:00:42`, which nobody asked for. Wireshark marks it **Duplicate IP address configured (10.10.0.1)**, also listed under **Analyze**, then **Expert Information**. Frame 7 shows the laptop's next request going to `02:00:0a:0a:00:42`, and frame 8 shows that machine passing it on to the gateway.

> **Floor path.** Open the `arp-trust` demo for steps 6 and 7. It steps through the same capture and shows the laptop's address cache after each frame. If Wireshark is on your own laptop, you may open the file there too. Only open captures you were given: never capture on a network you do not own.

*Segment 4: Prove it, break it, reset and write up*

8. **Write up the register item.** In your notes, write one line for item 15 in Taxila's words. *Expected:* the SIS server's database port is no longer open to the student Wi-Fi. Remote login is allowed from the staff network only, and the test copy on `8080` is stopped. The zone firewall drops everything it does not need. Add one line each for items 16 and 17 as you saw them this morning.

## Prove it

Your inventory lists the listening services and names the highest risk, port `3306` on the SIS server, with its mitigation. On the full tier, your firewall refuses `http://127.0.0.1/` while an outside site still loads, and the `pkts` counters show which rule did each job. On the floor tier, your written rules for the SIS server match Part B's order. You can also say which rule handles a student's portal request, and which handles the server's own replies.

## Break it

**Fault:** a drop-everything rule above the rule that lets your replies in.

1. Full tier, insert a second drop-everything rule at position 3, above the stateful rule.

```bash
sudo iptables -I INPUT 3 -j DROP
```

2. **Symptom:** reload the outside site. It no longer loads. Firefox waits, then says it cannot find or reach the site, because even the answer to its name lookup is dropped.
3. **Evidence:** list the rules with their counters. The new rule 3, `DROP`, has a `pkts` counter that climbs on every reload. Rule 4, the stateful rule, has stopped counting: no packet reaches it any more.

```bash
sudo iptables -L INPUT -n -v --line-numbers
```

4. **Fix:** delete rule 3, reload the site, and check the list is back to four rules.

```bash
sudo iptables -D INPUT 3
sudo iptables -L INPUT -n -v --line-numbers
```

> **Floor path.** Part A of `firewall-rules.txt` is this same fault. Write which packet each of its rules would catch first, then explain in two sentences why moving rule 2 to the bottom fixes it.

## Reset

1. Keep your inventory table and your notes from steps 2, 7 and 8 first.
2. Floor tier: keep your worksheet. Reload the demos to clear them.
3. Full tier: restore the `day-8-start` snapshot. This removes your rules and stops the web server. If you did not take a snapshot, run these:

```bash
sudo iptables -F INPUT
sudo systemctl stop apache2
sudo iptables -L INPUT -n -v --line-numbers
```

The list should show no rules. The rules you typed were never saved, so a restart would also remove them.

## Rules of engagement

No tool in this lab can affect anyone else's system. You list, filter and capture only on your own virtual machine, or read the provided files. Address poisoning is studied from a provided capture only and is never performed. Never check the ports of a machine you do not own, and never capture on a network that is not yours.

## Evidence required

There is no evidence pack today. Keep these, because your group uses them in its controls map:

1. **Your inventory worksheet.** The table from step 2, with the highest risk and its mitigation.
2. **Your firewall rules.** The four rules from step 4, or your written rules for the SIS server, and your line on why order matters.
3. **Your address notes.** The request and reply from step 6 or 7, and the field a false reply forges.

## Taxila connection

Item 15 on Taxila's register is firewalls and network zones. Today you found the SIS database answering the student Wi-Fi, and a forgotten test service hidden only by the firewall. You wrote rules that close the database door and still let the server's own replies in. The Head of IT asked what can be seen and what can be reached. Your inventory answers the first question, and your rules answer the second.
