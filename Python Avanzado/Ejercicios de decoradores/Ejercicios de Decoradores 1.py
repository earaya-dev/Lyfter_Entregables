# ============================================================
# DECORATORS - SUMMARY
# ============================================================
# WHAT IT IS:
#   A decorator is a function that takes another function,
#   adds extra behavior (before/after), and returns a new
#   "wrapped" version of it.
#
# STRUCTURE (always the same):
#   def decorator(func):           <- receives the original function
#       def wrapper(*args, **kwargs):  <- new wrapped version
#           # logic before
#           result = func(*args, **kwargs)  <- calls the original
#           # logic after
#           return result          <- return what the original returned
#       return wrapper             <- return the wrapper (NO parentheses!)
#
# HOW TO APPLY IT:
#   @decorator                     <- shorthand for: my_func = decorator(my_func)
#   def my_func(...):
#       ...
#
# KEY THINGS TO KEEP IN MIND:
#   - Functions are values: you can pass them, store them, return them.
#   - "func" (no parens) is the function as an object. "func()" runs it.
#   - After @, my_func is NO LONGER the original: it's the wrapper.
#   - The wrapper is a middleman: it receives the arguments and
#     forwards them to the original via func(*args, **kwargs).
#   - *args and **kwargs let the decorator work with ANY function,
#     no matter how many parameters it takes.
#   - The wrapper doesn't "understand" the arguments, it just forwards them.
#   - If the original function returns something, the wrapper must also
#     return it ("return result"), otherwise the caller gets None.
# ============================================================


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before exercising, i will stretch")
        print(*args, **kwargs)
        result = func(*args, **kwargs)
        print(result)
        print("After exercising i will take a shower and rest")
        return result
    return wrapper

@my_decorator
def do_exercise(repetitions):
    print("I am currently doing push-ups!")
    return repetitions

do_exercise(25)