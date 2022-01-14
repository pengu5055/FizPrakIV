import matplotlib.pyplot as plt
import numpy as np

U_RMS = np.genfromtxt("Prehod_Export.txt", skip_header=1, usecols=0)
C = np.genfromtxt("Prehod_Export.txt", skip_header=1, usecols=1)

plt.plot(U_RMS, C, c="#2de0ba", alpha=0.3)
plt.errorbar(U_RMS, C, xerr=0.05, markersize=3, color="#2ca88e", linestyle='None',
             marker="o", capsize=2, label=r"Data", alpha=1)
plt.title(r"Odvisnost $C$ od $U_{RMS}$")
plt.xlabel(r"$U_{RMS}$ [V]")
plt.ylabel(r"$C$ [nF]")
plt.legend()
plt.show()
