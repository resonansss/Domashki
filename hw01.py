#zadacha 1
chislo = input('enter your 3-znachnoe chislo: ')
summa = sum([int(i) for i in chislo])
print(f'summa chisel: {summa}')
#v odnu strochku :))
#print('summe chisel:', sum([int(i) for i in input('enter your 3-znachnoe chislo: ')]))

#zadacha 2
procent = int(input('enter procent po vkladu: '))
rubli = int(input('enter rubli: '))
kopeyki = int(input('enter kopeyki: '))
nachalo = 100 * rubli + kopeyki # perevodim vsё v kopeyki
dochod = (nachalo * procent) / 100 
konec = nachalo + dochod
print('vashi money cherez god so vklada:',
      int(konec // 100), 'rubley', int(konec % 100), 'kopeek')

#zadacha 3
km_1 = int(input('km v first day: '))
km_2 = int(input('km v kakoy-to day: '))
i = 1
while km_1 < km_2:
    km_1 *= 1.7
    i += 1
print(f'sportman run {km_2} km or more in {i} day of probezhka')

#zadacha 4
km_1 = int(input('km v first day: '))
km_2 = int(input('km v summe za predidushiye dni: '))
i = 1
sum_km = km_1
while sum_km < km_2:
    km_1 *= 1.7
    sum_km += km_1
    i += 1
print(f'sportman run okolo {km_2} km za {i} days of probezhka')

#zadacha 5 (dva varianta resheniya)
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
nomer_var1 = int(input('enter number: '))
fib0 = 0
fib1 = 1
fib2 = 1
for i in range(3, nomer_var1):
    fib1, fib2 = fib2, fib1 + fib2   
print(f'element fibonacci: {fib2}') 

nomer_var2 = int(input('enter number: '))    
fib0 = 0
fib1 = 1
fib2 = 1
i = 0
while i < (nomer_var2 - 3):
    summa_fibonacchi = fib1 + fib2
    fib1 = fib2
    fib2 = summa_fibonacchi
    i = i+1
print(f'element fibonacci: {fib2}')

#zadacha 6
sec = int(input('enter sekundy: '))
#про дни ничего не сказано, так что будем
#считать, что число вписывается в диапазон до 86 400
#(из чисто корытных помыслов об упрощении задания)
hours = sec // (60 * 60)
minutes = (sec % (60 * 60)) // 60
seconds = sec % 60
print(f'tochnoye vremya: {hours}:{minutes}:{seconds}')

#хацкерские методы
import datetime
sec = int(input('enter sekundy: '))
h_m_s = str(datetime.timedelta(seconds = sec))
print(f'tochnoye vremya: {h_m_s}')

