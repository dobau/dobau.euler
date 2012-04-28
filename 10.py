from math import *

def ehPrimo(numero):
    if (numero == 2):
        return True
    
    if (numero % 2 == 0):
        return False
    
    limite = int(floor(sqrt(numero)) + 1);
    for i in xrange(3, limite, 2):
        if (numero % i == 0):
            return False
    
    return True

soma = 0
for i in xrange(2, 2000000):
    if (ehPrimo(i)):
        soma += i

print soma