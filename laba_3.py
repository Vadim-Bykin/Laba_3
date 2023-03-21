# Формируется матрица F следующим образом: если в С количество нулевых элементов в нечетных столбцах в области 4 больше, чем количество нулевых  элементов в четных столбцах в области 1,
# то поменять в В симметрично области 2 и 3 местами, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
# После чего вычисляется выражение: ((F * A) – (K * Aт). Выводятся по мере формирования А, F и все матричные операции последовательно.

import random

K_test = 3
N_test = 10
E_test = [
    [9, 5, 1, 6, -3],
    [1, 6, -5, -1, -4],
    [-8, -2, -3, 7, 9],
    [-7, 6, 0, -8, 4],
    [-3, -9, -4, -1, -5]]

B_test = [
    [-8, -7, 1, 1, 10],
    [-1, 10, 5, -10, -6],
    [1, 8, 0, 9, 5],
    [2, 1, -8, -5, -1],
    [-3, -6, 9, 7, -6]]

C_test = [
    [5, 7, -1, -7, -6],
    [2, 3, 10, -8, 4],
    [-4, -7, -10, -4, -5],
    [0, 9, -8, 9, -4],
    [10, -8, -10, -1, 8]]

D_test = [
    [-7, 1, 7, 8, -3],
    [-1, 6, -5, 2, 2],
    [-4, -2, 1, -2, -2],
    [2, -3, 0, -7, -1],
    [-8, -10, 3, 0, -5]]

print('Использовать тестовые данные или случайные?')
choice = input('Ваш выбор (1 - тестовые данные, 2 - случайные, q - выход): ')

if choice == '1':
    K = K_test
    N = N_test
    B, C, D, E = B_test, C_test, D_test, E_test
    n = N // 2  # размерность матриц B, C, D, E (n x n)

if choice == '2':
    K = int(input('Введите K: '))
    N = int(input('Введите N: '))

    if (N % 2 != 0) or ((N / 2) % 2 == 0) or ((N / 2) < 3):
        print('Ошибка в исходных данных. Число N должно быть четным и таким, чтобы число N/2 было нечетным и больше или равно 3')
        exit()

    B, C, D, E = [], [], [], []
    n = N // 2  # размерность матриц B, C, D, E (n x n)
    for row in range(n):
        row_b, row_c, row_d, row_e = [], [], [], []
        for col in range(n):
            row_b.append(random.randint(-10, 10))
            row_c.append(random.randint(-10, 10))
            row_d.append(random.randint(-10, 10))
            row_e.append(random.randint(-10, 10))
        B.append(row_b)
        C.append(row_c)
        D.append(row_d)
        E.append(row_e)

if choice == 'q':
    exit()

A = []
for row in range(n):
    A.append(E[row] + B[row])

for row in range(n):
    A.append(D[row] + C[row])

# печатаем матрицы E, B, C, D, A
print('Матрица E:')
for row in range(n):
    print(E[row])

print('Матрица B:')
for row in range(n):
    print(B[row])

print('Матрица C:')
for row in range(n):
    print(C[row])

print('Матрица D:')
for row in range(n):
    print(D[row])

print('Матрица A:')
for row in range(N):
    print(A[row])

# считаем количество нулевых элементов в нечетных столбцах в области 4 матрицы С
count_zero_c_4 = 0
for row in range(1, n - 1):
    if row <= n // 2:
        end_col = row
    else:
        end_col = n - row - 1
    for col in range(0, end_col):
        # print(C[row][col])
        if (col + 1) % 2 == 1:  # считаем, что нумерация столбцов начинается с 1
            if C[row][col] == 0:
                count_zero_c_4 += 1  # увеличиваем счетчик
print(f'Количество нулевых элементов в матрице С в области 4 в нечетных столбцах: {count_zero_c_4}')

# считаем количество нулевых элементов в нечетных столбцах в области 1 матрицы С
count_zero_c_1 = 0
for col in range(1, n - 1):
    if col <= n // 2:
        end_row = col
    else:
        end_row = n - col - 1
    for row in range(0, end_row):
        # print(C[row][col])
        if (col + 1) % 2 == 0:  # считаем, что нумерация столбцов начинается с 1
            if C[row][col] == 0:
                count_zero_c_1 += 1  # увеличиваем счетчик
print(f'Количество нулевых элементов в матрице С в области 1 в четных столбцах: {count_zero_c_1}')

F = []
if count_zero_c_4 > count_zero_c_1:  # если в матрице С в области 4 больше нулевых элементов, чем в области 1
    for col in range(1, n - 1):  # симметрично меняем области 2 и 3 относительно диагонали
        if col <= n // 2:
            end_row = n - col - 1
        else:
            end_row = col
        for row in range(n - 1, end_row, -1):
            temp = B[row][col]
            B[row][col] = B[col][row]
            B[col][row] = temp
    print('Матрица B после изменений:')
    for row in range(n):
        print(B[row])
    # формируем матрицу F
    for row in range(n):
        F.append(E[row] + B[row])
    for row in range(n):
        F.append(D[row] + C[row])
else:  # если условие не выполнено
    # формируем матрицу F, меняем E и C несимметрично местами
    for row in range(n):
        F.append(C[row] + B[row])
    for row in range(n):
        F.append(D[row] + E[row])

print('Матрица F:')
for row in range(N):
    print(F[row])

F_mult_A = []  # результат перемножения матрицы F на A
for row in range(N):
    F_row = []
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += F[row][j] * A[j][i]
        F_row.append(sum)
    F_mult_A.append(F_row)

print('Матрица F*A: ')
for row in range(N):
    print(F_mult_A[row])

A_transpose = []
for row in range(N):
    A_transpose_row = []  # транспонированная матрица A
    for col in range(N):
        A_transpose_row.append(A[col][row])
    A_transpose.append(A_transpose_row)

print('Транспонированная матрица A: ')
for row in range(N):
    print(A_transpose[row])

A_transpose_mult_K = []  # матрица с результатом умножения K * Aт
for row in range(N):
    cur_row = []
    for col in range(N):
        cur_row.append(0)
    A_transpose_mult_K.append(cur_row)  # формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам

for row in range(N):
    for col in range(N):
        A_transpose_mult_K[row][col] = K * A_transpose[row][col]  # транспонированная матрица А умноженная на константу К

print('Транспонированная матрица A умноженная на K: ')
for row in range(N):
    print(A_transpose_mult_K[row])

result_matrix = []  # результирующая матрица
for row in range(N):  # формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам
    cur_row = []
    for col in range(N):
        cur_row.append(0)
    result_matrix.append(cur_row)

for row in range(N):
    for col in range(N):
        result_matrix[row][col] = F_mult_A[row][col] - A_transpose_mult_K[row][col]

print('Результат: ')
for row in range(N):
    print(result_matrix[row])