# Морской бой для двух игроков, есть 2 поля, где выставляются корабли
# есть 4 корабля по 1 клетке, 3 по 2 клетки, 2 по 3 клетки и 1 по 4 клетки
# корабли нельзя ставить впритык
# import random
from re import match
from models.models import Player

player1 = Player("Player 1")
player2 = Player("Player 2")

print("{}, введи поле:".format(player1.name))
player1.init()

print("{}, введи поле:".format(player2.name))
player2.init()

active_player_num = 1

endgame = False

while True:
    attacking_player = player1 if active_player_num == 1 else player2
    attacked_player = player2 if active_player_num == 1 else player1

    while True:
        try:
            print("{}, твой ход".format(attacking_player.name))
            print("твое поле:")
            attacking_player.field.print()
            print("поле врага:")
            attacked_player.field.print(hidden=True)

            invite = "{}, куда палить?, (буква, цифра, например a0)".format(attacking_player.name)
            input_str = input(invite)

            if not match(r"^[a-j][0-9]$", input_str):
                raise ValueError("плохой ввод")

            result = attacked_player.field.attack(input_str[0], input_str[1])

            print(attacked_player.name)
            attacked_player.field.print(hidden=True)

            if result is False:
                active_player_num = 2 if active_player_num == 1 else 1
            else:
                if attacked_player.field.check_all_ships_dead():
                    print("Игрок {} победил".format(attacking_player.name))
                    endgame = True

        except ValueError as v:
            print("ошибка " + str(v))
            continue

        break

    if endgame is True:
        break
