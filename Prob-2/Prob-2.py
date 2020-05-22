# Module 4
#   Programming Assignment 5
#       Prob-2.py

# Frank Dvorak

# Change Calculator

# starting point
# Calls up the price of the item(s) and change given

itemCost = float(input("Total: "))
amountTendered = float(input("Tendered: "))

#
changeDue = amountTendered - itemCost


print("Change Back: ", changeDue)

x = float(input("Please enter an amount of cents due: "))
x = float(x)
q = 25
d = 10
n = 5
p = 1

numberQ = x/q
numberQ = int(numberQ)

money2 = x - (numberQ * q)
numberD = money2/d
numberD = int(numberD)

money3 = money2 - (numberD * d)
numberN = money3/n
numberN = int(numberN)

numberP = p
money4 = money3 - (numberP * p)
numberP = money4/p
money4 = x - (numberP * p)
numberP = int(numberP)

print (numberQ, " Quarters")
print (numberD, " Dimes")
print (numberN, " Nickles")
print (numberP, " Pemnies")



# main function definition


