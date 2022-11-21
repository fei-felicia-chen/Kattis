from string import ascii_lowercase
import requests

letters = ascii_lowercase
for i in letters:
    for j in letters:
        for k in letters:
          word = i+j+k
          r = requests.post("https://conuhacks.io/api/auth",
                            json={"answer": word, "challenge":"cb3"})
          print(word)
          if "yes" in r.content.decode("utf-8"):
            print("found word", word)
            exit()