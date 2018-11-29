# 15 how to solve
import time
import random

from models import Field15

random.seed(127)

f = Field15.generate_shuffle()
print(f, f.distance)

f.print()

x1, y1 = find(1)

while y1 > 0:
    go(x1, y1 - 1)
    swap(x1, y1)

while x1 > 0:
    go(x1 - 1, y1)
    swap(x1, y1)


def go(xt, yt):
    if x<xt and not_fixed():
        swap()



# x1, y1
# if(y1>

#
# saved_states = {}
# available_states = {}
#
#
# def process_state(field_state):
#     for m in field_state.get_possible_movements():
#         zz = field_state.move(m)
#         z_str = str(zz)
#         z_dist = zz.distance
#
#         if z_str not in saved_states:
#             saved_states[z_str] = 1
#             if z_dist in available_states:
#                 available_states[z_dist].append(zz)
#             else:
#                 available_states[z_dist] = [zz]
#
#
# f.print()
#
# process_state(f)
# print(min(available_states.keys()))
#
# start = time.time()
#
# for z in range(0, 100000):
#
#     i = min(available_states.keys())
#
#     check_state = available_states[i].pop()
#
#     process_state(check_state)
#
#     if len(available_states[i]) == 0:
#         del available_states[i]
#
#     if time.time() - start > 10:
#         start = time.time()
#         print("iterations: ", z)
#         print('ss', len(saved_states))
#         print('as', len(available_states))
#         print('kl', min(available_states.keys()))
#
# print('ss', len(saved_states))
# print('as', len(available_states))
# print('kl', min(available_states.keys()))
#
# i = min(available_states.keys())
#
# available_states[i].pop().print()
