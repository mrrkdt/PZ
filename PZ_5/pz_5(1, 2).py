# 1
# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m.
# Суммирование оформить функцией с параметрами. Значения n и m программа должна запрашивать.

# -> 1 4
# <- 10


# функция
def sum_number(begin, end):
    sum = 0
    for n in range(begin, end + 1):
        sum += n
    return sum


# переменные
n = input("Enter n: ")
m = input("Enter m: ")

# обработка исключений
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        n = input("Enter n: ")

while type(m) != int:
    try:
        m = int(m) if int(m) >= n else int(input("Enter m (m >= n): "))
    except ValueError:
        m = input("Enter m: ")

print(f"the sum of a series of numbers from {n} to {m}: {sum_number(n, m)}")

# _________________________________________________________________________________________

# 2
# Описать функцию Power(A, B) вещественного типа,
# находящую величину AB по формуле AB = exp(B*ln(A)) (параметры A и B — вещественные).
# В случае нулевого или отрицательного параметра A функция возвращает 0.
# С помощью этой функции найти степени A^P, B^P, C^P, если даны числа P, A, B, C.


# -> 2 3 4 5
# <- 2.0^5.0 = (4.504829206342167+0j)
# <- 3.0^5.0 = (10.865648224040267+0j)
# <- 4.0^5.0 = (20.293486178313398+0j)


import cmath


# функция
def power(A, B):
    if A <= 0:
        return 0
    return cmath.exp(B * cmath.log10(A))


# переменные
A = input("Enter A: ")
B = input("Enter B: ")
C = input("Enter C: ")
P = input("Enter P: ")

# обработка исключений
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        A = input("Enter A: ")

while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        B = input("Enter B: ")

while type(C) != int:
    try:
        C = int(C)
    except ValueError:
        C = input("Enter C: ")

while type(P) != int:
    try:
        P = int(P)
    except ValueError:
        P = input("Enter P: ")

# вывод
print(f"{A}^{P} = {power(A, P)}")
print(f"{B}^{P} = {power(B, P)}")
print(f"{C}^{P} = {power(C, P)}")
