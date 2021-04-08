a = int(input('Enter the amount of kms, that the sportsman runs as of today - '))
b = int(input('Enter the amount of kms, that the sportsman should run - '))
i=1

while a < b:
    a = a*0.1 + a
    i = i + 1

print(f'It will take {i} days')