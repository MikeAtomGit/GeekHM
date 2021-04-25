wage = open('salary.txt', 'r')
av_sal = 0
Dict = {line.split()[0] : int(line.split()[1]) for line in wage}
for i in Dict.items():
    av_sal += i[1]
    if i[1] < 20000:
        print(i[0])
av_sal = av_sal/len(Dict)
print(av_sal)

    
print(Dict)