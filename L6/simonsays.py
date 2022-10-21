"""https://open.kattis.com/problems/simonsays"""
for _ in range(int(input())):
    phrase = input()
    if phrase[:10] == "Simon says": 
        print(phrase[11:])