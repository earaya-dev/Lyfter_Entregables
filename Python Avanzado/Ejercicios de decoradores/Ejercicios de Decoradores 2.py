def my_decorator(func):
    def is_it_a_number(*args, **kwargs):
        for elements in args[0]:
            if not isinstance(elements, (int, float)):
                raise TypeError("Only numbers are allowed")
                result = func(*args, **kwargs)
                return result
    return is_it_a_number



@my_decorator
def do_sum(numbers):
    result = sum(numbers)
    print(result)
    return numbers

do_sum([4,5,"hello"])