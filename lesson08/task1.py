# Морской бой для двух игроков, есть 2 поля, где выставляются корабли
# есть 4 корабля по 1 клетке, 3 по 2 клетки, 2 по 3 клетки и 1 по 4 клетки
# корабли нельзя ставить впритык
from models.models import Field, Ship

a = Field()

a.add_ship(Ship('a', 0, 4, 'h'))
a.add_ship(Ship('e', 2, 3, 'v'))
a.add_ship(Ship('f', 4, 3, 'h'))

a.print()
#
# ship1 = Ship('a', 0, 2, 'h')
# print(ship1.get_coords())
#
# ship2 = Ship('e', 2, 3, 'v')
# print(ship2.get_proximity_coords())
