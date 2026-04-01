def open_and_print_file(path):
    with open(path) as file:
        content = file.readlines()
        for line in content:
            
            print(line.strip())
    return content

def write_file(file_path):
    file_to_write = open_and_print_file('canciones favoritas.txt')
    file_to_write.sort()
    with open(file_path, 'w') as file:
        file.writelines(file_to_write)


write_file('canciones favoritas ordenado.txt')