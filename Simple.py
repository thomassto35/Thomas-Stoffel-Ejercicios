
from random import randint
import operator
def creaDiccionario():
    dicc={}
    for i in range(3):
        edad=randint(1,100)
        id=input("Ingrese su ID:")
        dicc[id]=edad
    return dicc
def simple():
    lista=[]
    for i in range(3):
            lista.append(creaDiccionario())
            
    return lista
    
def ordenar(lista):
    for dicc in lista:
        sortedDict= sorted(dicc.items(), key=operator.itemgetter(1))
        print(sortedDict)
        print("El mayor es",max(dicc, key=dicc.get))
        print("El menor es",min(dicc, key=dicc.get))
res=simple()
print(res)
ordenar(res)






