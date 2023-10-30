# Soru1: Bir dikdörtgeni temsil eden "Rectangle" adında bir Python sınıfı oluşturun. Rectangle sınıfı aşağıdaki özelliklere ve yöntemlere sahip olmalıdir:
#
# Özellikler:
# genişlik (bir tam sayı)
# yükseklik (bir tam sayı)
# Yöntemler:
# alan(self): Dikdörtgenin alanını hesaplayan ve döndüren bir yöntem.
# çevre(self): Dikdörtgenin çevresini hesaplayan ve döndüren bir yöntem.
# Rectangle sınıfından bir örnek oluşturun, genişliğini 5 ve yüksekliğini 7 olarak ayarlayın, ardından alanını ve çevresini yazdırın.

class Rectangle():
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan(self):
        return self.genislik*self.yukseklik
    def cevre(self):
        return 2 * (self.genislik+self.yukseklik)

Dikdortgen = Rectangle(5,7)

alan = Dikdortgen.alan()
print("Dikdortgenin alani:", alan)
cevre = Dikdortgen.cevre()
print("Dikdortgenin cevresi:", cevre)


# Soru2: Python'da bir "Okul" sınıfı oluşturun. Bu sınıf aşağıdaki özelliklere ve işlevselliklere sahip olmalıdır:
#
# Özellikler:
# "ad"
# "kuruluş_yılı"
# "öğrenciler"
# "öğretmenler"
# Metodlar:
# yeni_öğrenci_ekle(self, öğrenci_adı, sınıf): Yeni bir öğrenciyi okula eklemek için kullanılan bir metod. Öğrencinin
# adını ve sınıfını alır ve "öğrenciler" listesine ekler.
# yeni_öğretmen_ekle(self, öğretmen_adı, branş): Yeni bir öğretmeni okula eklemek için kullanılan bir metod. Öğretmenin
# adını ve branşını alır ve "öğretmenler" sözlüğüne ekler.
# öğrenci_listesi_görüntüle(self): Okula kayıtlı öğrencilerin listesini görüntülemek için kullanılan bir metod. Öğrenci
# adlarını ve sınıflarını listeleyin.
# öğretmen_listesi_görüntüle(self): Okulda çalışan öğretmenlerin listesini görüntülemek için kullanılan bir metod.
# Öğretmen adlarını ve branşlarını listeleyin.


class Okul():
    def __init__(self, ad, kurulus_yili):
        self.ad = ad
        self.kurulus_yili = kurulus_yili
        self.ogrenciler = []
        self.ogretmenler = {}
    def yeni_ogrenci_ekle(self, ogrenci_adi, sinifi):
        ogrenci = {"ad":ogrenci_adi,  "sinif": sinifi}
        self.ogrenciler.append(ogrenci)

    def ogrenci_listesi_goruntule(self):
        print("Okula kayıtlı öğrenciler:")
        for ogrenci in self.ogrenciler:
            print(f"Ad: {ogrenci['ad']}, Sınıf: {ogrenci['sinif']}")
    def yeni_ogretmen_ekle(self, ogretmen_adi, brans):
        self.ogretmenler[ogretmen_adi] = brans
    def ogretmen_listesi_goruntule(self):
        print("Okulda calisan ogretmenler:")
        for ogretmen, brans in self.ogretmenler.items():
            print(f"Isim: {ogretmen}, Brans: {brans}")

okul1 = Okul("Ozgur Okul", 1986)
okul1.yeni_ogrenci_ekle("Ali Cabbar", "6/D")
okul1.yeni_ogretmen_ekle("Mehmet Hoca", "Fen bilgisi")

okul1.ogrenci_listesi_goruntule()
okul1.ogretmen_listesi_goruntule()


  
