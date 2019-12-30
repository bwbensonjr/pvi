# pvi

Calculate Partisan Voter Index (PVI)

## calc_pvi

## pvi_string

## Example

The `pvi.calc_pvi` function works on a Pandas `DataFrame` that must include the
columns `cur_dem_votes`, `prev_dem_votes`, `cur_gop_votes`, `prev_gop_votes`,
and `pvi_year`, which will be used to calculate the PVI based on the
appropriate historical numbers.

For the PVI year of 2016, the vote columns correspond to Clinton'16, Obama'12,
Trump'16, and Romney'12.

```
>>> import pandas as pd
>>> import pvi
>>> MA_PRES = pd.DataFrame({
    "Region": ["MA"],
    "cur_dem_votes": [1995196],
    "cur_gop_votes": [1090893],
    "prev_dem_votes": [1921290],
    "prev_gop_votes": [1188314],
    "pvi_year": [2016],
    })
>>> ma_pvi_n = pvi.calc_pvi(MA_PRES)
>>> ma_pvi_n
0    11.677774
dtype: float64
>>> pvi.pvi_string(ma_pvi_n.iloc[0])
'D+12'
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
    'cur_dem_votes': [194036, 197492, 202952, 225976, 258908, 224858, 254037, 231356, 205581],
    'cur_gop_votes': [123953, 129437, 123347, 133705, 95922, 153244, 36018, 131624, 163643],
    'prev_dem_votes': [213423, 199549, 189461, 211423, 235984, 212003, 233382, 213364, 212701],
    'prev_gop_votes': [114339, 133195, 137869, 152699, 119934, 169966, 44275, 150825, 165212],
    'pvi_year': 2016,
})
>>> MA_CONG_DIST["PVI_N"] = pvi.calc_pvi(MA_CONG_DIST)
>>> MA_CONG_DIST["PVI"] = MA_CONG_DIST["PVI_N"].map(pvi.pvi_string)
>>> MA_CONG_DIST.sort_values("PVI_N", ascending=False)
            US_House  cur_dem_votes  cur_gop_votes  prev_dem_votes  prev_gop_votes  pvi_year      PVI_N   PVI
6  7th Congressional         254037          36018          233382           44275      2016  34.321470  D+34
4  5th Congressional         258908          95922          235984          119934      2016  18.094475  D+18
0  1st Congressional         194036         123953          213423          114339      2016  11.563203  D+12
7  8th Congressional         231356         131624          213364          150825      2016   9.622455  D+10
3  4th Congressional         225976         133705          211423          152699      2016   8.895402   D+9
1  2nd Congressional         197492         129437          199549          133195      2016   8.652280   D+9
2  3rd Congressional         202952         123347          189461          137869      2016   8.500778   D+9
5  6th Congressional         224858         153244          212003          169966      2016   5.941074   D+6
8  9th Congressional         205581         163643          212701          165212      2016   4.449378   D+4
```

## Run unit tests

```
python -m unittest tests.test_pvi
```
