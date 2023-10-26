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


  
