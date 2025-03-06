class Hayvan:
    def ses_cikar(self):
        pass

class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav!"

class Kopek(Hayvan):
    def ses_cikar(self):
        return "Hav!"
    
hayvanlar = [Kedi(), Kopek()]
for hayvan in hayvanlar:
    print(hayvan.ses_cikar())    
