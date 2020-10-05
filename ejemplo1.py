a=int(input("digite un numero: "))
b=int(input("digite otro numero: "))
suma=a+b
multi=a*b
print("la suma de " +str(a) + "y de " +str(b) + "es igual a: " + str(suma))
print("la multiplicacion de " +str(a) + "y de " +str(b) + "es igual a: " + str(multi))
#estructura if
if(a>b):
    print("el numero " + str(a) "es mayor que: " + str(b))
elif(a<b):
    print("el numero " + str(b) "es mayor que: " + str(a))
    else:
        print("Los numeros son iguales")
        