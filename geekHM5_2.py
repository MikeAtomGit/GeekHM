lines = open('geekhm.txt')
words_amount = 0
lines_amount = 0

for i in lines:
    lines_amount += 1
    words_amount = len(i.split()) 
    print(f'amount of words in line {lines_amount} - {words_amount}')
lines.close()
print(f'amount of lines - {lines_amount}')

