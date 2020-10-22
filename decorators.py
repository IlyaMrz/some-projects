import random
# lesson https://www.youtube.com/watch?v=pr1xfd6oTwY


def powerof(arg):
    def decorator(fun):
        def wrapper():
            return fun()**exponent
        return wrapper
    if callable(arg):
        exponent = 2
        return decorator(arg)
    else:
        exponent = arg
        return decorator


@powerof
def random_digit():
    return random.choice([4, 5, 6, 7, 9])


print(random_digit())
