user_text = input('Enter your text - ')
user_list = user_text.split()
n = 1
for word in user_list:
    if len(word) > 10:
        print(n, '.', word[0:10])
    else:
        print(n, '.', word)
    n +=1
