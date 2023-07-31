def wczytaj_dane_z_pliku(dane_z_pliku):
    try:
        with open(dane_z_pliku,"r") as f:
            dane = f.readlines()
            return dane
    except:
        print("Nie wczytano danych z pliku")
        return None

def zad1():
    x = wczytaj_dane_z_pliku('iris.txt')
    y = wczytaj_dane_z_pliku('atrybuty.txt')
    probki = []
    for element in x:
        probki.append(element.split())

    szer = 90
    print("-" * szer)

    print("| sepal_lenght_in_cm | sepal_width_in_cm | peta_length_in_cm | petal_width_in_cm | class |")
    print("*" * szer)
    for i in range(len(probki)):
        if probki[i][4] == '1':
            print("| {:18s} | {:17s} | {:17s} | {:17s} | {:11s} |".format(probki[i][0],probki[i][1],probki[i][2],probki[i][3],'Setosa'))
        elif probki[i][4] == '2':
            print("| {:18s} | {:17s} | {:17s} | {:17s} | {:11s} |".format(probki[i][0], probki[i][1], probki[i][2],
                                                                          probki[i][3], 'Versicolour'))
        else:
            print("| {:18s} | {:17s} | {:17s} | {:17s} | {:11s} |".format(probki[i][0], probki[i][1], probki[i][2],
                                                                          probki[i][3], 'Virginica'))
    print("-" * szer)
def zad2():
    y = wczytaj_dane_z_pliku('atrybuty.txt')
    atrybuty = []
    for element in y:
        atrybuty.append(element.split())
    czy_atr_sym = []
    nazwy_atr = []
    for i in range(len(atrybuty)):
        nazwy_atr.append(atrybuty[i][0])
        if atrybuty[i][1] == 's':
            czy_atr_sym.append(True)
        else:
            czy_atr_sym.append(False)
    szer = 48
    print("-" * szer)

    print("|   Nazwa atrybutu   | Czy atrybut symboliczny |")
    print("*" * szer)
    for i in range(len(nazwy_atr)):
        print("| {:18s} | {:10b}              |".format(nazwy_atr[i],czy_atr_sym[i]))

    print("-" * szer)


if __name__ == '__main__':
    zad1()
    zad2()
