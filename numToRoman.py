# Decimal number to roman numeral conversion
import sys
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
            return "M"*thous + convertToRoman(amountLeftOver)
        # If we've reached here, we have number < 1000
        elif number >= 900: # 900 in roman numerals is CM
            return "CM" + convertToRoman(number - 900)
        # If we've reached here, we have number < 900
        elif number >= 500: # Return D + recursive
            return "D" + convertToRoman(number - 500)
        # If we've reached here, we have number < 500
        elif number >= 400:
            return "CD" + convertToRoman(number - 400)
        elif number >= 100:
            # Take off 100 over and over until we get to a number < 100
            amountToConvert = 0
            amountLeftOver = number
            while amountLeftOver >= 100:
                amountLeftOver -= 100
                amountToConvert += 100
            huns = amountToConvert/100
            return "C"*huns + convertToRoman(amountLeftOver)
        # If we've reached here, we have number < 100
        elif number >= 90:
            return "XC" + convertToRoman(number - 90)
        # If we've reached here, we have number < 90
        elif number >= 50:
            return "L" + convertToRoman(number - 50)
        # If we've reached here, we have number < 50
        elif number >= 40:
            return "XL" + convertToRoman(number - 40)
        # If weave reached here, we have number < 40
        elif number >= 10:
            # Take off 10 over and over until we get to a number < 10
            amountToConvert = 0
            amountLeftOver = number
            while amountLeftOver >= 10:
                amountLeftOver -= 10
                amountToConvert += 10
            tens = amountToConvert/10
            return "X"*tens + convertToRoman(amountLeftOver)
        # If we reach here, we have number < 10
        elif number >= 9:
            return "IX" + convertToRoman(number - 9)
        # number < 9
        elif number >= 5:
            return "V" + convertToRoman(number - 5)
        # number < 5
        elif number >= 4:
            return "IV" + convertToRoman(number - 4)
        # number < 4, atomic base case
        else:
            return "I"*number

"""Gets and returns a valid input from the user"""
def getValidInput():
    # While loop to check the validity of the input string
    while True:
        # Input string
        inputString = raw_input("Number to convert: ")
        try:  # Assuming the input can be converted to an integer
            inNum = int(inputString)
            if inNum > 9999:
                print "Number too big. Only enter numbers <= 9999\n"
            else:
                return inNum # The only case where we return
        except Exception as e:  # If the input can't be converted
            # The user might want to exit the application
            if inputString.lower() == "exit":
                sys.exit()
            # If they don't want to exit, then their input is invalid
            print inputString, "is an invalid Input"

"""MAIN LOOP"""
print "Convert Numbers to Roman Numerals. Type 'exit' to quit"
while True:
    inNum = getValidInput()
    print inNum, "in Roman Numerals is", convertToRoman(inNum), "\n"
