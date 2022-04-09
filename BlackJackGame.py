from ast import Return
from random import random
from secrets import randbelow


import random
from telnetlib import PRAGMA_HEARTBEAT
def luo_korttipakka():
    pakka = []
    for x in ["Pata", "Hertta", "Ruutu", "Risti"]:
        for i in range (13):
            pakka.append (x + " " + str(i + 1))
    return pakka

def laske_arvo (kortit) :
    arvo = 0
    for k in kortit:
        if int(k.split () [1] ) > 10:
            arvo = arvo + 10
        else:
            arvo = arvo + int(k.split()[1])
    return arvo

while (input ("Pelataanko {K/E]? ") .upper() == "K") :
    pakka = luo_korttipakka()
    random.shuffle(pakka)

    pelaaja = [pakka]
    jakaja = []
    for i in range(2):
        pelaaja.append(pakka.pop())
        jakaja.append(pakka.pop())

        while True:
            pelaaja_pisteet = laske_arvo(pelaaja)
            print ("PELAAJAN VUORO:")
            print("Pelaaja:", pelaaja_pisteet,  ": ", pelaaja)
            print ("Jakaja:", jakaja [0])
            if pelaaja_pisteet >=21:
                break
            if input("Ota kortti [K]? ").upper() == "K":
                pelaaja.append(pakka.pop())
        else:
                break
        if pelaaja_pisteet >21:
                    print ("YLI 21: PEALAAJA HÄVISI!`\n")
                    continue
        elif pelaaja_pisteet ==21:
                    print ("BLACKJACK!: PELAAJA VOITTI!\n!")
                    continue
        while True:
                    jakaja_pisteet = laske_arvo(jakaja)
                    print ("JAKAJAN VUORO:")
                    print ("Pelaaja:", pelaaja_pisteet,": ", pelaaja)
                    print ("Jakaja: ", jakaja_pisteet, ", ", jakaja)
                    if jakaja_pisteet < 16:
                        jakaja.append(pakka.pop())
                    else:
                        break
        if jakaja_pisteet > 21 or jakaja_pisteet < pelaaja_pisteet:
                    print ("PELAAJA VOITTI!\n")
                    
        else:
                    print ("PELAAJA HÄVISI!\n")

