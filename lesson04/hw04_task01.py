# игра пятнашки

# поле
import random

field = [['', ] * 4, ['', ] * 4, ['', ] * 4, ['', ] * 4]


# с остатком не очень красиво, зато короче
def get_blank_pos():
    for i in range(0, 16):
        if (field[int((i - i % 4) / 4)][i % 4]) == ' ':
            return int((i - i % 4) / 4), i % 4


def check_is_target():
    btn_arr = list(range(1, 16))
    for i in range(0, 15):
        if field[int((i - i % 4) / 4)][i % 4] != str(btn_arr[i]):
            return False
    return field[3][3] == ' '


def reset_field():
    btn_arr = list(range(1, 16))
    random.shuffle(btn_arr)

    for i in range(0, 15):
        field[int((i - i % 4) / 4)][i % 4] = str(btn_arr[i])

    field[3][3] = ' '


def print_field():
    print("-" * 13)
    for i in range(0, 4):
        new_str = "|"
        for j in range(0, 4):
            if field[i][j] == ' ':
                new_str += '  |'
            elif int(field[i][j]) > 9:
                new_str += field[i][j] + "|"
            else:
                new_str += field[i][j] + " |"
        print(new_str)
    print("-" * 13)


def move_field(direction):
    if direction in ('up', 'down', 'left', 'right'):
        i, j = get_blank_pos()
        if direction == 'right' and j > 1:
            field[i][j] = field[i][j - 1]
            field[i][j - 1] = ' '
        if direction == 'left' and j < 3:
            field[i][j] = field[i][j + 1]
            field[i][j + 1] = ' '
        if direction == 'down' and i > 1:
            field[i][j] = field[i - 1][j]
            field[i - 1][j] = ' '
        if direction == 'up' and i < 3:
            field[i][j] = field[i + 1][j]
            field[i + 1][j] = ' '
    else:
        print("можно вводить только up, down, left, right")

    print_field()


reset_field()
print_field()

while True:
    dir_input = input("Введите куда двигать фишку up, down, left, right")
    move_field(dir_input)
    if check_is_target():
        break
