import set_compositions

##CODE CREATED BY RAUL PENAGUIAO
##May 2022


"""
Code created to manipulate matroids and create schubert matroids
"""


"""
PREP
P: vecs is a list of vectors, where the order is very important, S is a sublist of vectors
thatR: returns a set of bases
"""
def schubert_matroid(S, vecs):
    n = len(S)
    basis = []
    for subset in subsets_numb(vecs, n):
        if compare(subset, S):
            basis += [subset]
    return basis

"""
Compares two lists
Assumes that these lists have the same size
assumes that lists are ordered
"""
def compare(A, B):
    for (a, b) in zip(A, B):
        if a > b:
            return False
    return True


def subsets_numb(vecs, k):
    ans = subsets(vecs)
    return [subset for subset in ans if len(subset) == k]


def subsets(vecs):
    it = 0
    pow2 = [1]
    n = len(vecs)
    ans = []
    for i in range(n):
        pow2 += [pow2[-1]*2]
    while it < pow2[-1]:
        A = []
        for i in range(n):
            if (it//pow2[i])%2 == 1:
                A +=[ vecs[i]]
        ans += [A]
        it += 1
    return ans


"""
returns true or false, wether opi is SM(S)-generic or not
opi is a set composition, written of the form "str1,str2|str3,str4|str5"
that is, parts are separated by |, elements are separated by , and elements are strings that do not contain , or |
the parts are assumed to come with the elements ordered in increasing order
S is assumed to come with the elements ordered in increasing order
dict_map is a map that sents each string to the position corresponding to the string
"""
"""
EARLY VERSION
def schubert_generic(opi, S, dict_map):
    parts = opi.split("|")
    T = []
    R = [s for s in S]
    for part in parts:
        R += [t for t in T]
        R.sort(key = lambda x:dict_map[x])
        T = []
        if R == []: #here our set S is empty, so there is nothing else to check. It's better to check out here than latter in the code, 
            ##so we can freely access R[0] 
            return True
        els = part.split(",")
        while els != []:
            if dict_map[R[0]] < dict_map[els[0]]:
                T += R.pop(0)
                if R == []:
                    break
            elif len(els) > 1 and dict_map[els[1]] <= dict_map[R[0]]:
                return False
            else:
                els.pop(0)
                R.pop(0)
                if R == []:
                    break
    return True
"""

def schubert_generic(opi, S, dict_map):
    #print("Computing matroid Delta_", opi, " SM(", S, ")")
    parts = opi.split("|")
    R = [s for s in S] #creates a copy of S that we can manipulate without change the input
    for part in parts:
        #print(" - Computing part = ", part)
        T = unique_matching(R, part.split(","), dict_map)
        #print(" - unique matching? ", T)
        if T == "HALT":#if there is more than one basis
            return False
        #in this case there is a unique basis, so we remove it from R
        #print("R = ", R)
        #print("T = ", T)
        R = [r for r in R if not(r  in T)]
    return True



"""
PREP
P: two lists A, B with ordered elements, it is supposed to represent a bipartite graph between A and B if bj <= ai
R: returns "HALT" if there is more than one maximal matching
   returns the maximal ordered sublist of A that matches uniquely to B
E: 
    A = [1,2] B = [2, 3] returns [1, 2]
    A = [1, 2, 4] B = [3, 4] returns "HALT"
    A = [1, 3, 4] B = [2, 4] returns [3, 4]

"""
def unique_matching(A, B, dict_map):
    #print("Does S = ", A, " and parts = ", B, " have a unique matching?")
    la = len(A)
    lb = len(B)
    ##Find minimal matching
    min_match = [[], []]
    i = 0
    j = 0
    while i < la and j < lb:
        if dict_map[A[i]] >= dict_map[B[j]]:
            min_match[0] += [A[i]]
            min_match[1] += [B[j]]
            j += 1
        i += 1
    ##Find maximal matching
    max_match = [[], []]
    i = la - 1
    j = lb - 1
    while i >= 0 and j >= 0:
        if dict_map[A[i]] >= dict_map[B[j]]:
            max_match[0]+= [A[i]]
            max_match[1]+= [B[j]]
            i -= 1
        j -= 1
    max_match[0].reverse()
    max_match[1].reverse()
    #print(max_match)
    #print(min_match)
    ##Compare matchings
    if max_match[1] == min_match[1]:
        return min_match[0]
    return "HALT"

##print(unique_matching([], []))
## > []
##print(unique_matching([1], [2]))
## > []
##print(unique_matching([2], [1]))
## > [2]
##print(unique_matching([1, 2], [1]))
## > "HALT"
##print(unique_matching([1, 2], [2]))
## > [2]
##print(unique_matching([1, 3, 5], [2, 4]))
## > [3, 5]
##print(unique_matching([2, 4, 6], [1, 2]))
## > "HALT"
##print(unique_matching([2, 4, 6], [1, 2, 6]))
## > [2, 4, 6]


#print(schubert_generic("1,3|2", ["1", "3"], {"1":1, "2":2, "3":3}))
## > True
#print(schubert_generic("1,3|2", ["3"], {"1":1, "2":2, "3":3}))
## > False
#print(schubert_generic("3|1,2", ["2", "3"], {"1":1, "2":2, "3":3}))
## > False
#print(schubert_generic("1,2|3", ["2", "3"], {"1":1, "2":2, "3":3}))
## > True
#print(schubert_generic("2|1,3", ["1", "2", "3"], {"1":1, "2":2, "3":3}))
## > True
#print(schubert_generic("1|2,3", ["1", "3"], {"1":1, "2":2, "3":3}))
## > False
#print(schubert_generic("1|2,3", ["2", "3"], {"1":1, "2":2, "3":3}))
## > False
#print(schubert_generic("2|1,3", ["2", "3"], {"1":1, "2":2, "3":3}))
## > False
#print(schubert_generic("3|1,2", ["2", "3"], {"1":1, "2":2, "3":3}))
## > True


def matrix_WQSym_coeff(n):
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
        for (j, S) in enumerate(subs):
            if schubert_generic(opi, S, dict_map):
                ans[j][i] = 1
    return [set_comps, ans]


def matrix_QSym_coeff(n):
    [cols, mat] = matrix_WQSym_coeff(n)
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
    return [ [key for key in comps],   [[line[key] for key in line] for line in ans]]


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

[cols, s] = convert_to_Mathematica_matrix(5, True)
print(cols)
print(s)


"""
RANK and NULLITY of the map to WQSym:
n = 0 | r = 1 | n = 0 | set compositions = 1 
n = 1 | r = 1 | n = 0 | set compositions = 1
n = 2 | r = 2 | n = 1 | set compositions = 3
n = 3 | r = 5 | n = 8 | set compositions = 13
n = 4 | r = 12| n = 63| set compositions = 75
n = 5 | r = 27| n =514| set compositions = 541

n = 0 | r = 1 | n = 0 | compositions = 1 
n = 1 | r = 1 | n = 0 | compositions = 1
n = 2 | r = 2 | n = 0 | compositions = 2
n = 3 | r = 4 | n = 0 | compositions = 4
n = 4 | r = 8 | n = 0 | compositions = 8
n = 5 | r = 16| n = 0 | compositions = 16
n = 6 | r = | n = | compositions = 32

"""


