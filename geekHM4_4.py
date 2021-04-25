from random import randint

orig_list = [randint(-10, 10) for _ in range(20)]
new_list = [el for el in orig_list if orig_list.count(el) == 1]
print(f'Original list\n{orig_list}\n New list\n{new_list}')


