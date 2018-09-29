# это известная головоломка, я уже когда-то с ней встречался и алгоритм достаточно очевиден
# поэтому я сначал сделал, чтобы не портить удвольствие от решения и потом буду гулить
# решение является оптимальным, но как показать я не смотрел
# идея - перемещаяем меньшую пирамидку на свободное место, передвигаем основание на целевое место
# потом перемещаем пирамидку на свободное место, сложность 2^n - 1

height = 0

while not height > 0:
    try:
        height = int(input("введите натуральное число - высоту пирамидки: "))
        if height <= 0:
            raise ValueError()
    except ValueError:
        print("введите целое число больше нуля")


def get_number_use_to_move(number_move_from, number_move_to):
    for i in (1, 2, 3):
        if i != number_move_from and i != number_move_to:
            return i


def move_tower(tower_height, number_move_from, number_move_to):
    if tower_height == 0:
        return
    number_use_to_move = get_number_use_to_move(number_move_from, number_move_to)
    move_tower(tower_height - 1, number_move_from, number_use_to_move)
    move_base(tower_height, number_move_from, number_move_to)
    move_tower(tower_height - 1, number_use_to_move, number_move_to)


def move_base(base_number, move_from, move_to):
    print(base_number, move_from, move_to)


move_tower(height, 1, 3)
