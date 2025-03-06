class Kullanici:
    def __init__(self, ad, soyad, yas=18):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.email = f"{ad.lower()}.{soyad.lower()}@gmail.com"

    def bilgileri_göster(self):
        return f"Ad:{self.ad} {self.soyad}, Yaş:{self.yas}, E-posta:{self.email}"   

Kullanici1 = Kullanici("Ahmet", "Yılmaz", 25)
kullanici2 = Kullanici("Mehmet", "Kaya") # Yaş belirtilmezse 18 olur.
print(Kullanici1.bilgileri_göster())
print(kullanici2.bilgileri_göster())     