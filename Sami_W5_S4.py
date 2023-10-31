# Soru4: Python'da bir "Taşıt" (Vehicle) sınıfı oluşturun. Bu sınıfın aşağıdaki özelliklere sahip olmasını sağlayın:
#
# Özellikler:
# "marka" (Taşıtın markası)
# "model" (Taşıtın modeli)
# "yıl" (Taşıtın üretim yılı)
# Bir "Taşıt" sınıfı oluşturun ve bu sınıftan türetilmiş iki alt sınıf, "AraziAracı" (SUV) ve "SporAraba" (SportsCar) sınıfları oluşturun.
#
# "AraziAracı" sınıfı, "Taşıt" sınıfından miras alsın ve ek olarak bir "dört_çeker" özelliği eklesin.
# "SporAraba" sınıfı da "Taşıt" sınıfından miras alsın ve ek olarak bir "maksimum_hız" özelliği eklesin.
# Her bir sınıftan birer örnek oluşturun, özelliklerini belirleyin ve bu özellikleri görüntülemek için bir program yazın.

class Vehicle():
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

class SUV(Vehicle):
    def __init__(self, marka, model, yil, dort_ceker):
        super().__init__(marka, model, yil)
        self.dort_ceker = dort_ceker
        print(f"{self.marka} markasinin {self.model} {self.yil} modeli {self.dort_ceker} dir.")
class SportsCar(Vehicle):
    def __init__(self, marka, model, yil, maksimum_hiz):
        super().__init__(marka, model, yil)
        self.maksimum_hiz = maksimum_hiz
        print(f"{self.marka} markasinin {self.model} {self.yil} modelinin maksimum hizi {self.maksimum_hiz} km/h dur.")

SUV1 = SUV("Totoya", "RAV4", 2020, "4x4")
SPC1 = SportsCar("Mazda", "Coupe", 2010, 250)

#print(f"{SUV1.marka} markasinin {SUV1.model} {SUV1.yil} modeli {SUV1.dort_ceker} dir.")
#print(f"{SPC1.marka} markasinin {SPC1.model} {SPC1.yil} modelinin maksimum hizi {SPC1.maksimum_hiz} km/h dur.")