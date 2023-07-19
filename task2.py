k = 0
for A in [39, 76, 60, 66, 24]:
    for x in range(1, 500):
        f = (x % A == 0) <= (x % 6 == 0 and x % 4 == 0)
        if not f:
            break
    else:
        k += 1

print(k)
