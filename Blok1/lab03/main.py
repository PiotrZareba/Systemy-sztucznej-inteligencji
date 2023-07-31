import matplotlib.pyplot as plt
import numpy as np
import math
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

def wyznacz_punkty_x_y(lista,x,y):
    punktX = []
    punktY = []

    for n in range(len(lista)):
        punktX.append(float(lista[n][x]))
        punktY.append(float(lista[n][y]))

    return punktX,punktY

def wylicz_odleglosc_od_srodka(x1,y1,x2,y2):
    odleglosc = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    return odleglosc

def wybierz_srodki(m):
    srodki = []
    for i in range(m):
        srodki.append([np.random.uniform(-2,2),np.random.uniform(-2,2)])
    return srodki

def dzielenie_probek_na_grupy(losowe_punkty,spirala,x,y):
    pogrupowane_punkty = []
    for i in range(len(losowe_punkty)):
        pogrupowane_punkty.append([])
    for i in range(len(spirala)):
        tmp = 0
        wartosc = math.inf
        for j in range(len(losowe_punkty)):
            odleglosc = wylicz_odleglosc_od_srodka(losowe_punkty[j][0],losowe_punkty[j][1],x[i],y[i])
            if odleglosc<wartosc:
                tmp = j
                wartosc=odleglosc
        pogrupowane_punkty[tmp].append([spirala[i][0],spirala[i][1]])
    return pogrupowane_punkty

def wyznacz_nowe_srodki(pogrupowana_lista,m):
    nowe_punkty = []
    for i in range(m):
        x,y = wyznacz_punkty_x_y(pogrupowana_lista[i], 0, 1)
        nowy_punkt_x = 0
        nowy_punkt_y = 0
        for j in x:
            nowy_punkt_x = nowy_punkt_x + j
        for k in y:
            nowy_punkt_y = nowy_punkt_y + k
        nowy_punkt_x = nowy_punkt_x / len(x)
        nowy_punkt_y = nowy_punkt_y / len(y)
        nowe_punkty.append([nowy_punkt_x,nowy_punkt_y])
    return nowe_punkty

def wyznacz_nowe_punkty_grup(podzielone_grupy,m):
    nowe_x = []
    nowe_y = []
    for i in range(m):
        nowe_x.append([])
        nowe_y.append([])
    for i in range(len(podzielone_grupy)):
        for j in range(len(podzielone_grupy[i])):
            nowe_x[i].append(float(podzielone_grupy[i][j][0]))
            nowe_y[i].append(float(podzielone_grupy[i][j][1]))
    return nowe_x,nowe_y
if __name__ == '__main__':
    d1 = wczytaj_dane_z_pliku("spirala.txt")
    d2 = wczytaj_dane_z_pliku("spirala-type.txt")
    spirala = usun_biale_znaki(d1)
    spirala_type = usun_biale_znaki(d2)
    m = 4
    iteracje = 30
    x,y = wyznacz_punkty_x_y(spirala,0,1)
    losowe_punkty =wybierz_srodki(m)
    plt.figure(1)
    for i in range(len(losowe_punkty)):
        plt.plot(losowe_punkty[i][0],losowe_punkty[i][1],'r*')
    podzielone_grupy1 = dzielenie_probek_na_grupy(losowe_punkty, spirala, x, y)
    plt.plot(x,y,'.')
    plt.title("Startowe")
    plt.figure(2)
    for i in range(1,iteracje):
        nowe_srodki1 = wyznacz_nowe_srodki(podzielone_grupy1,m)
        podzielone_grupy1 = dzielenie_probek_na_grupy(nowe_srodki1, spirala, x, y)
        nowe_x1,nowe_y1 = wyznacz_nowe_punkty_grup(podzielone_grupy1,m)
        if i > 0:
            for j in range(len(nowe_srodki1)):
                plt.plot(nowe_srodki1[j][0], nowe_srodki1[j][1], 'b*')
        for k in range(len(podzielone_grupy1)):
            plt.plot(nowe_x1[k], nowe_y1[k], '.',label="Grupa: {}".format(k))
        plt.title("Iteracja: {}".format(i))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.pause(0.5)
        plt.clf()