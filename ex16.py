from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTR-C (^C).")
print("If you do want that, hit ENTER.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncate the file. Goodbye!\n")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()