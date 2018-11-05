# Морской бой для двух игроков, есть 2 поля, где выставляются корабли
# есть 4 корабля по 1 клетке, 3 по 2 клетки, 2 по 3 клетки и 1 по 4 клетки
# корабли нельзя ставить впритык
from models.models import Field, Ship
import random
from re import match

player1_field = Field()

need_to_insert = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

random.seed(127)


def random_fill():
    while len(need_to_insert) > 0:
        to_insert_len = need_to_insert[len(need_to_insert) - 1]
        # TODO: для корабля длинной 1 ориентация не нужна

        try:
            x = chr(random.randint(0, 9) + ord('a'))
            y = random.randint(0, 9)
            o = random.choice(('h', 'v'))

            player1_field.add_ship(Ship(x, y, to_insert_len, o))
        except ValueError as v:
            # print("ошибка " + str(v))
            continue

        del need_to_insert[len(need_to_insert) - 1]

    player1_field.print()


def interactive_fill():
    while len(need_to_insert) > 0:
        to_insert_len = need_to_insert[len(need_to_insert) - 1]
        # TODO: для корабля длинной 1 ориентация не нужна
        invite = "введите корабль, длинна {} (буква, цифра, ориентация (h,v), например a0v) ".format(to_insert_len)

        try:
            input_str = input(invite)

            if not match(r"^[a-j][0-9][hv]$", input_str):
                raise ValueError("плохой ввод")

            player1_field.add_ship(Ship(input_str[0], input_str[1], to_insert_len, input_str[2]))
            player1_field.print()

        except ValueError as v:
            print("ошибка " + str(v))
            continue

        del need_to_insert[len(need_to_insert) - 1]


random_fill()

player1_field.attack('a', '0')
player1_field.attack('a', '2')
player1_field.attack('a', '0')
player1_field.attack('a', '3')
player1_field.attack('a', '4')
player1_field.attack('a', '5')
player1_field.attack('b', '5')
player1_field.attack('a', '7')
player1_field.print()

while False:
    invite = "куда палить?, (буква, цифра, например a0)"

    try:
        input_str = input(invite)

        if not match(r"^[a-j][0-9]$", input_str):
            raise ValueError("плохой ввод")

        player1_field.attack(input_str[0], input_str[1])
        player1_field.print()

    except ValueError as v:
        print("ошибка " + str(v))
        continue

# input_str = "a8h"
#
# player1_field.add_ship(Ship(input_str[0], input_str[1], 4, input_str[2]))
# player1_field.print()

# ship1 = Ship('a', 0, 2, 'h')
# print(ship1.get_coords())
#
# ship2 = Ship('e', 2, 3, 'v')
# print(ship2.get_proximity_coords())
