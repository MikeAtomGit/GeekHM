notranslation = open('notrans.txt', 'r')
translation = open('trans.txt', 'w')
translator = ["Один", "Два", "Три", "Четыре"]
n = 0
for line in notranslation:
    orig = line.split(' - ')
    s = ' - '
    new = s.join([translator[n], orig[1]])
    n += 1
    translation.write(f'{new}\n')

