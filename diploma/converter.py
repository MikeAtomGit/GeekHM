# list_1 = [4,9,14,19,24,29,34,39,44]
# list_3 = [4, 34, 49]
# list_2 = [i + 3 for i in list_1]
# list_4 = [i + 3 for i in list_3]
# print(list_2)
# print(list_4)
listo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = input('ENter your shit: ')
b = a.split() 
 
if 'г' in b: 
    listo[0] = 1
if 'гг' in b: 
    listo[0] = 2
if 'ггг' in b: 
    listo[0] = 3
if 'ц' in b: 
    listo[1] = 1
if 'цц' in b: 
    listo[1] = 2
if 'ццц' in b: 
    listo[1] = 3
if 'л' in b: 
    listo[2] = 1
if 'лл' in b: 
    listo[2] = 2
if 'ллл' in b: 
    listo[2] = 3
if 'а' in b: 
    listo[3] = 1
if 'аа' in b: 
    listo[3] = 2
if 'ааа' in b: 
    listo[3] = 3
if 'с' in b: 
    listo[4] = 1
if 'сс' in b: 
    listo[4] = 2
if 'ссс' in b: 
    listo[4] = 3
if 'п' in b: 
    listo[5] = 1
if 'пп' in b: 
    listo[5] = 2
if 'ппп' in b: 
    listo[5] = 3
if 'ш' in b: 
    listo[6] = 1
if 'шш' in b: 
    listo[6] = 2
if 'шшш' in b: 
    listo[6] = 3
if 'э' in b: 
    listo[7] = 1
if 'ээ' in b: 
    listo[7] = 2
if 'эээ' in b: 
    listo[7] = 3
if 'и' in b: 
    listo[8] = 1
if 'ии' in b: 
    listo[8] = 2
if 'иии' in b: 
    listo[8] = 3
if 'н' in b: 
    listo[9] = 1
if 'нн' in b: 
    listo[9] = 2
if 'ннн' in b: 
    listo[9] = 3
if 'к' in b: 
    listo[10] = 1
if 'кк' in b: 
    listo[10] = 2
if 'ккк' in b: 
    listo[10] = 3
if 'д' in b: 
    listo[11] = 1
if 'дд' in b: 
    listo[11] = 2
if 'ддд' in b: 
    listo[11] = 3
if 'т' in b: 
    listo[12] = 1
if 'тт' in b: 
    listo[12] = 2
if 'ттт' in b: 
    listo[12] = 3
if 'в' in b: 
    listo[13] = 1
if 'вв' in b: 
    listo[13] = 2
if 'ввв' in b: 
    listo[13] = 3
if 'е' in b: 
    listo[14] = 1
if 'ее' in b: 
    listo[14] = 2
if 'еее' in b: 
    listo[14] = 3
if 'дма' in b: 
    listo[15] = 1
if 'дма2' in b: 
    listo[15] = 2
if 'дма3' in b: 
    listo[15] = 3
if 'м' in b: 
    listo[16] = 1
if 'мм' in b: 
    listo[16] = 2
if 'ммм' in b: 
    listo[16] = 3
if 'ф' in b: 
    listo[17] = 1
if 'фф' in b: 
    listo[17] = 2
if 'ффф' in b: 
    listo[17] = 3
print(listo)