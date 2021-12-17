a = []
for n in range(10_000_000, 10_500_000):
    s = 0
    k = 0
    for i in range(int(n ** 0.5) + 1 ,2, -1):
        if n % i == 0:
            s += n / i
            k += 1
            if k == 2:
                if 0 < s < 10000:
                    a.append((n, s))
                break      
    if len(a) == 5:
        break
print(a)
