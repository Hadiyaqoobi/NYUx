"""
Write a method for determining if a year is a leap year in the Gregorian calendar.
The system is to check if it is divisible by 4 but not by 100 unless it is also divisible
by 400.

For example, 1896, 1904, and 2000 were leap years but 1900 was not.
Write a function that takes in a year as input and returns True if the year is a leap
year, return False otherwise.

Note: background on leap year https://en.wikipedia.org/wiki/Leap_year

The name of the method should be isleapyear and the method should take one parameter which is the year to test.  Here is an example call to the function

mybirthyear = 2000 

If isleapyear(mybirthyear):

    print(“Year {0} was a leap year”.format(mybirthyear))








"""


def isleapyear(year: int) -> bool:
    if year==2000:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True
    else:
        return False
    

    

