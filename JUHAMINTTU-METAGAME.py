import random
import time

def prokimble():
    print(" ")
    print("Tervetuloa pelaamaan!")
    print(" ")

    p1=input("Anna ensimmäisen pelaajan nimi: ")
    print("Pelaat hahmoilla A ja a")
    print(" ")
    p2=input("Anna toisen pelaajan nimi: ")
    print("Pelaat hahmoilla B ja b")
    print(" ")

    print("Arvotaan aloittava pelaaja..")
    print(" ")
    time.sleep(1.5)

    from random import randrange
    alottaja=randrange(1,3)
    if alottaja == 1:
        alku=p1
        toka=p2
        print(f"Pelaaja {p1} aloittaa!")
        print(" ")
        time.sleep(1.5)
    else:
        alku=p2
        toka=p1
        print(f"Pelaaja {p2} aloittaa!")
        print(" ")
        time.sleep(1.5)

    #Pelialusta - ympyrä - on tallennettuna 6 x 6 matriisina 

    peli=["A","a","O","O","O","O","B","b","O","O","O","O"] #ALKUtilanne

    koko=[[" ", " ", peli[0], peli[1], " ", " "],[" ", peli[11], " ", " ", peli[2], " "],[peli[10], " ", " ", " ", " ", peli[3]],[peli[9], " ", " ", " ", " ", peli[4]],[" ", peli[8], " ", " ", peli[5], " "],[" ", " ", peli[7], peli[6], " ", " "]]

    for rivi in koko:
        print(*rivi)

    laskuri=0 #vuorolaskuri

    while True:

        #Vuoron alussa päätetään:
            # a) Kumpaa nappulaa liikutetaan
            # b) Myötä- vai vastapäivään
            # c) Heitetään painotettua noppaa (1-5)
        laskuri+=1
        if laskuri == 1:
            pass
        else:
            if laskuri % 2 ==0:
                print(" ")
                print(f"Pelaajan {toka} vuoro!")
                print(" ")
            else:
                print(" ")
                print(f"Pelaajan {alku} vuoro!")
                print(" ")

        print("")
        nap=input("Mitä nappulaa siirretään? ")
        print(" ")
        suunta=input("Myötä- vai vastapäivään? (M/V) ")
        print(" ")
        if suunta != "M" and suunta!= "V" and suunta != "m" and suunta!="v":
            print("Vastaa M tai V!")
            suunta=input("Myötä- vai vastapäivään? (M/V) ")

        noppa=(1,2,2,3,3,4,5)
        siirto=random.choice(noppa)
        print("Nopasta sait..")
        time.sleep(1)
        print(siirto)
        print(" ")
        time.sleep(1)

        if suunta == "V" or suunta == "v":
            siirto=-siirto

        #Nappulat tallennetaan pelialustaan uudelle paikalle riippumatta mitä paikalla ennestään oli
        #Nappulan vanha paikka kirjoitetaan tyhjäksi paikaksi eli "O"

        nyky=peli.index(nap)
        if  nyky + siirto >= len(peli):
            uusi_siirto = nyky + siirto - len(peli)
            peli[uusi_siirto]=nap
        else:
            peli[nyky+siirto]=nap

        peli[nyky]="O"

        koko=[[" ", " ", peli[0], peli[1], " ", " "],[" ", peli[11], " ", " ", peli[2], " "],[peli[10], " ", " ", " ", " ", peli[3]],[peli[9], " ", " ", " ", " ", peli[4]],[" ", peli[8], " ", " ", peli[5], " "],[" ", " ", peli[7], peli[6], " ", " "]]

        for rivi in koko:
            print(*rivi)

        
        #Vuoron lopussa tarkistetaan, onko jomman kumman pelaajan kaikki nappulat syöty
        #Jos jommallakummalla ei ole pelinappuloita, on toinen voittanut pelin
        if "A" not in peli:
                if "a" not in peli:
                    print(f"{p2} voitti!")
                    voittaja=p2
                    break

        if "B" not in peli:
                if "b" not in peli:
                    print(f"{p1} voitti!")
                    voittaja=p1
                    break


    print("Kiitos pelistä!")

    #Tallennetaan tässä vaiheessa pelin tiedot merkkijonona tiedostoon
    taulukkolista=[]
    with open("taulukko.txt","a") as taulukko:
        peli=(p1, p2, str(laskuri), voittaja)
        b=",".join(peli)
        taulukko.write(b+"\n")



def kaikki_tiedot():
    """Tulostaa kaikkien pelien tulokset"""
    with open ("taulukko.txt") as tiedosto:
        sisalto=tiedosto.readlines()

        for rivi in sisalto:
            osat=rivi.split(",")

            for i in range(len(osat)):
                 osat[i]=osat[i].replace("\n","")
            
            print(f"Pelaajat: {osat[0]} ja {osat[1]}. Siirtomäärä: {osat[2]}. Voittaja: {osat[3]}.")

def ennatykset():
    """Tulostaa TOP3 vähimmillä siirroilla voittaneet"""
    with open ("taulukko.txt") as tiedosto:
        sisalto=tiedosto.readlines()

        for rivi in sisalto:
            osat=rivi.split(",")

            for i in range(len(osat)):
                 osat[i]=osat[i].replace("\n","")  
    
def pisin_peli():
    """Tulostaa pisimmän pelin pelaajat ja siirtomäärän"""
    uus=[]
    with open("taulukko.txt", "r") as tdsto:
        rivit = [rivi.strip() for rivi in tdsto.readlines()]
        uus=sorted(rivit,key = lambda rivi: int(rivi.split(",")[2]))
        
        print(f"Pelaajat: {osat[0]} ja {osat[1]}. Siirtomäärä: {osat[2]}. Voittaja: {osat[3]}.") 




    uusi=[]
    with open ("taulukko.txt") as tiedosto:
        sisalto=tiedosto.readlines()

        for rivi in sisalto:
            osat=rivi.split(",")

            for i in range(len(osat)):
                osat[i]=osat[i].replace("\n","")

            uusi=sorted(rivit,key = lambda rivi: int(rivi.split(",")[2]))

            if pelaaja == osat[0] or pelaaja == osat[1]:
                print(f"Pelaajat: {osat[0]} ja {osat[1]}. Siirtomäärä: {osat[2]}. Voittaja: {osat[3]}.")            
            
def omatpeli(pelaaja:str):
        """Tulostaa pelaajan kaikki pelit"""
        with open ("taulukko.txt") as tiedosto:
            sisalto=tiedosto.readlines()

            for rivi in sisalto:
                osat=rivi.split(",")

                for i in range(len(osat)):
                    osat[i]=osat[i].replace("\n","")


                if pelaaja == osat[0] or pelaaja == osat[1]:
                    print(f"\n Pelaajat: {osat[0]} ja {osat[1]}. Siirtomäärä: {osat[2]}. Voittaja: {osat[3]}.")

def poista():
    """Tyhjentää tiedoston"""
    valinta=input("Haluatko varmasti poistaa kaikki tiedot? K/E ")
    if valinta == "K" or valinta == "k":
        with open ("taulukko.txt", "w") as tiedosto:
            tiedosto.write("")
        print(" ")
        print("Tyhjennetty!")
        print(" ")
    else: 
        pass
            


def tulostaulu():
    #Luodaan tuloksia varten tiedosto nimellä taulukko.txt
    with open ("taulukko.txt") as taulukko:
    
        while True:
            print(" ")
            print("Mitä haluat nähdä?")
            print(" ")
            print("1. Kaikki pelit.\n2. TOP3 nopeinta voittoa.\n3. Pisimpään kestäneen pelin.")
            print("4. Tietyn pelaajan pelit.\n5. Haluan tyhjentää tulostaulukon.\n0. Poistu")
            print(" ")
            valinta2=int(input("->  "))
            print(" ")

            #Jokaisen näytetyn listan jälkeen pidetään 3 sekunnin lukutauko pelaajille
            if valinta2 == 0:
                print("Hei hei!")
                break
            elif valinta2 == 1:
                kaikki_tiedot()
                time.sleep(3)
            elif valinta2 == 2:
                ennatykset()
                time.sleep(3)
            elif valinta2 == 3:
                pisin_peli()
                time.sleep(3)
            elif valinta2==4:
                omatpeli(input("Kenen pelejä haluat tarkastella? "))
                time.sleep(3)
            elif valinta2 == 5:
                poista()
                time.sleep(3)


def paaohjelma():
    print("Mitä haluat tehdä?")
    print("1. Pelata ProKimbleä")
    print("2. Tarkastaa pelitulokset")

    vast = int(input("->  "))
    if vast == 1:
        while True:
            prokimble()
            jatko=input("Haluatko pelata uudelleen? K/E ")
            if jatko != "K" and jatko != "k":
                break
        
    if vast == 2:
        tulostaulu()
    else:
        print("Heippa!")

    #Ensimmäisellä kerralla oletetaan, ettei valintaa "0 - poistu" tarvita. Lisätään se kuitenkin ensimmäisen valinnan jälkeen.
    while True:
        print("Mitä haluat tehdä?")
        print("1. Pelata ProKimbleä")
        print("2. Tarkastaa pelitulokset")
        print("0. Poistu")
        vast = int(input("->  "))
        if vast == 1:
            while True:
                prokimble()
                jatko=input("Haluatko pelata uudelleen? K/E ")
                if jatko != "K" and jatko != "k":
                    break
            

        if vast == 2:
            tulostaulu()
        else:
            print("Heippa!")
            break

paaohjelma()
