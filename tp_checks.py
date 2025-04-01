import math

tps = [
(3,5),
(5,7),
(11,13),
(17,19),
(29,31),
(41,43),
(59,61),
(71,73),
(101,103),
(107,109),
(137,139),
(149,151),
(179,181),
(191,193),
(197,199),
(227,229),
(239,241),
(269,271),
(281,283),
(311,313),
(347,349),
(419,421),
(431,433),
(461,463),
(521,523),
(569,571),
(599,601),
(617,619),
(641,643),
(659,661),
(809,811),
(821,823),
(827,829),
(857,859),
(881,883),
]

lowest = 111
vals = []
for i in range(len(tps)):
    for j in range(len(tps)):
        for k in range(len(tps)):
            m = (tps[i][0] * tps[i][1] * tps[j][0] * tps[j][1] * tps[k][0] * tps[k][1])
            lb = tps[i][0] * tps[j][0] * tps[k][0]
            rb = tps[i][1] * tps[j][1] * tps[k][1]
            
            mid = m ** (1 / 6)
            
            up, do = 0, 0
            
            while m % (int(mid) + up) != 0: up += 1
            while m % (int(mid) - do) != 0: do += 1
            
            li = abs(mid - min(tps[i][0], tps[j][0], tps[k][0]))
            ri = abs(min(tps[i][1], tps[j][1], tps[k][1]) - mid)
            
            
            print(m, mid, up, do, math.log(mid, 2), ri <= li, ri, li, i, j, k)
            if not ri <= li: input()
            
            
            
print("Done!")
