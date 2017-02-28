import math
import random


def print_matrix( matrix ):
    if not(any(isinstance(e, list) for e in matrix)):
        return matrix
    s = ""
    for c in range(len(matrix)):
        for r in range(len(matrix[0])):
            s+=str(matrix[c][r]) + "\t"
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
    if (len(m1[0])!=len(m2)):
        return "Matrixes cannot be multiplied. Please check dimensions"
    m = new_matrix(len(m1),len(m2[0]))
    row = 0
    col = 0
    for r in range(len(m)):
        for c in range(len(m[0])):
            m[r][c] = sumOf(m1,m2,c,r)
    return m

#helper to calculate the multiplaction of col-th col of m2 and row-th row of m1
def sumOf(m1, m2, col, row):
    num = 0
    mcol = []
    for i in m2:
        mcol.append(i[col])
    #print mcol
    index = 0;
    while index < len(mcol) and index < len(m1[row]):
        num+=mcol[index]*m1[row][index]
        index+=1
    return num
    

def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m


#test cases
#print print_matrix(new_matrix())
print "To show creating identity matrix works:"
print print_matrix(ident(new_matrix()))

print "To show scalar multiplication works:"
print "Original:"
t = new_matrix(4,4)
for c in range(len(t)):
    for r in range(len(t[0])):
        t[c][r]= random.randint(0,9)
print print_matrix(t)
rand = random.randint(0, 12)
print "Multiplied by "+str(rand)+" to get:"
print print_matrix(scalar_mult(t,rand))


count = 0
print "To show matrix multiplication works:"
while count < 15:
    print "m1:"
    m1 = new_matrix(4,4)
    for c in range(len(m1)):
        for r in range(len(m1[0])):
            m1[c][r]= random.randint(0,9)
    print print_matrix(m1)
    print "m2:"
    m2 = new_matrix(4,random.randint(1,15))
    for c in range(len(m2)):
        for r in range(len(m2[0])):
            m2[c][r]= random.randint(0,9)
    print print_matrix(m2)
    print "product: m1*m2"
    print print_matrix(matrix_mult(m1,m2))
    count +=1
    if count != 15:
        print "Multiplying matrixes again for good measure"
