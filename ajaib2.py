import string

'''
Cara membaca kode Python? Ngurut aja. Dari atas ke bawah. :)

Maka kalau kita kemudian ingin meningkatkan reusabilitas kode, dengan menjadikan kemampuan menghitung luas segitiga ini sebagai fungsi, kita ubah kode berikut ini :
'''

def hitung_luas_segitiga(alas,tinggi):
    return (alas * tinggi) / 2


print "Halo.. ini modul utama aplikasi"
print "Menghitung rumus luas segitiga ya : (alas*tinggi)/2"
alas = 30
tinggi = 40
luas = hitung_luas_segitiga(alas, tinggi)
print string.join(["Maka luasnya adalah ",`luas`])
