def height(m):
  return len(m)

def JCB(m, x0=None, eps=1e-5, max_iteration=100):
	n  = height(m)
	x0 = [0] * n if x0 == None else x0
	x1 = [None] * n
  
	for __ in range(max_iteration):
		for i in range(n):
			s = sum(-m[i][j] * x0[j] for j in range(n) if i != j)
			x1[i] = (m[i][n] + s) / float(m[i][i])
		if all(abs(x1[i]-x0[i]) < eps for i in range(n)):
			return x1 
		x0, x1 = x1, x0
	raise ValueError('Nao converge :( ')


A = [[3,-1,1,-1], [-1,3,-1,7],[1,-1,3,-7]]
s = JCB(A)

"""
    x1 = 1
    x2 = 2.2
    x3 = -2.2
"""

"""
A = [[4,3.2,0.5,9.2],[2.2,3,-0.3,0.9],[-3.1,-0.2,4,7]]
s = JCB(A)
"""
"""
A = A = [[1,-1,2,0], [-1,5,-4,1],[2,-4,6,0]]
s = JCB(A)
"""

print("Solution for x is: ", s)

