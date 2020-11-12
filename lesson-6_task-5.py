class Stationery:
    def __init__(self, name):
        self.name = name
    def draw(self):
        print('запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(self.name, 'is drawing ...............')

class Pencil(Stationery):
    def draw(self):
        print(self.name, 'is drawing _______________')

class Handle(Stationery):
    def draw(self):
        print(self.name, 'is drawing |||||||||||||||')

lamy = Pen('my pen')
rotring = Pencil('your pencil')
carioca = Handle('my handle')

lamy.draw()
rotring.draw()
carioca.draw()


