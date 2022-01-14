import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def theoreticalfit(alpha, p0, p1, delta):
    return p1 * (np.sin(alpha + delta))**2 + p0


kot = np.genfromtxt("polarizator_1.txt", skip_header=1, usecols=0)
kot_rad = [np.deg2rad(value) for value in kot]
I = np.genfromtxt("polarizator_1.txt", skip_header=1, usecols=1)
I_0 = 4.02 * 10**-4
I_err = [0.05 * element/I_0 for element in I]


fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(theoreticalfit, xdata=kot_rad, ydata=(I/I_0), p0=[0, -0.7, 15])
yfit = theoreticalfit(kot_rad, fitpar[0], fitpar[1], fitpar[2])
fittext= "Model fit:\n$P_0$ = {} ± {}\n$P_1$ = {} ± {}\n$\delta$ = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                             format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"),
                                                                             format(fitpar[2], ".4e"), format(fitcov[2][2]**0.5, ".4e"))

plt.errorbar(kot_rad, I/I_0, xerr=0.0174533, yerr=I_err, markersize=3, color="#27b7f5", linestyle='None',
             marker="o", capsize=2, label=r"Data", alpha=1)

plt.plot(kot_rad, yfit, color="#c7006a")
plt.title("Odvisnost prepuscene moci od kota polarizatorja")
plt.xlabel(r"$\alpha$ [rad]")
plt.ylabel(r"$\frac{I}{I_0}$")
plt.text(0.25, 0.175, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.show()

