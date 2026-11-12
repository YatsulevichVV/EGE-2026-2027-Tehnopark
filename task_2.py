def F(x, y, z, w):
    return int(((x == (not y)) <= (not (w <= x))) or (not z))

print('x', 'y', 'z', 'w', 'F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if F(x, y, z, w) == 0:
                    print(x, y, z, w, F(x, y, z, w))
