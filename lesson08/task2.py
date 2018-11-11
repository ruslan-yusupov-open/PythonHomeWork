# Морской бой для игры с компьютером

import random
from re import match
from models.models import Player

# random.seed(127)

player1 = Player("Player 1")
player2 = Player("Player 2", is_robot=True)

print("{}, введи поле:".format(player1.name))
player1.init()

player2.init()

active_player_num = 1

endgame = False

while True:
    attacking_player = player1 if active_player_num == 1 else player2
    attacked_player = player2 if active_player_num == 1 else player1

    if attacking_player.is_robot is False:
        print("{}, твой ход".format(attacking_player.name))
    else:
        print("{}, ходит компьютер".format(attacking_player.name))
        
    while True:
        try:
            if attacking_player.is_robot is False:
                print("твое поле:")
                attacking_player.field.print()
                print("поле врага:")
                attacked_player.field.print(hidden=True)

                invite = "{}, куда палить?, (буква, цифра, например a0)".format(attacking_player.name)
                input_str = input(invite)

                if not match(r"^[a-j][0-9]$", input_str):
                    raise ValueError("плохой ввод")
            else:
                x = chr(random.randint(0, 9) + ord('a'))
                y = random.randint(0, 9)
                input_str = "{}{}".format(x, y)

            result = attacked_player.field.attack(input_str[0], input_str[1])

            if result is False:
                active_player_num = 2 if active_player_num == 1 else 1
            else:
                if attacked_player.field.check_all_ships_dead():
                    print("Игрок {} победил".format(attacking_player.name))
                    endgame = True

        except ValueError as v:
            if attacking_player.is_robot is False:
                print("ошибка " + str(v))
            continue

        break

    if endgame is True:
        break
