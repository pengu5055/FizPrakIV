import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def ExpFit(x, a, b, c):
    return a*np.exp(b*x) + c


T = np.genfromtxt("Temp_Export.txt", usecols=0, skip_header=1)
dT = np.genfromtxt("Temp_Export.txt", usecols=1, skip_header=1)
Ic = np.genfromtxt("Temp_Export.txt", usecols=2, skip_header=1)


fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(ExpFit, xdata=T[2:], ydata=Ic[2:], p0=[1, 1, 1])
print(fitcov)
yfit = ExpFit(T[2:], fitpar[0], fitpar[1], fitpar[2])
plt.plot(T[2:], yfit, "r-", label="Exp Fit", c="#24C7F0")
#plt.scatter(T, np.log(Ic), c="#e326ed", alpha=0.8, label="Data", s=5)
#plt.plot(T, Ic, c="#24C7F0", alpha=0.3)
plt.errorbar(T[2:], Ic[2:], xerr=dT[2:], markersize=4, color="#e326ed", linestyle='None',
             marker="o", capsize=2, label="Data", alpha=0.7)
plt.title(r"Odvisnost $I_C$ od $T$ pri $U_{BE}=0.5V$")
plt.xlabel(r'T [K]')
plt.ylabel(r"$ln(I_{C}/I_1)$")
fittext= "Exp fit: $y = ae^bx + c$\na = {} ± {}\nb = {} ± {}\nc = {} ± {} ".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                                     format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"),
                                                                                     format(fitpar[2], ".4e"), format(fitcov[2][2]**0.5, ".4e"))
#plt.text(0.5, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.legend()
plt.show()
