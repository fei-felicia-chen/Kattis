"""run-time error??"""
d = dict()
walter, jesse = set(), set()
all_ingredients = list()

def dfs(ing):
    if (ing not in walter and ing not in jesse):
        walter.add(ing)
    for stg in d[ing]:
        not_anywhere = stg not in walter and stg not in jesse
        if (ing in walter and not_anywhere):
            jesse.add(stg)
            dfs(stg)
        if (ing in jesse and not_anywhere):
            walter.add(stg)
            dfs(stg)
        if (ing in walter and stg in walter) or (ing in jesse and stg in jesse):
            return False

for _ in range(int(input())):
    ing = input()
    all_ingredients.append(ing)
    d[ing] = set()

for _ in range(int(input())):
    ing1, ing2 = input().split()
    d[ing1].add(ing2)
    d[ing2].add(ing1)

for ing in all_ingredients:
    if dfs(ing) == False:
        print("impossible")
        break
else:
    for ing in walter:
        print(ing, end = " ")
    print("")
    for ing in jesse:
        print(ing, end = " ")