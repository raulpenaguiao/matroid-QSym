"""
SETS PACKAGE
package that manipulates set operations
Created by RAUL PENAGUIAO
June 2022
"""

"""
Compares two lists
Assumes that these lists have the same size
assumes that lists are ordered
"""


"""
Given two lists A, B, checks if A > B in the Gale order
"""
def compare(A, B):
    if not len(A) == len(B):
    	print("This is a serious error in  -sets.py file - sets to compare do not have the same length, A = ", A, " and B = ", B, " do not trust these computations")
    	return False
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



