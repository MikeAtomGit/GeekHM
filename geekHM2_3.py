user_number = input('Enter a number from 1 to 12 - ')
winter = {
    '1': 'January',
    '2': 'February',
    '12': 'December',
    'name': 'Winter',
}
spring = {
    '3': 'March',
    '4': 'April',
    '5': 'May',
    'name': 'Spring',
}
summer = {
    '6': 'June',
    '7': 'July',
    '8': 'April',
    'name': 'Summer',
}
fall = {
    '9': 'September',
    '10': 'October',
    '11': 'November',
    'name': 'Fall',
}
seasons = [winter, spring, summer, fall]
for i in seasons:
    if user_number in i:
        print(i['name'])
