import math
from matplotlib import pyplot as plt

N = 1000000

pi_values = [3.14159265358979, 3.141592653589, 3.1415926535, 3.14159265, 3.141592, 3.1415, 3.14, 3]


absolute_errors_o = []
relative_errors_o = []

absolute_errors_m = []
relative_errors_m = []

raznica_absolute = []
raznica_relative = []

labels = []

for i in range(0, len(pi_values)):
    S_exact = 0
    S_o = 0
    S_m = 0
    pi_value = pi_values[i]
    for n in range(N, 0, -1):
        S_exact += math.pi / (n*n)
    
    for n in range(N, 0, -1):
        S_o += pi_value / (n*n)

    for n in range(1, N + 1):
        S_m += pi_value / (n*n)
    
    # Ошибка окрубления
    absolute_error1 = abs(S_exact - S_o)
    relative_error1 = abs((S_exact - S_o) / S_o)
    
    absolute_errors_o.append(absolute_error1)
    relative_errors_o.append(relative_error1)

    # Ошибка окрубления + методологическая ошибка
    absolute_error2 = abs(S_exact - S_m)
    relative_error2 = abs((S_exact - S_m) / S_m)
    
    absolute_errors_m.append(absolute_error2)
    relative_errors_m.append(relative_error2)

    raznica_absolute.append(absolute_errors_o[i] - absolute_errors_m[i])
    raznica_relative.append(relative_errors_o[i] - relative_errors_m[i])
    
    # raznica_absolute.append(absolute_error1 - absolute_error2)
    # raznica_relative.append(relative_error1 - relative_error2)
    

    labels.append(f"x{i}")
    
    print(f"№ {i}")
    print(f"π: {pi_value}")
    print(f"S: {S_exact}")
    print(f"S_o: {S_o}")
    print(f"Δ(S) с ошибкой округления: {absolute_error1}")
    print(f"δ(S) с ошибкой округления: {relative_error1}\n")
    print(f"S_m: {S_m}")
    print(f"Δ(S) с методологической ошибкой: {absolute_error2}")
    print(f"δ(S) с методологической ошибкой: {relative_error2}\n")
for i in range(0, 8):
    print(raznica_absolute[i], raznica_relative[i])
plt.figure(figsize=(9, 9))

plt.subplot2grid((3, 2), (0, 0), colspan=2).plot(labels, absolute_errors_o, marker = '.', label = "Абсолютная погрешность с ошибкой округления")
# plt.yscale('log')
plt.legend()
plt.plot(labels, relative_errors_o, marker = '.', label = "Относительная погрешность с ошибкой округления")
plt.yscale('log')
plt.legend()
plt.title("Ошибка округления")

plt.subplot2grid((3, 2), (1, 0), colspan=2).plot(labels, absolute_errors_m, marker = '.', label = "Абсолютная погрешность с методологической ошибкой")
# plt.yscale('log')
plt.legend()
plt.plot(labels, relative_errors_m, marker = '.', label = "Относительная погрешность с методологической ошибкой")
plt.yscale('log')
plt.legend()
plt.title("Ошибка округления + методологическая ошибка")

plt.subplot2grid((3, 2), (2, 0), colspan=2).plot(labels, raznica_absolute, marker = '.', label = "Разница абсолютной погрешности")
plt.plot(labels, raznica_relative, marker = '.', label = "Разница относительной погрешности")
# plt.yscale('log')
plt.legend()
plt.title("Разница погрешностей")

plt.show()