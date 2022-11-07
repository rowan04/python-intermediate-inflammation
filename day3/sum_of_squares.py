from functools import reduce

l = range(5)
square_l = [i * i for i in l]
print(square_l)
print(reduce(lambda a, b: a + b, square_l))

# def sum_of_squares(square_l):
#     total = 0
#     for i in square_l:
#         total + i
#     print(total)