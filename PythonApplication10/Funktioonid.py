from math import *
import datetime
def arithmetic(a1:float,symbol:str,a2:float):
    """Lihtne kalkulaator
    + liitmine, - lahutamine, * korrutamine, / jagamine
    :param float a1: Esimene arv
    :param float a2: Teine arv
    :param str symbol: Tehing
    :rtype: var Määramata tüüp
    """
    if symbol in ["+","-","/","*"]:
        if symbol=="/" and a2==0:
            vas="Div/0"
        else:
            vas=eval(str(a1)+symbol+str(a2))
    else:
        vas="Tundmatu tehing!"
    return vas

def is_year_leap(year:int)->bool:
    """Liiga-aasta leidmine
    Tagastab True kui aasta on liigaasta ja False kui ei ole 
    :param int year: Aasta number
    :rtype: bool funktsiooni vastus loogilises formaadis
    """
    year=int(year)
    if year % 4 == 0:
        t=True
    else:
        t=False
    return t

def square(k:float):
    """Ümbermõõdu, ruudupindala, ruudu diagonaal leidmine
    Tagastab 3 argumendi 
    :param float katet1: arv
    :rtype: var määramata tüüp
    """
    try:
        k=float(k)
        if k>0:
            P=4*k
            S=k**2
            d=k*sqrt(2)
            return P, S, d
        else:
            v="---"
            return v
    except:
        v="---"
        return v
def season(kuupäev:int):
    """Kuupäeva määramine
    Tagastab kuupäeva aasta, mille see kuupäev kuulub(Talv, Kevad, Suvi, Sügis)
    :param int kuupäev: arv(1-12)
    :rtype: See arv ei sobi
    """
    kuupäev=int(kuupäev)
    if kuupäev == 1 or kuupäev == 2 or kuupäev == 12:
        print("Talv")
    elif kuupäev == 3 or kuupäev == 4 or kuupäev ==5:
        print("Kevad")
    elif kuupäev == 6 or kuupäev == 7 or kuupäev == 8:
        print("Suvi")
    elif kuupäev == 9 or kuupäev == 10 or kuupäev ==11:
        print("Sügis")
    else:
        print("Viga")
def bank(p,years):
    """ p= money, it can take 2 position
    :param p:int or float
    :param years: int or float
    """
    for each_year in range(years):
        p = (p * 1.1)
    return p
def is_prime(ordinary):
    #"""ordinary num divides without residue and only by itself
    #:param ordinary: int
    #"""
    for i in range(2, (ordinary//2)+1):
        if ordinary % i == 0:
            return False
    return True
def date(y:int,m:int,d:int):
    """based on datetime
    :param y:int
    :param m:int
    :param d:int
    """
    try:
        data=datetime.date(y,m,d)
        print(data)
        print("existing date")
    except:
        print("such date doesnt exist")

        return date

def xor_cipher(str,key):
    """encrypts the string 
    with key.
    """
    encript_str=""
    for letter in str:
        encript_str+=chr(ord(letter)^key)

    return encript_str