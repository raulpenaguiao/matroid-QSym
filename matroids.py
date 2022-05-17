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
PREP
P: two lists A, B with ordered elements, it is supposed to represent a bipartite graph between A and B if bj <= ai
R: returns "HALT" if there is more than one maximal matching
   returns the maximal ordered sublist of A that matches uniquely to B
E: 
    A = [1,2] B = [2, 3] returns [1, 2]
    A = [1, 2, 4] B = [3, 4] returns "HALT"
    A = [1, 3, 4] B = [2, 4] returns [3, 4]


def matching(A, B):





##print(schubert_generic("1,3|2", ["1", "3"], {"1":1, "2":2, "3":3}))
## > True
##print(schubert_generic("1,3|2", ["3"], {"1":1, "2":2, "3":3}))
## > False
##print(schubert_generic("3|1,2", ["2", "3"], {"1":1, "2":2, "3":3}))
## > False
print(schubert_generic("1,2|3", ["2", "3"], {"1":1, "2":2, "3":3}))
## > True
#print(schubert_generic("2|1,3", ["1", "2", "3"], {"1":1, "2":2, "3":3}))
## > True


"""
There is a major problem that is not taken care of, but needs a bit of theory behind
this will be discussed with Federico:
    Big question. Let A={a1 < ...< ar} and B = {b1 < ... < bq}
    Draw an edge between ai and bj if bj <= ai
    Find maximal matching, is it unique?
    This is the question that we are trying to ask

"""


def matrix_WQSym_coeff(n):
    dict_map = {str(k) : k for k in range(1, n+1)  }
    vecs = [str(k) for k in range(1, n+1)]
    set_comps = list(set_compositions.generate_set_compositions(vecs))
    set_comps.sort(key = set_compositions.alpha)
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
    comps = set(())
    for opi in cols:
        alph = tuple(set_compositions.alpha(opi))
        alpha_conv[opi] = alph
        comps.add(alph)
    y = len(mat)
    ans = [{comp:0 for comp in comps} for i in range(y)]
    for (i, opi) in enumerate(cols):
        for j in range(y):
            if mat[j][i] == 1:
                ans[j][alpha_conv[opi]] += 1
    return [ [key for key in comps],   [[line[key] for key in line] for line in ans]]

[cols, mat] = matrix_QSym_coeff(3)
print(cols)
for line in mat:
    print(line)
