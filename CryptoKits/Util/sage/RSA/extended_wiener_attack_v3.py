from sage.all import *

def _attack(e1, e2, e3, n):
    a = 2/5
    D = diagonal_matrix(ZZ,[int(n^1.5), n, int(n^(a+1.5)), int(n^0.5), int(n^(a+1.5)), int(n^(a+1)), int(n^(a+1)), 1])
    L = Matrix(ZZ,[[1, -n,   0,   n^2,   0,      0,      0,     -n^3],
                [0, e1, -e1, -n*e1, -e1,      0,   n*e1,   n^2*e1],
                [0,  0,  e2, -n*e2,   0,   n*e2,      0,   n^2*e2],
                [0,  0,   0, e1*e2,   0, -e1*e2, -e1*e2, -n*e1*e2],
                [0,  0,   0,     0,  e3,  -n*e3,  -n*e3,   n^2*e3],
                [0,  0,   0,     0,   0,  e1*e3,      0, -n*e1*e3],
                [0,  0,   0,     0,   0,      0,  e2*e3, -n*e2*e3],
                [0,  0,   0,     0,   0,      0,      0, e1*e2*e3]]) * D
    Ge = L.LLL()[0]
    x = vector(ZZ, Ge) / L
    phi = int(x[1]/x[0]*e1)
    return phi