from sympy import primerange
import random
import math

def prod(li):
    out = 1
    for a in li: out *= a
    return out

def filter(li, k):
    out = []
    for i in range(len(li)):
        if i % k == 0: out.append(li[i])
    return out

def bits(n):
    return len(bin(int(n))) - 2

while True:
    x = random.randint(1, 750)
    y = random.randint(1, 750)

    a, b = min(x, y), max(x, y)

    ps = list(primerange(a, b + 1))
    ps = filter(ps, 1)

    if len(ps) < 2: continue
    pr = prod(ps)
    
    try:
        rt = pr**(1/len(ps))
    except:
        continue
    # print(pr, rt)


    # phi = math.log(rt, 2) * len(ps) / 1.5
    phi = math.log(pr, 2)**2

    al = rt - phi
    if al < 0: al = 0
    be = rt + phi
    
    print(rt, phi, min(ps), al, max(ps), be, bits(pr), bits(be - al))
    print(pr)
    if min(ps) <= al or max(ps) >= be:
        print("fail")
        print(ps)
        print(rt, phi, min(ps), al, max(ps), be)
        break
    
