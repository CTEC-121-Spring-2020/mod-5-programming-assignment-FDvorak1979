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
    if number == 6:
        return 'VI'
    if number == 7:
        return 'VII'
    if number == 8:
        return 'VIII'
    if number == 9:
        return 'IX'
    if number == 10:
        return 'X'
    else:
        return 'unknown'

# unit test function
def unitTest():
    print("Number :  1 \tRoman Numeral:", romanNumeral(1))
    print("Number :  2 \tRoman Numeral:", romanNumeral(2))
    print("Number :  3 \tRoman Numeral:", romanNumeral(3))
    print("Number :  4 \tRoman Numeral:", romanNumeral(4))
    print("Number :  5 \tRoman Numeral:", romanNumeral(5))
    print("Number :  5 \tRoman Numeral:", romanNumeral(6))
    print("Number :  7 \tRoman Numeral:", romanNumeral(7))
    print("Number :  8 \tRoman Numeral:", romanNumeral(8))
    print("Number :  9 \tRoman Numeral:", romanNumeral(9))
    print("Number :  10 \tRoman Numeral:", romanNumeral(10))

def main():
    # replace the code below with your code
    print("Main")    

    # your code here

unitTest()
main()