def getNewStones(stone: int) -> list[int]:
    stoneAsString = str(stone)
    if stone == 0:
        return [1]
    elif len(stoneAsString) % 2 == 0:
        middle = len(str(stone)) // 2
        return [int(stoneAsString[:middle]), int(stoneAsString[middle:])]
    return [stone * 2024]

def getStoneNbr(stones: dict[int, int]) -> int:
    total = 0

    for nbr in stones.values():
        total += nbr

    return total

def addInDict(d: dict[int, int], stone: int, times: int):
    if stone in d:
        d[stone] += times
    else:
        d[stone] = times

    return d

def blink(stones: dict[int, int], times: int = 1):
    print(f"{times} blinks remaining")

    if times < 1:
        return stones

    newStones: dict[int, int] = {}

    for stone, nbr in stones.items():
        for stone in getNewStones(stone):
            addInDict(newStones, stone, nbr)

    return blink(newStones, times - 1)

def run(input: list[str]):
    stones: dict[int, int] = {}

    for e in input[0].split():
        x = int(e)
        if x in stones:
            stones[x] += 1
        else:
            stones[x] = 1

    print(f"After blinking 25 times, we now have {getStoneNbr(blink(stones, 25))} stones")
    print(f"After blinking 75 times, we now have {getStoneNbr(blink(stones, 75))} stones")
