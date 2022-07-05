from random import randint
matrix=[]
fila=5
columna=5
for f in range(fila):
    matrix.append([])
    for c in range(columna):
        valor=randint(1,100)
        matrix[f].append(valor)

for f in matrix:
    print(f)



    