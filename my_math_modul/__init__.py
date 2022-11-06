#zadacha 1
import combinatorics
import areas

print('''what do you need? 
      c for combinatorics
      a for areas''')

vybor = input('c or a: ')

if vybor == 'c':
    print('''what do you want?
          f as factorial
          p as perestanovka
          s as sochetanie
          r as razmeshshenie''')
    vybor_c = input('vash vybor: ')
    if vybor_c == 'f':
        n = int(input('vvedite n: '))
        print(combinatorics.factorial(n))
    elif vybor_c == 'p':
        n = int(input('vvedite n: '))
        print(combinatorics.perestanovka_bez_povt(n - 1) * (n))
    elif vybor_c == 's':
        n = int(input('vvedite n: '))
        k = int(input('vvedite k: '))
        print(combinatorics.sochetanie_bez_povt(n, k))
    elif vybor_c == 'r':
        n = int(input('vvedite n: '))
        k = int(input('vvedite k: '))
        print(combinatorics.razmeshshenie_bez_povt(n, k))
else:
    print('''what do you want?
        p as pryamougolnik
        kv as kvadrat
        t as treugolnik
        k as krug
        sh as shar''')
    vybor_a = input('vash vybor: ')
    if vybor_a == 'p':
        a = int(input('vvedite a: '))
        b = int(input('vvedite b: '))
        print(areas.pryamougolnik(a, b))
    elif vybor_a == 'kv':
        a = int(input('vvedite a: '))
        print(areas.kvadrat(a))
    elif vybor_a == 't':
        a = int(input('vvedite a: '))
        b = int(input('vvedite b: '))
        c = int(input('vvedite c: '))
        print(areas.treugolnik(a, b, c))
    elif vybor_a == 'k':
        r = int(input('vvedite r: '))
        print(areas.krug(r))
    elif vybor_a == 'sh':
         r = int(input('vvedite r: '))
         print(areas.shar(r))

