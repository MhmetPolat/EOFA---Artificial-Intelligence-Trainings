class Ucak:
    def ucus(self):
        return ("Uçak Havalanıyor.")
    
class Jet:
    def ucus(self):
        return ("Jet çok hızlı bir şekilde havalanıyor!")

ucak1 = Ucak()
jet1 = Jet()
print(ucak1.ucus())
print(jet1.ucus())
