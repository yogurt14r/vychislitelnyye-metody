def jacobi(A, b, eps=0.01, max_iterations=1000):
    n = len(A)
    x = [0.0 for _ in range(n)]
    x_new = x.copy()

    for iteration in range(max_iterations):
        for i in range(n):
            sum = 0.0
            for j in range(n):
                if j != i:
                    sum += A[i][j] * x[j]
            x_new[i] = (b[i] - sum) / A[i][i]

        converged = True
        for i in range(n):
            if abs(x_new[i] - x[i]) > eps:
                converged = False
                break

        if converged:
            print(f"Решение найдено за {iteration+1} итераций")
            return x_new

        x = x_new.copy()

    print("Достигнуто максимальное количество итераций")
    return x

A = [
    [5, 2, -1],
    [-4, 7, 3],
    [2, -2, 4]
]
b = [12, 24, 9]

solution = jacobi(A, b)
print("Решение:", solution)
