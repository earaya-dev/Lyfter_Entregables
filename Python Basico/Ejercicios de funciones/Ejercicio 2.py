
outside_monster = "Green Monster"

def function1 ():
    inside_monster  = "White Monster"
    global outside_monster
    print(f"Will it change color?:{outside_monster}")

# acceder a una variable global desde una funcion y cambiar el valor
# resultado no va a cambiar, sigue siendo green y no blue
print(f'This is the: {outside_monster}') 

# variable adentro de una funcion desde afuera
## tira no esta definido, porque no es global. 
# comento el print para poder guardar el codigo y que quede

# print(inside_monster) 