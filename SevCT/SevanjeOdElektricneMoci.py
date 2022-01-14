import matplotlib.pyplot as plt
import numpy as np

P_elek = np.genfromtxt("SevCT_Export.txt", usecols=0, skip_header=1)
dP_elek = np.genfromtxt("SevCT_Export.txt", usecols=1, skip_header=1)
P_izsev = np.genfromtxt("SevCT_Export.txt", usecols=7, skip_header=1)
dP_izsev = np.genfromtxt("SevCT_Export.txt", usecols=8, skip_header=1)


plt.plot(P_elek, P_izsev, c="#008bfc", alpha=0.1)
plt.errorbar(P_elek, P_izsev, xerr=dP_elek, yerr=dP_izsev, markersize=3, color="#C44BC4", linestyle='None',
             marker="o", capsize=3, label="Data")
plt.title("Odvisnost celotne izsevane moci v odvisnosti od elektricne moci")
plt.xlabel(r'P [W]')
plt.ylabel(r"P [mW]")
plt.show()
