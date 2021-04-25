data = open('data.txt', 'w')
while True:
    new_line = input('Enter your string:')
    data.write(new_line + '\n')
    if new_line == '':
        break