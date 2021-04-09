def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return my_list[-2] + my_list[-1]

num1 = int(input('Enter 1st number - '))
num2 = int(input('Enter 2nd number - '))
num3 = int(input('Enter 3rd number - '))

max_sum = my_func(num1, num2, num3)
print(max_sum)

