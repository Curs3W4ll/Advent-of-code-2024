def add(x: int, y: int) -> int: return x + y
def mul(x: int, y: int) -> int: return x * y
def concat(x: int, y: int) -> int: return int(f"{x}{y}")
operations = [add, mul, concat]

def toBase(number: int, base: int):
    if number == 0:
        return "0"

    digits = []

    while number > 0:
        digits.append(str(number % base))
        number //= base
    return "".join(reversed(digits))

def applyOperations(numbers: list[int], number: int):
    value = numbers[0]
    ops = [int(x) for x in toBase(number, len(operations)).zfill(len(numbers))]

    for i in range(1, len(numbers)):
        value = operations[ops[i - 1]](value, numbers[i])

    return value

def run(input: list[str]):
    calibration = 0
    for l in input:
        s = l.split(": ")
        total: int = int(s[0])
        numbers: list[int] = [int(x) for x in s[1].split()]

        for i in range(int(f"{len(operations) - 1}" * len(numbers), len(operations)) + 1):
            if applyOperations(numbers, i) == total:
                calibration += total
                break

    print(f"The total calibration result is {calibration}")
