try:
 
    with open("vedmensky_ub21_input.txt") as f:
        matrix = [[int(x) for x in row.split()] for row in f]

    with open('vedmensky_ub21_output.txt', 'w') as f1:
        n, k = 6, 6
        for n in range(0, len(matrix)):
            f1.writelines(f"matrix[{k-1}][{n}] / matrix[[{n}], [{n}]] = \
                        {matrix[k-1][n] / matrix[n][n]}\n")

        t = []
        for i in range(len(matrix)):
            t_r = []
            for r in matrix:
                t_r.append(r[i])
            t.append(t_r)
        f1.write('Transpose matrix\n')
        for i in t:
            f1.write(str(i))
    print('Success')

except FileNotFoundError:
    print('Файл не найден')