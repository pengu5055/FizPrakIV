import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

l = 0.0015
d = 0.0014


def theoreticalfit(U, B, p1, phi_0):
    return p1 * (np.sin(np.pi*l/d**2 * B * U**2 + phi_0/2))**2


U = np.genfromtxt("kerr.txt", skip_header=1, usecols=0)
I = np.genfromtxt("kerr.txt", skip_header=1, usecols=1)  # Tokovi v mA
I_0 = 0.402  # V mA
I_err = [0.05 * element/I_0 for element in I]

fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(theoreticalfit, xdata=U, ydata=(I/I_0), p0=[2.11*10**-9, 0.2, 5],
                           bounds=([2.1*10**-9, 0.2, 5], [2.2*10**-9, 0.3, 10]),
                           method="trf", verbose=2, loss="linear")
yfit = theoreticalfit(U, fitpar[0], fitpar[1], fitpar[2])
fittext= "Model fit:\n$B$ = {} ± {}\n$P_1$ = {} ± {}\n$\Phi_0$ = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                             format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"),
                                                                             format(fitpar[2], ".4e"), format(fitcov[2][2]**0.5, ".4e"))

plt.errorbar(U, I/I_0, yerr=I_err, markersize=3, color="#27b7f5", linestyle='None',
             marker="o", capsize=2, label=r"Data", alpha=1)

plt.plot(U, yfit, color="#c7006a")
plt.title("Kerrova Celica")
plt.xlabel(r"U [V]")
plt.ylabel(r"$\frac{I}{I_0}$")
plt.text(0.05, 0.85, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.show()
