# Soru5: Bir "Müşteri" sınıfı ve bir "Hesap" sınıfı oluşturun. "Hesap" sınıfı, "Müşteri" sınıfından miras alsın ve bir müşterinin banka hesap bilgilerini temsil etsin.
#
# Müşteri Sınıfı Özellikleri:
# "ad" (müşteri adı)
# "soyad" (müşteri soyadı)
# "tc_kimlik" (müşteri TC kimlik numarası)
# "telefon" (müşteri telefon numarası)
# Hesap Sınıfı Özellikleri:
# "müşteri" (bir Müşteri nesnesi)
# "hesap_numarası" (hesap numarası)
# "bakiye" (hesap bakiyesi)
# Müşteri Sınıfı Metodu:
# "bilgileri_görüntüle()": Müşterinin adını, soyadını, TC kimlik numarasını ve telefon numarasını görüntüler.
# Hesap (Account) Sınıfı Metodları:
# "para_yatır(self, miktar)": Hesaba belirli bir miktar para yatıran bir metod.
# "para_çek(self, miktar)": Hesaptan belirli bir miktar para çeken bir metod. Ancak hesapta yeterli bakiye yoksa işlem gerçekleşmemeli ve bir mesaj görüntülenmeli.
# "bakiyeyi_görüntüle()": Hesap bakiyesini görüntüleyen bir metod.
# Bu iki sınıfı oluşturun, ardından bir Müşteri nesnesi ve bir Hesap nesnesi oluşturun, müşteri bilgilerini Hesap nesnesine ekleyin ve hesap işlemlerini gerçekleştirerek sonuçları görüntüleyin.

class Musteri():
    def __init__(self, ad, soyad, tc_kimlik, telefon):
        self.ad = ad
        self.soyad = soyad
        self.tc_kimlik = tc_kimlik
        self.telefon = telefon

    def bilgileri_goruntule(self):
        print(f"Müşterinin adi : {self.ad}, soyadi {self.soyad}, TC kimlik numarasi : {self.tc_kimlik} ve telefon numarası : {self.telefon} dir")


class Hesap(Musteri):
    def __init__(self, ad, soyad, tc_kimlik, telefon, musteri, hesap_numarasi, bakiye):
        super().__init__(ad, soyad, tc_kimlik, telefon)
        self.musteri = musteri
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    def para_yatir(self, miktar):
#        self.bakiye = miktar
        self.bakiye += miktar
        print(f"Hesabiniza {miktar} euro para yatirilmistir.")

    def para_cek(self, miktar):
#        self.miktar = miktar
        if self.bakiye > miktar:
            self.bakiye -= miktar

        else:
            print("Hesabinizda yeterli bakiye yoktur.")


    def bakiye_goruntule(self):
        print(f"Hesabinizda {self.bakiye} euro para vardir.")


mus1 = Musteri("Ali", "Veli", 31680369564, 32158626587)
hesap1=Hesap(mus1.ad,mus1.soyad,mus1.tc_kimlik,mus1.telefon, "Ali Veli",'456456',2000)

hesap1.para_cek(400)
hesap1.bakiye_goruntule()
hesap1.para_cek(2000)
hesap1.bakiye_goruntule()
hesap1.para_yatir(1000)
hesap1.bakiye_goruntule()
hesap1.para_yatir(200)
hesap1.bakiye_goruntule()
hesap1.bilgileri_goruntule()