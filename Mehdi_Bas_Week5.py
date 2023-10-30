##Soru 1

class Rectangle():
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik
    def alan_hesapla(self,):
        alan = self.genislik * self.yukseklik
        return alan

    def cevre_hesapla(self):
        cevre = self.genislik * self.yukseklik
        return cevre
ornek = Rectangle(5,7)

print(ornek.alan_hesapla())

##Soru 2

class Okul:
    def __init__(self, ad, kurulus):
        self.ad = ad
        self.kurulus = kurulus
        self.ogrenciler = []
        self.ogretmenler = {}

    def ogrenci_ekle(self, ogrenci_adi, sinif):
        self.ogrenciler.append({'ogrencinin adi': ogrenci_adi, 'sinifi': sinif})
        return f'{ogrenci_adi} isimli ogrenci basari ile eklendi'

    def ogretmen_ekle(self, ogretmen_adi, brans):
        self.ogretmenler[ogretmen_adi] = brans
        return f'{ogretmen_adi} isimli ogretmen basari ile eklendi'

    def ogrenci_goruntule(self,):
        print(self.ogrenciler)

    def ogretmen_goruntule(self):
        return print(self.ogretmenler)


ornek_okul = Okul("EKol", "1994")
ornek_okul.ogrenci_ekle("Icardi", "1A")
ornek_okul.ogretmen_ekle("Mahmut Hoca", "Turkce")
ornek_okul.ogrenci_ekle("Mahsun", "3b")
ornek_okul.ogrenci_goruntule()
ornek_okul.ogretmen_goruntule()

##Soru 3

class Sekil:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

class Dikdortgen(Sekil):
    def alan_hesapla(self):
        dikdortgen_alan = self.genislik * self.yukseklik
        return print(f'Dikdortdenin alani :{dikdortgen_alan}')

class Kare(Sekil):
    def alan_hesapla(self):
        kare_alan = self.yukseklik * self.genislik
        return print(f"Karenin alani esittir:{kare_alan}")

kare1 = Kare(4, 4)
dikdortgen1 = Dikdortgen(3,8)

dikdortgen1.alan_hesapla()
kare1.alan_hesapla()

class Vehicle:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

class AraziAraci(Vehicle):
    def __init__(self, marka, model, yil, suv):
        super().__init__( marka, model, yil)
        self.suv = suv
    def __str__(self):
        return f"Arac: {self.marka} {self.model} {self.yil}, tip: {self.suv}"


class SporAraba(Vehicle):
    def __init__(self, marka, model, yil, maximum_hiz):
        super().__init__( marka, model, yil)
        self.maximum_hiz = maximum_hiz
    def __str__(self):
        return f"Arac: {self.marka} {self.model} {self.yil} maksimum hiz: {self.maximum_hiz}"

arac1= AraziAraci("Nivea", "4x4", 1994, "Dort Ceker")
arac2= SporAraba("Lamborghini", "Aventador", 2023, 360)
print(arac2)
print(arac1)

##Soru 5
class Musteri:
    def __init__(self, ad, soyad, tc_kimlik, telefon):
        self.ad = ad
        self.soyad = soyad
        self.tc_kimlik = tc_kimlik
        self.telefon = telefon
    def bilgiler(self):
        print(f"Adi ve soyadi: {self.ad}  {self.soyad}")
        print(f"Tc kimlik no: {self.tc_kimlik} ")
        print(f"telefon : {self.telefon}")

class Hesap(Musteri):
    def __init__(self, ad, soyad, tc_kimlik, telefon, hesap_no, bakiye):
        super().__init__(ad, soyad, tc_kimlik, telefon)
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, para):
        self.bakiye += para

    def para_cek(self, para):
        if para > self.bakiye:
            print("yetersiz bakiye")
        else:
            self.bakiye -= para


    def bakiye_goruntule(self):
        print(f"Hesabinizdaki mikta : {self.bakiye}")

kisi1 = Musteri("ahmet", "Ozokutan", 19458673321454 , 2162334567)
kisi1.bilgiler()
hesap1 = Hesap(kisi1.ad, kisi1.soyad, kisi1.tc_kimlik, kisi1.telefon, 182121, 0)
hesap1.para_yatir(15000)
hesap1.bakiye_goruntule()
hesap1.para_cek(3500)
hesap1.bakiye_goruntule()
