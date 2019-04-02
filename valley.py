'''
A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of strictly increasing values. The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing sequence is the first value of the increasing sequence.

Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise.

Here are some examples to show how your function should work.

  >>> valley([3,2,1,2,3])
  True

  >>> valley([3,2,1])
  False

  >>> valley([3,3,2,1,2])
  False
  '''
  #program
  def valley(list):
    if(len(list)==0):
        return(True)
    if(len(list)==1):
        return(False)
    if(list[0]<list[1]):
        return(False)
    for i in range(0,len(list)-1):
        if(list[i]<list[i+1]):
            pos=i
            break
        if(list[i]==list[i+1]):
            return(False)
    else:
        return(False)
    for i in range(pos,len(list)-1):
        if(list[i]>=list[i+1]):
            return(False)
    return(True)   
