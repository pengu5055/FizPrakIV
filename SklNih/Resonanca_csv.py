import matplotlib.pyplot as plt
import numpy as np
frekv = np.genfromtxt("CH1_Resonanca.csv", delimiter=",", usecols=3)
U1 = np.genfromtxt("CH1_Resonanca.csv", delimiter=",", usecols=4)


plt.plot(frekv, U1, label="Data", c="#27b7f5")
plt.title("CH1 C = 150 pF")
plt.xlabel(r't [s]')
plt.ylabel(r'$\frac{U_1}{U_0}$')
plt.legend()
plt.show()
