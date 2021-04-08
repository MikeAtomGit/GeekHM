sample_list = input('Enter your string list divided by spaces - ')
sample_list = sample_list.split()
n = 0
i = 0
while i < len(sample_list):
    first_ele = sample_list.pop(i)
    if n < len(sample_list):
        second_ele = sample_list.pop(n)
        sample_list.insert(i, second_ele)
        if n+1 <= len(sample_list):
            sample_list.insert(n+1, first_ele)
    else: 
        sample_list.insert(i, first_ele)
    i += 2
    n += 2
print(sample_list)