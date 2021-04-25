text = open('textnum.txt', 'w')
text.write(input('Enter numbers divided by spaces: '))
text = open('textnum.txt', 'r')
splitted = text.readline().split()
summary = 0
for i in splitted:
    summary += int(i)
print(summary)