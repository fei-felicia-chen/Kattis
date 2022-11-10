from math import pi, cos, sin

cases = int(input())

for _ in range(cases):
    commands = int(input())
    x = 0.
    y = 0.
    angle = 0
    for _ in range(commands):
        direction, distance = input().split()
        distance = int(distance)
        if (direction == "fd"):
            x += distance * sin(angle * (pi/180))
            y += distance * cos(angle * (pi/180))
        elif (direction == "bk"):
            x -= distance * sin(angle * (pi/180))
            y -= distance * cos(angle * (pi/180))
        elif (direction == "rt"):
            angle -= distance
        else:
            angle += distance
    distance = round((x**2 + y**2)**0.5)
    print(distance)