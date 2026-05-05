def my_decorator(func):
    def is_it_a_number(*args, **kwargs):
        for elements in args:
            if not isinstance(elements, (int, float)):
                raise TypeError("Only numbers are allowed")
        return func(*args, **kwargs)
    return is_it_a_number



@my_decorator
def do_sum(*numbers):
    result = sum(numbers)
    print(result)
    return result

do_sum(4,5,"hello")