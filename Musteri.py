class Musteri:
    def __init__(self,ad,soyad,tc_kimlik,telefon):
        self.ad=ad
        self.soyad=soyad
        self.tc_kimlik=tc_kimlik
        self.telefon=telefon
    def bilgileri_goster(self):
        print(f'Musteri ad-soyad: {self.ad}-{self.soyad}')
        print(f'Musteri tc_kimlik: {self.tc_kimlik}')
        print(f'Telefon: {self.telefon}')
class Hesap(Musteri):
    def __init__(self,ad,soyad,tc_kimlik,telefon,musteri,hesap_numarasi,bakiye):
        super().__init__(ad,soyad,tc_kimlik,telefon)
        self.musteri=musteri
        self.hesap_numarasi=hesap_numarasi
        self.bakiye=bakiye
    def para_yatir(self,miktar):
        self.bakiye+=miktar
        return self.bakiye
    def para_cek(self,miktar):
        if miktar<=self.bakiye:
            self.bakiye-=miktar
            return self.bakiye
        else:
            print('Islem basarisiz, yetersiz bakiye!')
    def bakiye_goruntule(self):
        print(f'Hesap no: {self.hesap_numarasi}')
        print(f'Bakiye: {self.bakiye}')
musteri1=Musteri('Ali','Can',36723406478,98763566364)
musteri1.bilgileri_goster()
hesap1=Hesap('Hasan','Yucel',5365327374,894756342,'Hasan Yucel',4756895847,10000)
print(hesap1.musteri)
print(hesap1.hesap_numarasi)
print(hesap1.bakiye)
print(hesap1.para_yatir(5000))
print(hesap1.para_yatir(20000))
print(hesap1.para_cek(5000))
print(hesap1.para_cek(1000))
print(hesap1.para_cek(30000))
hesap1.bakiye_goruntule()

