
factor = 1
def fact():
    global factor
    n = int(input('Enter your number - '))
    if n < 0:
        print('Invalid number!')
    elif n == 0:
        print('0! is 0')
    else:
        for i in range(1, n+1):
            factor = factor*i
            yield factor


for ele in fact():
    print(ele)

