#zadacha 1 
summa_chisel = 0
summa_kvadratov = 0
dlina = 0 
chislo = int(input('vvedite kakoe-to chislo: '))
while chislo != 0:
    summa_chisel += chislo
    summa_kvadratov += chislo ** 2
    dlina += 1
    chislo = int(input('vvedite kakoe-to chislo: '))
    
sigma = ((summa_kvadratov - summa_chisel ** 2 / dlina) / dlina) ** 0.5
print(f'standartnoe otklonenie: {sigma}')

#zadacha 2
chislo = int(input('vvedite kolichestvo krolikov: '))
while chislo != 0:
    if chislo == 11 or chislo == 12 or chislo == 13 or chislo == 14:
        print(f'{chislo} krolikov')
    elif str(chislo)[-1] == '1' and chislo != 11:
        print(f'{chislo} krolik')
    elif str(chislo)[-1] == '2' and chislo != 12 or str(chislo)[-1] == '3' and chislo != 13 or str(chislo)[-1] == '4' and chislo != 14:
        print(f'{chislo} krolika')
    elif chislo >= 5 and chislo <= 10 or chislo >= 15:
        print(f'{chislo} krolikov')
    chislo = int(input('vvedite kolichestvo krolikov: '))
    
#zadacha 3
chislo = int(input('vvedite kakoe-to chislo: '))
listochek = []
while chislo != 0:
    listochek.append(chislo)
    chislo = int(input('vvedite kakoe-to chislo: '))
    
sorted_listochek = sorted(listochek)
print('samoe bolshoye vvedennoe chislo:', sorted_listochek[-1])

#zadacha 4
veschsh = input('vvedite raznie veshcshi: ')
while veschsh.isspace() != True:
    if veschsh.isdigit() == True:
        print('kvadrat vvedennogo chisla:', int(veschsh) ** 2)
    if veschsh.isalpha() == True:
        print('vashe slovo:', veschsh.upper())
    veschsh = input('vvedite raznie veshcshi: ')
    
#zadacha 5
from random import randint
def random_chislo():
    sluch_chislo = randint(0, 1023)
    i = 1
    print('ya zagadal chislo ot 0 do 1023')
    while i <= 10:
        popitka = int(input('vvedite vashe chislo: '))
        i += 1
        if popitka == sluch_chislo:
            print(f'pozdravlayu, vy pobedili! bylo zagadano chislo {sluch_chislo}!')
            break
        elif popitka > sluch_chislo and popitka <= 1023:
            print('vashe chislo bolshe zagadannogo!')
        elif popitka < sluch_chislo and popitka >= 0:
            print('vashe chislo menshe zagadannogo!')
        elif popitka < 0 or popitka > 1023:
            print('vy vveli chislo ne iz togo diapozona!')
            i -= 1
    else:
        print('vy ne ugadali chislo! ya zagadal', sluch_chislo)
        print('sigraem eschshe razok?')
        otvet = input('yes no: ')
        if otvet == 'no':
            print('do vstrechi!')
        elif otvet == 'yes':
            print('nachinaem zanogo!')
            random_chislo()

random_chislo()

#Ответьте на вопрос: готовы ли вы ручаться, что угадаете загаданное число за эти 10 попыток?
#Я угадала, нужно взять середину и каждую попытку сужать диапозон вдвое. Но за других ручаться не могу

#zadacha 6
skobki = input('vvedite vashi skobki: ')
while '()' in skobki or '[]' in skobki or '{}' in skobki:
    skobki = skobki.replace('()', '')
    skobki = skobki.replace('[]', '')
    skobki = skobki.replace('{}', '')
if skobki != []:
    print(False)
else:
    print(True) 
    
#zadacha 7
alfavit_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_eng = 'abcdefghijklmnopqrstuvwxyz'
alfavit_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alfavity = [alfavit_EN, alfavit_eng, alfavit_RU, alfavit_rus]

for spisok in alfavity:
    for bukva in spisok:
        print('nomer iz Unicoda dlya bukvy', bukva, '-- eto', ord(bukva))
#по порядку, кроме Ёё, потому что умлаут как диакритика


#zadacha 8
alfavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
sdvig = 0
strochka = input('vasha strochka: ').lower()
rasshifrovka = ''
probel = '\n'
while sdvig != 33:
    rasshifrovka += probel
    for i in strochka:
        mesto = alfavit.find(i)
        new_mesto = mesto + sdvig
        if i in alfavit:
            rasshifrovka += alfavit[new_mesto]
        else:
            rasshifrovka += i
    sdvig += 1
print (f'rasshifrovka strochki: {rasshifrovka}')
