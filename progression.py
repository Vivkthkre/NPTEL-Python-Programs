'''
Define a Python function progression(l) that takes a nonempty list of integers l and returns True if the integers in l form an arithmetic progression: that is, l is of the form [a,a+d,a+2d,…,a+kd].

>>> progression([3])
True

>>> progression([7,3,-1,-5])
True

>>> progression([3,5,7,9,10])
False
''' 
#program
def progression (l):
      if len(l)<=0:
           return False
      if (len(l)== 1): return True
      d=l[1]-l[0]
      for i in range(2,len(l)):
             if l[i]-l[i-1]!=d:
                   return False
