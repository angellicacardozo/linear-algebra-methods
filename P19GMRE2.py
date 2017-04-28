import math

# Multiplica matriz com vetor
def multiply(A, x):
	m=len(A)
	n=len(x)

	y=[0 for i in range(m)]

	for i in range(m):
		for j in range(n):
			y[i] += A[i][j]*x[j]

	return y

# Subtrai dois vetores
def subtract(x, y):
	n=len(y)
	z=[0 for i in range(n)]

	for i in range(n):
		z[i]= x[i] - y[i]

	return z

# Calcula a norma
def norm(r):
	summ = 0;

	for i in range(len(r)):
		summ += r[i]**2

	summ = math.sqrt(summ)

	if(summ < 0.01):
		return 0

	return summ	

# Multiplica um escalar por um vetor
def scalarTimesVector(s, v):
	l=len(v)
	x=[1 for i in range(l)]

	for i in range(l):
		x[i]=s*v[i]

	return x

def innerProduct(u,v):
	l=len(u)
	p=0
	for i in range(l):
		p += u[i]*v[i]

	return p

def GMRES(A, b):

	maxIter = 5
	convergenceCount = 0

	EPSILON = 0.0001

	x = [0 for i in range(len(A[0]))]
	v = [0 for i in range(maxIter + 1)]
	h = [[0 for j in range(maxIter)] for i in range(maxIter + 1)]

	coss = [0 for i in range(maxIter - 1)]
	sine = [0 for i in range(maxIter - 1)]
	p 	 = [0 for i in range(maxIter)]

	while convergenceCount <= maxIter: # Limita as iteracoes do metodo para convergencia

		r = subtract(b, multiply(A,x))
		beta = norm(r) # Em matematica usamos as denominacoes gregas para as variaveis, poderia ser qualquer outra coisa
		v[0] = scalarTimesVector(1/float(beta), r)
		p[0] = beta

		for j in range(maxIter): # Iteracao dos passos do GMRES, limitada ao maximo de interacoes

			print("Roda a iteracao do GMRES")

			w = multiply(A, v[j]) # Aqui nao ha precondicionamento

			for i in range(j + 1): # Fazemos o Gramm-Schmidt, um pouco diferente do que eu aprendi na outra vez
				print("Realizando Gramm-Schmidt")
				h[i][j] = innerProduct(w, v[i])
				w = subtract(w, scalarTimesVector(h[i][j], v[i])) # Lembrando que w e um vetor

			h[j + 1][j] = norm(w)
			if not abs(h[j+1][j])<EPSILON: # verificamos se nossa matrix ficou pronta
				v[j + 1] = scalarTimesVector(1/float(h[j + 1][j]), w) # Aqui montamos o subespaco de Krylov

			# Teoricamente daqui para baixo esta fora do FOR

			# Aqui vem um ponto interessante, na implementacao original do QR com Givens, nao e necessario acumular seno e cosseno, aqui e necessario
			for i in range(j - 1): # Rotacao de Givens na matrix H
				print("Realizando rotacao de Givens")
				h[i][j] = coss[i]*h[i][j] + sine[i]*h[i + 1][j]
				h[i + 1][j] = (-1)*(sine[i]*h[i][j]) + (coss[i]*h[i + 1][j])

			# Aqui acumulamos os senos e cossenos
			rot = math.sqrt(h[j][j]**2 + h[j+1][j]**2)
			coss[j] = h[j][j]/float(rot)
			sine[j] = h[j + 1][j]/float(rot)

			print("Calculando os angulos coss[" + str(j) + "] = " + str(coss[j]) + " e sine["+ str(j) + "] = " + str(sine[j]))

			# Rotacao de Givens em H
			h[j][j] = rot
			h[j + 1][j] = 0

			# Rotacao de Givens em p
			p[j] = coss[j]*p[j]
			p[j + 1] = (-1)*(sine[j]*p[j])

			print("Calcula p[" + str(j + 1) + "]", p[j + 1])

			if abs(p[j + 1]) < EPSILON:
				break;

		print("Matriz H")
		print(h)

		if abs(p[j + 1]) < EPSILON:
			convergenceCount = maxIter + 1
		else:
			convergenceCount = convergenceCount + 1

	#print("H", h)

A = [[3,2,4],[1,1,2],[4,3,2]]
b = [1,2,3]

GMRES(A, b)