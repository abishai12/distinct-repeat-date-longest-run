# MEI Question 4 — Repeat vs Distinct Dates Solver

## Repo Title
**distinct-repeat-date-longest-run**

## File Name
`repeat_date_longest_run.py`

## GitHub Description
Python solver for MEI Question 4: finds the longest consecutive run of Repeat Dates (DDMMYY with a repeated digit) between now and 31/12/2098. Implements Distinct Date detection via digit-set uniqueness and gap analysis between successive Distinct Dates.

---

## Overview
This program solves **MEI Question 4** from the 28/10/26 paper.

We are given dates in the form `DDMMYY` (e.g. `281026` for 28 Oct 2026):

- **Repeat Date:** contains a repeated digit in its 6-digit string (e.g. `281026` repeats `2`)
- **Distinct Date:** all 6 digits are different (e.g. `180926` = 1,8,0,9,2,6)

Example from the question:
> `180926` and `140327` are both Distinct Dates and every date in between them is a Repeat Date.

**Task:** Find the longest run of Repeat Dates between now and `31/12/2098` and output it as `ddmmyyDDMMYY` where `ddmmyy` is the last Distinct Date before the run and `DDMMYY` is the first Distinct Date after the run.

## How This Program Works

Your original code (`repeat_date_longest_run.py`) does this:

1. **Iterate calendar:** Loop `year = 2026 → 2098`, `month = 1 → 12`, with correct `days_in_month` including leap year logic `year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)`.
2. **Build date string:** `DD + MM + YY[2:4]` e.g. `05` + `09` + `29` = `050929`
3. **Check for repeats:** 
   - Puts the 6 characters into `date_list`
   - Sorts with bubble sort (your `swap` loop)
   - Scans sorted list for `date_list[r] == date_list[r+1]` — if equal, it's a Repeat Date
4. **Track runs:**
   - `startdate` / `lastdate` store boundaries
   - `count` increments for each Repeat Date in current run
   - When a Distinct Date is hit, save `count` into `length_inbetween`, and save boundaries into `startdatelist` / `enddatelist`
5. **Find max:** Bubble sort a copy of `length_inbetween` to get longest, then look up its start/end.

### Result

Running from `28/10/2026` to `31/12/2098`:

- Total Distinct Dates: ~3562
- **Longest run: 601 days**
- **Answer: `310829250431`**
  - Last Distinct before run: `310829` = 31 Aug 2029
  - First Distinct after run: `250431` = 25 Apr 2031
  - Every date between is a Repeat Date

If you start from `03/11/2026` (today), the longest run is identical.

Other top runs:
- `180932` → `250134` = 493 days
- `081239` → `250341` = 472 days
- `301259` → `240361` = 449 days

## How to Run

```bash
python repeat_date_longest_run.py
```

Output will print each run found and finally:
```
310829 250431
```

So your submission value is:
```
310829250431
```

## Improvements (for a clean version)

Your bubble sort works but is O(n²). A simpler Pythonic check is:

```python
from datetime import date, timedelta

def is_distinct(d):
    s = d.strftime("%d%m%y")
    return len(set(s)) == 6
```

Then just collect distinct dates and compute `(next_distinct - prev_distinct).days - 1`.

This avoids manual month/day handling and string sorting.

## Complexity
- Dates checked: ~26k days (2026-2098)
- Original: O(N * 6²) due to bubble sort on 6 items — effectively O(N)
- Improved: O(N)

## Requirements
- Python 3.x
- No external libraries

## Author
Solution for MEI Challenge Question 4 — 28/10/26 paper
Original implementation by Abishai
