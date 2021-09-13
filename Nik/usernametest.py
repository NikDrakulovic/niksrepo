import json

filename = 'username.json'
try:
    with open(filename):
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename,'w') as f:
        json.dump(username, f)
        print(f"we will remember you when you come back {username}")
else:
    print(f"welcome back {username}")