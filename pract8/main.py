import random as rd

n, k = 6, 6
matrix = []
for r in range(n):
    b = []
    for c in range(k):
        b.append(rd.randint(1, 10))
    matrix.append(b)

def print_matrix(matrix):
    for _ in range(n):
        for __ in range(n):
            print(matrix[_][__], end=' ')
        print()

print_matrix(matrix)

for n in range(0, len(matrix)):
    print(f"matrix[{k-1}][{n}] / matrix[[{n}], [{n}]] = \
        {matrix[k-1][n] / matrix[n][n]}")

t = []
for i in range(len(matrix)):
    t_r = []
    for r in matrix:
        t_r.append(r[i])
    t.append(t_r)
    
print('Траспонированная матрица')
print(t)