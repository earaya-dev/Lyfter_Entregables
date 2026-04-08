number1 = "2"
number2 = "3"
number3 = 4
list1 = [1,2]
list2 = [3,4]
decimal = 3.2
bool1 = True
bool2 = False


print (number1 + number2) # concatena los resultados pero no los suma
print(number1 + str(number3)) # da error si no se usa str()
print(str(number3) + number1) # da error si no se usa str()
print(list1+list2) # crea una sola lista con ambos valores de ambas listas
print(number1 + str(list1)) # da error si no se usa str(), concatena el valor de la variable string con los valores de la lista
print(decimal + number3) # en vez de concatenar resuelve la operacion como suma
print(bool1 + bool2) # resuelve la operacion de acuerdo al valor de los booleanos, en este caso true + false es igual a 1







