def pryamougolnik(a, b):
    return a * b

def kvadrat(a):
    return a * a #a ** 2

def treugolnik(a, b, c):
    p = (a + b + c) / 2
    return round(((p * (p - a) * (p - b) * (p - c)) ** 0.5), 2)

def krug (r):
    from math import pi
    return round((pi * r ** 2), 2)

def shar (r):
    from math import pi
    return round(4 * pi * r ** 2, 2)

#print(pryamougolnik(2, 3)) => 6
#print(kvadrat(4)) => 16
#print(treugolnik(4, 5, 6)) => 9.92
#print(krug(3)) => 28.27
#print(shar(3)) => 113.1