money_gained = int(input("Enter the amount of money that you have gained over the period - "))
money_lost = int(input("Enter the amount of money that you have lost over the period - "))
profit = money_gained - money_lost

if profit > 0:
    print("This was a successful period!", "The profit is - ", profit)
    rent = profit / money_gained
    print('Rentability - ', rent)
elif profit < 0:
    print("It was a bad period.", 'The debt is - ', profit)
else:
    print("There is no profit nor debt!")

num_of_staff = int(input('Enter the amount of your staff - '))
profit_per_person = profit / num_of_staff
print('Profit per person is - ', profit_per_person)