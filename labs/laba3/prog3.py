def lu_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        
        if U[i][i] == 0:
            raise ValueError("Вырожденная матрица")
        
        for j in range(i+1, n): 
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
        
        L[i][i] = 1.0

    return L, U

def solve_lu(A, b):
    n = len(A)
    if len(b) != n:
        raise ValueError("Несовместимые размеры матрицы и вектора")
    
    L, U = lu_decomposition(A)
    
    # Прямая подстановка (Ly = b)
    y = [0.0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    
    # Обратная подстановка (Ux = y)
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]
    
    return x

def read_matrix(filename):
    with open(filename) as f:
        return [[float(x) for x in line.split()] for line in f]

def read_vector(filename):
    with open(filename) as f:
        return [float(x) for x in f.read().split()]

if __name__ == "__main__":
    try:
        A = read_matrix(r'C:\Users\student\Desktop\vychislitelnyye-metody\labs\laba3\a.txt')
        b = read_vector(r'C:\Users\student\Desktop\vychislitelnyye-metody\labs\laba3\b.txt')
        solution = solve_lu(A, b)
        print("Решение системы:")
        print([round(x, 6) for x in solution])
    except Exception as e:
        print(f"Ошибка: {e}")