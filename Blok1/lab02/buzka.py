import matplotlib.pylab as plt
import numpy as np

if __name__ == '__main__':

    x = [0,-0.765,-1.414,-1.847,-2,-1.847,-1.414,-0.765,0,0.765,1.414,1.847,2,1.847,1.414,0.765,0]
    y = [-2,-1.847,-1.414,-0.765,0,0.765,1.414,1.847,2,1.847,1.414,0.765,0,-0.765,-1.414,-1.847,-2]

    punktyX = [-1,0,1]
    punktyY = [1,0,1]

    usmiechX = np.linspace(-1,1,100)
    usmiechY = np.sin(2*usmiechX - np.pi/2)/1.4-0.29
    plt.plot(x,y,'r',label="lamane")
    plt.plot(punktyX,punktyY,'bo',label="punkty")
    plt.plot(usmiechX,usmiechY,'y',label="sinus")
    plt.title("Minka")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.show()