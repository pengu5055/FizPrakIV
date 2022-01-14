import matplotlib.pyplot as plt
import numpy as np

frekv = np.genfromtxt("Resonanca_0.txt", usecols=0, skip_header=1)
dfrekv = np.genfromtxt("Resonanca_0.txt", usecols=1, skip_header=1)
u1 = np.genfromtxt("Resonanca_0.txt", usecols=2, skip_header=1)
du1 = np.genfromtxt("Resonanca_0.txt", usecols=3, skip_header=1)


plt.errorbar(frekv, u1, xerr=dfrekv, yerr=du1, markersize=3, color="#C44BC4", linestyle='None',
             marker="o", capsize=2, label="Data", alpha=0.5)
plt.title(r'Resonancna krivulja pri $C_0 = 0 pF$')
plt.xlabel(r"$\nu$ [kHz]")
plt.ylabel(r'$U_RMS$ [mV]')
plt.legend()
plt.show()
