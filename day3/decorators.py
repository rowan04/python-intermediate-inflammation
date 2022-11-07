def with_logging(func):
    """A decorator which adds logging to a function"""
    def inner(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")

        return result

    return inner


def add_one(n):
    print("Adding one")
    return n + 1

add_one = with_logging(add_one)

@with_logging
def add_two(n):
    print("Adding two")
    return n + 2

print(add_one(1))
print(add_two(1))
