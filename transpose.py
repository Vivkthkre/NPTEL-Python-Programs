'''
A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

  1  2  3
  4  5  6 
would be represented as [[1, 2, 3], [4, 5, 6]].

The transpose of a matrix makes each row into a column. For instance, the transpose of the matrix above is

  1  4  
  2  5
  3  6
Write a Python function transpose(m) that takes as input a two dimensional matrix using this row-wise representation and returns the transpose of the matrix using the same representation.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

  >>> transpose([[1,4,9]])
  [[1], [4], [9]]

  >>> transpose([[1,3,5],[2,4,6]])
  [[1, 2], [3, 4], [5, 6]]

  >>> transpose([[1,1,1],[2,2,2],[3,3,3]])
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
'''
#program
def transpose(lst):
    return[list(x) for x in zip(*lst)]
