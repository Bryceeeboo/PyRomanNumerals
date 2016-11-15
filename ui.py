# UI for roman numeral converter
from numToRoman import *

"""MAIN LOOP"""
print("Convert Numbers to Roman Numerals. Type 'exit' to quit")
while True:
    inNum = getValidInput()
    print inNum, "in Roman Numerals is", OOMR(inNum), "\n"
