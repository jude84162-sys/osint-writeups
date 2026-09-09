# TryHackMe Progress Tracker

Professional documentation of TryHackMe rooms completed by **Jude** ([@jude84162-sys](https://github.com/jude84162-sys)).

> All rooms were completed through the official TryHackMe platform in dedicated training environments. No live, unauthorized, or third-party systems were accessed. See the [Legal Disclaimer](#legal-disclaimer) at the bottom.

---

## Progress Summary

| # | Room Name | Category | Difficulty | Completion Date | Key Skills Learned |
|---|-----------|----------|------------|-----------------|--------------------|
| 1 | OhSINT | OSINT | Easy | September 9, 2026 | Wi-Fi BSSID research, image metadata (EXIF) analysis, social-media pivoting from a single image |
| 2 | Searchlight — IMINT | OSINT / IMINT | Easy | September 9, 2026 | Imagery & geospatial intelligence, reverse image search, landmark/terrain identification, coordinate verification |
| 3 | Sakura Room | OSINT | Easy | September 9, 2026 | Multi-source OSINT pivot chains, geolocation, social-media investigation, Sockpuppet methodology |
| 4 | Typo Snare | Threat Hunting | Medium | September 9, 2026 | Threat hunting with Splunk, Atomic Red Team emulation, mapping ATT&CK techniques to detections |
| 5 | Bypass Disable Functions | Web Exploitation | Info | September 9, 2026 | PHP `disable_functions` bypasses, LD_PRELOAD and CGI-based abuse, PHP-FPM/FastCGI exploitation |
| 6 | Nightmare (Cypheron) | AI Security / Red Team | Insane | September 9, 2026 | AI/LLM attack surface analysis, AI agent & workflow-engine exploitation (n8n), CVE research and chaining |

**Totals:** 6 rooms · 1× Info · 3× Easy · 1× Medium · 1× Insane

---

## Room Details

### 1. OhSINT — OSINT Challenge
- **Room:** https://tryhackme.com/room/ohsint
- **What the room teaches:** How a single publicly posted image can unravel an entire online identity — connecting a person to their social accounts, interests, and even their home Wi-Fi access point, without ever touching the target directly.
- **Tools and techniques used:** ExifTool (EXIF metadata extraction), WiGLE (BSSID geolocation), Google, and social-media pivoting (Twitter/X and GitHub reconnaissance).
- **Key takeaway:** Metadata is a silent liability — a photo published online can carry enough embedded information to identify a person, their location, and their devices.

### 2. Searchlight — IMINT
- **Room:** https://tryhackme.com/room/searchlightosint
- **What the room teaches:** The discipline of Image Intelligence (IMINT) and Geospatial Intelligence (GEOINT): locating where a photo was taken using only visual clues such as architecture, signage, terrain, and vegetation.
- **Tools and techniques used:** Google Lens and Yandex reverse image search, Google Earth and Google Maps (Street View, satellite imagery), OpenStreetMap, and systematic cross-verification of coordinates.
- **Key takeaway:** Geolocation is about triangulating many small visual clues — no single detail gives away a location, but combined they pinpoint it precisely.

### 3. Sakura Room — OSINT
- **Room:** https://tryhackme.com/room/sakura
- **What the room teaches:** A full investigative OSINT storyline (created by the OSINT Dojo) that chains together multiple techniques: profiling a target, pivoting between platforms, geolocating images, and uncovering hidden accounts.
- **Tools and techniques used:** Reverse image search, Tor Browser (onion-site research), ExifTool, hashtag/username pivoting across social platforms, Wayback Machine, and search-engine operators.
- **Key takeaway:** Real investigations are pivot chains — each artifact (username, hashtag, image) is a lead that feeds the next step, so disciplined note-taking matters as much as tooling.

### 4. Typo Snare — Threat Hunting Simulator
- **Room:** https://tryhackme.com/room/typosnare
- **What the room teaches:** A blue-team threat hunting scenario: hunting a real intrusion in endpoint telemetry by emulating attacker behaviour with Atomic Red Team and then detecting it with Splunk against a SIEM dataset.
- **Tools and techniques used:** Splunk (SPL query writing), Atomic Red Team (ATT&CK technique emulation), MITRE ATT&CK mapping, Windows Event Log analysis, and IOC-based hunting.
- **Key takeaway:** Effective threat hunting is hypothesis-driven: emulate a known technique, learn what telemetry it produces, and build detections around the gaps.

### 5. Bypass Disable Functions — Web Exploitation
- **Room:** https://tryhackme.com/room/bypassdisablefunctions
- **What the room teaches:** Why hardening measures like PHP's `disable_functions` directive fail in practice, and how misconfigured PHP environments (CGI, PHP-FPM, LD_PRELOAD tricks, and PHP extensions) can be abused to execute system commands anyway.
- **Tools and techniques used:** PHP `phpinfo()` reconnaissance, `disable_functions` auditing, LD_PRELOAD hijacking via `mail()`/`putenv()`, FastCGI (PHP-FPM) direct exploitation, and exploitation of vulnerable PHP extensions (e.g., ImageMagick/Ghostscript-based vectors).
- **Key takeaway:** Defense in depth matters — hardening that relies on a single configuration directive is a speed bump, not a wall, when the interpreter itself is exposed.

### 6. Nightmare (Cypheron) — AI Security / Red Team
- **Room:** https://tryhackme.com/room/cypheron
- **What the room teaches:** Part of TryHackMe's "2026: An AI Odyssey" CTF; this Insane-difficulty challenge targets AI infrastructure — probing LLM-backed agents and workflow orchestration platforms for exploitable weaknesses and chaining them into full compromise.
- **Tools and techniques used:** AI agent recon (n8n workflow-engine enumeration), CVE research and exploitation of AI/orchestration components, prompt-injection analysis, web request manipulation, and multi-stage attack chaining.
- **Key takeaway:** AI systems inherit the weaknesses of the software beneath them — securing an AI deployment means securing the agents, integrations, and orchestrators it runs on, not just the model.

---

## Achievements

**Date of completion:** September 9, 2026

- 🏅 **6 rooms completed in a single day**, spanning four distinct domains: OSINT/IMINT, Threat Hunting (Blue Team), Web Exploitation (Offensive), and AI Security/Red Team.
- 🏅 **Insane-difficulty clearance:** Finished **Nightmare (Cypheron)** (120 pts, AI Sec + Red Team) — one of TryHackMe's highest-difficulty CTF challenges.
- 🏅 **Full-spectrum coverage:** Demonstrated skills on both offensive (web exploitation, AI red teaming) and defensive (SIEM-based threat hunting) sides of security.
- 🏅 **OSINT specialization advanced:** Completed three dedicated OSINT/IMINT rooms (OhSINT, Searchlight, Sakura), reinforcing open-source investigation methodology.
- 🏅 **Consistent documentation:** All progress recorded professionally in this repository for verifiable, long-term skill tracking.

---

## Legal Disclaimer

> **Disclaimer:** All content documented in this file relates to activities performed exclusively within TryHackMe's authorized training environments. These are purpose-built, legally sanctioned platforms for cybersecurity education. All techniques described were practiced against lab machines owned and operated by TryHackMe — **no unauthorized systems were accessed, and no real individuals or organizations were targeted.**
>
> Any tools, techniques, or knowledge referenced here are documented strictly for **educational purposes**. They must not be applied to systems, networks, or individuals without **explicit, prior written authorization**. Unauthorized access to computer systems is illegal under laws such as the **Computer Misuse Act 1990 (UK)**, the **Computer Fraud and Abuse Act (US)**, and equivalent legislation in other jurisdictions.
>
> The author assumes no liability for misuse of this material. Practice safely, ethically, and legally.

---

*Last updated: September 9, 2026*
