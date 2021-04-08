my_list = [9, 9, 9, 8, 8, 7, 7, 6, 6, 5, 4, 4, 4, 2, 2, 1]
new_num = int(input('Enter a new number - '))
i = 0

for n in my_list:
    if new_num <= n:
        i += 1
my_list.insert(i, float(new_num))
print(my_list)