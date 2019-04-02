'''Define a Python function descending(l) that returns True if each element in its input list is at most as big as the one before it. For instance:

  >>> descending([])
  True

  >>> descending([4,4,3])
  True

  >>> descending([19,17,18,7])
  False'''
  # program
  def descending(l):
    x=0
    if len(l)<=1 or (len(l)==2 and l[0]>=l[1]):
        return True
    else:
        if l[0]<=l[1]:
            return descending(l[1:])
        else:
            return False
