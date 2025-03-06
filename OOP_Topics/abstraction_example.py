from abc import ABC, abstractmethod

class Sekil(ABC):
    @abstractmethod
    def alan(self):
        pass

class Kare(Sekil):
    def __init__(self,kenar):
        self.kenar = kenar

    def alan(self):
        return self.kenar**2

kare1 = Kare(5)
print(f"Karenin Alanı: {kare1.alan()}")
