state = [True, False, False]
for char in input():
    if char == 'A':
        state[0], state[1] = state[1], state[0]
    elif char == 'B':
        state[1], state[2] = state[2], state[1]
    else:
        state[0], state[2] = state[2], state[0]

for i in range(3):
    if state[i]:
        print(i + 1)