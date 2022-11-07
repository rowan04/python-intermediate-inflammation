#example 1


def add_one(num):
    return num + 1


def add_ones(in_list):
    return [add_one(x) for x in in_list]


result = add_ones([0, 1, 2])
print (result)


#example 2


def add_one(num):
    return num + 1


def apply_fn(fn, in_list):
    return [fn(x) for x in in_list]


result = apply_fn(add_one, [0, 1, 2])
print(result)