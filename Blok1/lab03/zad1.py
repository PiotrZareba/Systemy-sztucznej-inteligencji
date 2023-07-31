def zadanie1(probki_str,numery_atr):
    probki_num = []
    try:
        if len(probki_str[0]) == len(probki_str[1]):
            for i in range(len(probki_str)):
                probki_num.append([float(probki_str[i][j]) for j in numery_atr])
            return probki_num
        else:
            print("Nierówna długość wierszy")
            return None
    except ValueError:
        print("Nie można przekonwertować elementu")
        return None
if __name__ == '__main__':
    probki_str = [['1','a','2.2'],['3','4','5']]
    numery_atr = [0,2]
    probki_num = []
    tmp = 0
    x = zadanie1(probki_str,numery_atr)
    print(x)