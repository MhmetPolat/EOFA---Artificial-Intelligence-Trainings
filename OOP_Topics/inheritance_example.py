from class_example import Araba

class elektrikli_araba(Araba):
    def __init__(self,marka,model,yil,batarya_kapasitesi):
      super().__init__(marka, model, yil)
      self.batarya_kapasitesi = batarya_kapasitesi

    def bilgileri_goster(self):
       return f"{self.yil} model {self.marka} {self.model}, Batarya: {self.batarya_kapasitesi} kWh"
    
e_araba = elektrikli_araba("Tesla", "Model S", 2023, 100)
print(e_araba.bilgileri_goster())
