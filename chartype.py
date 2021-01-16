"""


Write a program that  reads a character (string of  length  1)  from  the 
user, and classifies it to  one of the following: lower case letter, upper case letter, 
digit,  or non-alphanumeric character 

Sample  output (4 different executions):  
Enter a character: j
j is  a lower case  letter.
Enter a character: 7
7 is  a digit.
Enter a character: ^
^ is  a non-alphanumeric  character.
Enter a character: C
C is  an  upper case  letter.


"""

print("Enter a character: ")
s = input()
result = "a digit."
if s.isalpha():
    if s.isupper():
        result= "an upper case  letter."
    else:
        result="a lower case  letter."
elif s.isdigit()== False:
    result="a non-alphanumeric  character."
print(s, " is ", result, sep="")