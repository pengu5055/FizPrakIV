import matplotlib.pyplot as plt
import numpy as np

T = np.genfromtxt("Razmerje_Export.txt", usecols=0, skip_header=1)
dT = np.genfromtxt("Razmerje_Export.txt", usecols=1, skip_header=1)
B = np.genfromtxt("Razmerje_Export.txt", usecols=2, skip_header=1)
dB = np.genfromtxt("Razmerje_Export.txt", usecols=3, skip_header=1)
Bcorr = np.genfromtxt("Razmerje2_Export.txt", usecols=4, skip_header=1)

T_model = np.genfromtxt("Model_Export.txt", usecols=0, skip_header=1)
B_1 = np.genfromtxt("Model_Export.txt", usecols=1, skip_header=1)
B_2 = np.genfromtxt("Model_Export.txt", usecols=2, skip_header=1)

#plt.scatter(T, Bcorr)
plt.errorbar(T, Bcorr, xerr=dT, yerr=dB, markersize=3, color="#C44BC4", linestyle='None',
             marker="o", capsize=2, label="Data, BG Corrected", alpha=0.5)
plt.plot(T_model, B_1, alpha=0.7, label="Model: Brez upostevanja odboja", color="#6fd7f7")
plt.plot(T_model, B_2, alpha=0.7, label="Model: Z upostevanjem odboja", color="#edb634")
plt.title(r'Razmerje $\frac{P_{Si}}{P_{izsev}}$ v odvisnosti od temperature')
plt.xlabel(r'T [K]')
plt.ylabel(r"$\frac{P_{Si}}{P_{izsev}}$")
plt.legend(loc=1)
plt.show()
