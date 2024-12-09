spaceId = -1

def dumpCases(cases: list[int]):
    for case in cases:
        if case == spaceId:
            print(".", end="")
        else:
            print(case, end="")
    print("")

def getFirstSpaceIndex(cases: list[int]) -> int:
    for i in range(len(cases)):
        if cases[i] == spaceId:
            return i
    return len(cases)

def getChecksum(cases: list[int]) -> int:
    total = 0

    for i in range(len(cases)):
        if cases[i] == spaceId:
            break
        total += cases[i] * i

    return total

def fragment(cases: list[int]) -> int:
    for i in range(len(cases) -1, -1, -1):
        if cases[i] == spaceId:
            continue
        spaceIndex = getFirstSpaceIndex(cases)
        # No more fit possible
        if spaceIndex > i:
            break
        cases[spaceIndex] = cases[i]
        cases[i] = spaceId

    return getChecksum(cases)

def run(input: list[str]):
    cases: list[int] = []

    id = 0
    for i in range(len(input[0])):
        if i % 2 == 0:
            cases += [int(id) for _ in range(int(input[0][i]))]
            id += 1
        else:
            cases += [spaceId for _ in range(int(input[0][i]))]

    # dumpCases(cases)
    print(f"Filesystem checksum is {fragment(cases)}")
