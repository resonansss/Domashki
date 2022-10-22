#zadacha 1
kolvo_students = int(input('vvedite kolichestvo studentov: '))
yaziki = []

for i in range(kolvo_students):
    yaziki.extend(input(f'vvedide yaziki {i + 1}-go studenta: ').split())
    
unique_yaziki = set(yaziki)
yaziki_vseh = set()

for yazik in unique_yaziki:
    if yaziki.count(yazik) == kolvo_students:
        yaziki_vseh.add(yazik)

print (f'yaziki, kotorie znaet min odin student: {unique_yaziki}')
print (f'yaziki, kotorie znayut vse students: {yaziki_vseh}')

#zadacha 2
import re
stroka_s_textom = input('vvedite text: ')
znaki = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''

for znak in znaki:
    stroka_s_textom = stroka_s_textom.replace(znak, '')
    
print(f'slova v texte: {stroka_s_textom}')

stroka_s_textom = stroka_s_textom.split()

freq_dict = {}

for slovo in stroka_s_textom:
    freq_dict[slovo] = freq_dict.get(slovo, 0) + 1
    
sorted_fd = dict(sorted(freq_dict.items(), key = lambda i: i[1], reverse = True))

print(sorted_fd)

#zadacha 4
def summa_matric(matrica1, matrica2):
    sum_mc = []
    
    for i in range(len(matrica1)):
        l = []
        
        for j in range(len(matrica1[0])):
            l.append(matrica1[i][j] + matrica2[i][j])
        
        sum_mc.append(l)
        
    return sum_mc


matrica1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11, 12]]
matrica2 = [[12, 11, 10], [9, 8, 7], [6, 5, 4], [3, 2, 1, 0]]
print(summa_matric(matrica1, matrica2))

#zadacha 5
def multip_matric(matrica1, matrica2):
    mul_mc = []
    
    for i in range(len(matrica1)):
        l = []
        
        for j in range(len(matrica1[0])):
            l.append(matrica1[i][j] * matrica2[i][j])
        
        mul_mc.append(l)
        
    return mul_mc


matrica1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
matrica2 = [[12, 11, 10], [9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(multip_matric(matrica1, matrica2))