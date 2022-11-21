def play(a, b):
    if a > b:
        return play(b, a)
    if b == 0:
        return False
    if b % a == 0:
        return True
    if (b // a) == 1:
        return (not play(a, b - a))
    return True

a, b = map(int, input().split())

while (a | b):
    if (play(a, b)):
        print("Stan wins")
    else:
        print("Ollie wins")
    a, b = map(int, input().split())
