class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Starting to draw')
class Pen(Stationery):
    def draw(self):
        print(f'Starting to draw lines with {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'Starting to draw contures with {self.title}')
class Handler(Stationery):
    def draw(self):
        print(f'Starting to draw diagrams with {self.title}')
stat = Stationery('stat')
stat.draw()
pen_1 = Pen('Black pen')
pen_1.draw()
penc_1 = Pencil('Regular pencil')
penc_1.draw()
han_1 = Handler('Red handler')
han_1.draw()
#