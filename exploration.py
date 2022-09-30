import matroids as MP

opi="1|3,4|2"
opi="2,3|1|4"
S = ["1", "3"]
#print(MP.schubert_generic(opi, S, {"1":1, "2":2, "3":3, "4":4}))


[set_comps , mat] = MP.matrix_QSym_coeff(4)
for i in range(len(mat)):
    print(mat[i])




