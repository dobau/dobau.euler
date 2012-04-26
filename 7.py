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

num = 3
count = 2;
while(count != 10001):
    num += 2
    if (ehPrimo(num)):
        count += 1

print num