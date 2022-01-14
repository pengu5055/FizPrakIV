import matplotlib.pyplot as plt
import numpy as np
T_pravokotno = np.genfromtxt("Pravokotno_Export.txt", skip_header=1, usecols=0)
C_pravokotno = np.genfromtxt("Pravokotno_Export.txt", skip_header=1, usecols=1)
T_vzporedno = np.genfromtxt("Vzporedno_Export.txt", skip_header=1, usecols=0)
C_vzporedno = np.genfromtxt("Vzporedno_Export.txt", skip_header=1, usecols=1)
T_povprecje = np.genfromtxt("Povprecje_Export.txt", skip_header=1, usecols=0)
E_povprecje = np.genfromtxt("Povprecje_Export.txt", skip_header=1, usecols=1)
T_aniz = np.genfromtxt("Anizotropija_Export.txt", skip_header=1, usecols=0)
E_aniz = np.genfromtxt("Anizotropija_Export.txt", skip_header=1, usecols=1)

C_0_pravokotno = 0.06  # nF
C_0_vzporedno = 0.05  # nF

plt.plot(T_pravokotno, C_pravokotno/C_0_pravokotno, c="#27b7f5", alpha=0.3)
plt.plot(T_vzporedno, C_vzporedno/C_0_vzporedno, c="#d757d9", alpha=0.3)
plt.plot(T_povprecje, E_povprecje, c="#fce005", alpha=0.3)
plt.plot(T_aniz, E_aniz, c="#93f55b", alpha=0.3)
plt.errorbar(T_pravokotno, C_pravokotno/C_0_pravokotno, xerr=0.1, markersize=3, color="#27b7f5", linestyle='None',
             marker="o", capsize=2, label=r"$\epsilon_{\perp}$", alpha=1)
plt.errorbar(T_vzporedno, C_vzporedno/C_0_vzporedno, xerr=0.1, markersize=3, color="#d757d9", linestyle='None',
             marker="o", capsize=2, label=r"$\epsilon_{\parallel}$", alpha=1)
plt.errorbar(T_povprecje, E_povprecje, xerr=0.1, markersize=3, color="#fce005", linestyle='None',
             marker="o", capsize=2, label=r"$\bar{\epsilon}$", alpha=1)
plt.errorbar(T_aniz, E_aniz, xerr=0.1, markersize=3, color="#93f55b", linestyle='None',
             marker="o", capsize=2, label=r"$\Delta\epsilon$", alpha=1)
plt.axvline(x=330, color="#b50b66", ls="--", label="Temperatura prehoda")
plt.title("Meritev dielektricne anizotropije")
plt.xlabel(r'T [K]')
plt.ylabel(r'$\epsilon$')
plt.legend()
plt.show()
