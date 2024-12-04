"""
Desarrolla un programa que reciba 3 números e imprima el número mayor
Sólo utiliza condicionales
Ejemplo de entrada:
Ingresa el primer número: 9
Ingresa el segundo número: 3
Ingresa el tercero número: 15
Salida:
El número mayor es el tercero: 15
"""

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

if num1 > num2 and num1 > num3:
    print("El numero mayor es el : " , num1)
elif num2 > num1 and num2 > num3:
    print("El numero mayor es el : " , num2)
elif num3 > num1 and num3 > num2:
    print("El numero mayor es el : " , num3)
    
#ahora sin tanto if

print("El numero mayor sin tanta condicional es el : " , max(num1,num2,num3))