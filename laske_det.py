from fractions import Fraction
import math
import os


matriisi = [[0,0,0],[0,0,0],[0,0,0]]
determinantti = 0

def cls():
    os.system("cls" if os.name=="nt" else "clear")
    print("Laske determinantti: \n")

def syota_matriisi():
    for rivi in range(0,3):
        for arvo in range(0,3):
            loop = True
            cls()
            print(matriisi[0])
            print(matriisi[1])
            print(matriisi[2], "\n")
            while loop == True:
                inputti = input(f"syötä arvo {rivi+1,arvo+1}: ")
                if inputti.isdecimal():
                    matriisi[rivi][arvo] = int(inputti)
                    loop = False
                else:
                    print("Käytä kokonaislukuja pölö! Tää ei oo niin fiksu softa!")
                    loop = True           

def laske_determinantti():
    summa1 = matriisi[0][0] * (matriisi[1][1]*matriisi[2][2] - matriisi[1][2]*matriisi[2][1])
    summa2 = matriisi[0][1] * (matriisi[1][0]*matriisi[2][2] - matriisi[1][2]*matriisi[2][0])
    summa3 = matriisi[0][2] * (matriisi[1][0]*matriisi[2][1] - matriisi[1][1]*matriisi[2][0])
    determinantti = summa1 - summa2 + summa3

    print("Determinantti on:")
    print(determinantti)

syota_matriisi()
laske_determinantti()
