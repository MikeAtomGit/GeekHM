from abc import ABC, abstractmethod
class Cloth():

    @abstractmethod
    def cloth_count(self):
        pass

class Suit(Cloth):

    def __init__(self, height):
        self.height = height

    @property
    def cloth_count(self):
        return f'It will take {(2 * self.height + 0.3):2.2f} meters of cloth'

class Coat(Cloth):

    def __init__(self, volume):
        self.volume = volume
    @property
    def cloth_count(self):
        return f'It will take {(self.volume/6.5 + 0.5):2.2f} meters of cloth'

coat1 = Coat(50)
print(coat1.cloth_count)
suit1 = Suit(180)
print(suit1.cloth_count)
print(f'It will take {((coat1.volume/6.5 + 0.5) + (2 * suit1.height + 0.3)):2.2f} meters in total')