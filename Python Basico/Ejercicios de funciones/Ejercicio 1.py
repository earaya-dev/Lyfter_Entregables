def function1 ():
   print_something = "This is function 1"
   call_to_function2 = function2()
   return print_something, call_to_function2


def function2 ():
    print_something = "This is function 2"
    return print_something

print(function1())