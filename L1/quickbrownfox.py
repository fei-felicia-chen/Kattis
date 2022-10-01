for i in range(int(input())):
    phrase = input().lower()
    missingLetters = []
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in phrase: missingLetters += letter
    print("pangram") if not missingLetters else print("missing", ''.join(missingLetters))