import numpy as np
import math
from tkinter import *

szerokosc = 4
wysokosc = 5
liczbapikseli = 50
obrazy_wzorcowe=[]
obraz_testowy=[]
obraz_najbardziej_podobny=[]
def utworz_liste(szerokosc,wysokosc):
    bitmapa = []
    for i in range(wysokosc):
        dlugosc_wiersza = []
        for j in range(szerokosc):
            dlugosc_wiersza.append(0)
        bitmapa.append(dlugosc_wiersza)
    return bitmapa
bitmapa=utworz_liste(szerokosc,wysokosc)
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

    canvas = Canvas(root, height=250, width=200,bg="white")
    canvas.grid(row=1, column=0,padx=5,pady=5)
    canvas.bind("<Button-1>",rysuj)
    canvas.bind("<Button-3>",usun)

    def wyczysc_canvas():
        canvas.create_rectangle(0, 0, 250, 250, tag='kwad2', fill='white', outline="")
    def dodaj_do_listy_funkcja():
        global bitmapa
        test = bitmapa
        obrazy_wzorcowe.append(test)
        wyswietl_liste()
        bitmapa = utworz_liste(szerokosc,wysokosc)
        wyczysc_canvas()
        print(obrazy_wzorcowe)

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
    def klik():
        global bitmapa
        test = bitmapa
        if len(obraz_testowy)>0:
            obraz_testowy.clear()
            obraz_testowy.append(test)
        else:
            obraz_testowy.append(test)
        wynik = -math.inf
        ktory=0
        for i in range(len(obrazy_wzorcowe)):
            tmp = miara_podobienstwa_obustronnego(obraz_testowy[0],obrazy_wzorcowe[i])
            if tmp>wynik:
                wynik = tmp
                ktory= i
        obraz_najbardziej_podobny.append(obrazy_wzorcowe[ktory])
        print("Najbardziej podobny:{}".format(obrazy_wzorcowe[ktory]))
        print("Wynik najbardziej podobnego:{}".format(wynik))
        print("obraz wz:{}".format(obrazy_wzorcowe))
        print("obraz te:{}".format(obraz_testowy))
        print("dlugosc:{}".format(len(obraz_testowy)))
        narysuj_wynik(obraz_najbardziej_podobny[0])

        #wyczysc_canvas()

    button_dodaj_do_listy = Button(root, text="Dodaj obraz wzorcowy", bd=4, command=dodaj_do_listy_funkcja)
    button_dodaj_do_listy.place(x=250,y=80,height=40,width=200)
    button_porownaj_obrazy = Button(root,text="Znajdź najbardziej podobny obraz",bd=4,command=klik)
    button_porownaj_obrazy.place(x=250,y=130,height=40,width=200)
    button_wyczysc = Button(root,text="Wyczyść pole do rysowania",bd=4,command=wyczysc_canvas)
    button_wyczysc.place(x=250,y=180,height=40,width=200)
    napis_o_Wyniku=Label(root,text="Najbardziej podobny obraz:")
    napis_o_Wyniku.grid(row=2,column=0)

    napis_o_obrazach_wzorcowych = Label(root,text="Obrazy wzorcowe:")
    napis_o_obrazach_wzorcowych.grid(row=2,column=1)

    pole_do_wyswietlania_Wyniku=Canvas(root,height=250,width=200,bg="white")
    pole_do_wyswietlania_Wyniku.grid(row=3,column=0)
    def wyswietl_liste():
        pole_do_wyswietlania_obrazow_wzorcowych.insert(0,obrazy_wzorcowe[-1])
    pole_do_wyswietlania_obrazow_wzorcowych = Listbox(root,height=15,width=40,bg="white")
    pole_do_wyswietlania_obrazow_wzorcowych.grid(row=3,column=1)
    return root

def zczytaj_wspolrzedne(event):
    x_start = int(event.x/liczbapikseli)*liczbapikseli
    y_start = int(event.y/liczbapikseli)*liczbapikseli
    print("X: {} Y: {}".format(x_start,y_start))
    return x_start,y_start

def odleglosc_euklidesowa(x1,y1,x2,y2):
    odleglosc = np.abs(x1-x2)+np.abs(y1-y2)
    return odleglosc

def miara_niepodobienstwa(ba,bb):
    miara = 0
    for i in range(len(ba)):
        for j in range(len(ba[0])):
            if ba[i][j] == 1:
                odl_min = math.inf
                for m in range(len(bb)):
                    for n in range(len(bb[0])):
                        if bb[m][n] == 1:
                            odl_akt = odleglosc_euklidesowa(m,n,i,j)
                            odl_min = min(odl_min,odl_akt)
                miara = miara+odl_min
    return miara

def miara_podobienstwa_obustronnego(ba,bb):
    wynik = -(miara_niepodobienstwa(ba,bb)+miara_niepodobienstwa(bb,ba))
    return wynik

if __name__ == '__main__':
    root = okno()
    root.mainloop()
