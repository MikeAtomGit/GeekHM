arg1 = float(input('Enter first number - '))
arg2 = float(input('Enter second number - '))

def division(a, b):
    if b == 0:
        print('Invalid argument!')
    else:
        return a / b 
result = division(arg1, arg2)      
print(result)