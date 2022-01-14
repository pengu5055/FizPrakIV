import matplotlib.pyplot as plt
import numpy as np

# Data import
P_izsev = np.genfromtxt("SevCT_Export.txt", usecols=7, skip_header=1)
dP_izsev = np.genfromtxt("SevCT_Export.txt", usecols=8, skip_header=1)
U = np.genfromtxt("SevCT_Export.txt", usecols=3, skip_header=1)
dU = np.genfromtxt("SevCT_Export.txt", usecols=4, skip_header=1)
I = np.genfromtxt("SevCT_Export.txt", usecols=5, skip_header=1)
dI = np.genfromtxt("SevCT_Export.txt", usecols=6, skip_header=1)

# Temperature calibration  P/S = \simga T^4; T = 2700K at full power P = 4.9mW
S = 1.63 * 10**-8
dS = 10**-10
sigma = 5.67 * 10**-8

# Function plot
def temperature(P_izsev, S):
    return (P_izsev/(sigma * S))**(1/4)


def resistance(U, I):
    return U/I

# Error calculation
def temperror(P_izsev, dP_izsev, S, dS):
    return np.sqrt(((4*S*sigma*(P_izsev/(sigma*S))**(3/4))**-1 * dP_izsev)**2 + ((-P_izsev/(4*S**2 * sigma * (P_izsev/(sigma* S))**(3/4))) * dS)**2)


def resistanceerror(U, dU, I, dI):
    return np.sqrt((1/I * dU)**2 + (-U/I**2 * dI)**2)


# Plotting
plt.plot(temperature(P_izsev, S), resistance(U, I), c="#008bfc", alpha=0.1)
#plt.errorbar(P_elek, P_izsev, xerr=dP_elek, yerr=dP_izsev, markersize=3, color="#C44BC4", linestyle='None',
#             marker="o", capsize=3, label="Data")
plt.title("Elektricna upornost zarnice v odvisnosti od temperature")
plt.xlabel(r'T [K]')
plt.ylabel(r"R [$\Omega]")
plt.show()
