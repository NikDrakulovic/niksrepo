filename = 'programing.txt'

name = input("Enter your name ")

with open(filename, 'w') as file_object:
    file_object.write(f"{name} loves programming programming.\n")
    file_object.write(f"{name} loves creating new games. \n")
    file_object.write(f"{name} thinks andrew is a massive bitch\n")

with open(filename, 'a') as file_object:
    file_object.write("gaming poggers\n")
    file_object.write("big chungus \n")