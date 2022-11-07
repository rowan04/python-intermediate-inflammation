from functools import reduce

l = [1, 2, 3]

def product (a, b):
    return a * b

print(reduce(product, l))

#we can do the same with a lambda function
print(reduce(lambda a, b: a * b, l))