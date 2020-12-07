import json
import numpy as np
import os.path
from os import path
import sys

files = ['1981_1_fulltext.json', '1981_2_fulltext.json', '1982_1_fulltext.json', '1982_2_fulltext.json', '1982_3_fulltext.json', '1983_1_fulltext.json', '1983_2_fulltext.json', '1983_3_fulltext.json', '1984_1_fulltext.json', '1984_2_fulltext.json', '1984_3_fulltext.json', '1985_1_fulltext.json', '1985_2_fulltext.json', '1986_1_fulltext.json', '1986_2_fulltext.json', '1986_3_fulltext.json', '1987_1_fulltext.json', '1987_2_fulltext.json', '1987_3_fulltext.json', '1988_1_fulltext.json', '1988_2_fulltext.json', '1988_3_fulltext.json', '1989_1_fulltext.json', '1989_2_fulltext.json', '1989_3_fulltext.json', '1990_v1_1_fulltext.json', '1990_v1_2_fulltext.json', '1991_1_fulltext.json', '1991_2_fulltext.json', '1992_1_fulltext.json', '1992_2_fulltext.json', '1993_1_fulltext.json', '1993_2_fulltext.json', '1994_1_fulltext.json', '1994_2_fulltext.json', '1995_1_fulltext.json', '1995_2_fulltext.json', '1996_1_fulltext.json', '1996_2_fulltext.json', '1997_1_fulltext.json', '1997_2_fulltext.json', '1998_1_fulltext.json', '1998_2_fulltext.json', '1999_1_fulltext.json', '1999_2_fulltext.json', '2000_1_fulltext.json', '2001_2_fulltext.json', '2002_1_fulltext.json', '2002_2_fulltext.json', '2003_1_fulltext.json', '2003_2_fulltext.json', '2004_1_fulltext.json', '2004_2_fulltext.json', '2005_1_fulltext.json', '2005_2_fulltext.json', '2006_1_fulltext.json', '2006_2_fulltext.json', '2007_1_fulltext.json', '2007_2_fulltext.json', '2008_1_fulltext.json', '2008_2_fulltext.json', '2009_1_fulltext.json', '2009_2_fulltext.json', '2010_1_fulltext.json', '2010_2_fulltext.json', '2011_1_fulltext.json', '2011_2_fulltext.json', '2012_1_fulltext.json', '2012_2_fulltext.json', '2013_1_fulltext.json', '2013_2_fulltext.json', '2014_1_fulltext.json', '2014_2_fulltext.json', '2015_1_fulltext.json', '2015_2_fulltext.json', '2016_1_fulltext.json', '2016_2_fulltext.json', '2017_1_fulltext.json', '2017_2_fulltext.json', '2018_1_fulltext.json', '2018_2_fulltext.json']
prev = "1981"
a = []
for file in files:
    if file[:4] != prev:
        temp = prev
        prev = file[:4]
        np.save("new_data/" + temp, a)
        print(len(a))
        print(temp)
        a = []
    path = "FullOutput/"
    path += file
    with open(path) as fp:
        year = json.load(fp)
    for url in year.keys():
        body = year[url]["body_text"]
        new_body = body.replace("*", "")
        a.append(new_body)

np.save("new_data/2018", a)



