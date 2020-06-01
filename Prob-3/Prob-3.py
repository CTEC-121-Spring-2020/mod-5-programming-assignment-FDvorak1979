# Module 4
#   Programming Assignment 5
#       Prob-3.py

# Frank Dvorak

# Paint job cost calculator.  Calcluates how much it would cost for paint and labor needed for a job.

# function definition


# main function definition 

def main():
    hightOfwall = (input("High of wall in feet: "))
    widthOfwall = (input("Width of wall in feet: "))
    areatobepainted = hightOfwall * widthOfwall
    gallonsofpaintneeded = areatobepainted / 112
    hoursoflabor = gallonsofpaintneeded * 8
    laborcost = hoursoflabor * 50.00
    costofpaint = gallonsofpaintneeded * 9.84
    setupfee = 99.0
    totalcost = costofpaint + stupfee + laborcost


    paint("Gallons of paint needed is: ", gallonsofpaint)
    print("Hours of labor needed is: ", hoursoflabor)
    print("Cost of paint is: ")
    print("Cost of labor is: ", laborcost, " @ $50.00 /hr with", hoursoflabor, " needed")
    print("One time setup fee is: ", setupfee)
    print('')
    print("Total Cost is: ", totalcost)
   
# Call the main function.
main()
