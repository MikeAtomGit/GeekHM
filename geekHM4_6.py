from itertools import count, cycle
the_list = [1, 2, 3, 6, 7]
countable = 0
for i in cycle(the_list):
    print(i)
    countable += 1
    if countable == 30:
        break
for i in count(69):
    if i == 669:
        break
    print(i)