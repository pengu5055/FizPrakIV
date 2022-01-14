import matplotlib.pyplot as plt
import numpy as np

T1 = np.genfromtxt("CH1_square_0.csv", delimiter=",", usecols=3)
U1 = np.genfromtxt("CH1_square_0.csv", delimiter=",", usecols=4)
T2 = np.genfromtxt("CH2_square_0.csv", delimiter=",", usecols=3)
U2 = np.genfromtxt("CH2_square_0.csv", delimiter=",", usecols=4)
U0 = 0.043
beta = 8820
timescale = 5*10**-5
d =377

plt.plot(T1, U1/U0, label="Data", c="#27b7f5")
plt.plot(T1, np.exp(-beta*T1), label="Dusenje", linestyle="dashed", c="#d81adb")
plt.plot(T1, np.exp(-beta*T1)*np.cos(d/2 * T1), label="Utripanje", linestyle="dashed")
#plt.plot(T2, U2)
plt.title("CH1 C = 0 pF")
plt.xlabel(r't [s]')
plt.ylabel(r'$\frac{U_1}{U_0}$')
plt.legend()
plt.show()
