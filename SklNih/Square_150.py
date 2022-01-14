import matplotlib.pyplot as plt
import numpy as np

T1 = np.genfromtxt("CH1_square_150.csv", delimiter=",", usecols=3)
U1 = np.genfromtxt("CH1_square_150.csv", delimiter=",", usecols=4)
T2 = np.genfromtxt("CH2_square_150.csv", delimiter=",", usecols=3)
U2 = np.genfromtxt("CH2_square_150.csv", delimiter=",", usecols=4)
U0 = 0.043
U0_2 = 0.0184
beta = 8820
timescale = 5*10**-5
d = 25132

plt.plot(T1, U1/U0, label="Data", c="#27b7f5")
plt.plot(T1, np.exp(-beta*T1)*np.cos(d/2 * T1), label="Utripanje", linestyle="dashed", c="#d81adb")
#plt.plot(T2, U2/U0_2, label="Data", c="#27b7f5")
#plt.plot(T2, np.exp(-beta*T2)*np.cos(d/2 * T2), label="Utripanje", linestyle="dashed", c="#d81adb")
#plt.plot(T2, U2)
plt.title("CH1 C = 150 pF")
plt.xlabel(r't [s]')
plt.ylabel(r'$\frac{U_1}{U_0}$')
plt.legend()
plt.show()
