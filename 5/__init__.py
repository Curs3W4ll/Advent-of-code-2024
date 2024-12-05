def isUpdateMatchingRule(update: list[int], rule: tuple[int, int]) -> bool:
    if update.count(rule[0]) > 0:
        if update[:update.index(rule[0])].count(rule[1]):
            return False

    return True

def fixUpdate(update: list[int], rules: list[tuple[int, int]]) -> list[int]:
    for rule in rules:
        if not isUpdateMatchingRule(update, rule):
            update.remove(rule[1])
            update.insert(update.index(rule[0]) + 1, rule[1])

    return update

def run(input: list[str]):
    emptyLineIndex = input.index("")
    rules: list[tuple[int, int]] = []
    invalidUpdatesCorrected: list[list[int]] = []
    validUpdates: list[list[int]] = []
    validTotal = 0
    invalidTotal = 0

    for l in input[:emptyLineIndex]:
        numbers = l.split("|")
        rules.append((int(numbers[0]), int(numbers[1])))
    rules = sorted(rules, key=lambda rule: rule[1])

    for l in input[emptyLineIndex + 1:]:
        lineWithNumbers = [int(x) for x in l.split(",")]
        if all(isUpdateMatchingRule(lineWithNumbers, rule) for rule in rules):
            validUpdates.append(lineWithNumbers)
        else:
            invalidUpdatesCorrected.append(fixUpdate(lineWithNumbers, rules))

    for l in validUpdates:
        validTotal += l[len(l) // 2]
    for l in invalidUpdatesCorrected:
        invalidTotal += l[len(l) // 2]

    print(f"Sum of middle page number of correctly-ordered udpates is {validTotal}")
    print(f"Sum of middle page number of corrected udpates is {invalidTotal}")
