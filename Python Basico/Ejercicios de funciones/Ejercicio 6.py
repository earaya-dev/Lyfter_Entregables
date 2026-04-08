def morph_string (my_string):
    string_to_list = my_string.split("-")
    string_to_list.sort()
    list_to_string_again = "-".join(string_to_list)
    print(list_to_string_again)

morph_string("python-variable-funcion-computadora-monitor")