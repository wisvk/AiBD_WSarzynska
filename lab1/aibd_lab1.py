import numpy as np
import matplotlib.pyplot as plt

#zad 3
y = lambda x: x*x + 5
x1 = np.arange(-1,1, 0.1)
x2 = np.arange(-6,6, 0.1)
x3 = np.arange(0,5, 0.1)

plt.plot(x1, y(x1))
plt.title("Wykres funkcji y = x^2 +5")
plt.xlabel("x")
plt.ylabel("y")
plt.legend("y")
plt.show()

plt.plot(x2, y(x2))
plt.title("Wykres funkcji y = x^2 +5")
plt.xlabel("x")
plt.ylabel("y")
plt.legend("y")
plt.show()

plt.plot(x3, y(x3))
plt.title("Wykres funkcji y = x^2 +5")
plt.xlabel("x")
plt.ylabel("y")
plt.legend("y")
plt.show()

