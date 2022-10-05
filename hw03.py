#zadacha 1
chisla_spisok = input('vvedite chisla cherez probel: ').split()
chisla = [int(i) for i in chisla_spisok]
ind_max = chisla.index(max(chisla))
ind_min = chisla.index(min(chisla))
chisla[ind_min], chisla[ind_max] = chisla[ind_max], chisla[ind_min]
print(chisla)

#zadacha 2
spisok_chego_ugodno = input('vvodite chto ugodno cherez probel: ').split()
for i in range(1, len(spisok_chego_ugodno)):
#тут все элементы смещаются влево на 1 и первый => последний, но
#если нужно менять местами конкретно соседние элементы как было в примере 1 2 3 4 5 ==> 2 1 4 3 5, 
#то тогда нужно 
#for i in range(1, len(spisok_chego_ugodno, 2))
    spisok_chego_ugodno[i - 1], spisok_chego_ugodno[i] = spisok_chego_ugodno[i], spisok_chego_ugodno[i - 1]

print (spisok_chego_ugodno)

#zadacha 3
ravnyajs = [int(i) for i in input('vvedite rost uchenikov cherez probel: ').split()]
rost_Peti = int(input('vvedite rost Peti: '))
ravnyajs.append(rost_Peti)
ravnyajs.sort()
Petin_nomer = len(ravnyajs) - ravnyajs[::-1].index(rost_Peti) 
print(f'rost vseh ucenikov -- {ravnyajs}, a Petya sredi nih na {Petin_nomer} meste')

#zadacha 4
iks = ['x']
igrek = ['y']
spisochek = []
for i in iks*8 and igrek*8:
    iks[0] = int(input('vvedite koordinatu iks dlya tochki: '))
    igrek[0] = int(input('vvedite koordinatu igrek dlya tochki: '))
    xx = tuple(iks)
    yy = tuple(igrek)
    spisochek.append(xx + yy)
print('Spisochek par koordinat:', spisochek)
for i in range(8):
    for j in range(i + 1, 8):
        if (spisochek[i][0] == spisochek[j][0] or spisochek[i][1] == spisochek[j][1] or 
            abs(spisochek[i][0] - spisochek[j][0]) == abs(spisochek[i][1] - spisochek[j][1])):
            print ('ferzi bjut drug druga? YES')
            break
    else: continue
    break

else:
    print ('ferzi bjut drug druga? NO')
    
#zadacha 5
spisok = input('vvedite elementi spiska cherez probel: ').split()
spisok_bez_povtorov = []
for i in spisok:
    if i not in spisok_bez_povtorov:
        spisok_bez_povtorov.append(i)
print(f'spisok bez povtorov: {spisok_bez_povtorov}')
#потом я прочитала, что нельзя использовать доп память, поэтому 
#  |
#  |
# \ /

#var2
spisok = input('vvedite elementi spiska cherez probel: ').split()
for i in spisok:
    if spisok.count(i) > 1:
        spisok.remove(i)
print(f'spisok bez povtorov: {spisok}')
    
#zadacha 6
chislo_N = int(input('vvedite chislo N: '))
spisok_NNN = input('vvedite spisok cherez probel: ').split()
for i in spisok_NNN:
    if spisok_NNN.count(i) == chislo_N:
       for j in range(len(spisok_NNN) - 1, -1, -1):
           if spisok_NNN[j] == i:
               spisok_NNN.remove(i)
print(spisok_NNN)

#zadacha 7
import time

chislo_X = int(input('vvedite chislo X: '))
chislo_D = int(input('vvedite chislo D (1000, 10000 etc.): '))
spisok_chiselok = [int(i) for i in input('vvedite spisok chisel cherez probel: ').split()]
spisok_chiselok = spisok_chiselok * chislo_D
t = time.time()

i = 0
for j in range(len(spisok_chiselok)):
    if spisok_chiselok[j] != chislo_X:
        spisok_chiselok[i] = spisok_chiselok[j]
        i += 1

del spisok_chiselok[i:]

print('vremya:', time.time() - t)
print('spisok chiselok:', spisok_chiselok[:30])

#zadacha 8 
import time

spisok = input('vvedite elementi spiska cherez probel: ').split()
spisok_bez_povtorov = []
chislo_D = int(input('vvedite chislo D (1000, 10000 etc.): '))
spisok = spisok * chislo_D
t = time.time()

for i in spisok:
    if i not in spisok_bez_povtorov:
        spisok_bez_povtorov.append(i)

print(time.time() - t)
print (f'spisok bez povtorov: {spisok_bez_povtorov}')

#zadacha 10
def nomera_bukv (strochka):
    ord_bukv = []
    for bukva in strochka:
        ord_bukv.append(ord(bukva))
    return ord_bukv
print(nomera_bukv(input('vvedite strochku: ')))