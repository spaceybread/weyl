from sympy import isprime, primefactors
import itertools
import random
import math
import time


def generate_twin_prime_pairs(k):
    primes = []
    p = 3
    while len(primes) < k:
        if isprime(p) and isprime(p + 2):
            primes.append((p, p + 2))
        p += 2
    return primes

pairs = 3
li = generate_twin_prime_pairs(100000)

li = li[int(len(li)**0.25):]

samples = random.sample(li, pairs)

print("Samples:", samples)

# samples = [li[0], li[0], li[0], li[-1], li[-1], li[-1]]
#samples = [li[0], li[0], li[-1], li[-1]]
samples = [li[0], li[len(li) // 2], li[-1]]


samples.sort()
products = []
sets = []
pr = 1
for sa in samples: pr *= sa[0] * sa[1]
pr = pr ** 0.5

for i in range(2**pairs):
    b = bin(i)[2:]
    if len(b) < pairs: b = "0" * (pairs - len(b)) + b
    prod = 1
    set = []
    for i in range(len(samples)):
        prod *= samples[i][int(b[i])]
        set.append(samples[i][int(b[i])])
    # print(b, set)
    products.append(prod)
    sets.append(set)
    print(b, set, abs(pr - prod) / pr)

#print(products)
#

diffs = [abs(pr - p) / pr for p in products]
#print(diffs, sets)
print(min(diffs), max(diffs))
print(pr, pr**(1/pairs))
