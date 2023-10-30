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

# Soru3: Bir "Şekil" sınıfı oluşturun. Bu sınıfın altında iki alt sınıf, "Dikdörtgen" ve "Kare" sınıfları oluşturun.
# "Şekil" sınıfı, iki özelliğe sahip olsun: "genişlik" ve "yükseklik."
# "Dikdörtgen" sınıfı, "Şekil" sınıfından miras alsın ve ek olarak bir "alan_hesapla()" metodu eklesin.
# "Kare" sınıfı da "Şekil" sınıfından miras alsın ve aynı "alan_hesapla()" metodunu kullanarak karenin alanını hesaplasın.
# Bir "Dikdörtgen" ve bir "Kare" örneği oluşturun, her birinin genişliğini ve yüksekliğini belirleyin, ve her birinin
# alanını hesaplayarak sonuçları yazdırın.

class Sekil:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan_hesapla(self):
        alan = self.yukseklik * self.genislik
        return alan


class Dikdortgen(Sekil):
    def __init__(self,genislik, yukseklik):
        super().__init__(genislik, yukseklik)
        self.alan= super().alan_hesapla()
        print(f"dikdortgenin alani:{self.alan}")

class Kare(Sekil):
    def __init__(self,kenar_uzunlugu):
        super().__init__(kenar_uzunlugu,kenar_uzunlugu)
        self.alan = super().alan_hesapla()
        print(f"karenin alani: {self.alan}")

dikdortgen = Dikdortgen(5,6)
dikdortgen.alan_hesapla()

kare = Kare(4)
kare.alan_hesapla()

Soru4: Python'da bir "Taşıt" (Vehicle) sınıfı oluşturun. Bu sınıfın aşağıdaki özelliklere sahip olmasını sağlayın:
# #
# # Özellikler:
# # "marka" (Taşıtın markası)
# # "model" (Taşıtın modeli)
# # "yıl" (Taşıtın üretim yılı)
# # Bir "Taşıt" sınıfı oluşturun ve bu sınıftan türetilmiş iki alt sınıf, "AraziAracı" (SUV) ve "SporAraba" (SportsCar)
# # sınıfları oluşturun.
# #
# # "AraziAracı" sınıfı, "Taşıt" sınıfından miras alsın ve ek olarak bir "dört_çeker" özelliği eklesin.
# # "SporAraba" sınıfı da "Taşıt" sınıfından miras alsın ve ek olarak bir "maksimum_hız" özelliği eklesin.
# # Her bir sınıftan birer örnek oluşturun, özelliklerini belirleyin ve bu özellikleri görüntülemek için bir program yazın.
#
# class Vehicle:
#     def __init__(self, marka, model, yil):
#         self.marka = marka
#         self.model = model
#         self.yil = yil
#
#     def ozellikleri_goruntule(self):
#         print(f"Markasi: {self.marka}, Modeli: {self.model}, Yili: {self.yil}")
#
#
# class Suv(Vehicle):
#     def __init__(self, marka, model, yil, dort_ceker):
#         super().__init__(marka, model, yil)
#         self.dort_ceker = dort_ceker
#         super().ozellikleri_goruntule(dort_ceker)
#         print(f"Markasi: {self.marka}, Modeli: {self.model}, Yili: {self.yil}, Dort Ceker: {self.dort_ceker}")
#
# class Sporaraba(Vehicle):
#     def __init__(self, marka, model, yil, maksimum_hiz ):
#         super().__init__(marka, model, yil)
#         self.maksimum_hiz = maksimum_hiz
#         super().ozellikleri_goruntule(self.maksimum_hiz)
#
#
# vehicle1= Vehicle("Ford", "Taunus", 1976)
# vehicle1.ozellikleri_goruntule()
#
# suv= Suv("Renault", "Captur", 2013, "4x4")
# suv.ozellikleri_goruntule()
class Vehicle:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def ozellikleri_goruntule(self):
        print(f"Markasi: {self.marka}, Modeli: {self.model}, Yili: {self.yil}")


class Suv(Vehicle):
    def __init__(self, marka, model, yil, dort_ceker):
        super().__init__(marka, model, yil)
        self.dort_ceker = dort_ceker

    def ozellikleri_goruntule(self):
        super().ozellikleri_goruntule()
        print(f"4x4: {self.dort_ceker}")


class Sporaraba(Vehicle):
    def __init__(self, marka, model, yil, maksimum_hiz):
        super().__init__(marka, model, yil)
        self.maksimum_hiz = maksimum_hiz

    def ozellikleri_goruntule(self):
        super().ozellikleri_goruntule()
        print(f"maksimum hiz: {self.maksimum_hiz}")

vehicle1 = Vehicle("Ford", "Taunus", 1976)
vehicle1.ozellikleri_goruntule()

suv = Suv("Renault", "Captur", "2013", "4x4")
suv.ozellikleri_goruntule()

sporaraba = Sporaraba("Porche", "Carrera",2022, 360)
sporaraba.ozellikleri_goruntule()



