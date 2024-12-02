#bangun datar
import hitung_bangundatar

from hitung_bangundatar import luas_lingkaran

jari_jari = int(input("masukan nilai jari jari"))
luas= luas_lingkaran(jari_jari)
print(f"luas lingkaran dengan jari-jari {jari_jari} adalah {luas}")

from hitung_bangundatar import luas_persegi
sisi=int(input("masukan nilai sisi "))
luas= sisi*sisi
print(f"luas persegi adalah {luas}")

from hitung_bangundatar import luas_persegi_panjang
panjang = int(input("masukan nilai panjang "))
lebar = int(input("masukan nilai lebar"))
luas= panjang*lebar
print(f"luas dari persegi panjang adalah {luas}")

from hitung_bangundatar import luas_segitiga
alas=int(input("masukan nilai alas "))
tinggi=int(input("masukan nilai tinggi "))
luas= 1/2 * alas * tinggi
print(f"luas segitiga adalah {luas}")

from hitung_bangundatar import luas_jajargenjang
alas=int(input("masukan nilai alas "))
tinggi=int(input("masukan nilai tinggi"))
luas= alas * tinggi
print(f"luas dari jajargenjang adalah {luas}")

#operator
import hitung

from hitung import tambah
tambah
bil1 = int(input("masukan nilai bil1 "))
bil2 = int(input("masukan nilai bil2 "))
from hitung import kurang
kurang
bil1 = int(input("masukan nilai bil1 "))
bil2 = int(input("masukan nilai bil2 "))
from hitung import kali
kali
bil1 = int(input("masukan nilai bil1 "))
bil2 = int(input("masukan nilai bil2 "))
from hitung import bagi
bagi
bil1 = int(input("masukan nilai bil1 "))
bil2 = int(input("masukan nilai bil2 "))
from hitung import pangkat
pangkat
bil1 = int(input("masukan nilai bil1 "))
bil2 = int(input("masukan nilai bil2 "))

#bangun ruang 
import hitung_bangun_ruang

from hitung_bangun_ruang import luas_kubus
sisi=int(input("masukan nilai sisi "))
luas= 6 * sisi * sisi
print(f"luas kubus adalah {luas}")

from hitung_bangun_ruang import luas_balok
p=int(input("masukan nilai panjang"))
l=int(input("masukan nilai lebar"))
t=int(input("masukan nilai tinggi"))
luas= 2 *p*l + 2*p*t + 2*l*t
print(f"luas balok adalah {luas}")

from hitung_bangun_ruang import luas_tabung
phi=3.14
r=int(input("masukan nilai jari jari "))
t=int(input("masukan nilai tinggi "))
luas= 2 *phi *r *(r+t)
print(f"luas tabung adalah {luas}")

from hitung_bangun_ruang import luas_limas
luas_alas=int(input("masukan nilai luas alas "))
luas_sisi_tegak=int(input("masukan nilai sisi tegak "))
luas= luas_alas + luas_sisi_tegak
print(f"luas limas adalah {luas}")

from hitung_bangun_ruang import luas_prisma
luas_alas=int(input("masukan nilai luas alas "))
keliling=int(input("masukan nilai keliling"))
tinggi=int(input("masukan nilai tinggi "))
luas= (2* luas_alas) + (keliling*tinggi)
print(f"luas prisma adalah {luas}")