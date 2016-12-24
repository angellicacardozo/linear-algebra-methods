import math


def diff_absolute(n, a, b):
    ret = 0
    for i in range(0, n):
        ret += (a[i] - b[i])**2
    return math.sqrt(ret)


def absolute(n, a):
    ret = 0
    for i in range(0, n):
        ret += a[i]**2
    return math.sqrt(ret)


def matmul(n, A, x, b):
    for i in range(0, n):
        b[i] = 0
        for j in range(0, n):
            b[i] += A[i*n + j] * x[j]


def vecsub(n, x, y, r):
    for i in range(0, n):
        r[i] = x[i] - y[i]

def vecmul(n, a, b):
    ret = 0
    for i in range(0, n):
        ret += a[i] * b[i]
    return ret


# Solve A*x = b,[k_max: number of iteration]
def gmres(n, A, x0, b, k_max):
    if k_max == 0 or k_max > n:
        k_max = n

    g = [0.0 for i in range(0, k_max+1)]
    c = [0.0 for i in range(0, k_max+1)]
    s = [0.0 for i in range(0, k_max+1)]
    g0 = [0.0 for i in range(0, n)]
    H = [0.0 for i in range(0, (k_max+1) * (k_max+1))]
    V = [0.0 for i in range(0, (k_max+1) * n)]

    e = diff_absolute(n, b, x0)
    if e < 1e-6:
        for i in range(0, n):
            x0[i] = 1

    r = [0.0 for i in range(0, n)]
    matmul(n, A, x0, r)
    vecsub(n, b, r, g0)

    rho = absolute(n, g0)
    g[0] = rho
    for i in range(0, n):
        V[0*n + i] = g0[i] / rho

    for k in range(0, k_max):
        matmul(n, A, V[k*n:(k+1)*n], r)
        for i in range(0, n):
            V[(k+1)*n + i] = r[i]

        for j in range(0, k+1):
            H[k*(k_max+1) + j] = vecmul(n, V[(k+1)*n:(k+2)*n], V[j*n:(j+1)*n])
            for i in range(0, n):
                V[(k+1)*n + i] -=  V[j*n + i]*H[k*(k_max+1) + j]

        H[k*(k_max+1) + k+1] = absolute(n, V[(k+1)*n:(k+2)*n])
        for i in range(0, n):
            V[(k+1)*n + i] = V[(k+1)*n + i] / H[k*(k_max+1) + k+1]

        for i in range(0, k):
            w1 = c[i] * H[k*(k_max+1) + i] - s[i] * H[k*(k_max+1) + i+1]
            w2 = s[i] * H[k*(k_max+1) + i] + c[i] * H[k*(k_max+1) + i+1]
            H[k*(k_max+1) + i] = w1
            H[k*(k_max+1) + i+1] = w2

        nu = math.sqrt(H[k*(k_max+1) + k] * H[k*(k_max+1) + k] + H[k*(k_max+1) + k+1] * H[k*(k_max+1) + k+1])
        c[k] = H[k*(k_max+1) + k]/nu
        s[k] = H[k*(k_max+1) + k+1]/nu
        H[k*(k_max+1) + k] = c[k] * H[k*(k_max+1) + k] - s[k] * H[k*(k_max+1) + k+1]
        H[k*(k_max+1) + k+1] = 0
        w1 = c[k] * g[k] - s[k] * g[k+1]
        w2 = s[k] * g[k] + c[k] * g[k+1]
        g[k] = w1
        g[k+1] = w2
        rho = math.fabs(g[k+1])


    for i in reversed(range(0, k_max)):
        nu = g[i]
        for j in range(i+1, k_max):
            nu -= H[j*(k_max+1) + i] * c[j]
        c[i] = nu/H[i*(k_max+1) + i]

    for i in range(0, n):
        nu = 0
        for j in range(0, k_max):
            nu += V[j*n + i] * c[j]
        x0[i] += nu

    return x0


A = [
        3.0, -1.0, 1.0,
        -1.0, 3.0, 1.0,
        1.0, -1.0, 3.0]
b = [-1.0, 7.0, -7.0]
x0 = [1.0, 1.0, 1.0]

s = gmres(3, A, x0, b, 100)

print("Solution for x is: ", s)


"""
    x1 = 1
    x2 = 2.2
    x3 = -2.2
"""

