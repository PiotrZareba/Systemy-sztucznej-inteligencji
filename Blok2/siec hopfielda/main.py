import numpy as np
from tkinter import *

dlugosc = 25
liczbapikseli=50
szerokosc =5
wysokosc=5

def stworz_liste(n, m):
    lista = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(0)
        lista.append(wiersz)
    return lista
bitmapa=stworz_liste(szerokosc,wysokosc)

wagi = stworz_liste(dlugosc, dlugosc)
obraz_wzorcowy = []
obraz_testowy = []


def okno():
    root = Tk()
    root.geometry('500x580')

    def rysuj(event):
        start_x, start_y = zczytaj_wspolrzedne(event)
        bitmapa[int(start_y/liczbapikseli)][int(start_x / liczbapikseli)] = 1
        print(bitmapa)
        print("X: {} Y: {}".format(event.x,event.y))
        canvas.create_rectangle(start_x, start_y, start_x + liczbapikseli, start_y + liczbapikseli, tag='kwad',
                                fill='black', outline="")

    def usun(event):
        start_x, start_y = zczytaj_wspolrzedne(event)
        bitmapa[int(start_y/liczbapikseli)][int(start_x / liczbapikseli)] = 0
        print(bitmapa)
        canvas.create_rectangle(start_x, start_y, start_x + liczbapikseli, start_y + liczbapikseli, tag='kwad1',
                                fill='white', outline="")

    tekst_o_polu_do_rysowania = Label(root,text="Narysuj obraz")
    tekst_o_polu_do_rysowania.grid(row=0,column=0)

    canvas = Canvas(root, height=250, width=250,bg="white")
    canvas.grid(row=1, column=0,padx=5,pady=5)
    canvas.bind("<Button-1>",rysuj)
    canvas.bind("<Button-3>",usun)

    pole_do_wyswietlania_Wyniku=Canvas(root,height=250,width=250,bg="white")
    pole_do_wyswietlania_Wyniku.grid(row=3,column=0)

    def wyczysc_canvas():
        canvas.create_rectangle(0, 0, 250, 250, tag='kwad2', fill='white', outline="")

    def dodaj():
        global bitmapa
        bit1 = np.reshape(bitmapa,(1,25))
        ucz(bit1)
        bitmapa = stworz_liste(szerokosc, wysokosc)
        wyczysc_canvas()
        print(wagi)

    def napr():
        global bitmapa
        bit = np.reshape(bitmapa,(1,25))
        bit1 = zamien_wartosci(bit)
        napraw(bit1)
        pole_do_wyswietlania_Wyniku.create_rectangle(0, 0, 250, 250, tag='kwad2', fill='white', outline="")
        a = obraz_testowy
        b = stworz_liste(5, 5)
        tmp = 0
        for i in range(len(b)):
            for j in range(len(b[i])):
                b[i][j] = a[0][tmp]
                tmp = tmp + 1
        narysuj_wynik(b)
        bitmapa.clear()
        bitmapa=b


    def narysuj_wynik(list):
        for i in range(len(list)):
            for j in range(len(list[i])):
                if list[i][j] == 1:
                    pole_do_wyswietlania_Wyniku.create_rectangle(j * liczbapikseli, i * liczbapikseli,
                                                                 j * liczbapikseli + liczbapikseli,
                                                                 i * liczbapikseli + liczbapikseli, tag='kwad3',
                                                                 fill='black', outline="")
                else:
                    pole_do_wyswietlania_Wyniku.create_rectangle(j * liczbapikseli, i * liczbapikseli,
                                                                 j * liczbapikseli + liczbapikseli,
                                                                 i * liczbapikseli + liczbapikseli, tag='kwad4',
                                                                 fill='white', outline="")


    button_dodaj_do_listy = Button(root, text="Dodaj obraz wzorcowy", bd=4,command=dodaj)
    button_dodaj_do_listy.place(x=280,y=80,height=40,width=200)
    button_porownaj_obrazy = Button(root,text="Napraw",bd=4,command=napr)
    button_porownaj_obrazy.place(x=280,y=130,height=40,width=200)
    button_wyczysc = Button(root,text="Wyczyść pole do rysowania",bd=4,command=wyczysc_canvas)
    button_wyczysc.place(x=280,y=180,height=40,width=200)
    napis_o_Wyniku=Label(root,text="Najbardziej podobny obraz:")
    napis_o_Wyniku.grid(row=2,column=0)


    return root

def zczytaj_wspolrzedne(event):
    x_start = int(event.x/liczbapikseli)*liczbapikseli
    y_start = int(event.y/liczbapikseli)*liczbapikseli
    print("X: {} Y: {}".format(x_start,y_start))
    return x_start,y_start

def zamien_liste_na_wektor(lista):
    tmp = np.reshape(lista,(1,25))
    return tmp

def zamien_wartosci(lista_z_obrazem):
    tmp = zamien_liste_na_wektor(lista_z_obrazem)
    for i in range(len(tmp[0])):
        if tmp[0][i] > 0:
            tmp[0][i] = 1
        else:
            tmp[0][i] = -1
    return tmp

def ucz(obraz_wzorcowy):
    wektor_obraz_wzorcowy = zamien_wartosci(obraz_wzorcowy)
    tmp = stworz_liste(dlugosc,dlugosc)
    # print("wago",tmp)
    waga=tmp
    for i in range(len(wektor_obraz_wzorcowy[0])):
        for j in range(len(wektor_obraz_wzorcowy[0])):
            if i != j:
                waga[i][j] = tmp[i][j] +(1/dlugosc)* wektor_obraz_wzorcowy[0][i] * wektor_obraz_wzorcowy[0][j]
            else:
                continue
            wagi[i][j] = wagi[i][j]+waga[i][j]
    return waga

def napraw(obraz_test):
    obraz = []
    for i in range(len(obraz_test[0])):
        tmp = 0
        for j in range(len(wagi[i])):
            if i != j:
                suma = obraz_test[0][j]*wagi[i][j]
                tmp = tmp+suma
            else:
                continue
        if tmp >=0:
            # obraz_testowy.append(1)
            obraz.append(1)
        else:
            # obraz_testowy.append(0)
            obraz.append(0)
    obraz_testowy.append(obraz)
    return obraz
if __name__ == '__main__':
    root = okno()

    root.mainloop()