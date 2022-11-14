int(input())
cards = list(map(int, input().split()))
cards = [(lambda x: x & 1)(x) for x in cards]
stack = []

for card in cards:
    if stack and (stack[-1] == card):
        stack.pop()
    else:
        stack.append(card)

print(len(stack))