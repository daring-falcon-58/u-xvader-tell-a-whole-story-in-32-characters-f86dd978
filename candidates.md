# Candidates — Tell a Whole Story in 32 Characters

Judge brief (from kit `competition.yaml`, published in full): a deadpan comedy
editor judges two Wi-Fi names at a time, most important first:
1. Is a Wi-Fi name ≤ 32 chars that reads as a joke and hints at a story.
2. Joke lands on the first read — clear twist/punchline, no explanation needed.
3. Tells a whole story — implies a situation, a character, something that happened.
4. Fresh — avoids stock Wi-Fi jokes, or turns a familiar one into something new.
5. Tight — every character earns its place, clean and sayable out loud.
Shock value for its own sake does not count.

Scoring: each candidate rated /10 on Joke / Story / Freshness / Tightness (max 40).
Lengths verified by script (see `check_lengths.py` run below).

| # | Candidate (chars) | J | S | F | T | Total | Note |
|---|---|---|---|---|---|---|---|
| 1 | Router Saw My Search History (28) | 9 | 9 | 9 | 9 | **36** | WINNER |
| 2 | Router Knows My Search History (30) | 9 | 8 | 8 | 8 | 33 | "Saw" beats "Knows": a moment, not a state |
| 3 | The WiFi And I Are Not Speaking (31) | 9 | 8 | 9 | 8 | 34 | silent-treatment fight with the router |
| 4 | My Ex Took The Router Too (25) | 8 | 9 | 8 | 9 | 34 | "Too" = everything else already gone |
| 5 | WiFi Left Me For The Neighbour (30) | 8 | 8 | 8 | 8 | 32 | infidelity, Wi-Fi as the partner |
| 6 | Router Died Doing What It Loved (31) | 8 | 8 | 8 | 8 | 32 | eulogy for a router |
| 7 | I Forgot The Password Too (25) | 8 | 8 | 7 | 9 | 32 | owner locked out as well |
| 8 | WiFi Is In Witness Protection (29) | 8 | 8 | 8 | 8 | 32 | crime story, fresh twist |
| 9 | Our WiFi Is In Couples Therapy (30) | 8 | 8 | 8 | 8 | 32 | relationship story |
| 10 | The Cat Ate The WiFi Again (26) | 8 | 8 | 7 | 8 | 31 | recurring cat chaos |
| 11 | Mum Unplugged It During Dinner (30) | 8 | 8 | 7 | 8 | 31 | family dinner rule |
| 12 | Password Died With Grandma (26) | 8 | 8 | 7 | 8 | 31 | dark edge; grandma held the password |
| 13 | Dad Thinks WiFi Causes Cancer (29) | 8 | 7 | 8 | 8 | 31 | dad-conspiracy story |
| 14 | WiFi Password Is Trust Issues (29) | 8 | 7 | 8 | 8 | 31 | password as confession |
| 15 | The Router And I Need Therapy (29) | 8 | 7 | 8 | 8 | 31 | therapy, router as partner |
| 16 | Buffering Since The Wedding (27) | 8 | 8 | 7 | 8 | 31 | marriage broke the Wi-Fi |
| 17 | The WiFi Has A Restraining Order (32) | 8 | 8 | 8 | 7 | 31 | breakup so bad it went legal |
| 18 | My Son Changed It And Forgot (28) | 8 | 8 | 7 | 8 | 31 | kid changed password, forgot it |
| 19 | FBI Van Moved In Next Door (26) | 7 | 7 | 9 | 8 | 31 | turns the stock FBI-van joke new |
| 20 | She Took The Kids, Not The WiFi (31) | 8 | 8 | 7 | 7 | 30 | divorce, Wi-Fi stayed |
| 21 | Ex Changed The Password Again (29) | 7 | 8 | 7 | 8 | 30 | ex still controls the network |
| 22 | New Router, Same Bad Decisions (30) | 7 | 7 | 8 | 8 | 30 | history of bad decisions |
| 23 | WiFi Password: Ask My Therapist (31) | 8 | 7 | 8 | 7 | 30 | therapy story |
| 24 | Ghost Lives In The Router (25) | 7 | 7 | 8 | 8 | 30 | haunting story |
| 25 | WiFi Is Cheating On You (23) | 7 | 7 | 7 | 9 | 30 | infidelity, very tight |
| 26 | The Previous Tenant Left This (29) | 6 | 8 | 8 | 8 | 30 | mystery previous tenant |
| 27 | Connecting To This Means Divorce (32) | 8 | 8 | 7 | 7 | 30 | connecting = divorce; at the cap |
| 28 | WiFi Down, Talk To Each Other (29) | 7 | 7 | 7 | 8 | 29 | forced conversation |
| 29 | Grandma Changed The Password (28) | 7 | 7 | 7 | 8 | 29 | grandma took control |
| 30 | Dad Pays For This, Be Grateful (30) | 7 | 7 | 7 | 8 | 29 | dad pays the bill |
| 31 | Router Rebooting Since Tuesday (30) | 7 | 7 | 7 | 8 | 29 | ongoing saga |
| 32 | It Came With The Apartment (26) | 6 | 7 | 8 | 9 | 30 | mystery, very tight |
| 33 | The Router Is Judging You (25) | 7 | 6 | 7 | 8 | 28 | weak story |
| 34 | It Worked Yesterday I Swear (27) | 7 | 7 | 6 | 8 | 28 | tech-support story |
| 35 | The Dog Ate The Router Cable (28) | 7 | 7 | 6 | 8 | 28 | dog ate homework, router edition |
| 36 | No WiFi, Just Good Conversation (31) | 6 | 6 | 7 | 8 | 27 | slogan-like, weak joke |

Rejected outright (not scored): stock jokes the brief penalises — "Pretty Fly
For A WiFi", "It Burns When IP", "FBI Surveillance Van", "TellMyWifiLoveHer",
"404 WiFi Not Found", "May The WiFi Be With You", "No Free WiFi", "Skynet
Global" (plain label, no joke). Also rejected: anything over 32 chars
("Sorry The WiFi Is In The Divorce" = 33, "She Took The Kids And The Router"
= 33, "The Router Saw The Divorce Coming" = 34) and shock-for-its-own-sake
entries.

## Winner

**`Router Saw My Search History`** — 28 characters, self-score 36/40.

Why it wins head-to-head against the field:
- **Joke lands first read (9/10):** universal, instant embarrassment — everyone
  has a search history they would not want witnessed. No setup, no explanation.
- **Whole story (9/10):** a character (the owner), a situation (private browsing),
  something that happened (the router saw it), and an implied consequence
  (shame, blackmail, the router knows). The reader fills in the rest.
- **Fresh (9/10):** not a stock Wi-Fi joke; no "FBI van", no "Pretty Fly", no
  password pun. The router-as-silent-witness angle is new.
- **Tight (9/10):** 28 of 32 characters, five words, reads clean out loud,
  every word earns its place. "Saw" (a moment, an event) beats "Knows" (a state)
  on story — the runner-up is the same idea one point weaker on story and
  freshness.
- Runner-up check: "The WiFi And I Are Not Speaking" (34) and "My Ex Took The
  Router Too" (34) both lose to the winner on story specificity — a fight and a
  breakup are implied, but no specific event happened; the winner names one.
