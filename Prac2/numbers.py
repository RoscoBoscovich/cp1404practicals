


file = open("numbers.txt")
total = 0
for line in file:
    number = int(line)
    total = total + number
print("The total is",total)
file.close()