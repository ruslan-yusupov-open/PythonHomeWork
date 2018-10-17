# 15 how to solve
import time

from models import Field15

f = Field15.generate_shuffle()
print(f, f.distance)

saved_states = {}
available_states = {}


def process_state(field_state):
    for m in field_state.get_possible_movements():
        zz = field_state.move(m)
        z_str = str(zz)
        z_dist = zz.distance

        if z_str not in saved_states:
            saved_states[z_str] = 1
            if z_dist in available_states:
                available_states[z_dist].append(zz)
            else:
                available_states[z_dist] = [zz]


f.print()

check_state = f
process_state(f)
print(min(available_states.keys()))

start = time.time()

besti = 1000000
beststate = check_state

for z in range(0, 10000000):

    i = min(available_states.keys())

    check_state = available_states[i].pop()

    if i < besti:
        besti = i
        beststate = check_state

    process_state(check_state)

    if len(available_states[i]) == 0:
        del available_states[i]
        if len(available_states) == 0:
            break

    if time.time() - start > 10:
        start = time.time()
        print("iterations: ", z)
        print('ss', len(saved_states))
        print('as', len(available_states))
        print('kl', min(available_states.keys()))

if len(available_states) == 0:
    beststate.print()
    print(besti)
else:
    print('ss', len(saved_states))
    print('as', len(available_states))
    print('kl', min(available_states.keys()))

    i = min(available_states.keys())

    available_states[i].pop().print()
