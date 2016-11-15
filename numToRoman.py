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

# Dictionaries for the OOM concept
Ones = {1:"I",5:"V",10:"X"}
Tens = {1:"X",5:"L",10:"C"}
Huns = {1:"C",5:"D",10:"M"}
ooms = [Huns,Tens,Ones]
lims = [100, 10, 1] # Lower limits of the Huns, Tens, Ones OOMs
"""
OOMR (Orders of Magnitude Roman) conversion function.
    Input : int number, 0 <= number <= 9999
    Output: string, number represented as a roman numeral
"""
def OOMR(number):

    # Deal with thousands first, as this function takes numbers up to 9999
    if number >= 1000:
        thous = number/1000 # this returns floor(number/1000) as an int
        return "M"*thous + OOMR(number - thous*1000)

    # Reaching this point, we have number < 1000. Use OOM loop
    outString = "" # Set the outString, which will be added to in the loop
    for i,lowerlim in enumerate(lims): # For each order of magnitude
        # i is the dictionary we will use from ooms
        # lowerlim is the lower limit of that OOM. e.g. huns => 100 -> 999
        if number >= lowerlim: # Then we apply for this oom
            if number >= lowerlim*10: # 10
                outString += ooms[i][10] # M, C, X
            elif number >= lowerlim*9: # 9
                outString += ooms[i][1] + ooms[i][10] # CM, XC, IX
            elif number >= lowerlim*6: # 6, 7, 8
                outString += \
                    ooms[i][5] + ((number - lowerlim*5)/lowerlim)*ooms[i][1]
            elif number >= lowerlim*5: # 5
                outString += ooms[i][5] # D, L, V
            elif number >= lowerlim*4: #4
                outString += ooms[i][1] + ooms[i][5] # CD, XL, IV
            elif number >= lowerlim: # 1, 2, 3
                outString += ooms[i][1]*(number/lowerlim) # C, CC, CCC
            # Decrement the number for the next loop
            number -= (number/lowerlim)*lowerlim
        # else, decrease the order of magnitude
    return outString

"""
Converts an input number to a roman numeral.
    Input : int number, 0 <= number <= 9999
    Output: string, number represented as a roman numeral

NOTE - This function is NOT used. This represents the expanded version of the
smaller and more efficient OOMR function.
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
            if inNum > 9999 or inNum < 1:
                print "Number out of range. Only enter 1 <= numbers <= 9999\n"
            else:
                return inNum # The only case where we return
        except Exception as e:  # If the input can't be converted
            # The user might want to exit the application
            if inputString.lower() == "exit":
                sys.exit()
            # If they don't want to exit, then their input is invalid
            print inputString, "is an invalid Input"
