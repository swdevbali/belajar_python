import string

'''
Cara membaca kode Python? Ngurut aja. Dari atas ke bawah. :)

Maka kalau kita kemudian ingin meningkatkan reusabilitas kode, dengan menjadikan kemampuan menghitung luas segitiga ini sebagai fungsi, kita ubah kode berikut ini.

Kemudian lagi, kalau kita butuh mengenkapsulasi method tersebut ke dalam kelas tersendiri, misalnya kelas Geometri, maka tinggal ditambahkan satu baris deklarasi nama kelas, dan sesuaikan _INDENTASI_ nya (sangat intuitif), yang merupakan ciri khusus Python dibanding bahasa pemrograman sebelumnya yang saya kuasai.

Kemudian lagi, kode di alam satu file ini bisa aja diimport oleh file python yang lain, sehingga kode utama aplikasi sebaiknya diamakan dengan blok if __name__ == '__main__' : berikut ini. Lagi2, disini _INDENTASI memegang peran penting.

Conclusion : I Really Love Python!!!
'''

class Geometri:
    def hitung_luas_segitiga(self, alas,tinggi):
        return (alas * tinggi) / 2


if __name__ == '__main__' :
    print "Halo.. ini modul utama aplikasi"
    print "Menghitung rumus luas segitiga ya : (alas*tinggi)/2"
    alas = 30
    tinggi = 40
    
    geometri = Geometri()
    luas = geometri.hitung_luas_segitiga(alas, tinggi)
    print string.join(["Maka luasnya adalah ",`luas`])    
