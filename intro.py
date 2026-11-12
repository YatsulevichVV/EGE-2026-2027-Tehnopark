# КОНСПЕКТ, НЕ ДЛЯ ЗАПУСКА!!!

a = 5
b = 2
c = a + b
d = a - b
e = a * b

# Типы данных
int, float, bool, str, list, set, dict

f = a / b   # float
g = a // b  # int - целая часть
h = a % b   # int - остаток от деления

input() # Ввод
print() # Вывод

function_title(arg1, arg2, ..., argn)

s = input('Enter something: ')
print(s, 1, 2, 3, sep=',', end='!!!')
print(s, 1, 2, 3, sep=',', end='\a')

# 2. Условный оператор

if condition:
    ...
elif condition2:
    ...
else:
    ...

x = True
y = False
x and y, x or y, not x, x == y, x <= y

x = 1
y = 2
x == y, x < y, x > y, x <= y, x >= y, x != y

# 3. Циклы
while - количество итераций неизвестно
for - известное количество итераций

while condition:
    ...
else:
    ...

lst = [1, 'asds', 2, None, 0.5, [], {}]
for i in lst:
    print(i)

# range() - формирование набора чисел
n = 20
for i in range(30, n + 1, -1):
    print(i)

# Описание функции
def function_title(args):
    ...
    return ...

x = True
y = False
print(x <= y)

# Задача 31348
def F(w, x, y, z):
    return int((z <= (not (y <= x))) or w)

def F(w, x, y, z):
    return int(x and ((w <= y) == z))

print('w', 'x', 'y', 'z', 'F')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = F(w, x, y, z)
                print(w, x, y, z, f)