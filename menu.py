#crear menu con 3 opciones: 1. numeros 2. personas 3. finalizar

import os
def Numeros():
    #ingresar n numeros donde n es un numero ingresado por el usuario.
    #mostrar la cantidad de numeros positivos, negativos y cantidad de 0s
    n=int(input("ingrese num: "))
a=0
b=0
c=0
d=0
for i in range(n):
    
    a=int(input("ingrese: "))
    if(a>0):
       	b=b+1
    elif(a==0):
       	c=c+1
    elif(a<0):
        d=d+1
print("positivos: "+ str(b)+ " negativos: "+ str(d)+ "cero: "+ str(c))
pausa=input("presione una tecla para continuar")


def Personas():
    #ingresar nombre y edad para n personas. N es un numero ingresado por teclado
    #mostrar: promedio de edades

     n=int(input("ingrese numero de personas a ingresar: "))
    a=0
    sum=0
    for i in range(n):
        nom=input("ingrese nombre de la persona")
        a=int(input("ingrese la edad de la perdsona: "))
        sum=sum+a

    print("promedio: " + str(sum/n))
pausa=input("presione una tecla para continuar")

seguir=True
while(seguir):
    os.system('cls')
    print("-----Menu Principal-----")
    print("1. Numeros")
    print("2. Personas")
    print("3. Finalizar")
    op=int(input("digite opcion 1,2,3: "))
    if (op==1):
        Numeros()   #invocamos un def
    if (op==2):
        Personas()
    if (op=3):
        print("Programa finalizado")
        seguir=False
        break