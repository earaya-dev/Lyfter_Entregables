list_of_keys = ["access_level","age"]

employee = {
    'name': 'Esteban',
    'email': 'esteban.arayaleiton@gmail.com',
    'access_level': 5,
    'age': 30
}

for index in range(len(list_of_keys)):
    current_key = list_of_keys[index]
    if current_key in employee:
        employee.pop(current_key)
print(employee)