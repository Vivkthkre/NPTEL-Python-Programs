'''
Let us consider polynomials in a single variable x with integer coefficients: for instance, 3x4 - 17x2 - 3x + 5. Each term of the polynomial can be represented as a pair of integers (coefficient,exponent). The polynomial itself is then a list of such pairs.

We have the following constraints to guarantee that each polynomial has a unique representation:

Terms are sorted in descending order of exponent
No term has a zero cofficient
No two terms have the same exponent
Exponents are always nonnegative
For example, the polynomial introduced earlier is represented as

  [(3,4),(-17,2),(-3,1),(5,0)]
The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.

Write Python functions for the following operations:

  
  addpoly(p1,p2)
  multpoly(p1,p2)
that add and multiply two polynomials, respectively.

You may assume that the inputs to these functions follow the representation given above. Correspondingly, the outputs from these functions should also obey the same constraints.

Hint: You are not restricted to writing just the two functions asked for. You can write auxiliary functions to "clean up" polynomials – e.g., remove zero coefficient terms, combine like terms, sort by exponent etc. Build a library of functions that can be combined to achieve the desired format.

You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation, and then convert back.

Some examples:

  >>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
  [(2, 1),(3, 0)]
Explanation: (4x3 + 3) + (-4x3 + 2x) = 2x + 3

  >>> addpoly([(2,1)],[(-2,1)])
  []
Explanation: 2x + (-2x) = 0

  >>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
  [(1, 3),(-1, 0)]
Explanation: (x - 1) * (x2 + x + 1) = x3 - 1'''
#program
def addpoly(p1,p2):
	i=0
	su=0
	j=0
	c=[]
	if len(p1)==0:
		#if p1 empty
		return p2
	if len(p2)==0:
		#if p2 is empty
		return p1
	while i<len(p1) and j<len(p2):
		if int(p1[i][1])==int(p2[j][1]):
			su=p1[i][0]+p2[j][0]
			if su !=0:
				c.append((su,p1[i][1]))
			i=i+1
			j=j+1
		elif p1[i][1]>p2[j][1]:
			c.append((p1[i]))
			i=i+1
		elif p1[i][1]<p2[j][1]:
			c.append((p2[j]))
			j=j+1
	if p1[i:]!=[]:
		for k in p1[i:]:
			c.append(k)
	if p2[j:]!=[]:
		for k in p2[j:]:
			c.append(k)
	return c
def multpoly(p1,p2):
	p=[]
	s=0
	for i in p1:
		c=[]
		for j in p2:
			s=i[0]*j[0]
			e=i[1]+j[1]
			c.append((s,e))
		p=addpoly(c,p)
	return p
