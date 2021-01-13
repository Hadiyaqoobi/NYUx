import math
dollars=0
print("Please enter the number of coins:")
print("# of quarters:")
quarters = int(input())
cents = quarters * 25
print("# of dimes:")
dimes = int(input())
cents += (dimes * 10)

print("# of nickels:")
nickels = int(input())
cents += (nickels*5)
print("# of pennies:")
pennies = int(input())
cents += pennies 
dollars = cents // 100
cents = cents % 100
print("The total is ", dollars, " dollars and ",cents," cents", sep="")
