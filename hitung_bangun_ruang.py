import math

def luas_kubus():
    return 6 * sisi * sisi

def luas_balok():
    return 2 *p*l + 2*p*t + 2*l*t

def luas_tabung():
    return 2 *phi *r *(r+t)

def luas_limas():
    return luas_alas + luas_sisi_tegak

def luas_prisma():
    return (2* luas_alas) + (keliling * tinggi)