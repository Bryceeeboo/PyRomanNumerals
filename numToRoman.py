# Decimal number to roman numeral conversion

"""
General program structure:
    Take a number as an input string
    Check validity of input string
    If string is valid
        Convert number to roman numeral string
    Output roman numeral string
"""

# Input string
inputString = raw_input("Number to convert: ")
print "Input string: " , inputString

valid = false
while valid == false:
    try:
        inNum = int(inputString)
        valid = true
    except Exception as e:
        print "Invalid Input"
        inputString = raw_input("Number to convert: ")
