import copy

spaceId = -1

def dumpCases(cases: list[int]):
    for case in cases:
        if case == spaceId:
            print(".", end="")
        else:
            print(case, end="")
    print("")

def isFullOfSpaces(cases: list[int]) -> bool:
    for case in cases:
        if case != spaceId:
            return False
    return True

def getFirstSpaceIndex(cases: list[int], length: int = 1) -> int:
    for i in range(len(cases)):
        if isFullOfSpaces(cases[i:i + length]):
            return i

    return len(cases)

def getChecksum(cases: list[int]) -> int:
    total = 0

    for i in range(len(cases)):
        if cases[i] == spaceId:
            continue
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

def fragmentKeepFiles(cases: list[int]) -> int:
    i = len(cases) - 1
    while i >= 0:
        currentId = cases[i]
        if currentId == spaceId:
            i -= 1
            continue
        length = 1
        while i - length > 0 and cases[i - length] == currentId:
            length += 1
        spaceIndex = getFirstSpaceIndex(cases, length)
        # Fit possible
        if not spaceIndex > i:
            for l in range(length):
                cases[spaceIndex + l] = currentId
                cases[i - l] = spaceId
        i -= length

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

    dumpCases(cases)
    casesCopy = copy.copy(cases)
    print(f"Filesystem checksum is {fragment(casesCopy)}")
    # dumpCases(casesCopy)
    print(f"Filesystem checksum is {fragmentKeepFiles(cases)} when keeping files continuity")
    # dumpCases(cases)
