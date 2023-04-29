import math
from decimal import Decimal
import decimal
from tkinter import Tk, Label, Button, Entry, Frame
from tkinter import *
import webbrowser
from tkinter import filedialog
import sys
import os

# Si exite sys._MEIPASS estamos ejecutando el .exe creado con PyInstaller
# y en ese caso interesa que el directorio de trabajo sea sys._MEIPASS,
# que es donde se descomprime el directorio "resources" en tiempo de ejecución



def main():
    def resolver_ruta(ruta_relativa):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys.MEIPASS, ruta_relativa)
        return os.path.join(os.path.abspath('.'), ruta_relativa)

    def calcpi():
        valorPi = int(nVecesPi.get())
        valorN = valorPi
        # Intente poner 100000 y mi pc no aguanto.
        # Trabajar con la precisión adecuada
        decimal.getcontext().prec = 2*(valorN+3)

        a = Decimal(0)
        i = 3
        pi = Decimal(0)
        a = Decimal(0)

        while True:
            piold = pi
            x1= (2+a).sqrt()
            x = (2-x1).sqrt()
            y = Decimal(pow(2,i-1))
            pi = x*y
            if piold==pi:
                break
            a = (2+a).sqrt()
            i = i + 1 

        print(f"Detenido tras {i} iteraciones")
        print('El valor aproximado de pi es ')
        print(pi)
        # Este es el valor real con 65 digitos #
        # print("3.1415926535897932384626433832795028841971693993751058209749445923")
        resultadoDePi.delete(0,'end')
        resultadoDePi.insert(0,pi)
    def videoYT():
        webbrowser.open("https://youtu.be/-7Of6Y2Aebc")
    def videoYT2():
        webbrowser.open("https://youtu.be/pmNbxqvNu6Q")
    
    calculadora = Tk()
    calculadora.title("Calculadora de Pi (Por MARCUS MATOS)")
    calculadora.geometry("400x400")
    calculadora.config(bg="#B8B8B8")
    #error calculadora.iconbitmap(r'C:\Users\MarcoAntonio\Desktop\CalculadoraPi\resources\piImage.ico')

    nAprox = Label(calculadora,text="Numero de aproximaciones",font=("Helvetica",10))
    nAprox.place(relx=0.03,rely=0.04, relwidth=0.45, relheight=0.1)

    nVecesPi = Entry(calculadora, text="Colocar PI",bg="#DEDEDE",font=("Helvetica",10) )
    nVecesPi.place(relx=0.5,rely=0.04, relwidth=0.46, relheight=0.1)

    btncalcpi=Button(calculadora,text="Calcular Pi",command=calcpi,font=("Helvetica",18))
    btncalcpi.place(relx=0.03,rely=0.17, relwidth=0.93, relheight=0.1)

    resultadoPiTxt = Button(calculadora,text="Diagrama de Flujo", font=("Helvetica",10), command=videoYT2)
    resultadoPiTxt.place(relx=0.03,rely=0.3, relwidth=0.45, relheight=0.1)

    metodoArchimedes=Button(calculadora,text="Video explicativo",font=("Helvetica",10), command=videoYT)
    metodoArchimedes.place(relx=0.5,rely=0.3, relwidth=0.46, relheight=0.1)

    resultadoDePi = Entry(calculadora, bg="#DEDEDE",font=("Helvetica",10))
    resultadoDePi.place(relx=0.03,rely=0.43, relwidth=0.93, relheight=0.53)

    calculadora.mainloop()


if __name__ == "__main__":
    main()