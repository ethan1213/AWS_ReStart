import random


print("Bienvenido!")
print("Vamos a jugar un juego. Tienes que adivinar en que numero estoy pensando del 1 al 10")

numero = random.randint(1,10)

bandera = False

i = 1

while bandera == False:
    num = int(input("Escoge un numero del 1 al 10: "))
    
    if num == numero:
        bandera = True
        print("Bien acertaste al intento : ", i )
    else:
        i += 1
        print(f"escogiste el numero {num} y esta incorrecto, vuelve a intentarlo")
        
print("--------------------------------------")

#vamos a ver el ciclo for
print("Vamos a ver una cuenta del 1 al 10 con un ciclo for")

for i in range(1,11):
    print(i)