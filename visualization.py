#%%

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

H_0 = float(input("Enter value of Hubble Constant: "))
Omega = float(input("Enter value of matter density parameter: "))

s_cubed = (1 - Omega) / Omega
s = s_cubed**(1/3)
c = 1454.53286893


def eta(a):
    return 2 * sqrt(s_cubed + 1) * (1 / a**4 - 0.1540
                                    * s / a**3 + 0.4304 * s**2 / a**2 + 0.19097 * s_cubed / a + 0.066941 * s**4)**(-1/8)


def d_A(z):
    return 1 / (1 + z) * (c / H_0) * (eta(1) - eta(1 / (1 + z)))


z1 = np.linspace(0, 0.1, 11)
z2 = np.linspace(0.1, 1, 10)
z3 = np.linspace(1, 10, 10)
y1 = [d_A(i) for i in z1]
y2 = [d_A(i) for i in z2]
y3 = [d_A(i) for i in z3]

plt.xlabel('z')
plt.ylabel('dA')
plt.title("Change in angular diameter distance with redshift increase")
plt.plot(z1, y1, '-')
plt.plot(z2, y2, '-')
plt.plot(z3, y3, '-')
plt.show()

# %%
