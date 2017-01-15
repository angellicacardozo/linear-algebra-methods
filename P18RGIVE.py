import math

def Givens(A):

	rows = len(A)
	

	for i in range(rows -1):
		r = math.sqrt(A[i][i]**2 + A[i+1][1]**2)

		cos = (1/float(r))*A[i][i]
		sine = (1/float(r))*A[i+1][i]

		A[i][i] = r
		A[i + 1][i] = 0

	return A

A = [[3,2,4],[1,1,2],[4,3,2]]

print(Givens(A))