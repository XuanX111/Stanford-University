# matrix multiplication
# square matrix multiplication
import numpy as np
def square_matrix_mul(A,B):
    n = A.shape
    #print n
    C = np.zeros((n[0], n[1]))
    #print C
    for i in xrange(n[0]):
        for j in xrange(n[1]):
            for k in xrange(n[1]):
                C[i,j] += A[i,k]*B[k,j]
    return C
A = np.matrix([[1,2],[3,4]])
B = np.matrix([[5,6],[7,8]])
print type(A)
c = square_matrix_mul(A,B)
print c

#Strassen's method
def strassen(a, b, c, d, e, f, g, h):
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + g)
    p7 = (a - c) * (e + f)

    c11 = p5 + p6 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    return np.matrix([[c11, c12], [c21, c22]])


def matrix_multiplication_rec(a,b):
    (r, c) = a.shape
    C = np.zeros(r, c)
    if r > 2 and c > 2:

        a = a[:r / 2, :c / 2]
        b = a[:r / 2, c / 2:]
        c = a[r / 2:, :r / 2]
        d = a[r / 2:, c / 2:]

        e = b[:r / 2, :c / 2]
        f = b[:r / 2, c / 2:]
        g = b[r / 2:, :r / 2]
        h = b[r / 2:, c / 2:]

        matrix_multiplication_rec(a,e)
        matrix_multiplication_rec(b,f)
        matrix_multiplication_rec(c,d)
        matrix_multiplication_rec(d,h)

    for i in xrange(r):
        for j in xrange(c):
            C[r,c] = strassen(a,b,c,d,e,f,g,h)
    return C

A = np.matrix([[1,2],[3,4]])
B = np.matrix([[5,6],[7,8]])
c = square_matrix_mul(A,B)
print c



