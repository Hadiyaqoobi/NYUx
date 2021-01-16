"""
Fibonacci number is a series of numbers in which each number is the sum of the two preceding numbers. The first two numbers in the series are the number 1.  Write a program to print first n Fibonacci Numbers

For example, one execution would look like this:
Please enter a positive integer greater than 1: 4
1
1
2

3

"""

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 0:
        return 0
    # Second Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

print("Please enter a positive integer greater than 1: ")
x = int(input())
for y in range(x+1):
    z=Fibonacci(y)
    if(z>0):
        print(z)