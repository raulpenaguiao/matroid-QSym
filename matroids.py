import set_compositions
import numpy as np
import sets as SP


##CODE CREATED BY RAUL PENAGUIAO
##May 2022


"""
Code created to manipulate matroids and create schubert matroids
"""


"""
PREP
P: vecs is a list of vectors, where the order is very important, S is a sublist of vectors
that
R: returns a set of bases
"""
def schubert_matroid(S, vecs):
    n = len(S)
    basis = []
    for subset in SP.subsets_numb(vecs, n):
        if SP.compare(S, subset):
            basis += [subset]
    return basis


def schubert_generic(opi, S, dict_map):
    #opi = opi_r[::-1]
    parts = opi.split("|")
    parts.reverse()
    R = [s for s in S] #creates a copy of S that we can manipulate without change the input
    for part in parts:
        T = unique_matching(R, part.split(","), dict_map)
        if T == "HALT":#if there is more than one basis
            return False
        #in this case there is a unique basis, so we remove it from R
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
