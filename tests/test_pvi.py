import unittest
import pvi
import pandas as pd

MA_PRES = pd.DataFrame({
    "Region": ["MA"],
    "Clinton_16": [1995196],
    "Trump_16": [1090893],
    "Obama_12": [1921290],
    "Romney_12": [1188314],
    })

MA_PVI_N = 11.677774499748029
MA_PVI = "D+12"

MA_CONG_DIST = pd.DataFrame({
    'US_House': ['1st Congressional',
                 '2nd Congressional',
                 '3rd Congressional',
                 '4th Congressional',
                 '5th Congressional',
                 '6th Congressional',
                 '7th Congressional',
                 '8th Congressional',
                 '9th Congressional'],
    'Clinton_16': [194036, 197492, 202952, 225976, 258908, 224858, 254037, 231356, 205581],
    'Trump_16': [123953, 129437, 123347, 133705, 95922, 153244, 36018, 131624, 163643],
    'Obama_12': [213423, 199549, 189461, 211423, 235984, 212003, 233382, 213364, 212701],
    'Romney_12': [114339, 133195, 137869, 152699, 119934, 169966, 44275, 150825, 165212],
})

MA_CONG_PVI = pd.DataFrame({
    'US_House': ['1st Congressional',
                 '2nd Congressional',
                 '3rd Congressional',
                 '4th Congressional',
                 '5th Congressional',
                 '6th Congressional',
                 '7th Congressional',
                 '8th Congressional',
                 '9th Congressional'],
    'PVI': ['D+12', 'D+9', 'D+9', 'D+9', 'D+18', 'D+6', 'D+34', 'D+10', 'D+4'],
    'PVI_N': [11.563203,
              8.652280,
              8.500778,
              8.895402,
              18.094475,
              5.941074,
              34.321470,
              9.622455,
              4.449378],
})

def throws_pvi_year_exception():
    py2 = pvi.calc_pvi(MA_PRES, pvi_year=1973)
    return py2

class PviTests(unittest.TestCase):

    def test_ma_pvi(self):
        ma_pvi_n = pvi.calc_pvi(MA_PRES, pvi_year=2016).iloc[0]
        self.assertAlmostEqual(ma_pvi_n, MA_PVI_N, places=4)
        ma_pvi = pvi.pvi_string(ma_pvi_n)
        self.assertEqual(ma_pvi, MA_PVI)

    def test_ma_cong_pvi(self):
        MA_CONG_DIST["PVI_N"] = pvi.calc_pvi(MA_CONG_DIST, pvi_year=2016)
        for i in range(0, len(MA_CONG_DIST)):
            self.assertAlmostEqual(MA_CONG_DIST.iloc[i]["PVI_N"],
                                   MA_CONG_PVI.iloc[i]["PVI_N"],
                                   places=4)
        MA_CONG_DIST["PVI"] = MA_CONG_DIST["PVI_N"].map(pvi.pvi_string)
        for i in range(0, len(MA_CONG_DIST)):
            self.assertEqual(MA_CONG_DIST.iloc[i]["PVI"],
                             MA_CONG_PVI.iloc[i]["PVI"])

    def test_pvi_year_exception(self):
        self.assertRaises(pvi.PviYearException, throws_pvi_year_exception)
