# 15 how to solve

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

process_state(f)
print(min(available_states.keys()))

for z in range(0, 10000000):
    i = min(available_states.keys())

    process_state(available_states[i].pop())
    if len(available_states[i]) == 0:
        del available_states[i]

print('ss', len(saved_states))
print('as', len(available_states))
print('kl', min(available_states.keys()))

i = min(available_states.keys())

available_states[i].pop().print()
