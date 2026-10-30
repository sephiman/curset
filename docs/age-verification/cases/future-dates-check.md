# Future-dates check (R4, supuestos prácticos)

Rule (2026-10-30): no case question may depend on an unpublished calendar (2028 or later). A question depends on one when its key, or a count its explanation gives for an option, needs to know whether a 2028+ day is hábil or festivo.

Method: rule text from `pdftotext -layout` of LCSP (BOE-A-2017-12902), TREBEP (BOE-A-2015-11719), TRLCPE (BOE-A-1987-12636), RD 365/1995 (BOE-A-1995-8730), Resolución 14-04-2026 (BOE-A-2026-8287), LPAC art. 30 and CC art. 5; every date, weekday and amount recomputed in Python (scratch `check.py`).

| Question | Rule's cómputo | Recomputed | Unpublished calendar? | Why (one line) | Counts |
|---|---|---|---|---|---|
| sp-01/q29 | art. 103.5 LCSP: one year from formalización | 2 Aug 2027 + 1 y = Wed 2 Aug 2028 > Wed 9 Feb 2028 (14 Jan + 26 = 9 Feb) | no | Fixed anniversary, compared with a fixed delivery date; no hábil test, no rollover | ok |
| sp-01/q32 | art. 48.f) TREBEP: child under twelve months | born Wed 17 Feb 2027; twelve months on Thu 17 Feb 2028 < Mon 28 Feb 2028 | no | Birthday; no calendar | ok |
| sp-03/q35 | DA 17ª.4 TREBEP: 20 days per year, months prorated, cap 12 mensualidades | 4 Feb 2025–Fri 4 Aug 2028 = 3 y 6 m; 70 d × 80 = 5.600; 4.800 / 6.400 / 8.400 ok; cap 28.800 not reached | no | Cese date is fixed; service length counted in years/months, no hábil test | ok |
| sp-06/q15 | art. 28.2 TRLCPE: 60 years of age and 30 years of service | 60 on Wed 2 Jun 2027; 30 years from Mon 1 Dec 1997 met Wed 1 Dec 2027; 65 on Wed 2 Jun 2032 | no | Birthdays and service anniversaries; all 2027 except a fixed 2032 birthday | ok |
| sp-06/q24 | art. 67.3 TREBEP: forced retirement at 65 | Wed 2 Jun 2032; 67 Fri 2 Jun 2034; 70 Tue 2 Jun 2037 | no | Birthdays; no rollover | ok |
| sp-07/q08 | art. 29.2 LCSP: notice at least two months before the end | end Sun 30 Sep 2029; −2 m Mon 30 Jul 2029; −60 d Wed 1 Aug; −1 m Thu 30 Aug; −3 m Sat 30 Jun 2029 | no | Counted backwards date to date from a fixed end; no rollover applied to the key or to any option | ok |
| sp-09/q11 | art. 193.3 LCSP: 0,60 € per 1.000 € per day (natural days) | 1–14 Dec 2028 = 14 natural days; 26.040 / 31.508,40 / 24.180 ok; 8 hábiles ok only if 6 and 8 Dec 2028 are festivos | **yes** | Option b and its explanation count «ocho días hábiles» in Dec 2028, removing the 6 and 8 Dec 2028 festivos from an unpublished calendar | arithmetic ok |
| sp-10/q16 | art. 98.3 TREBEP: six months max; month-end rule | Mon 30 Aug 2027 + 6 m = Tue 29 Feb 2028 (both counting readings); +180 d = Sat 26 Feb 2028 | no | End of a fixed duration of a measure; the explanation cites art. 30.4 LPAC only for the month-end rule and applies no rollover (citing LPAC invites 30.5; safer to cite art. 5 CC) | ok |
| sp-11/q12 | apartado 9.7 Res. 14-04-2026: from the day after the sixth trienio | Thu 17 Jun 2027; distractor Fri 16 Jun 2028 is a fixed date | no | 2027 key; the 2028 distractor is a plain anniversary | ok |
| sp-14/q10 | art. 193.3 LCSP: per natural day of delay | Sat 25 Dec 2027–Mon 3 Jan 2028 = 10 natural days; 864 / 936 / 1.045,44 / 8.640 ok | no | Natural days, no hábil test, no rollover | ok |
| sp-14/q11 | art. 16.3 RD 365/1995: each period at least two years | Mon 1 Sep 2025 → ends Tue 31 Aug 2027, return Wed 1 Sep 2027; 1 Sep 2026 Tue, 1 Sep 2036 Mon | no | All 2027 or fixed anniversaries | ok |
| sp-14/q15 | art. 97 TREBEP: very serious faults prescribe in three years from cese | Mon 18 Oct 2027 + 3 y = Fri 18 Oct 2030; 6 m Tue 18 Apr 2028; 2 y Thu 18 Oct 2029; 6 y Tue 18 Oct 2033 (RD 33/1986 art. 20.1: six years, confirmed) | no | Prescription dates, fixed; no rollover | ok |
| sp-17/q10 | art. 10.1.d) TREBEP: nine months max | Mon 12 Apr 2027 + 9 m = Wed 12 Jan 2028 (date to date) / Tue 11 Jan 2028 (start day counted) | no | End of a fixed duration; no rollover | **disputed**: the explanation calls 11 Jan «cuenta el día del nombramiento como primero», but a nombramiento lasting nine months from 12 Apr inclusive ends on 11 Jan, and sp-14/q11 counts exactly that way (two years from 1 Sep 2025 end 31 Aug 2027); options a and b are both defensible |
| sp-18/q22 | art. 67.3 TREBEP: prolongation up to age 70 | born Mon 9 Apr 1962; 70 Fri 9 Apr 2032; 65 Fri 9 Apr 2027; 67 Mon 9 Apr 2029; Fri 31 Dec 2032 | no | Birthdays; no calendar | ok |
| sp-19/q22 | art. 29.4 LCSP: five years including prórrogas | initial Mon 1 Mar 2027–Wed 28 Feb 2029; prórrogas start Thu 1 Mar 2029, Fri 1 Mar 2030, Sat 1 Mar 2031 (last); Mon 1 Mar 2032 is past five years | no | Starting dates of prórrogas, fixed; no rollover | ok |

Drops appended: sp-09/q11 (unpublished calendar), sp-17/q10 (disputed count).
