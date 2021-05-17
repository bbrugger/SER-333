import matplotlib.pyplot as plt
import numpy as np


def rayleigh(theta_array):
    return (3/4)*(1 + np.cos(theta_array)**2)


def henyey_greenstein(g, theta_array):
    return (1/4/np.pi)*(1 - g**2)/(1 + g**2 - 2*g*np.cos(theta_array))**(3/2)


def fournier_forand(mi, n, theta_array):
    v = (3 - mi)/2
    delta = 4*(np.sin(theta_array/2)**2)/(3*(n-1)**2)
    delta180 = 4*(np.sin(180/2)**2)/(3*(n-1)**2)

    return (
        (1/(4*np.pi*((1-delta)**2)*delta**v))
        *(v*(1-delta) - (1-delta**v) + (delta*(1-delta**v) - v*(1-delta))*np.sin(theta_array/2)**-2)
        + (1 - delta180**v)/(16*np.pi*(delta180 - 1)*delta180**v)*(3*np.cos(theta_array)**2 - 1)
    )


ticks = np.arange(0.1, 2*np.pi, 0.1)
plt.polar(ticks, rayleigh(ticks), label="Rayleigh")
plt.plot(ticks, henyey_greenstein(0.7, ticks), label="Henyey-Greenstein g=0.7")
plt.plot(ticks, fournier_forand(4.065, 1.175, ticks), label="Fournier-Forand B=0.1")

# plt.ylabel("Função de fase de espalhamento")
# plt.xlabel("Ângulo (rad)")

plt.yscale("symlog")
plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
plt.show()
