"""https://open.kattis.com/problems/birds"""
wire_length, d, n = map(int, input().split())
pole = []

nb = 0

if n==0:
    pole.append(6)
    pole.append(wire_length-6)
    nb+=2
else:
    for _ in range(n):
        pole.append(int(input()))
    pole.sort()

    if pole[0] != 6 and pole[0]-6 >= d:
        pole.append(6)
        nb += 1
    if pole[-1] != wire_length-6 and abs(pole[-1] - (wire_length-6)) >= d:
        pole.append(wire_length - 6)
        nb += 1
    pole.sort()
for i in range(len(pole) - 1):
    a = pole[i]
    b = pole[i + 1]
    nb += ((b-a) // d) - 1
# 6 9 11 16
print(nb)
