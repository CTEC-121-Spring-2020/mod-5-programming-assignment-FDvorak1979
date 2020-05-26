# Module 4
#   Programming Assignment 5
#       Prob-1.py

# Frank Dvorak

# IPO

# function definition

def romanNumeral(number):
    if number == 1:
        return 'I'
    if number == 2:
        return 'II'
     if number == 3:
        return 'III'
    if number == 4:
        return 'IV'
    if number == 5:
        return 'V'
    else:
        return 'unknown'

# unit test function
def unitTest():
    print("Number :  1 \tRoman Numeral:", romanNumeral(1))
    

def main():
    # replace the code below with your code
    print("Main")    

    # your code here

unitTest()
main()