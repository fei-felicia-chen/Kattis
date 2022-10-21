"""https://open.kattis.com/problems/quickbrownfox"""
for i in range(int(input())):
    phrase = input().lower()
    missingLetters = []
    alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z'}
    for letter in alphabet:
        if letter not in phrase: missingLetters += letter
    print("pangram") if not missingLetters else print("missing", ''.join(missingLetters))