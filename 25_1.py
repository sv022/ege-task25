a = []
k = 0
for n in range(860_000, 1_000_000):
    if k != 5:
        for u in range(2, int(n ** 0.5) + 1):
            if n % u == 0:
                if str((n // u) - u)[-2::] == '18':
                    a.append((n, (n // u) - u))
                    k += 1
                    break
                else:
                    break
    else:
        break
print(a)
