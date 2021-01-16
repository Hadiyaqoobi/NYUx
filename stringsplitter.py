"""

Read from the user a string containing 
odd number of characters. Your program should: 
a) Print the middle character. 
b) Print the string up to but not including the middle character (i.e., the first half 
of the string). 
c) Print the string from the middle character to the end (not including the 
middle character). 

Sample output: 
Enter an odd length string: Fortune favors the bold
Middle character: o
First half: Fortune fav
Second half: rs the bold

"""

print("Enter an odd length string: ")
s = input()

size = len(s)
mid = size // 2

print("Middle character: ", s[mid])
print("First half: ", s[0: mid])
print("Second half: ", s[mid+1:size])