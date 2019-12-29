import unittest
import pvi
import pandas as pd

MA_VOTES = {
    "Obama_12": 1921290,
    "Romney_12": 1188314,
    "Clinton_16": 1995196,
    "Trump_16": 1090893,
    }

MA_PVI_N = 11.677772318663537
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
    'Obama_12': [213423, 199549, 189461, 211423, 235984, 212003, 233382, 213364, 212701],
    'Romney_12': [114339, 133195, 137869, 152699, 119934, 169966, 44275, 150825, 165212],
    'Clinton_16': [194036, 197492, 202952, 225976, 258908, 224858, 254037, 231356, 205581],
    'Trump_16': [123953, 129437, 123347, 133705, 95922, 153244, 36018, 131624, 163643],
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
    'PVI_N': [11.563200457363742,
              8.652278080423725,
              8.500775526052262,
              8.895400284891751,
              18.09447280082861,
              5.941071639760042,
              34.32146783259586,
              9.62245323391302,
              4.449376000045701],
})

class PviTests(unittest.TestCase):

    def test_ma_pvi(self):
        ma_pvi_n = pvi.calc_pvi(MA_VOTES)
        self.assertEqual(ma_pvi_n, MA_PVI_N)
        ma_pvi = pvi.pvi_string(ma_pvi_n)
        self.assertEqual(ma_pvi, MA_PVI)

    def test_ma_cong_pvi(self):
        MA_CONG_DIST["PVI_N"] = pvi.calc_pvi(MA_CONG_DIST)
        for i in range(0, len(MA_CONG_DIST)):
            self.assertAlmostEqual(MA_CONG_DIST.iloc[i]["PVI_N"],
                                   MA_CONG_PVI.iloc[i]["PVI_N"])
        MA_CONG_DIST["PVI"] = MA_CONG_DIST["PVI_N"].map(pvi.pvi_string)
        for i in range(0, len(MA_CONG_DIST)):
            self.assertEqual(MA_CONG_DIST.iloc[i]["PVI"],
                             MA_CONG_PVI.iloc[i]["PVI"])
        
