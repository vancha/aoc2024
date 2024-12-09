actual_str = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rules, updates = actual_str.split("\n\n")

def nums_must_come_before(input_str):
    global rules, updates;
    ordering = {}
    for rule in rules.split("\n"):
        before, after = map(int, rule.split("|"))
        if after not in ordering:
            ordering[after] = [before]
        else:
            ordering[after].append(before)
    return ordering

ordering = nums_must_come_before(actual_str)

def correctly_ordered(update):
    global ordering
    for index,value in enumerate(update):
        if value in ordering:
            for number in ordering[value]:
                if number in update[index:]:
                    return False
    return True

#turns the excerpt in to individual lines
update_lines        = updates.splitlines()
updates_as_integers = map(lambda x: list(map(int,x.split(","))),update_lines)
filtered            = filter(lambda x: correctly_ordered(x), updates_as_integers)
middle_numbers      = list(map(lambda x: x[len(x)//2], filtered))
summed              = sum(middle_numbers)

print(summed)
