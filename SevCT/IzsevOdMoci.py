import matplotlib.pyplot as plt
import numpy as np

P_elek = np.genfromtxt("Moc_Export.txt", usecols=0, skip_header=1)
dP_elek = np.genfromtxt("Moc_Export.txt", usecols=1, skip_header=1)
P_izsev = np.genfromtxt("Moc_Export.txt", usecols=2, skip_header=1)
dP_izsev = np.genfromtxt("Moc_Export.txt", usecols=3, skip_header=1)

P_elekBG = np.genfromtxt("MocBG_Export.txt", usecols=0, skip_header=1)
dP_elekBG = np.genfromtxt("MocBG_Export.txt", usecols=1, skip_header=1)
P_izsevBG = np.genfromtxt("MocBG_Export.txt", usecols=2, skip_header=1)
dP_izsevBG = np.genfromtxt("MocBG_Export.txt", usecols=3, skip_header=1)


plt.plot(P_elek, P_izsev, c="#008bfc", alpha=0.1)
plt.errorbar(P_elek, P_izsev, xerr=dP_elek, yerr=dP_izsev, markersize=3, color="#C44BC4", linestyle='None',
             marker="o", capsize=3, label="Data")
plt.plot(P_elekBG, P_izsevBG, c="#f2781b", alpha=0.1)
plt.errorbar(P_elekBG, P_izsevBG, xerr=dP_elekBG, yerr=dP_izsevBG, markersize=3, color="#b2f21b", linestyle='None',
             marker="o", capsize=3, label="Data, BG corrected")
plt.title("Odvisnost celotne izsevane moci v odvisnosti od elektricne moci")
plt.xlabel(r'$P_{elek}$ [W]')
plt.ylabel(r"$P_izsev$ [W]")
plt.legend()
plt.show()
