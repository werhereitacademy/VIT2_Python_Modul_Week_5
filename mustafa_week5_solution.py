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
    
