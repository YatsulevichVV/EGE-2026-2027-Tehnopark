# def F(x, y, z, w):
#     return int(((x == (not y)) <= (not (w <= x))) or (not z))

# 20569
def F_20569(w, x, y, z):
    return int(((w <= z) == (x <= (not y))) and (x or z))

# 17856
def F_17856(w, x, y, z):
    return int(((w <= y) <= x) or (not z))

def F_13089(u, w, x, y, z):
    return int(((z <= w) and (y == (not x))) <= (u == (y or z)))

def F_9149(w, x, y, z):
    return int(((x <= y) or (z == x)) and (w <= z))

def F_8460(w, x, y, z):
    return int(((x == z) or (not (x == w))) and ((y <= x) or (not z)))

print('w', 'x', 'y', 'z', 'F')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = F_8460(w, x, y, z)
                if f == 0:
                    print(w, x, y, z, f)
