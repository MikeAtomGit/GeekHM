time = int(input('Enter time in seconds - '))
h = time//3600
m = (time - h*3600)//60
s = (time - h*3600 - m*60)
print(f'{h:02}:{m:02}:{s:02}')