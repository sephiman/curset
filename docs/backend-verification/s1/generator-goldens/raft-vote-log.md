# Raft election restriction (`raft-vote-log`): 50 goldens

Generated items for the blind review (ambiguity, realism, key). Regenerate with `uv run python scripts/export_backend_goldens.py`.

## 1. seed 2278688058201767260, level 2

A Raft voter has not voted yet; its log has entry terms `[2, 3, 3, 3]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[2, 2, 2, 2, 2]`
b) log `[2, 3, 3]`
c) `[2, 2, 2, 2]`
d) `[2, 4]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 3, 3, 3]`. Step 1: the voter has last term 3, length 4. Step 2: candidate `[2, 4]` has last term 4, length 2, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 3, 3]` has last term 3, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 2, 2, 2, 2]` has last term 2, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 2, 2, 2]` has last term 2, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 2. seed 3233460177313415384, level 2

A Raft voter has not voted yet; its log has entry terms `[4, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[4, 4, 4, 4]`
b) log `[4, 5, 5]`
c) the candidate log `[4, 6, 6]`
d) `[4, 4, 4, 4, 4]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[4, 5, 5, 5]`. Step 1: the voter has last term 5, length 4. Step 2: candidate `[4, 6, 6]` has last term 6, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[4, 5, 5]` has last term 5, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[4, 4, 4, 4, 4]` has last term 4, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[4, 4, 4, 4]` has last term 4, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[4, 6, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 3. seed 3052091895710686797, level 1

A Raft voter has not voted yet; its log has entry terms `[2, 5, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[2, 5, 5, 5, 5, 5, 5]`
b) `[2, 4, 4, 4, 4]`
c) log `[2, 4, 4, 4, 4, 4, 4]`
d) `[2, 5, 5, 5]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 5, 5, 5, 5]`. Step 1: the voter has last term 5, length 5. Step 2: candidate `[2, 5, 5, 5, 5, 5, 5]` has last term 5, length 7, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 5, 5, 5]` has last term 5, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 4, 4, 4, 4, 4, 4]` has last term 4, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 4, 4, 4, 4]` has last term 4, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 5, 5, 5, 5, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 4. seed 2285824691877333039, level 1

A Raft voter has not voted yet; its log has entry terms `[3, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[3, 4, 4, 4]`
b) `[3, 5, 5, 5, 5, 5]`
c) log `[3, 5, 5]`
d) `[3, 4, 4, 4, 4, 4]`

**Key: b**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[3, 5, 5, 5]`. Step 1: the voter has last term 5, length 4. Step 2: candidate `[3, 5, 5, 5, 5, 5]` has last term 5, length 6, so the voter's log is not more up-to-date and it does not deny. Step 3: `[3, 5, 5]` has last term 5, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[3, 4, 4, 4, 4, 4]` has last term 4, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[3, 4, 4, 4]` has last term 4, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[3, 5, 5, 5, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 5. seed 1497107009180731952, level 2

A Raft voter has not voted yet; its log has entry terms `[4, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[4, 5, 5]`
b) the candidate log `[4, 4, 4, 4]`
c) log `[4, 4, 4, 4, 4]`
d) log `[4, 6, 6]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[4, 5, 5, 5]`. Step 1: the voter has last term 5, length 4. Step 2: candidate `[4, 6, 6]` has last term 6, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[4, 5, 5]` has last term 5, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[4, 4, 4, 4, 4]` has last term 4, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[4, 4, 4, 4]` has last term 4, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[4, 6, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 6. seed 1165992906572553514, level 2

A Raft voter has not voted yet; its log has entry terms `[2, 3, 3, 3, 3, 3]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[2, 2, 2, 2, 2, 2, 2]`
b) log `[2, 3, 3, 3, 3]`
c) the candidate log `[2, 2, 2, 2, 2, 2]`
d) the candidate log `[2, 4, 4, 4, 4]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 3, 3, 3, 3, 3]`. Step 1: the voter has last term 3, length 6. Step 2: candidate `[2, 4, 4, 4, 4]` has last term 4, length 5, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 3, 3, 3, 3]` has last term 3, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 2, 2, 2, 2, 2, 2]` has last term 2, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 2, 2, 2, 2, 2]` has last term 2, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 7. seed 3320732850280243169, level 2

A Raft voter has not voted yet; its log has entry terms `[2, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[2, 4, 4, 4]`
b) the candidate log `[2, 4, 4, 4, 4]`
c) log `[2, 6]`
d) `[2, 5, 5]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 5, 5, 5]`. Step 1: the voter has last term 5, length 4. Step 2: candidate `[2, 6]` has last term 6, length 2, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 5, 5]` has last term 5, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 4, 4, 4, 4]` has last term 4, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 4, 4, 4]` has last term 4, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 8. seed 3602019498597449252, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 3, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[1, 3, 3, 3, 3, 3, 3]`
b) log `[1, 3, 4, 4, 4, 4, 4]`
c) `[1, 3, 3, 3, 3]`
d) `[1, 3, 4, 4]`

**Key: b**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 3, 4, 4, 4]`. Step 1: the voter has last term 4, length 5. Step 2: candidate `[1, 3, 4, 4, 4, 4, 4]` has last term 4, length 7, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 3, 4, 4]` has last term 4, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 3, 3, 3, 3, 3, 3]` has last term 3, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 3, 3, 3, 3]` has last term 3, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 3, 4, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 9. seed 3592619770373233169, level 2

A Raft voter has not voted yet; its log has entry terms `[3, 4, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[3, 5, 5]`
b) `[3, 3, 3, 3, 3, 3]`
c) `[3, 4, 4, 4]`
d) log `[3, 3, 3, 3, 3]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[3, 4, 4, 4, 4]`. Step 1: the voter has last term 4, length 5. Step 2: candidate `[3, 5, 5]` has last term 5, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[3, 4, 4, 4]` has last term 4, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[3, 3, 3, 3, 3, 3]` has last term 3, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[3, 3, 3, 3, 3]` has last term 3, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[3, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 10. seed 3450859780894423386, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 5, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[1, 5, 5, 5]`
b) `[1, 5, 5, 5, 5, 5]`
c) the candidate log `[1, 4, 4, 4, 4, 4, 4]`
d) log `[1, 4, 4, 4, 4]`

**Key: b**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 5, 5, 5, 5]`. Step 1: the voter has last term 5, length 5. Step 2: candidate `[1, 5, 5, 5, 5, 5]` has last term 5, length 6, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 5, 5, 5]` has last term 5, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 4, 4, 4, 4, 4, 4]` has last term 4, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 4, 4, 4, 4]` has last term 4, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 5, 5, 5, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 11. seed 2006318701023362762, level 2

A Raft voter has not voted yet; its log has entry terms `[2, 3, 3, 3]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[2, 4, 4]`
b) the candidate log `[2, 2, 2, 2, 2]`
c) log `[2, 2, 2, 2]`
d) the candidate log `[2, 3, 3]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 3, 3, 3]`. Step 1: the voter has last term 3, length 4. Step 2: candidate `[2, 4, 4]` has last term 4, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 3, 3]` has last term 3, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 2, 2, 2, 2]` has last term 2, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 2, 2, 2]` has last term 2, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 12. seed 1729840364005579804, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[1, 4, 4]`
b) log `[1, 3, 3, 3, 3, 3]`
c) `[1, 4, 4, 4, 4, 4]`
d) log `[1, 3, 3, 3]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 4, 4, 4]`. Step 1: the voter has last term 4, length 4. Step 2: candidate `[1, 4, 4, 4, 4, 4]` has last term 4, length 6, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 4, 4]` has last term 4, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 3, 3, 3, 3, 3]` has last term 3, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 3, 3, 3]` has last term 3, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 4, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 13. seed 702160218951815005, level 1

A Raft voter has not voted yet; its log has entry terms `[2, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[2, 3, 3, 3]`
b) the candidate log `[2, 3, 3, 3, 3, 3]`
c) log `[2, 4, 4]`
d) log `[2, 4, 4, 4, 4, 4]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 4, 4, 4]`. Step 1: the voter has last term 4, length 4. Step 2: candidate `[2, 4, 4, 4, 4, 4]` has last term 4, length 6, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 4, 4]` has last term 4, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 3, 3, 3, 3, 3]` has last term 3, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 3, 3, 3]` has last term 3, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 4, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 14. seed 4275391554720066235, level 2

A Raft voter has not voted yet; its log has entry terms `[2, 5, 5, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[2, 4, 4, 4, 4, 4, 4]`
b) `[2, 5, 5, 5, 5]`
c) `[2, 4, 4, 4, 4, 4]`
d) the candidate log `[2, 6, 6, 6]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 5, 5, 5, 5, 5]`. Step 1: the voter has last term 5, length 6. Step 2: candidate `[2, 6, 6, 6]` has last term 6, length 4, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 5, 5, 5, 5]` has last term 5, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 4, 4, 4, 4, 4, 4]` has last term 4, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 4, 4, 4, 4, 4]` has last term 4, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 6, 6, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 15. seed 3356039559345553440, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 2, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[1, 2, 3, 3, 3]`
b) `[1, 2, 3, 3, 3, 3, 3]`
c) the candidate log `[1, 2, 4, 4]`
d) log `[1, 2, 4, 4, 4, 4, 4]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 2, 4, 4, 4]`. Step 1: the voter has last term 4, length 5. Step 2: candidate `[1, 2, 4, 4, 4, 4, 4]` has last term 4, length 7, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 2, 4, 4]` has last term 4, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 2, 3, 3, 3, 3, 3]` has last term 3, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 2, 3, 3, 3]` has last term 3, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 2, 4, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 16. seed 1487747716754085768, level 1

A Raft voter has not voted yet; its log has entry terms `[2, 2, 3, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[2, 2, 3, 4, 4, 4]`
b) `[2, 2, 3, 5, 5]`
c) the candidate log `[2, 2, 3, 4, 4, 4, 4, 4]`
d) the candidate log `[2, 2, 3, 5, 5, 5, 5]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 2, 3, 5, 5, 5]`. Step 1: the voter has last term 5, length 6. Step 2: candidate `[2, 2, 3, 5, 5, 5, 5]` has last term 5, length 7, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 2, 3, 5, 5]` has last term 5, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 2, 3, 4, 4, 4, 4, 4]` has last term 4, length 8: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 2, 3, 4, 4, 4]` has last term 4, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 2, 3, 5, 5, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 17. seed 3475422723369039521, level 2

A Raft voter has not voted yet; its log has entry terms `[2, 4, 5, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[2, 4, 6, 6, 6]`
b) `[2, 4, 4, 4, 4, 4]`
c) `[2, 4, 5, 5, 5]`
d) `[2, 4, 4, 4, 4, 4, 4]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 4, 5, 5, 5, 5]`. Step 1: the voter has last term 5, length 6. Step 2: candidate `[2, 4, 6, 6, 6]` has last term 6, length 5, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 4, 5, 5, 5]` has last term 5, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 4, 4, 4, 4, 4, 4]` has last term 4, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 4, 4, 4, 4, 4]` has last term 4, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 4, 6, 6, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 18. seed 2996454359302115426, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 1, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[1, 1, 3, 3, 3, 3, 3]`
b) `[1, 1, 3, 3, 3]`
c) `[1, 1, 4, 4, 4, 4, 4]`
d) the candidate log `[1, 1, 4, 4]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 1, 4, 4, 4]`. Step 1: the voter has last term 4, length 5. Step 2: candidate `[1, 1, 4, 4, 4, 4, 4]` has last term 4, length 7, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 1, 4, 4]` has last term 4, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 1, 3, 3, 3, 3, 3]` has last term 3, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 1, 3, 3, 3]` has last term 3, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 1, 4, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 19. seed 3949970992476567335, level 1

A Raft voter has not voted yet; its log has entry terms `[2, 4, 5, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[2, 4, 5, 5, 5]`
b) `[2, 4, 4, 4, 4, 4, 4, 4]`
c) log `[2, 4, 5, 5, 5, 5, 5, 5]`
d) `[2, 4, 4, 4, 4, 4]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 4, 5, 5, 5, 5]`. Step 1: the voter has last term 5, length 6. Step 2: candidate `[2, 4, 5, 5, 5, 5, 5, 5]` has last term 5, length 8, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 4, 5, 5, 5]` has last term 5, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 4, 4, 4, 4, 4, 4, 4]` has last term 4, length 8: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 4, 4, 4, 4, 4]` has last term 4, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 4, 5, 5, 5, 5, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 20. seed 4115703127681573726, level 2

A Raft voter has not voted yet; its log has entry terms `[1, 2, 3, 3, 3]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[1, 2, 4, 4]`
b) `[1, 2, 3, 3]`
c) the candidate log `[1, 2, 2, 2, 2]`
d) the candidate log `[1, 2, 2, 2, 2, 2]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 2, 3, 3, 3]`. Step 1: the voter has last term 3, length 5. Step 2: candidate `[1, 2, 4, 4]` has last term 4, length 4, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 2, 3, 3]` has last term 3, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 2, 2, 2, 2, 2]` has last term 2, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 2, 2, 2, 2]` has last term 2, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 2, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 21. seed 1054680653096880614, level 1

A Raft voter has not voted yet; its log has entry terms `[3, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[3, 3, 3, 3, 3, 3]`
b) the candidate log `[3, 4, 4]`
c) log `[3, 4, 4, 4, 4, 4]`
d) the candidate log `[3, 3, 3, 3]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[3, 4, 4, 4]`. Step 1: the voter has last term 4, length 4. Step 2: candidate `[3, 4, 4, 4, 4, 4]` has last term 4, length 6, so the voter's log is not more up-to-date and it does not deny. Step 3: `[3, 4, 4]` has last term 4, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[3, 3, 3, 3, 3, 3]` has last term 3, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[3, 3, 3, 3]` has last term 3, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[3, 4, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 22. seed 4191161705716035259, level 1

A Raft voter has not voted yet; its log has entry terms `[2, 3, 3, 3]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[2, 3, 3]`
b) `[2, 2, 2, 2]`
c) log `[2, 2, 2, 2, 2, 2]`
d) the candidate log `[2, 3, 3, 3, 3, 3]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 3, 3, 3]`. Step 1: the voter has last term 3, length 4. Step 2: candidate `[2, 3, 3, 3, 3, 3]` has last term 3, length 6, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 3, 3]` has last term 3, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 2, 2, 2, 2, 2]` has last term 2, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 2, 2, 2]` has last term 2, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 3, 3, 3, 3, 3]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 23. seed 2181411461930176137, level 2

A Raft voter has not voted yet; its log has entry terms `[3, 5, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[3, 4, 4, 4, 4, 4]`
b) `[3, 4, 4, 4, 4]`
c) the candidate log `[3, 6, 6]`
d) the candidate log `[3, 5, 5, 5]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[3, 5, 5, 5, 5]`. Step 1: the voter has last term 5, length 5. Step 2: candidate `[3, 6, 6]` has last term 6, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[3, 5, 5, 5]` has last term 5, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[3, 4, 4, 4, 4, 4]` has last term 4, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[3, 4, 4, 4, 4]` has last term 4, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[3, 6, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 24. seed 3648745236195072685, level 2

A Raft voter has not voted yet; its log has entry terms `[1, 2, 3, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[1, 2, 3, 4, 4]`
b) log `[1, 2, 3, 5, 5]`
c) the candidate log `[1, 2, 3, 3, 3, 3, 3]`
d) log `[1, 2, 3, 3, 3, 3]`

**Key: b**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 2, 3, 4, 4, 4]`. Step 1: the voter has last term 4, length 6. Step 2: candidate `[1, 2, 3, 5, 5]` has last term 5, length 5, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 2, 3, 4, 4]` has last term 4, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 2, 3, 3, 3, 3, 3]` has last term 3, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 2, 3, 3, 3, 3]` has last term 3, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 2, 3, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 25. seed 1817857299045391842, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 2, 3, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[1, 2, 3, 3, 3, 3]`
b) log `[1, 2, 3, 3, 3, 3, 3, 3]`
c) log `[1, 2, 3, 4, 4, 4, 4]`
d) the candidate log `[1, 2, 3, 4, 4]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 2, 3, 4, 4, 4]`. Step 1: the voter has last term 4, length 6. Step 2: candidate `[1, 2, 3, 4, 4, 4, 4]` has last term 4, length 7, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 2, 3, 4, 4]` has last term 4, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 2, 3, 3, 3, 3, 3, 3]` has last term 3, length 8: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 2, 3, 3, 3, 3]` has last term 3, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 2, 3, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 26. seed 3777017563768647363, level 1

A Raft voter has not voted yet; its log has entry terms `[3, 5, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[3, 5, 5, 5, 5, 5]`
b) the candidate log `[3, 5, 5, 5]`
c) log `[3, 4, 4, 4, 4]`
d) the candidate log `[3, 4, 4, 4, 4, 4, 4]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[3, 5, 5, 5, 5]`. Step 1: the voter has last term 5, length 5. Step 2: candidate `[3, 5, 5, 5, 5, 5]` has last term 5, length 6, so the voter's log is not more up-to-date and it does not deny. Step 3: `[3, 5, 5, 5]` has last term 5, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[3, 4, 4, 4, 4, 4, 4]` has last term 4, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[3, 4, 4, 4, 4]` has last term 4, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[3, 5, 5, 5, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 27. seed 1388470600261616527, level 1

A Raft voter has not voted yet; its log has entry terms `[2, 2, 2, 3, 3, 3]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[2, 2, 2, 3, 3, 3, 3]`
b) the candidate log `[2, 2, 2, 2, 2, 2]`
c) log `[2, 2, 2, 2, 2, 2, 2, 2]`
d) `[2, 2, 2, 3, 3]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 2, 2, 3, 3, 3]`. Step 1: the voter has last term 3, length 6. Step 2: candidate `[2, 2, 2, 3, 3, 3, 3]` has last term 3, length 7, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 2, 2, 3, 3]` has last term 3, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 2, 2, 2, 2, 2, 2, 2]` has last term 2, length 8: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 2, 2, 2, 2, 2]` has last term 2, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 2, 2, 3, 3, 3, 3]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 28. seed 2338314615139439868, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 2, 2, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[1, 2, 2, 4, 4, 4, 4, 4]`
b) log `[1, 2, 2, 4, 4]`
c) `[1, 2, 2, 3, 3, 3]`
d) log `[1, 2, 2, 3, 3, 3, 3, 3]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 2, 2, 4, 4, 4]`. Step 1: the voter has last term 4, length 6. Step 2: candidate `[1, 2, 2, 4, 4, 4, 4, 4]` has last term 4, length 8, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 2, 2, 4, 4]` has last term 4, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 2, 2, 3, 3, 3, 3, 3]` has last term 3, length 8: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 2, 2, 3, 3, 3]` has last term 3, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 2, 2, 4, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 29. seed 2165458646318826251, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 2, 2, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[1, 2, 2, 4, 4]`
b) `[1, 2, 2, 3, 3, 3, 3, 3]`
c) `[1, 2, 2, 3, 3, 3]`
d) the candidate log `[1, 2, 2, 4, 4, 4, 4]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 2, 2, 4, 4, 4]`. Step 1: the voter has last term 4, length 6. Step 2: candidate `[1, 2, 2, 4, 4, 4, 4]` has last term 4, length 7, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 2, 2, 4, 4]` has last term 4, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 2, 2, 3, 3, 3, 3, 3]` has last term 3, length 8: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 2, 2, 3, 3, 3]` has last term 3, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 2, 2, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 30. seed 3879859878036297608, level 2

A Raft voter has not voted yet; its log has entry terms `[2, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[2, 5, 5]`
b) `[2, 4, 4, 4, 4]`
c) the candidate log `[2, 4, 4, 4]`
d) the candidate log `[2, 6, 6]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 5, 5, 5]`. Step 1: the voter has last term 5, length 4. Step 2: candidate `[2, 6, 6]` has last term 6, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 5, 5]` has last term 5, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 4, 4, 4, 4]` has last term 4, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 4, 4, 4]` has last term 4, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 6, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 31. seed 872574403322019408, level 2

A Raft voter has not voted yet; its log has entry terms `[1, 1, 1, 3, 3, 3]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[1, 1, 1, 4]`
b) the candidate log `[1, 1, 1, 2, 2, 2, 2]`
c) `[1, 1, 1, 2, 2, 2]`
d) log `[1, 1, 1, 3, 3]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 1, 1, 3, 3, 3]`. Step 1: the voter has last term 3, length 6. Step 2: candidate `[1, 1, 1, 4]` has last term 4, length 4, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 1, 1, 3, 3]` has last term 3, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 1, 1, 2, 2, 2, 2]` has last term 2, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 1, 1, 2, 2, 2]` has last term 2, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 1, 1, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 32. seed 4022184813507916117, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[1, 3, 3, 3]`
b) `[1, 3, 3, 3, 3, 3]`
c) `[1, 4, 4]`
d) the candidate log `[1, 4, 4, 4, 4]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 4, 4, 4]`. Step 1: the voter has last term 4, length 4. Step 2: candidate `[1, 4, 4, 4, 4]` has last term 4, length 5, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 4, 4]` has last term 4, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 3, 3, 3, 3, 3]` has last term 3, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 3, 3, 3]` has last term 3, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 33. seed 1957104197194107204, level 2

A Raft voter has not voted yet; its log has entry terms `[1, 5, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[1, 6, 6]`
b) `[1, 5, 5, 5]`
c) log `[1, 4, 4, 4, 4, 4]`
d) the candidate log `[1, 4, 4, 4, 4]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 5, 5, 5, 5]`. Step 1: the voter has last term 5, length 5. Step 2: candidate `[1, 6, 6]` has last term 6, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 5, 5, 5]` has last term 5, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 4, 4, 4, 4, 4]` has last term 4, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 4, 4, 4, 4]` has last term 4, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 6, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 34. seed 1509472254649870633, level 2

A Raft voter has not voted yet; its log has entry terms `[2, 4, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[2, 4, 4, 4]`
b) the candidate log `[2, 5, 5, 5]`
c) log `[2, 3, 3, 3, 3]`
d) log `[2, 3, 3, 3, 3, 3]`

**Key: b**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 4, 4, 4, 4]`. Step 1: the voter has last term 4, length 5. Step 2: candidate `[2, 5, 5, 5]` has last term 5, length 4, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 4, 4, 4]` has last term 4, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 3, 3, 3, 3, 3]` has last term 3, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 3, 3, 3, 3]` has last term 3, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 5, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 35. seed 4503450058927838337, level 2

A Raft voter has not voted yet; its log has entry terms `[1, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[1, 4, 4, 4, 4]`
b) the candidate log `[1, 4, 4, 4]`
c) log `[1, 5, 5]`
d) `[1, 6]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 5, 5, 5]`. Step 1: the voter has last term 5, length 4. Step 2: candidate `[1, 6]` has last term 6, length 2, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 5, 5]` has last term 5, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 4, 4, 4, 4]` has last term 4, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 4, 4, 4]` has last term 4, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 36. seed 2141446718480230571, level 2

A Raft voter has not voted yet; its log has entry terms `[3, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[3, 5, 5]`
b) the candidate log `[3, 3, 3, 3, 3]`
c) `[3, 3, 3, 3]`
d) log `[3, 4, 4]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[3, 4, 4, 4]`. Step 1: the voter has last term 4, length 4. Step 2: candidate `[3, 5, 5]` has last term 5, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[3, 4, 4]` has last term 4, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[3, 3, 3, 3, 3]` has last term 3, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[3, 3, 3, 3]` has last term 3, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[3, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 37. seed 4165263952241833526, level 2

A Raft voter has not voted yet; its log has entry terms `[3, 5, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[3, 4, 4, 4, 4]`
b) the candidate log `[3, 4, 4, 4, 4, 4]`
c) log `[3, 6, 6, 6]`
d) log `[3, 5, 5, 5]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[3, 5, 5, 5, 5]`. Step 1: the voter has last term 5, length 5. Step 2: candidate `[3, 6, 6, 6]` has last term 6, length 4, so the voter's log is not more up-to-date and it does not deny. Step 3: `[3, 5, 5, 5]` has last term 5, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[3, 4, 4, 4, 4, 4]` has last term 4, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[3, 4, 4, 4, 4]` has last term 4, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[3, 6, 6, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 38. seed 1749347912354064382, level 2

A Raft voter has not voted yet; its log has entry terms `[3, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[3, 3, 3, 3]`
b) log `[3, 4, 4]`
c) the candidate log `[3, 3, 3, 3, 3]`
d) the candidate log `[3, 5]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[3, 4, 4, 4]`. Step 1: the voter has last term 4, length 4. Step 2: candidate `[3, 5]` has last term 5, length 2, so the voter's log is not more up-to-date and it does not deny. Step 3: `[3, 4, 4]` has last term 4, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[3, 3, 3, 3, 3]` has last term 3, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[3, 3, 3, 3]` has last term 3, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[3, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 39. seed 707585605997521527, level 1

A Raft voter has not voted yet; its log has entry terms `[2, 3, 3, 3, 3, 3]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[2, 3, 3, 3, 3, 3, 3]`
b) the candidate log `[2, 3, 3, 3, 3]`
c) the candidate log `[2, 2, 2, 2, 2, 2]`
d) the candidate log `[2, 2, 2, 2, 2, 2, 2, 2]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 3, 3, 3, 3, 3]`. Step 1: the voter has last term 3, length 6. Step 2: candidate `[2, 3, 3, 3, 3, 3, 3]` has last term 3, length 7, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 3, 3, 3, 3]` has last term 3, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 2, 2, 2, 2, 2, 2, 2]` has last term 2, length 8: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 2, 2, 2, 2, 2]` has last term 2, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 3, 3, 3, 3, 3, 3]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 40. seed 4559958747556606947, level 2

A Raft voter has not voted yet; its log has entry terms `[2, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[2, 4, 4]`
b) log `[2, 5, 5]`
c) log `[2, 3, 3, 3, 3]`
d) `[2, 3, 3, 3]`

**Key: b**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 4, 4, 4]`. Step 1: the voter has last term 4, length 4. Step 2: candidate `[2, 5, 5]` has last term 5, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 4, 4]` has last term 4, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 3, 3, 3, 3]` has last term 3, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 3, 3, 3]` has last term 3, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 41. seed 1567315959238416278, level 2

A Raft voter has not voted yet; its log has entry terms `[1, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[1, 4, 4]`
b) `[1, 5, 5]`
c) log `[1, 3, 3, 3, 3]`
d) log `[1, 3, 3, 3]`

**Key: b**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 4, 4, 4]`. Step 1: the voter has last term 4, length 4. Step 2: candidate `[1, 5, 5]` has last term 5, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 4, 4]` has last term 4, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 3, 3, 3, 3]` has last term 3, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 3, 3, 3]` has last term 3, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 42. seed 3393496650673887891, level 2

A Raft voter has not voted yet; its log has entry terms `[1, 2, 2, 3, 3, 3]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[1, 2, 2, 3, 3]`
b) `[1, 2, 2, 2, 2, 2, 2]`
c) log `[1, 2, 2, 4]`
d) the candidate log `[1, 2, 2, 2, 2, 2]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 2, 2, 3, 3, 3]`. Step 1: the voter has last term 3, length 6. Step 2: candidate `[1, 2, 2, 4]` has last term 4, length 4, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 2, 2, 3, 3]` has last term 3, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 2, 2, 2, 2, 2, 2]` has last term 2, length 7: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 2, 2, 2, 2, 2]` has last term 2, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 2, 2, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 43. seed 2897720077350564011, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[1, 4, 4, 4, 4, 4]`
b) `[1, 5, 5, 5, 5]`
c) the candidate log `[1, 4, 4, 4]`
d) the candidate log `[1, 5, 5]`

**Key: b**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 5, 5, 5]`. Step 1: the voter has last term 5, length 4. Step 2: candidate `[1, 5, 5, 5, 5]` has last term 5, length 5, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 5, 5]` has last term 5, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 4, 4, 4, 4, 4]` has last term 4, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 4, 4, 4]` has last term 4, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 5, 5, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 44. seed 3212394741955260809, level 1

A Raft voter has not voted yet; its log has entry terms `[2, 2, 4, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[2, 2, 4, 5, 5, 5, 5, 5]`
b) log `[2, 2, 4, 5, 5]`
c) the candidate log `[2, 2, 4, 4, 4, 4]`
d) the candidate log `[2, 2, 4, 4, 4, 4, 4, 4]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 2, 4, 5, 5, 5]`. Step 1: the voter has last term 5, length 6. Step 2: candidate `[2, 2, 4, 5, 5, 5, 5, 5]` has last term 5, length 8, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 2, 4, 5, 5]` has last term 5, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 2, 4, 4, 4, 4, 4, 4]` has last term 4, length 8: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 2, 4, 4, 4, 4]` has last term 4, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 2, 4, 5, 5, 5, 5, 5]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 45. seed 649728390197174601, level 2

A Raft voter has not voted yet; its log has entry terms `[1, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[1, 4, 4, 4]`
b) the candidate log `[1, 5, 5]`
c) the candidate log `[1, 4, 4, 4, 4]`
d) log `[1, 6]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 5, 5, 5]`. Step 1: the voter has last term 5, length 4. Step 2: candidate `[1, 6]` has last term 6, length 2, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 5, 5]` has last term 5, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 4, 4, 4, 4]` has last term 4, length 5: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 4, 4, 4]` has last term 4, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 46. seed 2286972324604821941, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) the candidate log `[1, 3, 3, 3, 3, 3]`
b) the candidate log `[1, 4, 4]`
c) log `[1, 4, 4, 4, 4, 4]`
d) the candidate log `[1, 3, 3, 3]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 4, 4, 4]`. Step 1: the voter has last term 4, length 4. Step 2: candidate `[1, 4, 4, 4, 4, 4]` has last term 4, length 6, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 4, 4]` has last term 4, length 3: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 3, 3, 3, 3, 3]` has last term 3, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 3, 3, 3]` has last term 3, length 4: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 4, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 47. seed 3402658695056878348, level 1

A Raft voter has not voted yet; its log has entry terms `[1, 3, 3, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[1, 3, 3, 3, 3, 3, 3, 3]`
b) the candidate log `[1, 3, 3, 3, 3, 3]`
c) log `[1, 3, 3, 4, 4, 4, 4]`
d) the candidate log `[1, 3, 3, 4, 4]`

**Key: c**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 3, 3, 4, 4, 4]`. Step 1: the voter has last term 4, length 6. Step 2: candidate `[1, 3, 3, 4, 4, 4, 4]` has last term 4, length 7, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 3, 3, 4, 4]` has last term 4, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 3, 3, 3, 3, 3, 3, 3]` has last term 3, length 8: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 3, 3, 3, 3, 3]` has last term 3, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 3, 3, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 48. seed 3622602545937387817, level 2

A Raft voter has not voted yet; its log has entry terms `[1, 2, 3, 3, 3]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[1, 2, 2, 2, 2, 2]`
b) log `[1, 2, 2, 2, 2]`
c) the candidate log `[1, 2, 3, 3]`
d) the candidate log `[1, 2, 4]`

**Key: d**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[1, 2, 3, 3, 3]`. Step 1: the voter has last term 3, length 5. Step 2: candidate `[1, 2, 4]` has last term 4, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[1, 2, 3, 3]` has last term 3, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[1, 2, 2, 2, 2, 2]` has last term 2, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[1, 2, 2, 2, 2]` has last term 2, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[1, 2, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 49. seed 3271237108336063038, level 2

A Raft voter has not voted yet; its log has entry terms `[2, 2, 5, 5, 5]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) `[2, 2, 6]`
b) log `[2, 2, 4, 4, 4]`
c) the candidate log `[2, 2, 5, 5]`
d) `[2, 2, 4, 4, 4, 4]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 2, 5, 5, 5]`. Step 1: the voter has last term 5, length 5. Step 2: candidate `[2, 2, 6]` has last term 6, length 3, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 2, 5, 5]` has last term 5, length 4: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 2, 4, 4, 4, 4]` has last term 4, length 6: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 2, 4, 4, 4]` has last term 4, length 5: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 2, 6]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.

## 50. seed 1355875741630817367, level 1

A Raft voter has not voted yet; its log has entry terms `[2, 4, 4, 4, 4, 4]`. Candidates ask for its vote with these logs. For which log does it NOT deny the vote because of the log?

a) log `[2, 4, 4, 4, 4, 4, 4, 4]`
b) log `[2, 3, 3, 3, 3, 3, 3, 3]`
c) log `[2, 3, 3, 3, 3, 3]`
d) `[2, 4, 4, 4, 4]`

**Key: a**

Explanation: Rule: the voter denies its vote if its own log is more up-to-date than the candidate's. Raft compares the last entries of the two logs: the later last term is more up-to-date, and with the same last term the longer log is. Inputs: voter log `[2, 4, 4, 4, 4, 4]`. Step 1: the voter has last term 4, length 6. Step 2: candidate `[2, 4, 4, 4, 4, 4, 4, 4]` has last term 4, length 8, so the voter's log is not more up-to-date and it does not deny. Step 3: `[2, 4, 4, 4, 4]` has last term 4, length 5: same last term, shorter, so the voter's log is more up-to-date and it denies. Step 4: `[2, 3, 3, 3, 3, 3, 3, 3]` has last term 3, length 8: longer log, older last term, so the voter's log is more up-to-date and it denies. Step 5: `[2, 3, 3, 3, 3, 3]` has last term 3, length 6: older last term, same length, so the voter's log is more up-to-date and it denies. Result: `[2, 4, 4, 4, 4, 4, 4, 4]`. Source: `paper-raft-dissertation#p40`; `paper-raft-dissertation#p42`.
