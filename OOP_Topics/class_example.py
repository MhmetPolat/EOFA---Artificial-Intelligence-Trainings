class Araba:
    def __init__(self,marka,model,yil):
       self.marka = marka 
       self.model = model 
       self.yil = yil 
    
    def bilgileri_goster(self):
        return f"{self.yil} model {self.marka} {self.model}"
    
araba1 = Araba("Toyota", "Corolla", 2022)
print(araba1.bilgileri_goster())    
    








