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

left.sort()
right.sort()

result = 0
for num in left:
    result += abs(num - right.pop(0))

print(result)
