'''
Cara membaca kode Python? Ngurut aja. Dari atas ke bawah. :)
'''

import string

print "Halo.. ini modul utama aplikasi"
print "Menghitung rumus luas segitiga ya : (alas*tinggi)/2"
alas = 30
tinggi = 40
luas = (alas * tinggi) / 2
print string.join(["Maka luasnya adalah ",`luas`])
