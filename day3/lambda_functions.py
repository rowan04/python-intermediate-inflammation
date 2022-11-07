"""Lambda function
For small functions we only need in a single place, 
we can use a lambda function instead. These don't have names.
"""


def apply_fn(fn, in_list):
    return [fn(x) for x in in_list]


result = apply_fn(lambda x: x + 1, [0, 1, 2])
print (result)

# don't do this
add_one = lambda x: x + 1

# do this instead
def add_one(x):
    return x + 1