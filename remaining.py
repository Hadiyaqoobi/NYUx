"""

Write a function that is given a phrase and returns the phrase we get if we take  
out the first word from the input phrase.
For example, given ‘the quick brown fox’, your function should return ‘quick brown fox’


Here is an example call to the function

print(remainingwords(“the quick brown fox”)):







"""

def remainingwords(data: str) -> str:
    s = data.split()
    ret=" "
    for x in s:
        if x!=s[0]:
          ret +=x + " "

    ret=ret.rstrip()
    ret=ret.lstrip()
    return ret