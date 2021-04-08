x = int(input('Enter a number - '))
max = 0
while x > max:
    if x % 10 > max:
        max = x % 10
    x = x // 10
print(max)