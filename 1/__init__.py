from typing import List

def run(input: List[str]):
    l1,l2 = [int(i.split()[0]) for i in input],[int(i.split()[1]) for i in input]
    total = 0

    l1.sort()
    l2.sort()

    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])
    print(f"Total distance is: {total}")