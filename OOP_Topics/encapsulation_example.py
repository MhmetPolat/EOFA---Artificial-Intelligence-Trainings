class BankaHesabi:
    def __init__(self, bakiye):
     self.__bakiye = bakiye

    def bakiye_goster(self):
       return f"Bakiyeniz: {self.__bakiye} TL"
    
hesap = BankaHesabi(1000)
print(hesap.bakiye_goster())
#print(hesap.__bakiye)  # Hata verir çünkü __bakiye özel bir değişkendir.
     
