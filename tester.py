# Tester for regular recursive function vs OOM recursive function

import time
from numToRoman import *

trials = 100
averages = []
for i in range(trials):
    start = time.time()
    for i in range(9999):
        roman = OOMR(i)
    fin = time.time()
    averages.append(fin - start)

print "OOM ",sum(averages)/trials

averages = []
for i in range(trials):
    start = time.time()
    for i in range(9999):
        roman = convertToRoman(i)
    fin = time.time()
    averages.append(fin - start)

print "CTR ",sum(averages)/trials
