"""Calculate Partisan Voter Index (PVI)"""

# Copyright (c) 2019, Brent Benson
# See package file LICENSE for more information

US_VOTES = {
    "Obama_12": 65915796,
    "Romney_12": 60933500,
    "Clinton_16": 65853516,
    "Trump_16": 62984824,
    }

def dem_pct(d, r):
    return (d / (d + r))

US_DEM_PCT = dem_pct(US_VOTES["Obama_12"] + US_VOTES["Clinton_16"],
                     US_VOTES["Romney_12"] + US_VOTES["Trump_16"])

def calc_pvi(df):
    dem = df["Obama_12"] + df["Clinton_16"]
    gop = df["Romney_12"] + df["Trump_16"]
    pvi = (dem_pct(dem, gop) - US_DEM_PCT) * 100
    return pvi

def pvi_string(pvi):
    if pvi <= -0.5:
        s = "R+{:.0f}".format(abs(pvi))
    elif pvi >= 0.5:
        s = "D+{:.0f}".format(abs(pvi))
    else:
        s = "EVEN"
    return s

