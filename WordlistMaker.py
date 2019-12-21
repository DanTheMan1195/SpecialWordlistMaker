import sys
from itertools import permutations

lines = 0

with open("email.txt", "w") as wl:
    for group in permutations(['mark', 'andy', 'donovin', 'donny', '12', '1998', 'paul', 'birthday'], 2):
        wl.write("".join(group)+"\n")
        lines = lines + 1
print("Done!")
print("Amount of lines: ", str(lines))
