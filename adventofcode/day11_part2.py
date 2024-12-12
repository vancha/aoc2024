def process(stones):
    tmp = {}
    #stone holds the number written on the rock
    for stone in stones.keys():
        
        if stone == 0:
            if 1 in tmp:
                tmp[1] += stones[stone]
            else:
                tmp[1] = stones[stone]
        else:
            #has the number in string form
            word = str(stone)
            if len(word) % 2 == 0:
                middle = len(word) // 2
                left = int(word[0:middle])
                right = int(word[middle:])

                if left in tmp:
                    tmp[left] += stones[stone]
                else:
                    tmp[left] = stones[stone]

                if right in tmp:
                    tmp[right] += stones[stone]
                else:
                    tmp[right] = stones[stone]
            else:
                val = stone * 2024
                if val in tmp:
                    tmp[val] += stones[stone]
                else:
                    tmp[val] = stones[stone]
    return tmp
               
    
#stones = {125:1, 17:1}
stones = {5:1, 89749:1, 6061:1, 43:1, 867:1, 1965860:1, 0:1, 206250:1}
blinks = 75

for blink in range(blinks):
    stones = process(stones)

total = 0

for val in stones.keys():
    total +=  stones[val]

print(total)
     


