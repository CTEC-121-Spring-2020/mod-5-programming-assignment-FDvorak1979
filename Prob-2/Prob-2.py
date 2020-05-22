# Module 4
#   Programming Assignment 5
#       Prob-2.py

# Frank Dvorak

# Change Calculator

# starting point
# Calls up the price of the item(s) and change given

itemCost = float(input("Total: "))
amountTendered = float(input("Tendered: "))

# Calculates who much the customer gets back
changeDue = amountTendered - itemCost

# Prints total change due
print("Change Back: ", changeDue)

# Calls up denomination devision using cents as int
x = float(input("Please enter an amount of cents due as whole number: "))
x = float(x)
q = 25
d = 10
n = 5
p = 1

# Calculates cents back
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

#Prints out what change is needed

print (numberQ, " Quarters")
print (numberD, " Dimes")
print (numberN, " Nickles")
print (numberP, " Pemnies")



# main function definition


