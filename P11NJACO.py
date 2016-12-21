from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot
def JCB(A,b,N=25,x=None):
                                                                                   
	if x is None:
		x = zeros(len(A[0]))
                                                                                               
	D = diag(A)
	R = A - diagflat(D)
                                                                                                                        
	for i in range(N):
		x = (b - dot(R,x))/D

	pprint(x)
	return x

A = [[3,-1,1], [-1,3,-1],[1,-1,3]]
b = [-1,7,-7]
s = JCB(A,b,100)

print("Solution for x is: ", s)

"""
    x1 = 1
    x2 = 2.2
    x3 = -2.2
"""