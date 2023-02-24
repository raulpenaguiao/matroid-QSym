import set_compositions
import numpy as np
import sets as SP
import matroids as MT



def matrix_WQSym_coeff(n):
    dict_map = {str(k) : k for k in range(1, n+1)  }
    vecs = [str(k) for k in range(1, n+1)]
    set_comps = list(set_compositions.generate_set_compositions(vecs))
    set_comps.sort(key = set_compositions.alpha)
    set_comps.sort(key = lambda x :  len( set_compositions.alpha(x)))
    x = len(set_comps)
    subs = SP.subsets(vecs)[1:]
    y = len(subs)
    ans = [[0 for j in range(x)] for i in range(y)]
    for (i, opi) in enumerate(set_comps):
        for (j, S) in enumerate(subs):
            if MT.schubert_generic(opi, S, dict_map):
                ans[j][i] = 1
    return [set_comps, ans, subs]



def WQSym_chromatic_function(S):
    dict_map = {str(k) : k for k in range(1, n+1)  }
    vecs = [str(k) for k in range(1, n+1)]
    set_comps = list(set_compositions.generate_set_compositions(vecs))
    set_comps.sort(key = set_compositions.alpha)
    set_comps.sort(key = lambda x :  len( set_compositions.alpha(x)))
    x = len(set_comps)
    subs =  subsets(vecs)
    y = len(subs)
    ans = [[0 for j in range(x)] for i in range(y)]
    for (i, opi) in enumerate(set_comps):
        if MT.schubert_generic(opi, S, dict_map):
            ans[i] = 1
    return [set_comps, ans, subs]



def matrix_QSym_coeff(n):
    [cols, mat, subs] = matrix_WQSym_coeff(n)
    alpha_conv = {}
    comps = []
    for (i, opi) in enumerate(cols):
        alph = tuple(set_compositions.alpha(opi))
        alpha_conv[opi] = alph
        if i == 0 or (i > 0 and not(alph == alpha_conv[cols[i-1]])):
            comps += [alph]
    y = len(mat)
    ans = [{comp:0 for comp in comps} for i in range(y)]
    for (i, opi) in enumerate(cols):
        for j in range(y):
            if mat[j][i] == 1:
                ans[j][alpha_conv[opi]] += 1
    return [ [key for key in comps],   [[line[key] for key in line] for line in ans], subs]


def convert_to_Mathematica_matrix(n, WQSym = True):
    if WQSym:
        [cols, mat, subs] = matrix_WQSym_coeff(n)
    else:
        [cols, mat, subs] = matrix_QSym_coeff(n)
    s = "{"
    for line in mat:
        s += "{"
        for i in line:
            s += str(i) + ", "
        s = s[:len(s)-2]
        s += "}, "
    s = s[:len(s)-2]
    s += "}"
    return [cols, s, subs]



#[cols, s] = convert_to_Mathematica_matrix(6, True)
#print(cols)
#print(s)
def compute_rank(n):#Given n, computes the rank of the non-commutative CSF of matroids
    cols, mat = matrix_WQSym_coeff(n)
    r = np.linalg.matrix_rank(np.array(mat))
    return r

#Takes 1 minute to run
#for i in range(2,8):
#    print("For n = ", i, " rank is = ", compute_rank(i))




"""
RANK and NULLITY of the map to WQSym:
n = 0 | r = 1 | n = 0 | set compositions = 1 
n = 1 | r = 1 | n = 0 | set compositions = 1
n = 2 | r = 2 | n = 1 | set compositions = 3
n = 3 | r = 5 | n = 8 | set compositions = 13
n = 4 | r = 12| n = 63| set compositions = 75
n = 5 | r = 27| n =514| set compositions = 541
n = 6 | r = 58| n = | set composition = 4683 
n = 7 | r =121| n = | set composition = 47293
CONJECTURE
n = 8 | r =248| n = | set compositions = 545835
r = 2**n-n

n = 0 | r = 1 | n = 0 | compositions = 1 
n = 1 | r = 1 | n = 0 | compositions = 1
n = 2 | r = 2 | lin = 0 | compositions = 2
n = 3 | r = 4 | n = 0 | compositions = 4
n = 4 | r = 8 | n = 0 | compositions = 8
n = 5 | r = 16| n = 0 | compositions = 16
n = 6 | r = | n = | compositions = 32

"""



"""
Now we will try to print the rows of the matrix, but only those rows that are not repeated, and with the 1 -> 0 manipulation that we talked on the 28th of Oct
"""


def sub_matrix(lines, cols, i_lines, i_cols, mat):
    m = [[ mat[j][i] for i in cols] for j in lines]
    i_l = [i_lines[i] for i in lines]
    i_c = [i_cols[i] for i in cols]
    return [i_c, m, i_l]



def inv_01(mat):
    return[[ 1 - mat[j][i] for i in range(len(mat[0]))] for j in range(len(mat))]


n = 2
print(" n = ", n, " and the matrix is = ")
s_c, mat, subs = matrix_WQSym_coeff(2)
def pma(sc, s, m):
	print(sc)
	print(s)
	for c in range(len(m)):
		print(m[c])


"""
print(s_c)
print(subs)
for c in range(len(mat)):
    print(mat[c])
"""

"""
lines = [k for k in range(len(subs))]
cols = [k for k in range(len(s_c))]
print(lines)
print(cols)
"""

lines = [0, 1]
cols = [0, 2]

s_c, mat, subs = sub_matrix(lines, cols, subs, s_c, mat)
mat = inv_01(mat)
print(s_c)
print(subs)
for c in range(len(mat)):
    print(mat[c])



n = 3
print(" n = ", n, " and the matrix is = ")
s_c, mat, subs = matrix_WQSym_coeff(n)
"""
print(s_c)
print(subs)
for c in range(len(mat)):
    print(mat[c])
"""

"""
lines = [k for k in range(len(subs))]
cols = [k for k in range(len(s_c))]

print(lines)
print(cols)
"""

lines = [0, 3, 5, 6, 1]
cols = [5, 2, 1, 0, 7]

s_c, mat, subs = sub_matrix(lines, cols, subs, s_c, mat)
mat = inv_01(mat)
print(s_c)
print(subs)
for c in range(len(mat)):
    print(mat[c])



n = 4
print(" n = ", n, " and the matrix is = ")
s_c, mat, subs = matrix_WQSym_coeff(n)
"""
print(s_c)
print(subs)
for c in range(len(mat)):
    print(mat[c])
"""

"""
lines = [k for k in range(len(subs))]
cols = [k for k in range(len(s_c))]

print(lines)
print(cols)
"""


lines = [0, 13, 5, 12, 10, 4, 7, 8, 3, 1, 9, 11]
cols = [19, 20, 21, 18, 17, 8, 48, 6, 5, 10, 11, 51]


s_c, mat, subs = sub_matrix(lines, cols, subs, s_c, mat)
mat = inv_01(mat)
print(s_c)
print(subs)
for c in range(len(mat)):
    print(mat[c])

st = "-"*99
print(st)

s_c, mat, subs = matrix_WQSym_coeff(4)
cols = [i for i in range(len(s_c))]
cols = cols[:-23]
lines = [i for i in range(len(subs))]

def n_of_1s(j):
	return -sum([mat[i][j] for i in range(len(lines))])
def row_sum(i):
	return -sum([mat[i][j] for j in range(len(cols))])
#lines = sorted(lines, key = row_sum)
#cols = sorted(cols, key = n_of_1s)

s_c, mat, subs = sub_matrix(lines, cols, subs, s_c, mat)
mat = inv_01(mat)
print(s_c)
print(subs)
for c in range(len(mat)):
    print(mat[c])

#s_c, mat, subs = matrix_WQSym_coeff(4)
#mat = inv_01(mat)
#pma(s_c, subs, mat)

s_c, mat, subs = matrix_WQSym_coeff(5)
cols = [i for i in range(len(s_c))]
cols = cols[:-119]
lines = [i for i in range(len(subs))]

def n_of_1s(j):
	return -sum([mat[i][j] for i in range(len(lines))])
def row_sum(i):
	return -sum([mat[i][j] for j in range(len(cols))])

cols = sorted(cols, key = n_of_1s)

s_c, mat, subs = sub_matrix(lines, cols, subs, s_c, mat)
mat = inv_01(mat)
print(s_c)
print(subs)
for c in range(len(mat)):
    print(mat[c])


