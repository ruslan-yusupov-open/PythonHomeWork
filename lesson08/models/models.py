# размера поля жестко задан 10х10
X_SIZE = 10
Y_SIZE = 10


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


# поле 10х10, содержит корабли
class Ship:
    def __init__(self, x, y, length, orientation):
        if orientation not in ['h', 'v']:
            raise ValueError("ориентация должна быть h или v")
        if length not in range(1, 5):
            raise ValueError("длинна должна быть от 1 до 4")

        self.length = length
        self.orientation = orientation
        x = ord(x) - ord('a')
        y = int(y)
        self.pos = Coord(x, y)
        self.damage = [False] * length

    def attack(self, attack_point: Coord):
        coords = self.get_coords()
        for coord in enumerate(coords):
            if coord[1] == attack_point:
                self.damage[coord[0]] = True
                print("убит!" if self.check_if_dead() else "ранен!")

        return False

    def get_coords(self):
        if self.orientation == 'v':
            return [Coord(self.pos.x + i, self.pos.y) for i in range(0, self.length)]
        else:
            return [Coord(self.pos.x, self.pos.y + i) for i in range(0, self.length)]

    def get_proximity_coords(self):
        proximity_coords = []
        for i in range(-1, self.length + 1):
            x = self.pos.x + i if self.orientation == 'v' else self.pos.x
            y = self.pos.y if self.orientation == 'v' else self.pos.y + i
            if x in range(0, X_SIZE) and y in range(0, Y_SIZE):
                proximity_coords.append(Coord(x, y))

            x = self.pos.x + i if self.orientation == 'v' else self.pos.x + 1
            y = self.pos.y + 1 if self.orientation == 'v' else self.pos.y + i
            if x in range(0, X_SIZE) and y in range(0, Y_SIZE):
                proximity_coords.append(Coord(x, y))

            x = self.pos.x + i if self.orientation == 'v' else self.pos.x - 1
            y = self.pos.y - 1 if self.orientation == 'v' else self.pos.y + i
            if x in range(0, X_SIZE) and y in range(0, Y_SIZE):
                proximity_coords.append(Coord(x, y))

        return proximity_coords

    def check_if_dead(self):
        for b in self.damage:
            if b is False:
                return False
        return True


class Field:
    def __init__(self):
        self.ships = []
        self.attack_points = []

    def add_ship(self, ship: Ship):
        self.check_ships_collision(ship)
        self.ships.append(ship)

    def check_ships_collision(self, ship):
        for coord in ship.get_coords():
            if coord.x not in range(0, X_SIZE) or coord.y not in range(0, Y_SIZE):
                raise ValueError("корабль выходит за границу поля")

        for coord in ship.get_proximity_coords():
            for other_ship in self.ships:
                for other_coord in other_ship.get_coords():
                    if coord == other_coord:
                        raise ValueError("корабли стоят слишком близко")

    def print(self):
        # noinspection PyUnusedLocal
        temp_matrix = [[' ' for x in range(X_SIZE + 1)] for y in range(Y_SIZE + 1)]
        self.__init_temp_matrix(temp_matrix)
        for ship in self.ships:
            self.render_ship_proximity_on_temp_matrix(ship, temp_matrix)
        self.__render_attack_points_on_temp_matrix(temp_matrix)
        for ship in self.ships:
            self.render_ship_on_temp_matrix(ship, temp_matrix)
        self.__print_temp_matrix(temp_matrix)

    @staticmethod
    def render_ship_proximity_on_temp_matrix(ship, temp_matrix):
        proximity_coords = ship.get_proximity_coords()
        for coord in proximity_coords:
            temp_matrix[coord.x + 1][coord.y + 1] = "."

    @staticmethod
    def render_ship_on_temp_matrix(ship, temp_matrix):
        coords = ship.get_coords()
        for num_coord in enumerate(coords):
            damage = ship.damage[num_coord[0]]
            coord = num_coord[1]
            temp_matrix[coord.x + 1][coord.y + 1] = "X" if damage else "S"

    def __render_attack_points_on_temp_matrix(self, temp_matrix):
        for coord in self.attack_points:
            temp_matrix[coord.x + 1][coord.y + 1] = "_"

    @staticmethod
    def __init_temp_matrix(temp_matrix):
        for y in range(0, Y_SIZE + 1):
            temp_matrix[0][y] = str(y - 1) if y > 0 else ' '
        for x in range(0, X_SIZE + 1):
            temp_matrix[x][0] = chr(ord('a') + x - 1) if x > 0 else ' '

    @staticmethod
    def __print_temp_matrix(temp_matrix):
        for row in temp_matrix:
            tstr = ''
            for col in row:
                tstr += col
            print(tstr)

    def attack(self, x_input, y_input):
        x = ord(x_input) - ord('a')
        y = int(y_input)
        attack_point = Coord(x, y)

        self.attack_points.append(attack_point)

        for ship in self.ships:
            if ship.attack(attack_point):
                break
