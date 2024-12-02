import copy

def areLevelsValids(increasing: bool, l1:int , l2:int) -> bool:
    diff = abs(l1 - l2)
    actualIsIncreasing = l1 < l2
    return (diff >= 1 and diff <= 3) and (increasing == actualIsIncreasing)

def isReportSafe(l: list[int], dampener: bool = False) -> bool:
    isIncreasing = l[0] < l[1]
    for i in range(1, len(l)):
        if not areLevelsValids(isIncreasing, l[i - 1], l[i]):
            if dampener:
                lWithoutFirst = copy.copy(l)
                del lWithoutFirst[0]
                lWithoutPrevious = copy.copy(l)
                del lWithoutPrevious[i - 1]
                lWithoutActual = copy.copy(l)
                del lWithoutActual[i]
                return isReportSafe(lWithoutFirst) or isReportSafe(lWithoutPrevious) or isReportSafe(lWithoutActual)
            else:
                return False
    return True

def run(input: list[str]):
    reports: list[list[int]] = [[int(x) for x in l.split()] for l in input]
    safeReports = 0
    safeReportsWithDampener = 0

    for r in reports:
        if isReportSafe(r):
            safeReports += 1
        if isReportSafe(r, True):
            safeReportsWithDampener += 1

    print(f"Total {safeReports} 100% safe reports")
    print(f"Total {safeReportsWithDampener} safe reports with Problem Dampener")
