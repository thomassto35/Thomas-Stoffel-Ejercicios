from math import pi
from tkinter import N 
class circulo:
    def __init__(self,radio,mult):
        self.radio=radio
        self.mult=mult
    def calcularArea(self):
        area = (pi*self.radio)**2
        print("El area es:",area)
    def calcularPerimetro(self):
        perimetro =pi*2*(self.radio)
        print("El perimetro es:",perimetro)
    def multiplicacion(self):
        m=self.radio*self.mult
        print("El radio multiplicado es:",m)
r=int(input("Ingrese el radio:"))
n=int(input("Ingrese un numero para multiplicar:"))
while r<=0 and n<=0:
    print("Error 0 es invalido como radio y para multiplicar, intentar de nuevo.")
    r=int(input("Ingrese el radio mayor a 0:"))
    n=int(input("Ingrese un numero para multiplicar mayor a 0:"))
while r>0 and n>0:
    c1=circulo(r,n)
    c1.calcularArea()
    c1.calcularPerimetro()
    c2=circulo(r,n)
    c2.multiplicacion()
    r=int(input("Ingrese el radio 0 -1 para finalizar:"))
    n=int(input("Ingrese un numero para multiplicar:"))



