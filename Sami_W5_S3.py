# Soru3: Bir "Şekil" sınıfı oluşturun. Bu sınıfın altında iki alt sınıf, "Dikdörtgen" ve "Kare" sınıfları oluşturun.
#
# "Şekil" sınıfı, iki özelliğe sahip olsun: "genişlik" ve "yükseklik."
# "Dikdörtgen" sınıfı, "Şekil" sınıfından miras alsın ve ek olarak bir "alan_hesapla()" metodu eklesin.
# "Kare" sınıfı da "Şekil" sınıfından miras alsın ve aynı "alan_hesapla()" metodunu kullanarak karenin alanını hesaplasın.
# Bir "Dikdörtgen" ve bir "Kare" örneği oluşturun, her birinin genişliğini ve yüksekliğini belirleyin, ve her birinin alanını hesaplayarak sonuçları yazdırın.

class Sekil:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

class Dikdortgen(Sekil):
        def alan_hesapla(self):
            return self.genislik * self.yukseklik
class Kare(Sekil):
        def alan_hesapla(self):
            return self.genislik * self.yukseklik

Dik1 = Dikdortgen(3, 5)

print("Dikdörtgenin alanı :",Dik1.alan_hesapla())

Kare1 = Kare(3,3)
print("Karenin alanı :",Kare1.alan_hesapla())






