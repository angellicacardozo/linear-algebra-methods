import math

def multiply(A, B):

	# Where A*B

	result = [] # final result
	for i in range(len(A)):

		row = [] # the new row in new matrix
		for j in range(len(B[0])):

			product = 0 # the new element in the new row
			for v in range(len(A[i])):
				product += A[i][v] * B[v][j]
			
			row.append(product) # append sum of product into the new row

		result.append(row) # append the new row into the final result

	return result


def transpose(A):
	B = []
	l = len(A)
	c = len(A[0])

	if(c==1):
		# A is a vector
		for i in range(c):
			B.append([])
			for j in range(l):
				B[i].append(A[j])
	else:
		for i in range(c):
			B.append([])
			for j in range(l):
				B[i].append(A[j][i])

	return B


def GivensQR(A):

	cols = len(A[0])
	rows = len(A)

	count = 0

	accG = []

	while count < cols:

		for i in range(cols - 1, count - 1, -1):

			# Montar a Matriz G, G e quadrada, mesmo num. de linhas de A
			G = [[ 0 for j in range(rows)] for k in range(rows)]
			for j in range(rows):
				G[j][j] = 1

			# Calcular a rotacao e os angulos
			line = i + 1
			r = math.sqrt(A[i][count]**2 + A[line][count]**2)
			cos = A[i][count] * (1/float(r))
			sine = A[line][count] * (1/float(r))

			# Preencher as linhas com cos e sen
			G[i][i] = cos
			G[i][i + 1] = sine

			G[i + 1][i] = -1*(sine)
			G[i + 1][i + 1] = cos

			# Recalcular A : Gi,i+1 * A
			A = multiply(G,A)

			# Zera o indice em A
			A[line][count] = 0.

			# Acumula G
			accG.append(G)

		count = count + 1

	R = A

	# Calcular o fator Q

	inter = len(accG)
	acc = []

	for i in range(inter - 1, -1, -1):

		if not len(acc) > 0:
			# Primeira rodada
			acc = transpose(accG[i])
		else:
			acc = multiply(accG[i], acc)

	Q = acc

	return (Q,R)

# A = [[3,2,4],[1,1,2],[4,3,2]]
A = [[1, -1, 4], [1, 4, -2], [1, 4, 2], [1, -1, 0]]

print(GivensQR(A))