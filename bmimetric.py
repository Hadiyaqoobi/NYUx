

#Body mass index (BMI) is a number calculated from  a person’s weight and height.
#According to the Centers for Disease Control and Prevention, the BMI is a fairly
#reliable indicator of body fatness for most people. BMI does not measure body fat
#directly, but research has shown that  BMI correlates to direct  measures  of  body  fat,  
#such  as  underwater  weighing  and dual-energy X-ray absorptiometry. The formula 
#for BMI is
    #Weight/Height2

#Where    weight is in kilograms    and height is in meters.


#Write a program that prompts for metric weight and height and outputs the BMI.


#For example, an execution could look  like  this:
#Please enter weight in kilograms: 50
#Please enter height in meters: 1.58
#BMI is: 20.0288415318


import math

print("Please enter weight in kilograms: ")

k = float (input())

print("Please enter height in meters: ")
h = float(input())
bmi = k / (h * h)

print("BMI is: ", bmi, sep="")