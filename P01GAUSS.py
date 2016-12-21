'''
	Gauss function to solve a mxn matrix
	It takes one more step than the original version: https://martin-thoma.com/solving-linear-equations-with-gaussian-elimination/
'''

# returns: A X vector with the solution for the sistem
def Gauss(A):
	
	n = len(A) # Give us total of lines

	# Create an upper triangular matrix
	for i in range(0,n): # for i in [0,1,2,..,n]
		# (1) Find the maximun value in a column in order to change lines
		maxElem = abs(A[i][i])
		maxRow = i
		for k in range(i+1, n): # Interacting over the next line
			if(abs(A[k][i]) > maxElem):
				maxElem = abs(A[k][i]) # Next line on the diagonal
				maxRow = k

		# (2) Swap the rows pivoting the maxRow, i is the current row
		for k in range(i, n+1): # Interacting column by column
			tmp=A[maxRow][k]
			A[maxRow][k]=A[i][k]
			A[i][k]=tmp

		# (3) Subtract lines
		for k in range(i+1,n):
			c = -A[k][i]/float(A[i][i])
			for j in range(i, n+1):
				A[k][j] += c*A[i][j] # Multiply with the pivot line and subtract

		# (4) Make the rows bellow this one zero in the current column
		for k in range(i+1, n):
			A[k][i]=0

	# (5) Solve the equation Ax=b
	x = [0 for i in range(n)] # x <- 0
	for i in range(n-1, -1, -1): # [n-1, n, ..., 1, 0], where n is the total of lines
		x[i] = A[i][n]/A[i][i]
		for k in range(i-1,-1,-1):
			A[k][n] -= A[k][i]*x[i]

	return x

A = [[1,-1,2,0], [-1,5,-4,1],[2,-4,6,0]]

sol = Gauss(A)

print("Solution for x is: ", sol)

"""
	x1 = 0.5
	x2 = 0.5
	x3 = -0.5
"""