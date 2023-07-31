import matplotlib.pyplot as plt

def wczytaj_dane_z_pliku(dane_z_pliku):
    try:
        with open(dane_z_pliku,"r") as f:
            dane = f.readlines()
            return dane
    except:
        print("Nie wczytano danych z pliku")
        return None

def usun_biale_znaki(lista):
    probki = []
    for element in lista:
        probki.append(element.split())
    return probki

def wyznacz_serie(lista,numerSerii):
    seria = []
    lista1 = usun_biale_znaki(lista)
    for i in range(len(lista1)):
        if float(lista1[i][4]) == 1 and numerSerii == 1:
            seria.append(lista1[i])
        elif float(lista1[i][4]) == 2 and numerSerii == 2:
            seria.append(lista1[i])
        elif float(lista1[i][4]) == 3 and numerSerii == 3:
            seria.append(lista1[i])
    return seria

def wyznacz_punkty_x_y(seria,x,y):
    punktX = []
    punktY = []
    for n in range(len(seria)):
        punktX.append(float(seria[n][x]))
        punktY.append(float(seria[n][y]))

    return punktX,punktY

if __name__ == '__main__':
    x=wczytaj_dane_z_pliku('iris.txt')
    lista = usun_biale_znaki(x)
    seria1 = wyznacz_serie(x,1)
    seria2 = wyznacz_serie(x,2)
    seria3 = wyznacz_serie(x,3)

    x11, y11 = wyznacz_punkty_x_y(seria1, 2, 3)
    x12, y12 = wyznacz_punkty_x_y(seria1, 1, 3)
    x13, y13 = wyznacz_punkty_x_y(seria1, 0, 3)
    x14, y14 = wyznacz_punkty_x_y(seria1, 1, 2)

    x21, y21 = wyznacz_punkty_x_y(seria2, 2, 3)
    x22, y22 = wyznacz_punkty_x_y(seria2, 1, 3)
    x23, y23 = wyznacz_punkty_x_y(seria2, 0, 3)
    x24, y24 = wyznacz_punkty_x_y(seria2, 1, 2)

    x31, y31 = wyznacz_punkty_x_y(seria3, 2, 3)
    x32, y32 = wyznacz_punkty_x_y(seria3, 1, 3)
    x33, y33 = wyznacz_punkty_x_y(seria3, 0, 3)
    x34, y34 = wyznacz_punkty_x_y(seria3, 1, 2)

    plt.subplot(2, 2, 1)
    plt.plot(x11, y11, 'r.',label="Setosa")
    plt.plot(x21,y21,'b.',label="Versicolour")
    plt.plot(x31,y31,'g.',label="Virginica")
    plt.xlabel("Petal_length_in_cm")
    plt.ylabel("Petal_width_in_cm")

    plt.title('Przestrzeń numer 1')
    plt.legend()
    plt.subplot(2, 2, 2)
    plt.plot(x12, y12, 'r.', label="Setosa")
    plt.plot(x22, y22, 'b.', label="Versicolour")
    plt.plot(x32, y32, 'g.', label="Virginica")
    plt.xlabel("Sepal_width_in_cm")
    plt.ylabel("Petal_width_in_cm")
    plt.legend()
    plt.title('Przestrzeń numer 2')
    plt.subplot(2, 2, 3)
    plt.plot(x13, y13, 'r.', label="Setosa")
    plt.plot(x23, y23, 'b.', label="Versicolour")
    plt.plot(x33, y33, 'g.', label="Virginica")
    plt.xlabel("Sepal_length_in_cm")
    plt.ylabel("Petal_width_in_cm")
    plt.legend()
    plt.title('Przestrzeń numer 3')
    plt.subplot(2, 2, 4)
    plt.plot(x14, y14, 'r.', label="Setosa")
    plt.plot(x24, y24, 'b.', label="Versicolour")
    plt.plot(x34, y34, 'g.', label="Virginica")
    plt.xlabel("Sepal_width_in_cm")
    plt.ylabel("Petal_length_in_cm")
    plt.legend()
    plt.title('Przestrzeń numer 4')

    plt.show()