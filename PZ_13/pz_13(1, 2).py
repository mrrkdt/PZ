# 16. В матрице найти суммы элементов каждой строки и поместить их в новый массив.
# Выполнить замену элементов третьего столбца исходной матрицы на полученные
# суммы.

import random

count_colums = int(input("Введите количество столбцов (минимум 3): "))
count_rows = int(input("Введите количество строк: "))

matrix = [[random.randint(1, 10) for _ in range(count_colums)] for _ in range(count_rows)]


print("<--------------- Матрица --------------->")
for rows in matrix:
    print(rows)


sum_rows_matrix = [sum(rows) for rows in matrix]
print("<--------- Суммы строк матрицы ---------->")
print(sum_rows_matrix)

# выполняем замену элементов третьего столбца исходной матрицы на полученные суммы
for r in range(count_rows):
    matrix[r][2] = sum_rows_matrix[r]
print("<------------ Новая матрица ------------->")
for rows in matrix:
    print(rows)

# _________________________________________________________________________________________

# В матрице найти сумму элементов второй половины матрицы.

import random

rows = int(input("Введите четное количество строк: "))
cols = int(input("Введите четное количество столбцов: "))

matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

print("<--------------- Матрицв --------------->")
for row in matrix:
    print(row)


# находим сумму элементов во второй половине по строкам
half_rows = rows // 2
second_half_rows_sum = sum(sum(row) for row in matrix[half_rows:])
print(f"Сумма элементов во второй половине по строкам: {second_half_rows_sum}")


# находим сумму элементов во второй половине по столбцам
half_cols = cols // 2
second_half_cols_sum = sum(sum(row[c] for row in matrix) for c in range(half_cols, cols))
print(f"Сумма элементов во второй половине по столбцам: {second_half_cols_sum}")
