### Soru1 ###

class Rectangle:
    def __init__(self,genislik,yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik
    def alan(self):
        alan = self.yukseklik*self.genislik
        return f"dikdortgenin alani : {alan}"
    def cevre(self):
        cevre = 2*(self.yukseklik +self.genislik)
        return f"dikdortgenin cevresi : {cevre}"
rec = Rectangle(5,7)
print(rec.alan())
print(rec.cevre())


###soru2####

class Okul:
    ogrenciler = []
    def __init__(self,ad,kurulus_yili):
        self.ad = ad
        self.kurulus_yili = kurulus_yili
        self.ogrenciler = []
        self.ogretmenler = []
    def ogrenci_ekle(self,ogrenci_adi,sinif):
        self.ogrenciler.append((ogrenci_adi,sinif))
    def ogretmen_ekle(self,ogretmen_adi,bransi):
        self.ogretmenler.append((ogretmen_adi,bransi))
    def oğrenci_listesi_görüntüle(self):
        for adi,sinifi in self.ogrenciler:
            print(f"Ogrenci: {adi}    Sinif: {sinifi} ")
    def oğretmen_listesi_görüntüle(self):
        for adi,bransi in self.ogretmenler:
            print(f"Ogretmen: {adi}    Brans: {bransi} ")
okul= Okul("YunusemreIO",1992)
okul.ogrenci_ekle("osman",8)
okul.ogrenci_ekle("samet",3)
okul.ogretmen_ekle("bekir","matematik")
okul.ogretmen_ekle("mahmut","Felsefe")
okul.oğrenci_listesi_görüntüle()
okul.oğretmen_listesi_görüntüle()


###Soru3 ###

class Sekil:
    def __init__(self,genislik,yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

class Dikdortgen(Sekil):
    def __init__(self, genislik, yukseklik):
        super().__init__(genislik, yukseklik)
    def alan_hesapla(self):
        alan = self.genislik*self.yukseklik
        print( f"sekllimizin alani : {alan}")
class Kare(Dikdortgen):
    def __init__(self, genislik, yukseklik):
        super().__init__(genislik, yukseklik)
    def alan_hesapla(self):
        return super().alan_hesapla()
    
kare = Kare(5,5)
dikdrtgn = Dikdortgen(5,7)
dikdrtgn.alan_hesapla()
kare.alan_hesapla()

