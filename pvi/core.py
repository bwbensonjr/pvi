"""Calculate Partisan Voter Index (PVI)"""

# Copyright (c) 2019, Brent Benson
# See package file LICENSE for more information

import pandas as pd

def dem_pct(d, r):
    return (d / (d + r))

CANDIDATE_COLUMNS = {
    2020: {"cur_dem": "Biden_20", "cur_gop": "Trump_20",
           "prev_dem": "Clinton_16", "prev_gop": "Trump_16"},
    2016: {"cur_dem": "Clinton_16", "cur_gop": "Trump_16",
           "prev_dem": "Obama_12", "prev_gop": "Romney_12"},
    2012: {"cur_dem": "Obama_12", "cur_gop": "Romney_12",
           "prev_dem": "Obama_08", "prev_gop": "McCain_08"},
    2008: {"cur_dem": "Obama_08", "cur_gop": "McCain_08",
           "prev_dem": "Kerry_04", "prev_gop": "Bush_04"},
    2004: {"cur_dem": "Kerry_04", "cur_gop": "Bush_04",
           "prev_dem": "Gore_00", "prev_gop": "Bush_00"},
    2000: {"cur_dem": "Gore_00", "cur_gop": "Bush_00",
           "prev_dem": "Clinton_96", "prev_gop": "Dole_96"},
    }

PRES_VOTES = {
    "Biden_20": 81281502,
    "Trump_20": 74222593,
    "Clinton_16": 65853514,
    "Trump_16": 62984828,
    "Obama_12": 65915795,
    "Romney_12": 60933504,
    "Obama_08": 69498516,
    "McCain_08": 59948323,
    "Kerry_04": 59028444,
    "Bush_04": 62040610,
    "Gore_00": 50999897,
    "Bush_00": 50456002,
    "Clinton_96": 47402357,
    "Dole_96": 39198755,
    }

class PviYearException(Exception):
    pass

def dem_pres_pct(df, pvi_year=2020):
    cand_cols = CANDIDATE_COLUMNS[pvi_year]
    dpp = dem_pct(df[cand_cols["cur_dem"]] + df[cand_cols["prev_dem"]],
                  df[cand_cols["cur_gop"]] + df[cand_cols["prev_gop"]])
    return dpp

def calc_pvi(df, pvi_year=2020):
    if pvi_year not in CANDIDATE_COLUMNS:
        raise PviYearException("Unsupported PVI year", pvi_year)
    df_pvi = (dem_pres_pct(df, pvi_year) - dem_pres_pct(PRES_VOTES, pvi_year)) * 100
    return df_pvi

def pvi_string(pvi):
    if pvi <= -0.5:
        s = "R+{:.0f}".format(abs(pvi))
    elif pvi >= 0.5:
        s = "D+{:.0f}".format(abs(pvi))
    else:
        s = "EVEN"
    return s

