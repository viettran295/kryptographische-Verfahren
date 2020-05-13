import numpy as np

matrixKlar = ([4, 22, 17, 4, 14], 
    [8, 0, 5, 11, 19], 
    [13, 17, 17, 0, 19], 
    [18, 3, 4, 13, 3], 
    [19, 4, 21, 6, 4])

#inverse Matrix ausrechnen
inverseMatrix1 = np.linalg.inv(matrixKlar)
det = np.linalg.det(matrixKlar)

matrixChiff = ([23, 7, 2, 17, 19], 
    [3, 17, 7, 5, 19], 
    [19, 24, 16, 12, 5], 
    [4, 20, 25, 11, 10], 
    [10, 21, 14, 25, 3])
 
 #i finden, um die Brüche wegzumachen
print("Mod = det*i%26, mit det: Determinant der inversen Matrix von Klartext.")
for i in range (20, 30):
    Mod = det*i%26 
    print("i =", i, "Mod =", Mod)
inverseMatrix2 = inverseMatrix1*25*det%26
print("inverse Matrix: \n", inverseMatrix2)

#überprüfen die neu inverse Matrix
print("überprüfen die neu inverse Matrix (matrixKlar*die neue inverse Matrix)mod26):")
testMatrix = np.matrix.round(np.matmul(inverseMatrix2, matrixKlar))
testMatrix = testMatrix%26
#np.set_printoptions(suppress = True)
print(testMatrix)

#Matrixchiffre ausrechnen
Matrixchiffre = np.matrix.round(np.matmul(matrixChiff, inverseMatrix2))
Matrixchiffre = Matrixchiffre%26
print(Matrixchiffre)





