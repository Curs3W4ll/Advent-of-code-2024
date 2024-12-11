def dumpStones(stones: list[int]):
    for stone in stones:
        print(stone, end=" ")
    print()

def blink(stones: list[int], times: int = 1):
    print(f"{times} blinks remaining")

    if times < 1:
        return stones

    newStones: list[int] = []

    for stone in stones:
        stoneAsString = str(stone)
        if stone == 0:
            newStones.append(1)
        elif len(stoneAsString) % 2 == 0:
            middle = len(str(stone)) // 2
            newStones.append(int(stoneAsString[:middle]))
            newStones.append(int(stoneAsString[middle:]))
        else:
            newStones.append(stone * 2024)

    return blink(newStones, times - 1)

def run(input: list[str]):
    stones: list[int] = [int(x) for x in input[0].split()]

    print(f"After blinking 25 times, we now have {len(blink(stones, 25))} stones")
