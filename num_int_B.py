import numpy as np
from scipy.integrate import quad

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

M = 400.967
C2 = 1.32
B = 7.28

d0 = find_min_d0(M, C2, B)
print(f"Minimum d0: {d0}")

