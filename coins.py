#Description

#Write a program that asks the user to enter an amount of money in the format of dollars and remaining cents.  The program should calculate and print the minimum number of coins (quarters, dimes, nickels and pennies) that are equivalent to the given amount.

#Hint: In order to find the minimum number of coins, first find the maximum number of quarters that fit in the given amount of money, then find the maximum number of dimes that fit in the remaining amount, and so on.


#File Name 

#coins.py




#For example,  an  execution should look  like  this:
#Please enter the amount of money to convert:

# of dollars: 2
# of cents: 37
#The coins are 9 quarters, 1 dimes, 0 nickels and 2 pennies

import math

print("Please enter the amount of money to convert: ")

print("# of dollars: ")

dollars = int(input())

print("# of cents:")

cents = int(input())

total = (100*dollars) + cents
q = total // 25
total = total - (q*25)
d = total // 10
total = total - (d*10)
n = total // 5
total = total - (n*5)
p = total

dollars = cents // 100
cents = cents % 100
print("The coins are ", q, " quarters, ", d, " dimes, ", n, " nickels and ", p, " pennies", sep="")


