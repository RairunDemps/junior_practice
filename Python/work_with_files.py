file_string = "Hello World!\nToady is a good day!\nMarco Polo"
filename = "data.txt"
with open(filename, "w") as file:
    file.write(file_string)

with open(filename, "r") as file:
    file.seek(4)
    print(file.tell())
    print(file.readline())
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
