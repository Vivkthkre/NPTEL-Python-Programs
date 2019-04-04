'''
A list in Python can contain nested lists. The degree of nesting need not be uniform. For instance [1,2,[3,4,[5,6]]] is a valid Python list. Write a Python function flatten(l) that takes a nonempty list of lists and returns a simple list of all the elements in the nested lists, flattened out. You can make use of the following function that returns True if its input is of type list.

def listtype(l):
  return(type(l) == type([]))
Here are some examples to show how flatten(l) should work.

>>> flatten([1,2,[3],[4,[5,6]]])
[1, 2, 3, 4, 5, 6]

>>> flatten([1,2,3,(4,5,6)])
[1, 2, 3, (4, 5, 6)]'''
#program
def flatten(lis):
  new_lis = []
  for item in lis:
      if type(item) == type([]):
          new_lis.extend(flatten(item))
      else:
          new_lis.append(item)
  return new_lis
