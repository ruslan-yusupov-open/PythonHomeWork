from random import shuffle


class Field15:
    coords = {
        0: (0, 0),
        1: (1, 0),
        2: (2, 0),
        3: (3, 0),
        4: (0, 1),
        5: (1, 1),
        6: (2, 1),
        7: (3, 1),
        8: (0, 2),
        9: (1, 2),
        10: (2, 2),
        11: (3, 2),
        12: (0, 3),
        13: (1, 3),
        14: (2, 3),
        15: (3, 3),
    }

    reverseCoords = {
        (0, 0): 0,
        (1, 0): 1,
        (2, 0): 2,
        (3, 0): 3,
        (0, 1): 4,
        (1, 1): 5,
        (2, 1): 6,
        (3, 1): 7,
        (0, 2): 8,
        (1, 2): 9,
        (2, 2): 10,
        (3, 2): 11,
        (0, 3): 12,
        (1, 3): 13,
        (2, 3): 14,
        (3, 3): 15,
    }

    perfectPosition = {
        '1': (0, 0),
        '2': (1, 0),
        '3': (2, 0),
        '4': (3, 0),
        '5': (0, 1),
        '6': (1, 1),
        '7': (2, 1),
        '8': (3, 1),
        '9': (0, 2),
        'a': (1, 2),
        'b': (2, 2),
        'c': (3, 2),
        'd': (0, 3),
        'e': (1, 3),
        'f': (2, 3),
        ' ': (3, 3),
    }

    __way = ''

    NORM_STR = '123456789abcdef '

    @staticmethod
    def __get_distance(point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

    @staticmethod
    def generate_shuffle():
        norm_str = Field15.NORM_STR
        the_list = [c for c in norm_str]
        shuffle(the_list)
        return Field15(''.join(the_list))

    def __init__(self, state=NORM_STR, way=''):
        self.__possible_movements = []
        self.__state = state
        self.__way = way
        self.__empty_coords = self.coords[state.find(" ")]
        self.__fill_possible_movements()
        self.distance = 0
        self.set_metric()

    def __str__(self):
        return self.__state

    def print(self):
        print(self.__way)
        print(self.__state[0:4])
        print(self.__state[4:8])
        print(self.__state[8:12])
        print(self.__state[12:16])
        print(self.__empty_coords)
        print(self.__possible_movements)
        print(self.distance)

    def __fill_possible_movements(self):
        if self.__empty_coords[0] > 0:
            self.__possible_movements.append('r')
        if self.__empty_coords[0] < 3:
            self.__possible_movements.append('l')
        if self.__empty_coords[1] > 0:
            self.__possible_movements.append('d')
        if self.__empty_coords[1] < 3:
            self.__possible_movements.append('u')

    def get_possible_movements(self):
        return self.__possible_movements

    def move(self, direction):
        if direction in self.__possible_movements:
            swap_coords = None
            if direction == 'd':
                swap_coords = (self.__empty_coords[0], self.__empty_coords[1] - 1)
            if direction == 'u':
                swap_coords = (self.__empty_coords[0], self.__empty_coords[1] + 1)
            if direction == 'r':
                swap_coords = (self.__empty_coords[0] - 1, self.__empty_coords[1])
            if direction == 'l':
                swap_coords = (self.__empty_coords[0] + 1, self.__empty_coords[1])

            swap_char = self.__state[self.reverseCoords[swap_coords]]
            new_state = self.__state.replace(swap_char, "#").replace(" ", swap_char).replace("#", " ")
            return Field15(new_state, self.__way + direction)

    def set_metric(self):
        self.distance = 0
        for i in range(0, 16):
            char = self.__state[i]
            self.distance += Field15.__get_distance(self.perfectPosition[char], self.coords[i]) * (16 - i) * (16 - i)
            self.distance += len(self.__way)
