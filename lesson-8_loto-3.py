import random


class Card():
    def __init__(self):
        self.card_row = self.generator()
        self.footer = '\n----------------------------\n'

    def __str__(self):
        return self.card_row

    def generator(self):
        five_of_nine = [1, 1, 1, 1, 1, 0, 0, 0, 0]
        row = []
        number = ''
        for card_row in range(0, 3):
            five_of_nine_rnd = random.sample(five_of_nine, 9)
            column = 1
            for i in range(0, 9):
                if five_of_nine_rnd[i] == 1:
                    while str(number) in row:
                        number = random.randint(column * 10 - 9, column * 10)
                    row.append(str(number))
                    column += 1
                else:
                    row.append('  ')
                    column += 1
            row.append('\n')
        return row[:-1]

    def __iter__(self):
        for i in self.card_row:
            yield i

    def output(self):
        print(self.title)
        for i in self.card_row:
            print('{:>3}'.format(i), end='')
        print(self.footer)


class CompCard(Card):
    def __init__(self):
        super().__init__()
        self.title = '--- Карточка компьютера ----'


class UserCard(Card):
    def __init__(self):
        super().__init__()
        self.title = '------ Ваша карточка -------'

class Run():
    def __init__(self):
        self.u_card = UserCard()
        self.c_card = CompCard()
        self.gameplay()

    def gameplay(self):
        while True:
            tile_list = random.sample(range(1, 91), 90)
            tile_no = -1
            while True:
                self.c_card.output()
                self.u_card.output()
                tile_no += 1
                print('----------------------------------')
                print('выпало: ', tile_list[tile_no], '  ----   осталось: ', 90 - (tile_no +1))
                answer = input('Зачеркнуть цифру? (y / n) ')
                if str(tile_list[tile_no]) in self.u_card:
                    print('yes')
                    if answer == 'y':
                        print('1')

                        self.u_card[self.u_card.index(tile_list[tile_no])] = '--'
                        continue
                    else:
                        input('game over')
                        break
                else:
                    if answer == 'y':
                        input('game is over')
                        break
                    else:
                        continue
                if tile_list[tile_no] in self.c_card:
                    self.c_card[self.c_card.index(tile_list[tile_no])] = '--'


game_1 = Run()