def isUpdateMatchingRules(update: list[int], rule: tuple[int, int]) -> bool:
    if update.count(rule[0]) > 0:
        if update[:update.index(rule[0])].count(rule[1]):
            return False

    return True

def run(input: list[str]):
    emptyLineIndex = input.index("")
    rules: list[tuple[int, int]] = []
    validUpdates: list[list[int]] = []
    total = 0

    for l in input[:emptyLineIndex]:
        numbers = l.split("|")
        rules.append((int(numbers[0]), int(numbers[1])))

    for l in input[emptyLineIndex + 1:]:
        lineWithNumbers = [int(x) for x in l.split(",")]
        if all(isUpdateMatchingRules(lineWithNumbers, rule) for rule in rules):
            validUpdates.append(lineWithNumbers)

    for l in validUpdates:
        total += l[len(l) // 2]

    print(f"Sum of middle page number of correctly-ordered udpates is {total}")
