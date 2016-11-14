# Tester for regular recursive function vs OOM recursive function

import time
from numToRoman import *

trials = 100
maxnum = 9999
averages = []
for i in range(trials):
    start = time.time()
    for i in range(maxnum):
        roman = OOMR(i)
    fin = time.time()
    averages.append(fin - start)

print "OOM ",sum(averages)/trials/maxnum

averages = []
for i in range(trials):
    start = time.time()
    for i in range(maxnum):
        roman = convertToRoman(i)
    fin = time.time()
    averages.append(fin - start)

print "CTR ",sum(averages)/trials/maxnum
