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
    subs = SP.subsets(vecs)
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
        [cols, mat] = matrix_WQSym_coeff(n)
    else:
        [cols, mat] = matrix_QSym_coeff(n)
    s = "{"
    for line in mat:
        s += "{"
        for i in line:
            s += str(i) + ", "
        s = s[:len(s)-2]
        s += "}, "
    s = s[:len(s)-2]
    s += "}"
    return [cols, s]


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
n = 2 | r = 2 | n = 0 | compositions = 2
n = 3 | r = 4 | n = 0 | compositions = 4
n = 4 | r = 8 | n = 0 | compositions = 8
n = 5 | r = 16| n = 0 | compositions = 16
n = 6 | r = | n = | compositions = 32

"""



"""
Now we will try to print the rows of the matrix, but only those rows that are not repeated, and with the 1 -> 0 manipulation that we talked on the 28th of Oct

"""

n = 3
s_c, mat, sets = matrix_WQSym_coeff(n)

def row_red(mat):
    l = len(mat)
    c = len(mat[1])
    return [mat[1]] + [[mat[1][i] - mat[j][i] for i in range(c)] for j in range(1, l)]

def matrix_permutation(mat, lis_row, lis_col):
    return [ [ mat[i][j] for j in lis_col] for i in lis_row]

mat = row_red(mat)
columns = [7, 5, 6, 4, 0]
rows = [0, 4, 5, 2, 6]
s_c = [s_c[i] for i in columns]
sets = [sets[i] for i in rows]
mat = matrix_permutation(mat, rows, columns)
print(sets)
print(s_c)
for c in range(len(mat)):
    print(mat[c])

n = 4
s_c, mat, sets = matrix_WQSym_coeff(n)
mat = row_red(mat)
columns = [51, 46, 47, 42, 43, 37, 38, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 39, 40, 41, 44, 45, 48, 49, 50, 51]
rows = [0, 8, 9, 4, 5, 12, 13, 6, 10, 11, 14]
mat = matrix_permutation(mat, rows, columns)


print(sets)
print(s_c)
for c in range(len(mat)):
    print(mat[c])


