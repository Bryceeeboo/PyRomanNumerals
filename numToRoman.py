# Decimal number to roman numeral conversion

"""
General program structure:
    Take a number as an input string
    Check validity of input string
    If string is valid
        Convert number to roman numeral string
    Output roman numeral string
"""

"""
Converts an input number to a roman numeral.
    Input : int number, 0 <= number <= 9999
    Output : string, number represented as a roman numeral
"""
def convertToRoman(number):
    if number is 0:
        return "" # Return an empty string if the input number is 0
    else: # The input is nonzero
        if number >= 1000:
            # Take off 1000 over and over until we get to a number < 1000
            amountToConvert = 0
            amountLeftOver = number
            while amountLeftOver >= 1000:
                amountLeftOver -= 1000
                amountToConvert += 1000
            thous = amountToConvert/1000
            print thous,amountLeftOver
            return "M"*thous + convertToRoman(amountLeftOver)
        else:
            return "NZ"

# Input string
inputString = raw_input("Number to convert: ")
print "Input string : " , inputString

# While loop to check the validity of the input string
valid = False
while valid is False:
    try:  # Assuming the input can be converted to an integer
        inNum = int(inputString)
        valid = True
    except Exception as e:  # If the input can't be converted
        print "Invalid Input"
        # Ask the user to input a valid string again
        inputString = raw_input("Number to convert: ")
print "A valid input is now sitting in inNum"
print inNum, " in Roman Numerals is ", convertToRoman(inNum)

# At this point, we have a valid number to convert to a roman numeral
charDictionary = { 1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
