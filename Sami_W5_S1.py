# Soru1: Bir dikdörtgeni temsil eden "Rectangle" adında bir Python sınıfı oluşturun.
# Rectangle sınıfı aşağıdaki özelliklere ve yöntemlere sahip olmalıdir:
#
# Özellikler:
# genişlik (bir tam sayı)
# yükseklik (bir tam sayı)
# Yöntemler:
# alan(self): Dikdörtgenin alanını hesaplayan ve döndüren bir yöntem.
# çevre(self): Dikdörtgenin çevresini hesaplayan ve döndüren bir yöntem.
# Rectangle sınıfından bir örnek oluşturun, genişliğini 5 ve yüksekliğini 7 olarak ayarlayın,
# ardından alanını ve çevresini yazdırın.



# 1. yol
class Rectangle():
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan(self):
        return self.genislik * self.yukseklik
    def cevre(self):
        return (self.genislik + self.yukseklik)*2

Rectangle1 = Rectangle(5,7)
print("Dikdörtgenin alanı {} m2 dir. ".format(Rectangle1.alan()))
print("Dikdörtgenin cevresi {} cm dir. ".format(Rectangle1.cevre()))



# 2. yol
class Rectangle():
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan(self):
        alan = self.genislik * self.yukseklik
        print("Dikdörtgenin alanı {} m2 dir. ".format(alan))


    def cevre(self):
        cevre = (self.genislik + self.yukseklik) * 2
        print("Dikdörtgenin cevresi {} cm dir. ".format(cevre))


Rectangle1 = Rectangle(5, 7)
alan = Rectangle1.alan()
cevre = Rectangle1.cevre()

