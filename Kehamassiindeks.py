from ast import Str
from math import *
print("Tere! Olen sinu uus sõber - Python!")
nimi=str(input("Palun sisestage oma nimi: "))
print(f"{nimi}, oi kui ilus nimi!")
try:
    vastus=input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
    if vastus==1:
        pikkus=int(float("Sissetus täisarv: "))
        mass=float(input("massiarv: "))
        indeks=round(mass/(0.01*pikkus)**2,2)
        print("Sinu keha indeks on: {indeks}")
    else:
        print("Kahju! See on väga kasulik info!")
        print("")
        print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
    if indeks>=0 and indeks<19:
        print("Alakaal")
    elif indeks<16:
        print("Tervisele ohtlik alakaal")
    elif indeks>19 and indeks<25:
        print("Normaalkaal")
    elif indeks>25 and indeks< 30:
        print("Ülekaal")
    elif indeks>30 and indeks<35:
        print("Rasvumine")
    elif indeks>35 and indeks<40:
        print("Tugev rasvumine")
    elif indeks>40:
        print("Tervisele ohtlik rasvumine")
except:
    print("ValueError")