import numpy as np
import matplotlib.pylab as plt

def funkcja_przystosowania(x):
    return np.sin(x/10.0)*np.sin(x/200)

if __name__ == '__main__':
    rozrzut = 10
    wsp_przyrostu = 1.1
    l_iteracji = 100
    zakres_zmiennosci = [0,100]

    wykresX = np.linspace(zakres_zmiennosci[0], zakres_zmiennosci[1], 100)
    wykresY = funkcja_przystosowania(wykresX)

    x = np.random.uniform(zakres_zmiennosci[0],zakres_zmiennosci[1])
    y = funkcja_przystosowania(x)

    for i in range(l_iteracji):
        plt.plot(wykresX, wykresY,label="sin(x/10.0)*sin(x/200)")
        plt.xlim([0, 100])
        plt.ylim([-0.4, 0.4])
        plt.xlabel('x')
        plt.ylabel('Y')
        plt.plot(x, y, 'ro')
        x_pot = x + np.random.uniform(-rozrzut,rozrzut)
        if x_pot > 100:
            x_pot = 100
        elif x_pot < 0:
            x_pot = 0
        y_pot = funkcja_przystosowania(x_pot)
        if y_pot >= y:
            x = x_pot
            y = y_pot
            rozrzut = rozrzut * wsp_przyrostu
        if y_pot<y:
            rozrzut = rozrzut/wsp_przyrostu
        plt.title("Iteracja: {}\n X: {} Y: {} \n Rozrzut: {}".format(i, x, y, rozrzut))
        plt.legend()
        plt.pause(0.5)
        plt.clf()
    plt.close()
    plt.show()