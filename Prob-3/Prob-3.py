# Module 4
#   Programming Assignment 5
#       Prob-3.py

# Frank Dvorak

# Paint job cost calculator.  Calcluates how much it would cost for paint and labor needed for a job.

# function definition


# main function definition 
def paintEstimator(sizeSqFeet, costPerGallon):
    # Calculations
    gallons = int(sizeSqFeet / 112 + 1)
    laborHours = (sizeSqFeet / 112) * 8
    costPaint =  gallons * costPerGallon
    totalLabor = laborHours * 35 + 99
    totalJobCost = costPaint + totalLabor

    #Print estimate
    print("Size of Job: ", sizeSqFeet, "suqare feet")
    print("Paint: ", gallons, "gallons at", costPerGallon, "per gallon\t\t\t${0:.2f}".format(costPaint))
    print("Labor: {0:.1f} hours at 35.00 per hours plus $99.00 setup\t${1:.2f}".format(laborHours, totalLabor))
    print("_______________________________________________________________________")
    print("Total:\t\t\t\t\t\t\t${0:.2f}".format(totalJobCost))


    
# main function definition
def main():
    size = eval(input("Enter the size of the job in square feet: "))
    paintCost = eval(input("Enter the cost of paint per gallon: "))
    paintEstimator(size, paintCost)
    
main()
