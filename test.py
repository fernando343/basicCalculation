from matplotlib import cm  # para manejar colores
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sin(x) + 2*np.cos(y)


resolucion = 100

x = np.linspace(-4, 4, resolucion)
y = np.linspace(-4, 4, resolucion)

x, y = np.meshgrid(x, y)

if __name__ == '__main__':
    z = f(x, y)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(x, y, z, cmap=cm.cool)
    fig.colorbar(surf)
    plt.show()
