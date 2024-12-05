def isMatchingSearchWord(s: str, searchWord: str):
    return (s == searchWord or s == searchWord[::-1])

def part1(input: list[str]):
    searchingWord = "XMAS"
    searchingWord = searchingWord.upper()
    searchingWordLen = len(searchingWord)
    wordCount = 0

    for i in range(len(input)):
        for y in range(len(input[i])):
            if input[i][y] != "X":
                continue
            # Right
            if y <= (len(input[i]) - searchingWordLen):
                if isMatchingSearchWord(input[i][y:y + searchingWordLen], searchingWord):
                    wordCount += 1

            # Left
            if y >= (searchingWordLen - 1):
                if isMatchingSearchWord(input[i][y - searchingWordLen + 1:y + 1], searchingWord):
                    wordCount += 1

            # Top
            if i >= (searchingWordLen - 1):
                w = ""
                for j in range(i, i - searchingWordLen, -1):
                    w += input[j][y]
                if isMatchingSearchWord(w, searchingWord):
                    wordCount += 1

                # Top Right
                if y <= (len(input[i]) - searchingWordLen):
                    k = y
                    w = ""
                    for j in range(i, i - searchingWordLen, -1):
                        w += input[j][k]
                        k += 1
                    if isMatchingSearchWord(w, searchingWord):
                        wordCount += 1

                # Top Left
                if y >= (searchingWordLen - 1):
                    k = y
                    w = ""
                    for j in range(i, i - searchingWordLen, -1):
                        w += input[j][k]
                        k -= 1
                    if isMatchingSearchWord(w, searchingWord):
                        wordCount += 1

            # Bottom
            if i <= (len(input) - searchingWordLen):
                w = ""
                for j in range(i, i + searchingWordLen):
                    w += input[j][y]
                if isMatchingSearchWord(w, searchingWord):
                    wordCount += 1

                # Bottom Right
                if y <= (len(input[i]) - searchingWordLen):
                    k = y
                    w = ""
                    for j in range(i, i + searchingWordLen):
                        w += input[j][k]
                        k += 1
                    if isMatchingSearchWord(w, searchingWord):
                        wordCount += 1

                # Bottom Left
                if y >= (searchingWordLen - 1):
                    k = y
                    w = ""
                    for j in range(i, i + searchingWordLen):
                        w += input[j][k]
                        k -= 1
                    if isMatchingSearchWord(w, searchingWord):
                        wordCount += 1

    return wordCount

def part2(input: list[str]):
    searchingWord = "MAS"
    searchingWord = searchingWord.upper()
    searchingWordLen = len(searchingWord)
    count = 0

    for i in range(len(input) - searchingWordLen + 1):
        for y in range(len(input[i]) - searchingWordLen + 1):
            k = y

            # Top left to Bottom right
            w = ""
            for j in range(i, i + searchingWordLen):
                w += input[j][k]
                k += 1
            if isMatchingSearchWord(w, searchingWord):
                # Top right to Bottom left
                w = ""
                k -= 1
                for j in range(i, i + searchingWordLen):
                    w += input[j][k]
                    k -= 1
                if isMatchingSearchWord(w, searchingWord):
                    count += 1

    return count

def run(input: list[str]):
    for i in range(len(input)):
        input[i] = input[i].upper()

    print(f"The input contains {part1(input)} words!")

    print(f"The input contains {part2(input)} X-MAS!")
