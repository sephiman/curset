# Error budget in minutes (`error-budget-minutes`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 159873681226414319, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.75% over 30 days allows how many minutes of full outage?

a) about 0.075 minutes
b) about 108 minutes
c) 1.8 minutes
d) 10,800 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.75%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.75% = 0.25%. Step 3: 43200 x 0.25% = 108 minutes. Result: 108 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 2. seed 3282400390636635636, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 90 days allows how many minutes of full outage?

a) 648 minutes
b) approximately 64,800 minutes
c) 216 minutes
d) 0.45 minutes

**Key: a**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 129600 x 0.5% = 648 minutes. Result: 648 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 3. seed 2657330678423097558, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 30 days allows how many minutes of full outage?

a) approximately 432 minutes
b) 7.2 minutes
c) about 0.3 minutes
d) approximately 25,920 minutes

**Key: a**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 43200 x 1% = 432 minutes. Result: 432 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 4. seed 48110080289914026, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) about 51,840 minutes
b) about 864 minutes
c) 86,400 minutes
d) about 14.4 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 5. seed 3419769241164669551, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) about 51,840 minutes
b) approximately 864 minutes
c) about 14.4 minutes
d) 86,400 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 6. seed 4499359114295700343, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) 14.4 minutes
b) approximately 51,840 minutes
c) about 864 minutes
d) 0.6 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 7. seed 3494547388270906577, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) approximately 51,840 minutes
b) approximately 86,400 minutes
c) approximately 0.6 minutes
d) 864 minutes

**Key: d**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 8. seed 141461741150704662, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 90 days allows how many minutes of full outage?

a) 216 minutes
b) approximately 648 minutes
c) 64,800 minutes
d) about 10.8 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 129600 x 0.5% = 648 minutes. Result: 648 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 9. seed 632255767424417637, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) approximately 864 minutes
b) 14.4 minutes
c) approximately 51,840 minutes
d) 0.6 minutes

**Key: a**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 10. seed 2375895717637344050, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 90 days allows how many minutes of full outage?

a) 64,800 minutes
b) 10.8 minutes
c) 648 minutes
d) 38,880 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 129600 x 0.5% = 648 minutes. Result: 648 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 11. seed 2761169790224687322, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.75% over 30 days allows how many minutes of full outage?

a) about 0.075 minutes
b) approximately 10,800 minutes
c) about 108 minutes
d) about 6,480 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.75%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.75% = 0.25%. Step 3: 43200 x 0.25% = 108 minutes. Result: 108 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 12. seed 1272366818358869578, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 90 days allows how many minutes of full outage?

a) about 0.9 minutes
b) approximately 21.6 minutes
c) approximately 1,296 minutes
d) 129,600 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 129600 x 1% = 1,296 minutes. Result: 1,296 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 13. seed 1478020586136311311, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 90 days allows how many minutes of full outage?

a) about 432 minutes
b) 1,296 minutes
c) approximately 21.6 minutes
d) 0.9 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 129600 x 1% = 1,296 minutes. Result: 1,296 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 14. seed 4324659023847719921, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 30 days allows how many minutes of full outage?

a) approximately 0.15 minutes
b) approximately 3.6 minutes
c) about 216 minutes
d) about 21,600 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 43200 x 0.5% = 216 minutes. Result: 216 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 15. seed 3602815215178677315, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 60 days allows how many minutes of full outage?

a) approximately 864 minutes
b) approximately 0.6 minutes
c) about 432 minutes
d) 86,400 minutes

**Key: a**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 60 days. Step 1: the window is 60 x 1440 = 86400 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 86400 x 1% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 16. seed 3202289065909371464, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) about 86,400 minutes
b) 51,840 minutes
c) about 864 minutes
d) 0.6 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 17. seed 3053190858185240824, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 30 days allows how many minutes of full outage?

a) about 3.6 minutes
b) 12,960 minutes
c) about 216 minutes
d) about 0.15 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 43200 x 0.5% = 216 minutes. Result: 216 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 18. seed 2439273825666428878, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.75% over 30 days allows how many minutes of full outage?

a) about 0.075 minutes
b) about 108 minutes
c) 6,480 minutes
d) 1.8 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.75%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.75% = 0.25%. Step 3: 43200 x 0.25% = 108 minutes. Result: 108 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 19. seed 1578104721227294233, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 90 days allows how many minutes of full outage?

a) 21.6 minutes
b) approximately 77,760 minutes
c) about 129,600 minutes
d) 1,296 minutes

**Key: d**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 129600 x 1% = 1,296 minutes. Result: 1,296 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 20. seed 1216287967675383538, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 30 days allows how many minutes of full outage?

a) approximately 12,960 minutes
b) 21,600 minutes
c) approximately 216 minutes
d) approximately 0.15 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 43200 x 0.5% = 216 minutes. Result: 216 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 21. seed 1923042989676195595, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.75% over 30 days allows how many minutes of full outage?

a) 0.075 minutes
b) approximately 108 minutes
c) approximately 6,480 minutes
d) about 10,800 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.75%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.75% = 0.25%. Step 3: 43200 x 0.25% = 108 minutes. Result: 108 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 22. seed 2687675536150232099, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 60 days allows how many minutes of full outage?

a) 216 minutes
b) about 432 minutes
c) about 7.2 minutes
d) about 0.3 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 60 days. Step 1: the window is 60 x 1440 = 86400 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 86400 x 0.5% = 432 minutes. Result: 432 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 23. seed 413431189432590527, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 90 days allows how many minutes of full outage?

a) about 648 minutes
b) about 216 minutes
c) 64,800 minutes
d) about 0.45 minutes

**Key: a**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 129600 x 0.5% = 648 minutes. Result: 648 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 24. seed 2206881291886697584, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 30 days allows how many minutes of full outage?

a) 0.3 minutes
b) about 432 minutes
c) about 7.2 minutes
d) 25,920 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 43200 x 1% = 432 minutes. Result: 432 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 25. seed 2037579320421699445, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 60 days allows how many minutes of full outage?

a) approximately 216 minutes
b) about 7.2 minutes
c) approximately 0.3 minutes
d) about 432 minutes

**Key: d**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 60 days. Step 1: the window is 60 x 1440 = 86400 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 86400 x 0.5% = 432 minutes. Result: 432 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 26. seed 618677665184766180, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.75% over 30 days allows how many minutes of full outage?

a) about 1.8 minutes
b) about 108 minutes
c) 10,800 minutes
d) 6,480 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.75%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.75% = 0.25%. Step 3: 43200 x 0.25% = 108 minutes. Result: 108 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 27. seed 939475701487247721, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 30 days allows how many minutes of full outage?

a) 3.6 minutes
b) 216 minutes
c) 0.15 minutes
d) about 21,600 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 43200 x 0.5% = 216 minutes. Result: 216 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 28. seed 2066347450081295297, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 90 days allows how many minutes of full outage?

a) approximately 38,880 minutes
b) about 0.45 minutes
c) approximately 648 minutes
d) 10.8 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 129600 x 0.5% = 648 minutes. Result: 648 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 29. seed 358138070733962336, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.75% over 30 days allows how many minutes of full outage?

a) approximately 10,800 minutes
b) approximately 108 minutes
c) about 6,480 minutes
d) 0.075 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.75%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.75% = 0.25%. Step 3: 43200 x 0.25% = 108 minutes. Result: 108 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 30. seed 2056037755740088193, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 30 days allows how many minutes of full outage?

a) approximately 216 minutes
b) 21,600 minutes
c) approximately 3.6 minutes
d) about 0.15 minutes

**Key: a**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 43200 x 0.5% = 216 minutes. Result: 216 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 31. seed 2711930178437957477, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 30 days allows how many minutes of full outage?

a) 43,200 minutes
b) about 432 minutes
c) about 7.2 minutes
d) 25,920 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 43200 x 1% = 432 minutes. Result: 432 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 32. seed 3716323214059927440, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) approximately 86,400 minutes
b) about 51,840 minutes
c) 864 minutes
d) approximately 14.4 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 33. seed 4188317010928694299, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 30 days allows how many minutes of full outage?

a) 0.15 minutes
b) about 21,600 minutes
c) approximately 3.6 minutes
d) approximately 216 minutes

**Key: d**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 43200 x 0.5% = 216 minutes. Result: 216 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 34. seed 1388911810982500831, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) about 14.4 minutes
b) approximately 864 minutes
c) about 51,840 minutes
d) about 86,400 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 35. seed 618027809057687626, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.75% over 30 days allows how many minutes of full outage?

a) 6,480 minutes
b) about 1.8 minutes
c) approximately 108 minutes
d) 10,800 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.75%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.75% = 0.25%. Step 3: 43200 x 0.25% = 108 minutes. Result: 108 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 36. seed 1571565662450241450, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.75% over 30 days allows how many minutes of full outage?

a) about 6,480 minutes
b) approximately 10,800 minutes
c) approximately 0.075 minutes
d) approximately 108 minutes

**Key: d**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.75%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.75% = 0.25%. Step 3: 43200 x 0.25% = 108 minutes. Result: 108 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 37. seed 1726921518858455126, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) approximately 0.6 minutes
b) 14.4 minutes
c) about 51,840 minutes
d) 864 minutes

**Key: d**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 38. seed 2428080484940295252, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 90 days allows how many minutes of full outage?

a) about 864 minutes
b) 43.2 minutes
c) 2,592 minutes
d) approximately 1.8 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 129600 x 2% = 2,592 minutes. Result: 2,592 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 39. seed 77263980580205815, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 30 days allows how many minutes of full outage?

a) 3.6 minutes
b) approximately 12,960 minutes
c) about 216 minutes
d) 21,600 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 43200 x 0.5% = 216 minutes. Result: 216 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 40. seed 2677679773242010741, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 30 days allows how many minutes of full outage?

a) 21,600 minutes
b) 12,960 minutes
c) approximately 3.6 minutes
d) approximately 216 minutes

**Key: d**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 43200 x 0.5% = 216 minutes. Result: 216 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 41. seed 4311697872233554046, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 30 days allows how many minutes of full outage?

a) 21,600 minutes
b) 3.6 minutes
c) about 0.15 minutes
d) about 216 minutes

**Key: d**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 43200 x 0.5% = 216 minutes. Result: 216 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 42. seed 4555729540250932165, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 90 days allows how many minutes of full outage?

a) about 129,600 minutes
b) about 0.9 minutes
c) 77,760 minutes
d) 1,296 minutes

**Key: d**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 129600 x 1% = 1,296 minutes. Result: 1,296 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 43. seed 1965351208115029867, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 90 days allows how many minutes of full outage?

a) about 864 minutes
b) about 1.8 minutes
c) approximately 2,592 minutes
d) approximately 43.2 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 129600 x 2% = 2,592 minutes. Result: 2,592 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 44. seed 385121425281774814, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) 86,400 minutes
b) 0.6 minutes
c) approximately 864 minutes
d) about 14.4 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 45. seed 1567049611971592819, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 30 days allows how many minutes of full outage?

a) approximately 3.6 minutes
b) 21,600 minutes
c) 0.15 minutes
d) 216 minutes

**Key: d**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 43200 x 0.5% = 216 minutes. Result: 216 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 46. seed 3322363032965966867, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99.5% over 90 days allows how many minutes of full outage?

a) approximately 648 minutes
b) approximately 10.8 minutes
c) approximately 64,800 minutes
d) 216 minutes

**Key: a**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99.5%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99.5% = 0.5%. Step 3: 129600 x 0.5% = 648 minutes. Result: 648 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 47. seed 3928917354899626971, level 2

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 90 days allows how many minutes of full outage?

a) approximately 1,296 minutes
b) 21.6 minutes
c) 432 minutes
d) 0.9 minutes

**Key: a**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 90 days. Step 1: the window is 90 x 1440 = 129600 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 129600 x 1% = 1,296 minutes. Result: 1,296 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 48. seed 4402262153895917404, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 30 days allows how many minutes of full outage?

a) approximately 25,920 minutes
b) 432 minutes
c) 7.2 minutes
d) approximately 43,200 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 43200 x 1% = 432 minutes. Result: 432 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 49. seed 129114714830715341, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 99% over 30 days allows how many minutes of full outage?

a) approximately 7.2 minutes
b) 25,920 minutes
c) about 432 minutes
d) approximately 43,200 minutes

**Key: c**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 99%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 99% = 1%. Step 3: 43200 x 1% = 432 minutes. Result: 432 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.

## 50. seed 3833148948681073218, level 1

According to Google's Site Reliability Workbook, an error rate of 100% minus the SLO, held for the whole window, uses exactly the error budget. An SLO of 98% over 30 days allows how many minutes of full outage?

a) approximately 51,840 minutes
b) 864 minutes
c) about 0.6 minutes
d) about 14.4 minutes

**Key: b**

Explanation: Rule: according to Google's Site Reliability Workbook, an error rate of 100% minus the SLO held for the whole window uses exactly the error budget, so the budget is the window times (100% - SLO). Inputs: SLO 98%, window 30 days. Step 1: the window is 30 x 1440 = 43200 minutes. Step 2: the allowed error rate is 100% - 98% = 2%. Step 3: 43200 x 2% = 864 minutes. Result: 864 minutes. Source: `sre-workbook-slo-alerting#4-alert-on-burn-rate`.
