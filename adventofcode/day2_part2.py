input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

for line in input.split('\n'):
    characters = line.split(" ")
    prev = characters[0]
    ascending = characters[1] > prev
    for character in characters[2:]:
        print(character)
    print("\n")
