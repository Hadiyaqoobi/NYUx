#Modify your earlier BMI Metric program to round to two decimal positions and also display the CDC standard weight status categories:

#The CDC standard weight status categories are:




import math

print("Please enter weight in kilograms: ")

k = float (input())

print("Please enter height in meters: ")
h = float(input())
bmi = k / (h * h)

status="Underweight"
if(bmi>30.0):
    status="Obese"
elif(bmi >= 25):
    status="Overweight"
 
elif(bmi>18.5 and bmi <25):
    status="Normal"
print("BMI is: ",round(bmi, 2),"," " Status is ",status,sep="")

