k = 0
f = True
for i in range(60_000_000, 50_000_000, -1):
    a = set()
    if str(i ** 0.5)[-2::] == '.0': 
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                a.add(j)
                a.add(i // j)
        if len(a) == 7:
            if f:
                print(i)
                print(a)
                f = False
            k += 1

print(k)
