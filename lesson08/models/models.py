# размера поля жестко задан 10х10
X_SIZE = 10
Y_SIZE = 10


# поле 10х10, содержит корабли
class Ship:
    def __init__(self, x, y, length, orientation):
        if orientation not in ['h', 'v']:
            raise ValueError("orientation should be h or v")

        self.length = length
        self.orientation = orientation
        self.x = ord(x) - ord('a')
        self.y = int(y)

    def get_coords(self):
        if self.orientation == 'v':
            return [(self.x + i, self.y) for i in range(0, self.length)]
        else:
            return [(self.x, self.y + i) for i in range(0, self.length)]

    def get_proximity_coords(self):
        proximity_coords = []
        for i in range(-1, self.length + 1):
            x = self.x + i if self.orientation == 'v' else self.x
            y = self.y if self.orientation == 'v' else self.y + i
            if x in range(0, X_SIZE) and y in range(0, Y_SIZE):
                proximity_coords.append((x, y))

            x = self.x + i if self.orientation == 'v' else self.x + 1
            y = self.y + 1 if self.orientation == 'v' else self.y + i
            if x in range(0, X_SIZE) and y in range(0, Y_SIZE):
                proximity_coords.append((x, y))

            x = self.x + i if self.orientation == 'v' else self.x - 1
            y = self.y - 1 if self.orientation == 'v' else self.y + i
            if x in range(0, X_SIZE) and y in range(0, Y_SIZE):
                proximity_coords.append((x, y))

        return proximity_coords


class Field:
    def __init__(self):
        self.ships = []

    def add_ship(self, ship: Ship):
        self.check_ships_collision(ship)
        self.ships.append(ship)

    def check_ships_collision(self, ship):
        for coord in ship.get_coords():
            if coord[0] not in range(0, X_SIZE) or coord[1] not in range(0, Y_SIZE):
                raise ValueError("корабль выходит за границу поля")

        for coord in ship.get_proximity_coords():
            other_ship: Ship
            for other_ship in self.ships:
                for other_coord in other_ship.get_coords():
                    if other_coord[0] == coord[0] and other_coord[1] == coord[1]:
                        raise ValueError("корабли стоят слишком близко")

    def print(self):
        # noinspection PyUnusedLocal
        temp_matrix = [[' ' for x in range(X_SIZE + 1)] for y in range(Y_SIZE + 1)]
        self.__init_temp_matrix(temp_matrix)
        for ship in self.ships:
            self.render_ship_on_temp_matrix(ship, temp_matrix)
        self.__print_temp_matrix(temp_matrix)

    @staticmethod
    def render_ship_on_temp_matrix(ship, temp_matrix):
        proximity_coords = ship.get_proximity_coords()
        for coord in proximity_coords:
            temp_matrix[coord[0] + 1][coord[1] + 1] = "."
        coords = ship.get_coords()
        for coord in coords:
            temp_matrix[coord[0] + 1][coord[1] + 1] = "S"

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
