from itertools import permutations

lines = 0
array = input("All words (separate by spaces): ").split()
min = int(input("What's the min amount of words to combine per word: "))
max = int(input("What's the max amount of words to combine per word: "))
output = input("Output file name: ")
combination = 0

wl = open(output, "w")
while combination != max:
    for group in permutations(array, combination):
        wl.write("".join(group)+"\n")
        lines = lines + 1
    combination = combination + 1
    print(str(combination))
wl.close()
print("Done!")
print("Amount of lines: ", str(lines))
