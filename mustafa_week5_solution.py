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


###Soru4###

class Vehicle:
    def __init__(self,marka,model,yil):
        self.marka = marka
        self.model = model
        self.yil = yil
class SUV(Vehicle):
    def __init__(self, marka, model, yil,dort_ceker):
        super().__init__(marka, model, yil)
        self.dort_ceker = dort_ceker
    def __str__(self) :
        return f"{self.marka} marka {self.model} model {self.yil} yili araç {self.dort_ceker} dir"
class SportsCar(Vehicle):
    def __init__(self, marka, model, yil,max_hiz):
        super().__init__(marka, model, yil)
        self.max_hiz = max_hiz
    def goster(self) :
        return f"{self.marka} marka {self.model} model {self.yil} yili araç ve maksimum hizi {self.max_hiz} dir"
sporArac = SportsCar("mitsubichi","lancer",2002,280)
araziArac = SUV("Jeep","ciks",2023,"dortceker")
print(sporArac.goster())
print(araziArac)



###Soru5###

class Musteri():
    def __init__(self, ad, soyad,kimlik_no, telefon):
        self.ad = ad
        self.soyad = soyad
        self.kimlik_no = kimlik_no
        self.telefon = telefon
    def bilgileri_görüntüle(self):
        print(f"Müsterinin adi:{self.ad}")
        print(f"Müsterinin soyadi:{self.soyad}")
        print(f"Müsterinin TC kimlik numarasi:{self.kimlik_no}")
        print(f"Müsterinin telefonu:{self.telefon}")

class Hesap(Musteri):
    def __init__(self,ad,soyad,kimlik_no,telefon,hesap_no,bakiye):
        super().__init__(ad, soyad,kimlik_no, telefon)
        self.hesap_no=hesap_no
        self.bakiye=bakiye

    def para_cek(self,miktar):
        if miktar>self.bakiye :
            print("Yetersiz bakiye !..")
        else:
            self.bakiye -= miktar

    def para_yatir(self,miktar):
        self.bakiye += miktar

    def bakiyeyi_goruntule(self):
        print("Güncel bakiyeniz:", self.bakiye)
    def __str__(self) :
        return f"{self.ad} {self.soyad} kimlik no : {self.kimlik_no}  tel: {self.telefon}  bakiyesi {self.bakiye}"

musteri1 = Musteri("mustafa","Kara","18181818","05325553334")
hesap = Hesap(musteri1.ad,musteri1.soyad,musteri1.kimlik_no,musteri1.telefon,"777777",5000)
hesap.para_yatir(1000)
hesap.bakiyeyi_goruntule()
hesap.para_cek(300)
hesap.para_yatir(100)
hesap.bakiyeyi_goruntule()
print(hesap)

