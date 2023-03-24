# Формируется матрица F следующим образом: если в С количество нулевых элементов в нечетных столбцах в области 4 больше, чем количество нулевых  элементов в четных столбцах в области 1,
# то поменять в В симметрично области 2 и 3 местами, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
# После чего вычисляется выражение: ((F * A) – (K * Aт). Выводятся по мере формирования А, F и все матричные операции последовательно.

import random

K_test = 3
N_test = 11
A_test = [
    [1, 2, 3, 4, 5, 4, -9, 8, -1, 5, 3],
    [6, 7, 8, 9, 10, 2, -4, -8, -5, -1, 3],
    [10, 9, 8, 7, 6, 9, -3, 3, 5, -1, -9],
    [5, 4, 3, 2, 1, -5, 2, 7, 3, 8, 0],
    [1, 2, 3, 4, 5, -4, 3, 3, -2, 4, -1],
    [-1, 8, 6, 10, -3, 7, -8, -9, -9, -5, 2],
    [-2, -6, -3, 1, 2, -3, 0, 5, 0, 0, 7],
    [-7, 10, -4, -8, -9, -9, 0, 5, 0, -10, -4],
    [3, 6, -9, 7, 2, -10, 4, 0, 2, -4, 0],
    [10, 9, 9, 5, 8, -8, -8, 0, 10, -7, 1],
    [6, -5, 0, 1, -5, -3, -5, 0, 7, -2, 0]]

print('Использовать тестовые данные или случайные?')
choice = input('Ваш выбор (1 - тестовые данные, 2 - случайные, q-выход): ')

if choice == '1':
    K = K_test
    N = N_test
    A = A_test

if choice == '2':
    K = int(input('Введите K: '))
    N = int(input('Введите N: '))

    if (N < 6):
        print('Ошибка в исходных данных. Длина сторон матрицы А (N,N) должна быть больше 5!')
        exit()

    A = []
    for row in range(N):
        cur_row = []
        for col in range(N):
            cur_row.append(random.randint(-10, 10))
        A.append(cur_row)

B, C, D, E = [], [], [], []
n = N // 2  # размерность матриц B, C, D, E (n x n)

if N % 2 == 0:
    step = N // 2
else:
    step = N // 2 + 1

for row in range(n):
    row_b, row_c, row_d, row_e = [], [], [], []
    for col in range(n):
        row_e.append(A[row][col])
        row_b.append(A[row][col + step])
        row_d.append(A[row + step][col])
        row_c.append(A[row + step][col + step])
    B.append(row_b)
    C.append(row_c)
    D.append(row_d)
    E.append(row_e)

if choice == 'q':
    exit()

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
    if n % 2 == 1:
        if row <= n // 2:
            end_col = row
        else:
            end_col = n - row - 1
    else:
        if row < n // 2:
            end_col = row
        else:
            end_col = n - row - 1
    for col in range(0, end_col):
        # print(C[row][col])
        if col % 2 == 1:
            if C[row][col] == 0:
                count_zero_c_4 += 1  # увеличиваем счетчик
print(f'Количество нулевых элементов в матрице С в области 4 в нечетных столбцах: {count_zero_c_4}')

# считаем количество нулевых элементов в нечетных столбцах в области 1 матрицы С
count_zero_c_1 = 0
for col in range(1, n - 1):
    if n % 2 == 1:
        if col <= n // 2:
            end_row = col
        else:
            end_row = n - col - 1
    else:
        if col < n // 2:
            end_row = col
        else:
            end_row = n - col - 1
    for row in range(0, end_row):
        # print(C[row][col])
        if col % 2 == 0:
            if C[row][col] == 0:
                count_zero_c_1 += 1  # увеличиваем счетчик
print(f'Количество нулевых элементов в матрице С в области 1 в четных столбцах: {count_zero_c_1}')

F = []
for row in range(N):
    cur_row = []
    for col in range(N):
        cur_row.append(A[row][col])
    F.append(cur_row)

if count_zero_c_4 > count_zero_c_1:  # если в матрице С в области 4 больше нулевых элементов, чем в области 1
    for col in range(1, n - 1):  # симметрично меняем области 2 и 3 матрицы B относительно диагонали
        if n % 2 == 1:
            if col <= n // 2:
                end_row = n - col - 1
            else:
                end_row = col
        else:
            if col < n // 2:
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
    if N % 2 == 0:
        step = N // 2
    else:
        step = N // 2 + 1
    for row in range(n):
        for col in range(n):
            F[row][col] = E[row][col]
            F[row][col + step] = B[row][col]
            F[row + step][col] = D[row][col]
            F[row + step][col + step] = C[row][col]

else:  # если условие не выполнено
    # формируем матрицу F, меняем E и C несимметрично местами
    if N % 2 == 0:
        step = N // 2
    else:
        step = N // 2 + 1
    for row in range(n):
        for col in range(n):
            F[row][col] = C[row][col]
            F[row][col + step] = B[row][col]
            F[row + step][col] = D[row][col]
            F[row + step][col + step] = E[row][col]

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

A_transpose = [] # транспонированная матрица A
for row in range(N):
    A_transpose_row = []
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
    A_transpose_mult_K.append(
        cur_row)  # формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам

for row in range(N):
    for col in range(N):
        A_transpose_mult_K[row][col] = K * A_transpose[row][
            col]  # транспонированная матрица А умноженная на константу К

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
