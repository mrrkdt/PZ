#1
# Дано вещественное число A и целое число N (N>0). Используя один цикл,
# найти значение выражения 1 - А + А^2 + A^3 + ... + (-1)^N. Условный оператор не использовать.

# -> 5.0 4
# <- 147.0

count = 0   # значение выражения
i = 1      # счётчик
A = input("Enter A: ")
N = input("Enter N: ")


# обработка исключений
while type(A) != float:
  try:
    A = float(A)
  except ValueError:
    A = input("Enter A: ")

while type(N) != int:
  try:
    N = int(N) if int(N) > 0 else int(input("Enter N (N > 0): "))
  except ValueError:
    N = input("Enter N: ")

count = 1 - A

while N - 1 > i:
  i += 1
  count = count + A**i

count = count + (-1)**N

print("expression value: ", count)

# _________________________________________________________________________________________

#2
# даны положительные числа А и В (А > В).
# На отрезке длинны А размещено максимально возможное количество отрезков длинны В (без наложений).
# Не используя операции умножения и деления, найти количество отрезков В, размещённых на отрезке А.

# -> 6 2
# <- 3

sum = 0     # число, которое стремится к длинне A
i = 0       # максимально возможное количество отрезков длинны В
A = input("Enter A: ")
B = input("Enter B: ")


# обработка исключений
while type(A) != int:
  try:
    A = int(A) if int(A) > 0 else int(input("Enter A (A > 0): "))
  except ValueError:
    A = input("Enter A: ")

while type(B) != int:
  try:
    B = int(B) if int(B) > 0 and int(B) <= A else int(input("Enter B: "))
  except ValueError:
    B = input("Enter B: ")

while A >= B:
  A -= B
  i += 1
print("number of segments B placed on segment A: ", i)
