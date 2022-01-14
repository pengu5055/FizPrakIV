import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def LinearFit(x, k, n):
    return k*x + n


T = np.genfromtxt("Temp2_Export.txt", usecols=0, skip_header=1)
dT = np.genfromtxt("Temp2_Export.txt", usecols=1, skip_header=1)
Ic = np.genfromtxt("Temp2_Export.txt", usecols=2, skip_header=1)


fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(LinearFit, xdata=T, ydata=np.log(Ic))
yfit = LinearFit(T, fitpar[0], fitpar[1])
plt.plot(T, yfit, "r-", label="Linear Fit", c="#24C7F0")
#plt.scatter(T, np.log(Ic), c="#e326ed", alpha=0.8, label="Data", s=5)
plt.errorbar(T, np.log(Ic), xerr=dT, markersize=4, color="#e326ed", linestyle='None',
             marker="o", capsize=2, label="Data", alpha=0.7)
plt.title(r"Linearizirana odvisnost $I_C$ od $T$ pri $U_{BE}=0.57V$")
plt.xlabel(r'T [K]')
plt.ylabel(r"$ln(I_{C}/I_1)$")
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                     format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.5, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.legend()
plt.show()
