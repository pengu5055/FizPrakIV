import matplotlib.pyplot as plt
from math import sin
import numpy as np
from scipy.optimize import curve_fit

lam = 632.8 * 10**-9
n_perp = 1.532
n_para = 1.708

def theoreticalfit(alpha, p0, p1, f):
    return p1 * (np.sin(f*(np.sqrt(n_perp**2 - (np.sin(alpha))**2) - np.sqrt(n_para**2 - (np.sin(alpha))**2))))**2 + p0


kot = np.genfromtxt("Zasuk.txt", skip_header=1, usecols=0)
kot_rad = np.array([np.deg2rad(value/2) for value in kot])
I = np.genfromtxt("Zasuk.txt", skip_header=1, usecols=1)
I_0 = 4.02 * 10**-4
I_err = [0.05 * element/I_0 for element in I]

print(len(kot_rad))
fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(theoreticalfit, xdata=kot_rad, ydata=(I/I_0), p0=[1.7, 0, 288],
                           bounds=([-4, -4, 200], [2, 1, 300]),
                           method="trf", loss="linear", verbose=2)
print(fitpar)
yfit = theoreticalfit(kot_rad, fitpar[0], fitpar[1], fitpar[2])
print(len(yfit))
fittext= "Model fit:\n$P_0$ = {} ± {}\n$P_1$ = {} ± {}\n$f$ = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                              format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"),
                                                                              format(fitpar[2], ".4e"), format(fitcov[2][2]**0.5, ".4e"))

plt.errorbar(kot_rad, I/I_0, xerr=0.0174533, yerr=I_err, markersize=3, color="#27b7f5", linestyle='None',
             marker="o", capsize=2, label=r"Data", alpha=1)

plt.plot(kot_rad, yfit, color="#c7006a")
plt.title("Prepuscena moc v odvisnosti zasuka celice tekocega kristala")
plt.xlabel(r"$\alpha$ [rad]")
plt.ylabel(r"$\frac{I}{I_0}$")
plt.text(0.25, 0.175, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.show()
