'''Write a function nestingdepth(s) that takes as input a string s and computes the maximum nesting depth of brackets if s has properly nested brackets. If the string is not properly matched, your function should return -1.

Hint: Use the function matched() from the practice assignment.

Here are some examples to show how your function should work.

 
>>> nestingdepth("zb%78")
0

>>> nestingdepth("(7)(a")
-1

>>> nestingdepth("a)*(?")
-1

>>> nestingdepth("((jkl)78(A)&l(8(dd(FJI:),):)?)")
4'''
#program
def nestingdepth(s):
    count=0
    maxdepth=0
    for i in s:
        if i=="(":
                 count+=1
                 if count> maxdepth:
                     maxdepth=count
        elif i==")":
            if count>0:
                 count-=1
            else:
                return -1
    if count!=0:
        return -1
    return maxdepth
