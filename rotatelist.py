'''A list rotation consists of taking the first element and moving it to the end. For instance, if we rotate the list [1,2,3,4,5], we get [2,3,4,5,1]. If we rotate it again, we get [3,4,5,1,2].

Write a Python function rotatelist(l,k) that takes a list l and a positive integer k and returns the list l after k rotations. If k is not positive, your function should return l unchanged. Note that your function should not change l itself, and should return the rotated list.

Here are some examples to show how your function should work.

>>> rotatelist([1,2,3,4,5],1)
[2, 3, 4, 5, 1]

>>> rotatelist([1,2,3,4,5],3)
[4, 5, 1, 2, 3]

>>> rotatelist([1,2,3,4,5],12)
[3, 4, 5, 1, 2]'''
#program
def rotatelist(l,k):
    if k<0:
        return l
    else:
        return l[k%len(l):]+l[:k%len(l)]
