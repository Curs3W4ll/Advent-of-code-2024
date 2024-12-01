def run(input: list[str]):
    l1,l2 = [int(i.split()[0]) for i in input],[int(i.split()[1]) for i in input]
    total = 0
    similarityScore = 0

    l1.sort()
    l2.sort()

    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])
    print(f"Total distance is: {total}")

    for i in range(len(l1)):
        if l1[i] in l2:
            similarityScore += (l1[i] * l2.count(l1[i]))
    print(f"Similarity score is: {similarityScore}")
