# VIT2 Python-Module-Week5

Soru1: Bir dikdörtgeni temsil eden "Rectangle" adında bir Python sınıfı oluşturun. Rectangle sınıfı aşağıdaki özelliklere ve yöntemlere sahip olmalıdir:
##### Özellikler:
- genişlik (bir tam sayı)
- yükseklik (bir tam sayı)
##### Yöntemler:
- alan(self): Dikdörtgenin alanını hesaplayan ve döndüren bir yöntem.
- çevre(self): Dikdörtgenin çevresini hesaplayan ve döndüren bir yöntem.
- Rectangle sınıfından bir örnek oluşturun, genişliğini 5 ve yüksekliğini 7 olarak ayarlayın, ardından alanını ve çevresini yazdırın.
##
Soru2: Python'da bir "Okul" sınıfı oluşturun. Bu sınıf aşağıdaki özelliklere ve işlevselliklere sahip olmalıdır:

##### Özellikler:
- "ad" 
- "kuruluş_yılı" 
- "öğrenciler" 
- "öğretmenler"
- 
##### Metodlar:
- yeni_öğrenci_ekle(self, öğrenci_adı, sınıf): Yeni bir öğrenciyi okula eklemek için kullanılan bir metod. Öğrencinin adını ve sınıfını alır ve "öğrenciler" listesine ekler.
- yeni_öğretmen_ekle(self, öğretmen_adı, branş): Yeni bir öğretmeni okula eklemek için kullanılan bir metod. Öğretmenin adını ve branşını alır ve "öğretmenler" sözlüğüne ekler.
- öğrenci_listesi_görüntüle(self): Okula kayıtlı öğrencilerin listesini görüntülemek için kullanılan bir metod. Öğrenci adlarını ve sınıflarını listeleyin.
- öğretmen_listesi_görüntüle(self): Okulda çalışan öğretmenlerin listesini görüntülemek için kullanılan bir metod. Öğretmen adlarını ve branşlarını listeleyin.
##
Soru3: Bir "Şekil" sınıfı oluşturun. Bu sınıfın altında iki alt sınıf, "Dikdörtgen" ve "Kare" sınıfları oluşturun.

- "Şekil" sınıfı, iki özelliğe sahip olsun: "genişlik" ve "yükseklik."
- "Dikdörtgen" sınıfı, "Şekil" sınıfından miras alsın ve ek olarak bir "alan_hesapla()" metodu eklesin.
- "Kare" sınıfı da "Şekil" sınıfından miras alsın ve aynı "alan_hesapla()" metodunu kullanarak karenin alanını hesaplasın.
- Bir "Dikdörtgen" ve bir "Kare" örneği oluşturun, her birinin genişliğini ve yüksekliğini belirleyin, ve her birinin alanını hesaplayarak sonuçları yazdırın.
##
Soru4: Python'da bir "Taşıt" (Vehicle) sınıfı oluşturun. Bu sınıfın aşağıdaki özelliklere sahip olmasını sağlayın:

##### Özellikler:
- "marka" (Taşıtın markası)
- "model" (Taşıtın modeli)
- "yıl" (Taşıtın üretim yılı)
  
Bir "Taşıt" sınıfı oluşturun ve bu sınıftan türetilmiş iki alt sınıf, "AraziAracı" (SUV) ve "SporAraba" (SportsCar) sınıfları oluşturun.

- "AraziAracı" sınıfı, "Taşıt" sınıfından miras alsın ve ek olarak bir "dört_çeker" özelliği eklesin.
- "SporAraba" sınıfı da "Taşıt" sınıfından miras alsın ve ek olarak bir "maksimum_hız" özelliği eklesin.

Her bir sınıftan birer örnek oluşturun, özelliklerini belirleyin ve bu özellikleri görüntülemek için bir program yazın.





## HackerRank Questions

* **Inheritance:** https://www.hackerrank.com/challenges/inheritance/problem
  
* **Classes: Dealing with Complex Numbers:** https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
