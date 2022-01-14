import matplotlib.pyplot as plt
import numpy as np

ne = np.genfromtxt("metoda2_export_corr.txt", usecols=0)

plt.hist(ne, cumulative=True, color="#fcc203", bins=ne)
plt.title("Metoda 2: N(e)")
plt.xlabel(r'$n e_0$[As]')
plt.ylabel(r"N")
plt.show()
