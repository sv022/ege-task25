a = []
for i in range(850_001, 1_200_000):
    for j in range(2, int(i ** 0.5)):
        if i % j == 0:
            if ((i // j) - j) %  7 == 0:
                a.append((i, ((i // j) - j)))
            break
    if len(a) == 6:
        print(a)
        exit()
