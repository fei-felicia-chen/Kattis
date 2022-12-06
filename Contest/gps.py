import math


def getPos(positions, time):
    x1, y1, t1 = positions[0]
    x2, y2, t2 = positions[1]
    for i in range(1, len(positions) - 1):
        if t1 <= time and t2 >= time:
            break
        else:
            x1, y1, t1 = positions[i]
            x2, y2, t2 = positions[i + 1]
    ratio = (time - t1) / (t2 - t1)
    x = (x2 - x1) * ratio + x1
    y = (y2 - y1) * ratio + y1
    return x, y


# Get input
num_pos, interval = map(int, input().split())
positions = [list(map(int, input().split())) for _ in range(num_pos)]
_, _, final_time = positions[-1]

# Get true distance
true_distance = 0
for i in range(num_pos - 1):
    x1, y1, t1 = positions[i]
    x2, y2, t2 = positions[i + 1]
    true_distance += math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

# Get GPS Coords
gps_pos = [positions[0]]
time = interval
while True:
    x1, y1 = getPos(positions, time)
    gps_pos.append((x1, y1, time))
    time += interval
    if time >= final_time:
        gps_pos.append(positions[-1])
        break

# Get GPS distance
gps_distance = 0
for i in range(len(gps_pos) - 1):
    x1, y1, t1 = gps_pos[i]
    x2, y2, t2 = gps_pos[i + 1]
    gps_distance += math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
print((true_distance - gps_distance) / true_distance * 100)
