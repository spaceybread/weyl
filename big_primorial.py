import random
from sympy import sieve
from mpmath import mp, log

mp.dps = 100

def prod(li):
    out = 1
    for a in li:
        out *= a
    return out

while True:
    x = random.randint(10**6, 10**7)
    y = random.randint(10**6, 10**7)

    a, b = min(x, y), max(x, y)

    ps = list(sieve.primerange(a, b + 1))

    if len(ps) < 2:
        continue
    
    pr = prod(ps)

    rt = mp.power(pr, 1 / len(ps))
    phi = log(pr, 2) * (3 / 5)

    al = rt - phi
    be = rt + phi
    
    print(rt, phi, min(ps), al, max(ps), be)

    if min(ps) <= al or max(ps) >= be:
        print("fail")
        print(rt, phi, min(ps), al, max(ps), be)
        break
