import math

N = 1000000

pi_values = [3.14159265358979, 3.141592653589, 3.1415926535, 3.14159265, 3.141592, 3.1415, 3.14, 3]

S = 0
S_recursive = 0

for i in range(1, len(pi_values)):
    print(f"{i})")
    pi_value = pi_values[i - 1]
    for n in range(1, N + 1):
        S += pi_value / (n**2)
    for n in range(N, 0, -1):
        S_recursive += pi_value / (n**2)
    absolute_error = abs(S_recursive - S)
    relative_error = absolute_error / abs(S)
    print(f"Сумма (прямой метод): {S}")
    print(f"Сумма (рекуррентный метод): {S_recursive}")
    print(f"Абсолютная погрешность: {absolute_error}")
    print(f"Относительная погрешность: {relative_error}\n")

# absolute_error = abs(S - S_recursive)
# relative_error = absolute_error / abs(S)

# print(f"Сумма (прямой метод): {S}")
# print(f"Сумма (рекуррентный метод): {S_recursive}")
# print(f"Абсолютная погрешность: {absolute_error}")
# print(f"Относительная погрешность: {relative_error}")

