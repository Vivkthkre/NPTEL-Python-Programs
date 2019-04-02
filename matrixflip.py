'''
A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

1  2  3
4  5  6 
7  8  9
would be represented as [[1, 2, 3], [4, 5, 6], [7, 8, 9]].

A horizonatal flip reflects each row. For instance, if we flip the previous matrix horizontally, we get

3  2  1
6  5  4 
9  8  7
which would be represented as [[3, 2, 1], [6, 5, 4], [9, 8, 7]].

A vertical flip reflects each column. For instance, if we flip the previous matrix that has already been flipped horizontally, we get

9  8  7
6  5  4 
3  2  1
which would be represented as [[9, 8, 7], [6, 5, 4], [3, 2, 1]].

Write a Python function matrixflip(m,d) that takes as input a two dimensional matrix m and a direction d, where d is either 'h' or 'v'. If d == 'h', the function should return the matrix flipped horizontally. If d == 'v', the function should retun the matrix flipped vertically. For any other value of d, the function should return m unchanged. In all cases, the argument m should remain undisturbed by the function.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

>>> myl = [[1,2],[3,4]]

>>> myl
[[1, 2], [3, 4]]  

>>> matrixflip(myl,'h')
[[2, 1], [4, 3]]

>>> myl
[[1, 2], [3, 4]]  

>>> matrixflip(myl,'v')
[[3, 4], [1, 2]]  

>>> myl
[[1, 2], [3, 4]]  '''
#program
def matrixflip(a,b):
    temp=[]
    for i in range(len(a)):
        temp=temp+[a[i][:]]
    if b=='h':
        for i in range(len(temp)):
            temp[i].reverse()
            i=i+1
        return temp
    elif b=='v':
      temp.reverse()
      return(temp) 
