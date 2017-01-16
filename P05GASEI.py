def stopByLines(x,k):
    if(k==0):
        return False

    maxdiff=0
    tmpdiff=0
    EPSILON=0.001

    for i in range(1,len(x),1):
        tmpdiff = abs(x[i]) - abs(x[i-1])
        if(tmpdiff > maxdiff):
            maxdiff = tmpdiff

    return (maxdiff < EPSILON)

def norm(x):
    s=0;
    l=len(x)

    for i in range(l):
        s += x[i]**2

    return math.sqrt(s)


def GS(A,b):
    rows    = len(A[0])
    lines   = len(A)
    xs      = [0 for i in range(lines)]
    k=0

    while not stopByLines(xs,k):

        k = k + 1

        for i in range(lines):
            summ=0
            for j in range(rows):
                if not i==j:
                    summ = summ - (A[i][j]*xs[j])

            xs[i] = ((b[i] + summ) * (1/float(A[i][i])))

    return xs


A = [[1,-1,2], [-1,5,-4],[2,-4,6]]
b = [0,1,0]

x = GS(A, b)

print("Solution for x is: ", x)

"""
    x1 = -0.5
    x2 = 0.5
    x3 = 0.5
"""