input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

#supposed to have two safe rows

#returns true if all numbers in number list are strictly increasing (No similar numbers)
def strictly_increasing(number_list):
    prev = number_list[0]
    for num in number_list[1:]:
        if num < prev or num == prev:
            return False
        prev = num
    return True

#same, but for decreasing numbers
def strictly_decreasing(number_list):
    prev = number_list[0]
    for num in number_list[1:]:
        if num > prev or num == prev:
            return False
        prev = num
    return True

#returns true if the differences between all subsequent numbers is at least one and at most three
def level_difference(number_list):
    prev = number_list[0]
    for num in number_list[1:]:
        if abs(num - prev) < 1  or abs(num - prev) > 3:
            return False
        prev = num
    return True

result = 0


def generate_permutations(original_list):
    duplicates = []#original_list]*len(original_list)

    for index in range(len(original_list)-1):
        duplicates.append(original_list.copy())
        duplicates[index].pop(index)

    return duplicates

for line in input.split('\n'):
    characters = line.split(" ")
    numberlist = list(map(int, characters))
    if (strictly_increasing(numberlist) or strictly_decreasing(numberlist)) and level_difference(numberlist):
        result += 1
    else:
        #if the current list has N values, generate n-1 new lists from it. Every list has one digit removed. If any of those lists are valid, still increment the result with one.
        for permutation in generate_permutations(numberlist):
            if (strictly_increasing(permutation) or strictly_decreasing(permutation)) and level_difference(permutation):
                result += 1
                break


print(result)
