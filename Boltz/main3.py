import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def LinearFit(x, k, n):
    return k*x + n


U = np.genfromtxt("Main3_Export.txt", usecols=0, skip_header=1)
Ic = np.genfromtxt("Main3_Export.txt", usecols=1, skip_header=1)


fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(LinearFit, xdata=U, ydata=np.log(Ic))
yfit = LinearFit(U, fitpar[0], fitpar[1])
plt.plot(U, yfit, "r-", label="Linear Fit", c="#24C7F0")
plt.scatter(U, np.log(Ic), c="#e326ed", alpha=0.8, label="Data", s=5)
plt.title(r"Linearizirana odvisnost $I_C$ od $U_{BE}$ pri $T=333K$")
plt.xlabel(r'$U_{BE}$ [V]')
plt.ylabel(r"$ln(I_{C}/I_1)$")
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                     format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.5, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.legend()
plt.show()
