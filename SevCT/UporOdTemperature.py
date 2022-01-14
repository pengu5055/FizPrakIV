import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

T = np.genfromtxt("UporBG_Export.txt", usecols=0, skip_header=1)
dT = np.genfromtxt("UporBG_Export.txt", usecols=1, skip_header=1)
R = np.genfromtxt("UporBG_Export.txt", usecols=2, skip_header=1)
dR = np.genfromtxt("UporBG_Export.txt", usecols=3, skip_header=1)


def LinearFit(x, k, n):
    return k*x + n

#plt.plot(T, R, c="#008bfc", alpha=0.1)
fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(LinearFit, xdata=T, ydata=R)
yfit = LinearFit(T, fitpar[0], fitpar[1])
plt.plot(T, yfit, "r-", label="Linear Fit", c="#24C7F0", alpha=0.2)
plt.errorbar(T, R, xerr=dT, yerr=dR, markersize=3, color="#C44BC4", linestyle='None',
             marker="o", capsize=3, label="Data, BG Corrected")
plt.title("Elektricna upornost zarnice v odvisnosti od temperature")
plt.xlabel(r'T [K]')
plt.ylabel(r"R [$\Omega$]")
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                     format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.5, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.legend()
plt.show()
