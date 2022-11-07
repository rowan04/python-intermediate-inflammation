#List comprehension
integers = range(5)
double_ints = [2 * i for i in integers]
print(double_ints)

#Conditions with list comprehension
integers = range(5)
double_ints = [2 * i for i in integers if i % 2 == 0]
print(double_ints)

#Set comprehension
integers = range(5)
double_ints = {2 * i for i in integers if i % 2 == 0}
print(double_ints)

#Dict comprehension
integers = range(5)
double_even_int_dict = {i: 2 * i for i in integers if i % 2 == 0}
print(double_even_int_dict)
