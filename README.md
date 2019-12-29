# pvi

Calculate Partisan Voter Index (PVI)

## calc_pvi

## pvi_string

## Example

```
>>> import pvi
>>> MA_VOTES = {
    "Obama_12": 1921290,
    "Romney_12": 1188314,
    "Clinton_16": 1995196,
    "Trump_16": 1090893,
    }
>>> ma_pvi_n = pvi.calc_pvi(MA_VOTES)
>>> ma_pvi_n
11.677772318663537
>>> ma_pvi = pvi.pvi_string(ma_pvi_n)
>>> ma_pvi
'D+12'
```

## Run unit tests

```
python -m unittest tests.test_pvi
```
