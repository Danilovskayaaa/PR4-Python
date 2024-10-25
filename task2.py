filename = input("Введите имя файла: ")

with open(filename, 'r') as file:
    lines = file.readlines()

index = 1
for line in lines:
    print(f"{index} {line.rstrip()}")
    index+=1
