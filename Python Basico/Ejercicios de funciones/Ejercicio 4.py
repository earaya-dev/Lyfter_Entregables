
def string_sideways (my_string):
    reversed_string = ""
    for index in range(len(my_string) -1,-1,-1):
        reversed_string += my_string[index]
    return reversed_string


print(string_sideways("Hola Mundo"))
