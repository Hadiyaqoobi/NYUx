"""
Implement function max_abs_val(lst), which returns the maximum absolute
value of the elements in list.
For example, given a list lst: [-19, -3, 20, -1, 0, -25], the function
should return 25.


The name of the method should be max_abs_val and the method should take one parameter which is the list of values to test.  Here is an example call to the function

print(max_abs_val([-19, -3, 20, -1, 0, -25]))







"""


import math


def max_abs_val(lst):
    z = abs(lst[0])
    x: int
    for x in lst:
        if abs(x) > z:
            z = abs(x)
    return z

#print(max_abs_val([-19, -3, 20, -1, 0, -25]))


