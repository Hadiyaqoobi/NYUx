"""

Write a program that computes how much a customer has to pay after purchasing
two items. 

The price is calculated according to the following rules:
• Buy one get one half off promotion: the lower price item is half price.
• If the customer is club card member, additional 10% off.
• Tax is added.


Inputs to the program include:
• Two items’ prices
• Have club card or not (User enters ‘Y’ or ‘y’ for “yes”; ‘N’ or ‘n’ for “no”)
• Tax rate (User enters the percentage as a number; for example, they enter
8.25 if the tax rate is 8.25%)


Program displays:
• Base price - the price before the discounts and taxes
• Price after discounts - the price after the buy one get one half off promotion
and the member’s discount, if applicable
• Total price – the amount of money the customer has to pay (after tax)
printed with the precision of 2 decimal digits.


Hint: In order to print a number in a specific precision, you can use the round
function passing 2 arguments to it. Use help(round) to get a brief explanation of
this function, and try playing with it, to better understand what it does.
To format to two decimal places you can use the string format function with the format of 2.2f.

For example, an execution could look like this:

Enter price of the first item: 10
Enter price of the second item: 20
Does customer have a club card? (Y/N): y
Enter tax rate, e.g. 5.5 for 5.5% tax: 8.25
Base price = 30.00
Price after discounts = 22.50
Total price = 24.36





"""





import math

print("Enter price of the first item:")
p1 = float(input())
print("Enter price of the second item:")
p2 = float(input())
base = p1 + p2
print("Does customer have a club card? (Y/N):")
bCard = input()
discount = 0.00
print("Enter tax rate, e.g. 5.5 for 5.5% tax:")
tax = float(input())

if p1 > p2:
    discount += round((p2 / 2), 2)
else:
    discount += round((p1 / 2), 2)
if 'y' == bCard or bCard == 'Y':
    discount += round(((base-discount)* .10) ,2)
price = base - discount
price = round(price, 2)
total = price + (price * (tax/100))
total = round(total, 2)

print("Base price = %2.2f" % base)
print("Price after discounts = %2.2f" % price)
print("Total price = %2.2f" % total)