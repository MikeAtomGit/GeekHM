total = {'name': '', 'surname': '', 'phone number': '', 'birth year': '', 'city': '', 'email': ''}
def info():
    for key in total:
        feat = input(f'Enter your {key} - ')
        total[key] = feat
    return total

result = info()
print(result)