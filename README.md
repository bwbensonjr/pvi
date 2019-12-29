# pvi

Calculate Partisan Voter Index (PVI)

## calc_pvi

## pvi_string

## Example

You can call the `pvi.calc_pvi` function on anything that responds with
with indexes for the required values, e.g., dictionaries or Pandas DataFrames.

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

DataFrame example for Massachusetts Congressional district PVI.

```
>>> MA_CONG_DIST = pd.DataFrame({
    'US_House': ['1st Congressional',
                 '2nd Congressional',
                 '3rd Congressional',
                 '4th Congressional',
                 '5th Congressional',
                 '6th Congressional',
                 '7th Congressional',
                 '8th Congressional',
                 '9th Congressional'],
    'Obama_12': [213423, 199549, 189461, 211423, 235984, 212003, 233382, 213364, 212701],
    'Romney_12': [114339, 133195, 137869, 152699, 119934, 169966, 44275, 150825, 165212],
    'Clinton_16': [194036, 197492, 202952, 225976, 258908, 224858, 254037, 231356, 205581],
    'Trump_16': [123953, 129437, 123347, 133705, 95922, 153244, 36018, 131624, 163643],
})
>>> MA_CONG_DIST["PVI_N"] = pvi.calc_pvi(MA_CONG_DIST)
>>> MA_CONG_DIST["PVI"] = MA_CONG_DIST["PVI_N"].map(pvi.pvi_string)
>>> MA_CONG_DIST.sort_values("PVI_N", ascending=False)
            US_House  Obama_12  Romney_12  Clinton_16  Trump_16      PVI_N   PVI
6  7th Congressional    233382      44275      254037     36018  34.321468  D+34
4  5th Congressional    235984     119934      258908     95922  18.094473  D+18
0  1st Congressional    213423     114339      194036    123953  11.563200  D+12
7  8th Congressional    213364     150825      231356    131624   9.622453  D+10
3  4th Congressional    211423     152699      225976    133705   8.895400   D+9
1  2nd Congressional    199549     133195      197492    129437   8.652278   D+9
2  3rd Congressional    189461     137869      202952    123347   8.500776   D+9
5  6th Congressional    212003     169966      224858    153244   5.941072   D+6
8  9th Congressional    212701     165212      205581    163643   4.449376   D+4
```

## Run unit tests

```
python -m unittest tests.test_pvi
```
