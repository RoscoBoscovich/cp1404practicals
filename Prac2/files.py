


OUTPUT_FILE = "names.txt"
out_file = open(OUTPUT_FILE, 'a')

name = (input("Enter your name: "))
print(name, file=out_file)


file = open(OUTPUT_FILE)
for line in file:
    name = line
    print("Your Name is",format(line))
file.close()



