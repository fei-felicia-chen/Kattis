testCases = int(input())
for _ in range(testCases):
    encoded = input()
    key = int(len(encoded) ** 0.5)
    square = [[''] * key for __ in range(key)]
    decoded = ""
    for index, character in enumerate(encoded):
        square[index // key][index % key] = character
    for index, row in enumerate(square):
        square[index] = row[::-1]
    for i in range(key):
        for j in range(key):
            decoded += square[j][i]
    print(decoded)