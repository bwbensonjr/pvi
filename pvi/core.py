"""Calculate Partisan Voter Index (PVI)"""

# Copyright (c) 2019, Brent Benson
# See package file LICENSE for more information

import pandas as pd

def dem_pct(d, r):
    return (d / (d + r))

def dem_pres_pct(df):
    dpp = dem_pct(df["cur_dem_votes"] + df["prev_dem_votes"],
                  df["cur_gop_votes"] + df["prev_gop_votes"])
    return dpp

PRES_VOTES = pd.DataFrame({
    'cur_dem': ['Clinton_16', 'Obama_12', 'Obama_08', 'Kerry_04', 'Gore_00'],
    'cur_dem_votes': [65853514, 65915795, 69498516, 59028444, 50999897],
    'prev_dem': ['Obama_12', 'Obama_08', 'Kerry_04', 'Gore_00', 'Clint_96'],
    'prev_dem_votes': [65915795, 69498516, 59028444, 50999897, 47402357],
    'cur_gop': ['Trump_16', 'Romney_12', 'McCain_08', 'Bush_04', 'Bush_00'],
    'cur_gop_votes': [62984828, 60933504, 59948323, 62040610, 50456002],
    'prev_gop': ['Romney_12', 'McCain_08', 'Bush_04', 'Bush_00', 'Dole_96'],
    'prev_gop_votes': [60933504, 59948323, 62040610, 50456002, 39198755],
    'valid_as_of': [pd.to_datetime('2016-11-09'),
                    pd.to_datetime('2012-11-07'),
                    pd.to_datetime('2008-11-05'),
                    pd.to_datetime('2004-11-03'),
                    pd.to_datetime('2000-11-08')],
    'valid_until': [pd.to_datetime('2020-11-03'),
                    pd.to_datetime('2016-11-08'),
                    pd.to_datetime('2012-11-06'),
                    pd.to_datetime('2008-11-04'),
                    pd.to_datetime('2004-11-02')],
    'pvi_year': [2016, 2012, 2008, 2004, 2000],
    })
PRES_VOTES["us_pres_pct"] = dem_pres_pct(PRES_VOTES)

def calc_pvi(df):
    df_w_us = pd.merge(df, PRES_VOTES[["pvi_year", "us_pres_pct"]], on="pvi_year", how="left")
    dem_pct = dem_pres_pct(df_w_us)
    df_pvi = (dem_pct - df_w_us["us_pres_pct"]) * 100
    return df_pvi

def pvi_string(pvi):
    if pvi <= -0.5:
        s = "R+{:.0f}".format(abs(pvi))
    elif pvi >= 0.5:
        s = "D+{:.0f}".format(abs(pvi))
    else:
        s = "EVEN"
    return s

