def wage(hrs, payment, extra):
    return (hrs * payment) + extra
result = wage(
    hrs = int(input('Enter the amount of time - ')),
    payment = int(input('Enter payment per hour -')),
    extra = int(input('Enter extra payment - ')))
print(f'The resulting amount of paycheque is {result}')