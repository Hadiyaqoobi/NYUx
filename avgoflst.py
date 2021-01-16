"""
Implement function avg_val(lst), which returns the average
value of the elements in list.
For example, given a list lst: [19, 2, 20, 1, 0, 18], the function
should return 10.


The name of the method should be avg_val and the method should take one parameter which is the list of values to test.  Here is an example call to the function

print(avg_val([19, 2, 20, 1, 0, 18]))

File Name 





"""

def avg_val(lst):
    x: int
    z = y = 0
    ret = 0
    for x in lst:
        z += x
        y = y + 1

    ret = (z / y)
    return ret


#print(avg_val([19, 2, 20, 1, 0, 18]))

