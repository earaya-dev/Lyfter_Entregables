def calculator_menu ():
    current_result = 0
    while True:
        print(f"--- CURRENT OPERATION RESULT: {current_result} ---")
        print("1. Sum")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Erase Result")
        print("6. Exit")
        user_input = input("Please choose a calculator function in the menu above: ")
        if user_input == "1":
            current_result = sum_function(current_result)
        elif user_input == "2":
            current_result = subtraction_function(current_result)
        elif user_input == "3":
            current_result = multiplication_function(current_result)
        elif user_input == "4":
            current_result = division_function(current_result)
        elif user_input == "5":
            current_result = 0
            print("Your previous operation result was erased.")
        elif user_input == "6":
            print(f'Goodbye!')
            break
        else:
            print("ERROR: Please enter a valid function number from the menu.")
        


def sum_function (current_result):
    try:
        input_number = int(input("Enter your first number: "))
        execute_sum = input_number + current_result
        current_result = execute_sum
        return current_result
    except ValueError as e:
        print(f'Error [ValueError]: Cant convert entered value to a valid number. Details: {e}')
        return current_result


def subtraction_function (current_result):
    try:
        input_number = int(input("Enter your first number: "))
        execute_subtraction = current_result - input_number
        current_result = execute_subtraction
        return current_result
    except ValueError as e:
        print(f'Error [ValueError]: Cant convert entered value to a valid number. Details: {e}')
        return current_result


def multiplication_function (current_result):
    try:
        input_number = int(input("Enter your first number: "))
        execute_multiplication = input_number * current_result
        current_result = execute_multiplication
        return current_result
    except ValueError as e:
        print(f'Error [ValueError]: Cant convert entered value to a valid number. Details: {e}')
        return current_result


def division_function (current_result):
    try:
        input_number = int(input("Enter your first number: "))
        execute_division = current_result / input_number
        current_result = execute_division
        return current_result
    except ValueError as e:
        print(f'Error [ValueError]: Cant convert entered value to a valid number. Details: {e}')
        return current_result
    except ZeroDivisionError as e:
        print(f'Error [ZeroDivisionError]: Input number cannot be 0 ')
        return current_result

calculator_menu()