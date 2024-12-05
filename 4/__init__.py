searchingWord = "XMAS"
searchingWord = searchingWord.upper()

def isMatchingSearchWord(s: str):
    return (s == searchingWord or s == searchingWord[::-1])

def run(input: list[str]):
    searchingWordLen = len(searchingWord)
    wordCount = 0

    for i in range(len(input)):
        input[i] = input[i].upper()
    for i in range(len(input)):
        for y in range(len(input[i])):
            if input[i][y] != "X":
                continue
            # Right
            if y <= (len(input[i]) - searchingWordLen):
                if isMatchingSearchWord(input[i][y:y + searchingWordLen]):
                    wordCount += 1

            # Left
            if y >= (searchingWordLen - 1):
                if isMatchingSearchWord(input[i][y - searchingWordLen + 1:y + 1]):
                    wordCount += 1

            # Top
            if i >= (searchingWordLen - 1):
                w = ""
                for j in range(i, i - searchingWordLen, -1):
                    w += input[j][y]
                if isMatchingSearchWord(w):
                    wordCount += 1

                # Top Right
                if y <= (len(input[i]) - searchingWordLen):
                    k = y
                    w = ""
                    for j in range(i, i - searchingWordLen, -1):
                        w += input[j][k]
                        k += 1
                    if isMatchingSearchWord(w):
                        wordCount += 1

                # Top Left
                if y >= (searchingWordLen - 1):
                    k = y
                    w = ""
                    for j in range(i, i - searchingWordLen, -1):
                        w += input[j][k]
                        k -= 1
                    if isMatchingSearchWord(w):
                        wordCount += 1

            # Bottom
            if i <= (len(input) - searchingWordLen):
                w = ""
                for j in range(i, i + searchingWordLen):
                    w += input[j][y]
                if isMatchingSearchWord(w):
                    wordCount += 1

                # Bottom Right
                if y <= (len(input[i]) - searchingWordLen):
                    k = y
                    w = ""
                    for j in range(i, i + searchingWordLen):
                        w += input[j][k]
                        k += 1
                    if isMatchingSearchWord(w):
                        wordCount += 1

                # Bottom Left
                if y >= (searchingWordLen - 1):
                    k = y
                    w = ""
                    for j in range(i, i + searchingWordLen):
                        w += input[j][k]
                        k -= 1
                    if isMatchingSearchWord(w):
                        wordCount += 1

    print(f"The input contains {wordCount} words!")
