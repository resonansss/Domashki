def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

def perestanovka_bez_povt(n):
    if n == 0:
        return 1
    return perestanovka_bez_povt(n - 1) * n

def sochetanie_bez_povt(n, k):
    if k == n or k == 0:
        return 1
    elif k != 1:
        return sochetanie_bez_povt(n - 1, k) + sochetanie_bez_povt(n - 1, k - 1)
    else:
        return n
    
def razmeshshenie_bez_povt(n, k):
    if n == k:
        if n == 0:
            return 1
        else:
            return razmeshshenie_bez_povt(n - 1) * n
    else:
        return (sochetanie_bez_povt(n - 1, k) + sochetanie_bez_povt(n - 1, k - 1)) * factorial(k - 1) * k
    
    
#print(factorial(5)) => 120
#print(perestanovka_bez_povt(5)) => 120
#print(sochetanie_bez_povt(5, 3)) => 10
#print(razmeshshenie_bez_povt(5, 3)) => 60