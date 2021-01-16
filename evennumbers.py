"""

Description

Write a program that reads a positive integer n, and prints the first
n even numbers.

For example, one execution would look like this:
Please enter a positive integer: 3
2
4
6






"""








import math

print("Please enter a positive integer: ")

number = int(input())

for x in range (number + (number+1)):
    y = (x)
    
    if (y % 2 == 0) and x  != 0:
        print(y)
