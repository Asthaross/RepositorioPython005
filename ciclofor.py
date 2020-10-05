#crar ciclo for que permita ingresar para n numeros, donde n es un numero ingresado por teclado
#calcular y mostrar: cantidad de numeros pares y cantidad de numeros impares

veces=int(input("cuantos numeros ingresa?: " ))
par=0
impar=0
for x in range(veces):
    nume=int(input("ingrese un numero: "))
    if (nume%2==0):
        par=par+1
    elif(nume%2!=0):
        impar=impar+1

print("la cantidad de numeros pares es: " +str(par))
print("la cantidad de numeros impares es : " +str(impar))
