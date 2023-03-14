# Поляков Андрей ИУ7-12Б
#
# КВ цел матрица сумму в левом и правом треугольнике без учета диагональных

n = int(input("Размер матрицы: "))
arr = [[0] * n for i in range(n)]
m_width = 0
for i in range(n):
    for j in range(n):
        x = input(f"x{i + 1},{j + 1}: ")
        arr[i][j] = int(x)
        m_width = max(len(x), m_width)

for i in range(n):
    for j in range(n):
        print(f"| {str(arr[i][j]).center(m_width)} |", end='')
    print("")

tri_sum = 0
for i in range(n):
    for j in range(n):
        if (j < i < n - j - 1) or (j > i > n - j - 1):
            tri_sum += arr[i][j]

print(f"Сумма: {tri_sum:g}")
