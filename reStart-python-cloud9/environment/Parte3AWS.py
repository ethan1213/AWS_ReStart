myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

print("--------------------------------")

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

print("--------------------------------")

name = input("Cual es tu nombre?:")

print(name)

print("--------------------------------")

color = input("Cual es tu color favorito?:")
animal = input("cual es tu animal favorito?")

print("{}, te gusta {} {}! ".format(name,color,animal))