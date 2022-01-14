import matplotlib.pyplot as plt
import numpy as np

r = np.genfromtxt("metoda1_export.txt", usecols=2, delimiter=";")
ne = np.genfromtxt("metoda1_export.txt", usecols=3, delimiter=";")

plt.hist(ne, cumulative=True, color="#45c466", bins=ne)
plt.title("Metoda 1: N(e)")
plt.xlabel(r'$n e_0$[As]')
plt.ylabel(r"N")
plt.show()
