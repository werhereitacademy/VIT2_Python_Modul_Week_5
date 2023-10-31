# Soru2: Python'da bir "Okul" sınıfı oluşturun. Bu sınıf aşağıdaki özelliklere ve işlevselliklere sahip olmalıdır:
#
# Özellikler:
# "ad"
# "kuruluş_yılı"
# "öğrenciler"
# "öğretmenler"
# Metodlar:
# yeni_öğrenci_ekle(self, öğrenci_adı, sınıf): Yeni bir öğrenciyi okula eklemek için kullanılan bir metod. Öğrencinin adını ve sınıfını alır ve "öğrenciler" listesine ekler.
# yeni_öğretmen_ekle(self, öğretmen_adı, branş): Yeni bir öğretmeni okula eklemek için kullanılan bir metod. Öğretmenin adını ve branşını alır ve "öğretmenler" sözlüğüne ekler.
# öğrenci_listesi_görüntüle(self): Okula kayıtlı öğrencilerin listesini görüntülemek için kullanılan bir metod. Öğrenci adlarını ve sınıflarını listeleyin.
# öğretmen_listesi_görüntüle(self): Okulda çalışan öğretmenlerin listesini görüntülemek için kullanılan bir metod. Öğretmen adlarını ve branşlarını listeleyin.

class Okul():
    def __init__(self, ad, kurulus_yili, ogrenciler=None, ogretmenler=None):
        self.ad = ad
        self.kurulus_yili = kurulus_yili
        self.ogrenciler = []
        self.ogretmenler = []

    def yeni_ogrenci_ekle(self, ogrenci_adi, sinif):
        self.ogrenciler.append((ogrenci_adi, sinif))


    def yeni_ogretmen_ekle(self, ogretmen_adi, brans):
        self.ogretmenler.append((ogretmen_adi, brans))


    def ogrenci_listesi_goruntule(self):
        print("Okula kayitli ogrenciler :")
        for ogrenci in self.ogrenciler:
            print(f"{ogrenci[0]} - Sinif : {ogrenci[1]}")

    def ogretmen_listesi_goruntule(self):
        print("Okulda çalışan öğretmenler :")
        for ogretmen in self.ogretmenler:
            print(f"{ogretmen[0]} - Branş: {ogretmen[1]}")

# Okul örneği oluşturma
okul1 = Okul("Örnek Okul", 1990)

# Öğrenci ve öğretmen ekleme
okul1.yeni_ogrenci_ekle("Ahmet", "9. Sınıf")
okul1.yeni_ogrenci_ekle("Ayşe", "10. Sınıf")
okul1.yeni_ogretmen_ekle("Mehmet Hoca", "Matematik")
okul1.yeni_ogretmen_ekle("Zeynep Hoca", "Tarih")

# Öğrenci ve öğretmen listelerini görüntüleme
okul1.ogrenci_listesi_goruntule()
okul1.ogretmen_listesi_goruntule()