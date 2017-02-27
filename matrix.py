import math


def print_matrix( matrix ):
    s = ""
    for c in range(len(matrix)):
        for r in range(len(matrix[0])):
            s+=str(matrix[c][r]) + " "
        s+="\n"
    return s

def ident( matrix ):
    cols = len(matrix)
    rows = len(matrix[0])
    if cols != rows:
        return "unable to create an identity matrix, please check size"
    m = new_matrix()
    for c in range (cols):
        for r in range (rows):
            if c == r:
                m[c][r] = 1
            else:
                m[c][r] = 0
    return m

def scalar_mult( matrix, s ):
    cols = len(matrix)
    rows = len(matrix[0])
    for c in range( cols ):
        for r in range (rows):
            matrix[c][r] = s * matrix[c][r]
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = new_matrix(len(m1),len(m2[0]))
    row = 0
    col = 0
    for c in range(len(m)):
        for r in range(len(m[0])):
            m[c][r] = sumOf(m1,m2,c,r)
    return m

def sumOf(m1, m2, col, row):
    num = 0;
    for c in range(len(m1)):
        for r in range(len(m2[row])):
            num+=m1[
    

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

print print_matrix(new_matrix())
print print_matrix(ident(new_matrix()))
print print_matrix(scalar_mult(ident(new_matrix()), 5))
