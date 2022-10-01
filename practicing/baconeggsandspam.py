visitors = int(input())
while visitors != 0:
    all = list()
    ingredients = list()
    for _ in range(visitors):
        order = input().split()
        all.append(order)
        for i in range(1, len(order)):
            ingredients.append(order[i])
    ing = set(ingredients).sort()
    for ingr in ing:
        for o in all:
            if ingr in o:
                print("bruh wtf is this")
    visitors = int(input())