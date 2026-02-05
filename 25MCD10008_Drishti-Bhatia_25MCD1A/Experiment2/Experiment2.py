import math
from collections import Counter

def permutations_count(s):
    n = len(s)
    freq = Counter(s)
    res = math.factorial(n)
    for v in freq.values():
        res //= math.factorial(v)
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    best_string = s
    best_value = permutations_count(s)

    for i in range(n):
        for j in range(n):
            temp = list(s)
            temp[i] = s[j]
            temp = "".join(temp)

            val = permutations_count(temp)
            if val < best_value:
                best_value = val
                best_string = temp

    print(best_string)
