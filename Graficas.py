
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 6, 100)
x2=np.arange(0, 10,0.2)

y=np.log2(x)
y2=np.log2(x)*x

plt.plot(x, y, label='O(log n)')
plt.plot(x, y2, label='O(n log n)')
plt.plot(x, x, label='O(n)')

plt.plot(x, x**2, label='O(n^2)')

plt.plot(x, 2**x, label='O(2^n)')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title("Complejidad Big O")
plt.legend()
plt.savefig('grafica_Big_O.png')
plt.show()