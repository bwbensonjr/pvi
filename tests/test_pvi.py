import unittest
import pvi
import pandas as pd

MA_PRES = pd.DataFrame({
    "Region": ["MA"],
    "cur_dem_votes": [1995196],
    "cur_gop_votes": [1090893],
    "prev_dem_votes": [1921290],
    "prev_gop_votes": [1188314],
    "pvi_year": [2016],
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
    'cur_dem_votes': [194036, 197492, 202952, 225976, 258908, 224858, 254037, 231356, 205581],
    'cur_gop_votes': [123953, 129437, 123347, 133705, 95922, 153244, 36018, 131624, 163643],
    'prev_dem_votes': [213423, 199549, 189461, 211423, 235984, 212003, 233382, 213364, 212701],
    'prev_gop_votes': [114339, 133195, 137869, 152699, 119934, 169966, 44275, 150825, 165212],
    'pvi_year': 2016,
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
    py2 = pvi.calc_pvi_year(pd.to_datetime("1998-03-04"))
    return py2

class PviTests(unittest.TestCase):

    def test_ma_pvi(self):
        ma_pvi_n = pvi.calc_pvi(MA_PRES).iloc[0]
        self.assertAlmostEqual(ma_pvi_n, MA_PVI_N, places=4)
        ma_pvi = pvi.pvi_string(ma_pvi_n)
        self.assertEqual(ma_pvi, MA_PVI)

    def test_ma_cong_pvi(self):
        MA_CONG_DIST["PVI_N"] = pvi.calc_pvi(MA_CONG_DIST)
        for i in range(0, len(MA_CONG_DIST)):
            self.assertAlmostEqual(MA_CONG_DIST.iloc[i]["PVI_N"],
                                   MA_CONG_PVI.iloc[i]["PVI_N"],
                                   places=4)
        MA_CONG_DIST["PVI"] = MA_CONG_DIST["PVI_N"].map(pvi.pvi_string)
        for i in range(0, len(MA_CONG_DIST)):
            self.assertEqual(MA_CONG_DIST.iloc[i]["PVI"],
                             MA_CONG_PVI.iloc[i]["PVI"])

    def test_calc_pvi_year(self):
        py1 = pvi.calc_pvi_year(pd.to_datetime("2007-06-12"))
        self.assertEqual(py1, 2004)
        self.assertRaises(pvi.PviYearException, throws_pvi_year_exception)
