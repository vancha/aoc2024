def process(stones):
    tmp = []
    for stone in stones:
        word = str(stone)
        if stone == 0:
            tmp.append(1)
        elif len(word) % 2 == 0:
            middle = len(word) // 2
            tmp.append(int(word[0:middle]))
            tmp.append(int(word[middle:]))
            print(f"added {tmp[-2:]}")
        else:
            tmp.append(stone * 2024)
    return tmp
               
    
    
stones = [125, 17]
blinks = 25

for blink in range(blinks):
    stones = process(stones)
    print(stones)

print(len(stones))
     


