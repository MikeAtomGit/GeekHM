total_sum = 0
def summary():
    global total_sum
    print(total_sum)
    num_list = input("Enter numbers with spaces - ").split()
    while True:
        if 'q' in num_list:
            stop = num_list.index('q')
            num_list = num_list[:stop]
            total_sum = total_sum + sum([int(x) for x in num_list])
            return total_sum
            break
    
        else: 
            total_sum = total_sum + sum([int(x) for x in num_list])
            summary()
            return total_sum 

overall = summary()
print(overall)
    


