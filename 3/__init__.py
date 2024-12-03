import re

regexPattern = r"mul\((\d{1,3}),(\d{1,3})\)"
dontRegexPattern = r"don't\(\).*?do\(\)"

def countMulValue(s: str):
    total = 0

    matches = re.finditer(regexPattern, s)
    for match in matches:
        total += int(match.group(1)) * int(match.group(2))

    return total

def run(input: list[str]):
    print(f"Result of all the multiplications is {countMulValue(''.join(input))}")

    withoutDont = re.sub(dontRegexPattern, "", "".join(input))
    print(f"Result valid multiplications is {countMulValue(withoutDont)}")
