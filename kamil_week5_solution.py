# SORU1

class Rectangle():
    def __init__ (self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan(self):
        dikdortgen_alan = self.genislik*self.yukseklik
        return "Dikdortgenin alani: {} cm karedir.".format(dikdortgen_alan)
    
    def cevre(self):
        dikdortgenin_cevresi = (self.genislik+self.yukseklik)*2
        return "Dikdortgenin cevresi: {} cm dir.".format(dikdortgenin_cevresi)
    
rectangle1 = Rectangle(5,7)
print(rectangle1.alan())
print(rectangle1.cevre())

print("----------------------------")

#SORU2

class Okul():
    def __init__ (self, ad, kurulus_yili):
        self.ad = ad
        self.kurulus_yili = kurulus_yili
        self.ogrenciler = []
        self.ogretmenler = {}
        

    def yeni_ogrenci_ekle (self, ogrenci_adi, sinif):
        self.ogrenci_adi = ogrenci_adi
        self.sinif = sinif
        self.ogrenciler.append((self.ogrenci_adi, self.sinif))

    def yeni_ogretmen_ekle (self, ogretmen_adi, brans):
        self.ogretmen_adi = ogretmen_adi
        self.brans  = brans
        
        self.ogretmenler[ogretmen_adi] = brans

    def ogrenci_listesi_goruntule(self):
       # return self.ogrenciler
       for i in self.ogrenciler:
           print(f"Ogrencinin adi: {i[0]} Ogrencinin sinifi: {i[1]}")

    def ogretmen_listesi_goruntule(self):
        for ad, brans in self.ogretmenler.items():
            
            print(f"Ogretmenin adi: {ad} Ogretmenin bransi: {brans}")
          


okul1 = Okul("Denizli ilkogretim okulu", "1993")
okul1.yeni_ogrenci_ekle("Kamil", "5")
okul1.yeni_ogretmen_ekle("Ayse", "Kimya")
okul1.yeni_ogretmen_ekle("Ali", "Mat")
okul1.ogrenci_listesi_goruntule()
okul1.ogretmen_listesi_goruntule()

print("----------------------------------")

#SORU3

class Sekil():

    def __init__ (self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

class Dikdortgen(Sekil):
    def alan_hesapla (self):
        print(f"dikdortgenin alani: {self.genislik * self.yukseklik} cm karedir.")

class Kare (Sekil):
    def alan_hesapla (self):
        print(f"Karenin alani: {self.genislik * self.yukseklik} cm karedir.")

dikdortgen1 = Dikdortgen(5,9)
kare1 = Kare( 10, 10)

dikdortgen1.alan_hesapla()
kare1.alan_hesapla()

print("---------------------------")

#SORU4

class Tasit():
    def __init__(self,marka,model,yil):
        self.marka=marka
        self.model=model
        self.yil=yil

    def ozellikleri_bul (self):
        print(f"aracin markasi: {self.marka}\naracin model: {self.model}\naracin yili: {self.yil}")

class AraziAraci (Tasit):
    def __init__ (self,marka,model,yil,dort_ceker):
        super().__init__(marka,model,yil)
        self.dort_ceker=dort_ceker

    def ozellikleri_bul(self):
        super().ozellikleri_bul()
        print(f"arac dort ceker mi: {self.dort_ceker}")

class SporAraba (Tasit):
    def __init__ (self,marka,model,yil,maksimim_hiz):
        super().__init__(marka,model,yil)
        self.maksimim_hiz=maksimim_hiz

    def ozellikleri_bul(self):
        super().ozellikleri_bul()
        print(f"Aracin maksimim hizi: {self.maksimim_hiz}")

tasit1 = Tasit("Volvo", "XC90", 2020)
tasit1.ozellikleri_bul()

arazi_araci1 = AraziAraci("Audi", "Q8", 2021, "Evet")
arazi_araci1.ozellikleri_bul()

spor_araba1 = SporAraba("BMW", "M3", 2023, 380)
spor_araba1.ozellikleri_bul()

print("-----------------------")

#SORU5

class Musteri ():
    def __init__ (self, ad, soyad, tc_kimlik, telefon):
        self.ad = ad
        self.soyad = soyad 
        self.tc_kimlik = tc_kimlik
        self.telefon = telefon

    def bilgileri_goruntule(self):
        print(f"Musterinin adi: {self.ad} Soyadi: {self.soyad} TC numarasi: {self.tc_kimlik} Telefonu: {self.telefon} ")


class Hesap(Musteri):
    def __init__ (self, ad, soyad, tc_kimlik, telefon, hesap_numarasi, bakiye):
        super().__init__ (ad, soyad, tc_kimlik, telefon)
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"Guncel hesap bakiyeniz: {self.bakiye}")

    def para_cek(self, miktar):
        if miktar<=self.bakiye:
            self.bakiye-=miktar
            print(f"Guncel bakiyeniz: {self.bakiye}")
        else:
            print("Hesapta yeterli bakiye bulunmamaktadir")

    def bakiyeyi_goruntule(self):
        print(f"Bakiyeniz: {self.bakiye}")

musteri1 = Musteri("Dusan", "Tadic", "12345", "069876")
hesap1 = Hesap (musteri1.ad, musteri1.soyad, musteri1.tc_kimlik, musteri1.telefon, "H_N 12345", 10000)

musteri1.bilgileri_goruntule()
hesap1.para_yatir(500)
hesap1.para_cek(1000)
hesap1.bakiyeyi_goruntule()
            

            
