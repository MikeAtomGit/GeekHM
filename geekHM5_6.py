lessons = open('lessons.txt', 'r')
lessons_dict = {}
for line in lessons:
    name, stats = line.split(':')
    lessons_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
    lessons_dict[name] = lessons_sum
print(lessons_dict)
        
