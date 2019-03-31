'''Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.

>>> sumprimes([3,3,1,13])
19

>>> sumprimes([2,4,6,9,11])
13

>>> sumprimes([-3,1,6])
0'''
#program
def sumprimes(l):
    sum=0
    for i in l:
        if i>1:
            prime=True
            for j in range(2,i):
                if(i%j==0):
                    prime=False
            if prime:
                sum=sum+i
    return sum
