'''
Write a Python function squareprime(l) that takes a nonempty list of integers and returns True if the elements of l alternate between perfect squares and prime numbers, and returns False otherwise. Note that the alternating sequence of squares and primes may begin with a square or with a prime.

Here are some examples to show how your function should work.

>>> primesquare([4])
True

>>> primesquare([4,5,16,101,64])
True

>>> primesquare([5,16,101,36,27])
False
'''
#program
from math import sqrt
def square(n):
    if(sqrt(n) % 1 == 0):
        return True
    else:
        return False
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def primesquare(list_nums):
   if len(list_nums) == 0:
       return False
   if len(list_nums) == 1:
       if (square(list_nums[0]) or isprime(list_nums[0])):
           return True
       else:
           return False
   else:
       flag = True
       if square(list_nums[0]):
           check_for = 'prime'
       elif isprime(list_nums[0]):
           check_for = 'square'
       else:
           return False
       for i in range(1,len(list_nums)):
           if (check_for == 'prime' and isprime(list_nums[i])):
               check_for = 'square'
           elif (check_for == 'square' and square(list_nums[i])):
               check_for = 'prime'
           else:
               flag = False
               break     
       if flag:
           return True
       else:
           return False
