import numpy as np
from scipy.integrate import quad
from sympy import primerange
import random

def generate_twin_primes(limit):
    primes = list(primerange(0, limit))
    twin_primes = [(p, p + 2) for p in primes if p + 2 in primes]
    return twin_primes

def select_random_twin_primes(twin_primes, X):
    return random.sample(twin_primes, X)

def compute_M(twin_prime_pairs, X):
    log_m = sum(np.log(p1 * p2) for p1, p2 in twin_prime_pairs)
    return np.exp(log_m / (2 * X))

def pi2(d0, M, C2):
    if d0 >= M:
        return float('inf')
    
    a = -np.log(M + d0)
    b = -np.log(M - d0)
    
    integral, _ = quad(lambda t: t**-2 * np.exp(-t), a, b)
    return C2 * integral

def find_min_d0(M, C2, B, tol=1e-6):
    low, high = 0, M
    
    while high - low > tol:
        mid = (low + high) / 2
        if pi2(mid, M, C2) >= B:
            high = mid
        else:
            low = mid
    
    return (low + high) / 2

LIMIT = 100000
X = 300
C2 = 1.32
k = 2 * X
epsilon = (1e-7) / X
TRIALS = 10000

failures = 0
twin_primes = generate_twin_primes(LIMIT)
vals = []
for _ in range(TRIALS):
    print("At trial:", _)
    selected_pairs = select_random_twin_primes(twin_primes, X)
    M = compute_M(selected_pairs, X)
    B = (-1 / k) * np.log(epsilon) * len(twin_primes)
    d0 = find_min_d0(M, C2, B)
    
    is_contained = any(M - d0 <= p1 <= M + d0 or M - d0 <= p2 <= M + d0 for p1, p2 in selected_pairs)
    
    if not is_contained:
        print(M, B, d0, selected_pairs)
        failures += 1
    vals.append(d0 / M)

print(f"Out of {TRIALS} trials, {failures} failed to contain at least one twin prime pair in [M - d0, M + d0]")
print(sum(vals) / len(vals), max(vals), min(vals))
