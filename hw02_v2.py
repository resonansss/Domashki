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
a = [2, 3, 4]
ov = [0, 5, 6, 7, 8, 9]
chislo = int(input('vvedite kolichestvo krolikov: '))
while chislo != 0:
    if 11 <= chislo % 100 <= 14:
        print(f'{chislo} krolikov')
    elif chislo % 10 in a:
        print(f'{chislo} krolika')
    elif chislo % 10 in ov:
        print(f'{chislo} krolikov')
    else:
        print(f'{chislo} krolik')
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
veschsh = input('vvodite raznie veshcshi: ')
while veschsh.isspace() != True:
    if veschsh.isdigit():
        print('kvadrat vvedennogo chisla:', int(veschsh) ** 2)
    if veschsh.isalpha():
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

#zadacha 6
skobki = input('vvedite vashi skobki: ')
while '()' in skobki or '[]' in skobki or '{}' in skobki:
    skobki = skobki.replace('()', '')
    skobki = skobki.replace('[]', '')
    skobki = skobki.replace('{}', '')
if skobki != '':
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
