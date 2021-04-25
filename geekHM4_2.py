first_list = [600, 700, 3, 4, 2, 9, 13, 1, 0, 7, 10]

second_list = [el for el in first_list[1:] if el > first_list[first_list.index(el)-1]]
print(second_list)