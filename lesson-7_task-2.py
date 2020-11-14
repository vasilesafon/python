class Clothing():
    def __init__(self, color):
        self.color = color


class Coat(Clothing):
    def __init__(self, size, color):
        super().__init__(color)
        self.size = size

    def calc(self):
        print(self.size / 6.5 + 0.5)


class Suit(Clothing):

    def __init__(self, height, color):
        super().__init__(color)
        self.height = height

    def calc(self):
        print(2 * self.height + 0.3)


summer_suit = Suit(10, 'red')
summer_suit.calc()

winter_coat = Coat(65, 'black')
winter_coat.calc()