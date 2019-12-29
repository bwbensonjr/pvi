import unittest
import pvi

MA_VOTES = {
    "Obama_12": 1921290,
    "Romney_12": 1188314,
    "Clinton_16": 1995196,
    "Trump_16": 1090893,
    }

MA_PVI_N = 11.677772318663537
MA_PVI = "D+12"

class PviTests(unittest.TestCase):

    def test_ma_pvi(self):
        ma_pvi_n = pvi.calc_pvi(MA_VOTES)
        self.assertEqual(ma_pvi_n, MA_PVI_N)
        ma_pvi = pvi.pvi_string(ma_pvi_n)
        self.assertEqual(ma_pvi, MA_PVI)
