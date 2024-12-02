input = """3   4
4   3
2   5
1   3
3   9
3   3"""

left,right = [],[]
for line in input.split("\n"):
   split = line.split("   ")
   left.append(int(split[0]))
   right.append(int(split[1]))

occurances = {}

left.sort()
right.sort()

result = 0
for num in left:
    if num not in occurances:
        occurances[num] = right.count(num)

for num in left:
    result += num * occurances[num]

print(result)
