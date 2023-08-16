#Много было чего было переделано / и списано. нельзя давать вебинары на дз=/. одним глазком глянул и сразу понимаешь что то что писал сам вообще не в какие ворота=(
import random


class AllEception(Exception):
    pass


class OutException(AllEception):
    def __str__(self):
        return "Выстрел за доску"


class ShotException(AllEception):
    def __str__(self):
        return "Туда уже стрельнули"


class BoardWrongShipException(AllEception):
    pass


class Ships:
    def __init__(self, x, y, l, o):
        self.x = x
        self.y = y
        self.l = l
        self.o = o

    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.x
            cur_y = self.y

            if self.o == 0:
                cur_x += i
            elif self.o == 1:
                cur_y += i
            ship_dots.append((cur_x, cur_y))

        return ship_dots

    def gunshot(self, gunx, guny):
        guns = [gunx, guny]
        return guns in self.dots()


class Board:
    def __init__(self, hid=False, size=6):
        self.size = size  # pohue
        self.hid = hid  # poheu
        self.count = 0  # pohue
        self.field = [["O"] * size for _ in range(size)]
        self.busy = []
        self.ships = []

    def __str__(self):

        res = "   1  2  3  4  5  6 \n"
        for i in range(1, 7):
            res += f"{i}  "
            for j in range(1, 7):
                res += self.field[i - 1][j - 1]
                res += "  "
            res += "\n"

        if self.hid:
            res = res.replace("S", "O")
        return res

    def out(self, x, y):
        return not ((0 <= x < self.size) and (0 <= y < self.size))

    def carpet(self, ship, verb=False):
        carpets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for (x, y) in ship.dots():
            for cx, cy in carpets:
                carpetsx = x + cx
                carpetsy = y + cy
                if not (self.out(carpetsx, carpetsy)) and (carpetsx, carpetsy) not in self.busy:
                    if verb:
                        self.field[carpetsx][carpetsy] = "T"
                    self.busy.append((carpetsx, carpetsy))

    def add(self, ship):
        for x, y in ship.dots():
            if self.out(x, y) or (x, y) in self.busy:
                raise BoardWrongShipException()
        for x, y in ship.dots():
            self.field[x][y] = "S"
            self.busy.append((x, y))

        self.ships.append(ship)
        self.carpet(ship)

    def proverka(self, ship):
        carpets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        k = 0
        for x, y in ship.dots():
            for cx, cy in carpets:
                carpetsx = x + cx
                carpetsy = y + cy
                if not (self.out(carpetsx, carpetsy)) and self.field[carpetsx][carpetsy] in "S":
                    k += 1
        if k > 0:
            return False
        else:
            return True

    def shot(self, x, y):
        if self.out(x, y):
            raise OutException() #Стрельба вне поля
        if (x, y) in self.busy:
            raise ShotException() #Стрельба где уже стреляли
        self.busy.append((x, y))

        for ship in self.ships:
            if (x, y) in ship.dots():
                self.field[x][y] = "X"
                print("Попадание")
                self.count += 1
                print(self.count)
                if self.proverka(ship) == True:
                    print("Убил")
                    self.carpet(ship, verb=True)
                    print("Стреляй еще, если еще не победил")
                    return True
                else:
                    print("RANEN")
                    print("Стреляй еще,")
                    return True

        self.field[x][y] = "T"
        print("Мимо")
        return False

    def begin(self):
        self.busy = []


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy



    def move(self):
        while True:
            try:
                targetx, targety = self.ask()
                repeat = self.enemy.shot(targetx, targety)
                return repeat
            except AllEception as e:
                print(e)


class AI(Player):
    def ask(self):
        dx = random.randint(0, 5)
        dy = random.randint(0, 5)
        print(f"Ход противника: {dx + 1} {dy + 1}")
        return dx, dy


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход:").split()

            if len(cords) != 2:
                print("введите 2 координаты")
                continue
            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue
            x, y = int(x), int(y)

            return x, y


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True
        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 10000:
                    return None
                ship = Ships(random.randint(0, self.size), random.randint(0, self.size), l, random.randint(0, 1))
                try:
                    board.add(ship)
                    break
                except AllEception:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def loop(self):
        num = 0
        while True:
            print("ME")
            print(self.us.board)
            print("KOMP")
            print(self.ai.board)
            if num % 2 == 0:
                print("Turn ME")
                repeat = self.us.move()
            else:
                print("Turn KOMP")
                repeat = self.ai.move()
            if repeat:
                num -= 1
            if self.ai.board.count == 11:
                print("YOU WIN")
                break
            if self.us.board.count == 11:
                print("YOU lOSE")
                break
            num += 1

    def start(self):
        self.loop()


g = Game()
g.start()
