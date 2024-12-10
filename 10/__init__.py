import copy

class Dir:
    TOP = "top"
    RIGHT = "right"
    BOTTOM = "bottom"
    LEFT = "left"

directions: dict[str, tuple[int, int]] = {
    Dir.TOP: (-1, 0),
    Dir.RIGHT: (0, 1),
    Dir.BOTTOM: (1, 0),
    Dir.LEFT: (0, -1),
}

class MapCase:
    height: int

    def __init__(self, height: int):
        self.height = height

def applyDirection(pos: tuple[int, int], dir: str):
    return pos[0] + directions[dir][0], pos[1] + directions[dir][1]

class Map:
    map: list[list[MapCase]]
    currentDirection: str
    currentPosition: tuple[int, int]
    trailheadsEnds: set[tuple[int, int]] = set()
    trailsNumbers: int = 0

    def __init__(self, input: list[str]):
        self.map = []
        for l in input:
            self.map.append([MapCase(int(x)) for x in l])

    def isPosOutOfBounds(self, pos: tuple[int, int]) -> bool:
        if pos[0] < 0 or pos[0] >= len(self.map):
            return True
        if pos[1] < 0 or pos[1] >= len(self.map[0]):
            return True
        return False

    def goForward(self, pos: tuple[int, int]):
        # self.dumpMap(pos)
        # input()
        if self.map[pos[0]][pos[1]].height >= 9:
            self.trailheadsEnds.add(pos)
            self.trailsNumbers += 1
            return
        for d in directions.keys():
            nextPos = applyDirection(pos, d)
            if not self.isPosOutOfBounds(nextPos) and self.map[nextPos[0]][nextPos[1]].height == self.map[pos[0]][pos[1]].height + 1:
                self.goForward(nextPos)

    def getTrailheadScore(self, start: tuple[int, int]) -> int:
        self.trailheadsEnds.clear()

        self.goForward(start)

        return len(self.trailheadsEnds)

    def getAllTrailheadsScore(self) -> int:
        self.trailsNumbers = 0
        total = 0

        for i in range(len(self.map)):
            for y in range(len(self.map[i])):
                if self.map[i][y].height == 0:
                    total += self.getTrailheadScore((i, y))

        return total

    def dumpMap(self, pos: tuple[int, int]):
        for i in range(len(self.map)):
            for y in range(len(self.map[i])):
                if i == pos[0] and y == pos[1]:
                    print(".", end="")
                elif (i, y) in self.trailheadsEnds:
                    print("X", end="")
                else:
                    print(self.map[i][y].height, end="")
            print()

def run(input: list[str]):
    map = Map(input)

    print(f"Sum of all trailheads scores is {map.getAllTrailheadsScore()}")
    print(f"There are {map.trailsNumbers} distinct trails")
