from functools import reduce as r
the_list = [el for el in range(100, 1000) if el % 2 == 0]
def composition(a,b):
    return a * b
print(r(composition, the_list))
print(the_list)