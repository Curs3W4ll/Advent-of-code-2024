# class Dir:
#     TOP = "top"
#     RIGHT = "right"
#     BOTTOM = "bottom"
#     LEFT = "left"

# directions: dict[str, tuple[int, int]] = {
#     Dir.TOP: (-1, 0),
#     Dir.RIGHT: (0, 1),
#     Dir.BOTTOM: (1, 0),
#     Dir.LEFT: (0, -1),
# }

class MapCase:
    antinode: bool
    antenna: None|str

    def __init__(self, antenna: None|str):
        self.antenna = antenna
        self.antinode = False

class Map:
    map: list[list[MapCase]]
    antennasLocations: dict[str, list[tuple[int, int]]] = {}

    def __init__(self, input: list[str]):
        self.map = []
        for i in range(len(input)):
            line = []
            for y in range(len(input[i])):
                if input[i][y] != ".":
                    line.append(MapCase(input[i][y]))
                    if not input[i][y] in self.antennasLocations:
                        self.antennasLocations[input[i][y]] = []
                    self.antennasLocations[input[i][y]].append((i, y))
                else:
                    line.append(MapCase(None))
            self.map.append(line)

    def isPosOutOfBounds(self, pos: tuple[int, int]) -> bool:
        if pos[0] < 0 or pos[0] >= len(self.map):
            return True
        if pos[1] < 0 or pos[1] >= len(self.map[0]):
            return True
        return False

    def computeAntinodes(self):
        for locations in self.antennasLocations.values():
            for a1 in range(len(locations)):
                for a2 in range(a1 + 1, len(locations)):
                        vector: tuple[int, int] = locations[a1][0] - locations[a2][0], locations[a1][1] - locations[a2][1]
                        p1: tuple[int, int] = locations[a1][0] + vector[0], locations[a1][1] + vector[1]
                        if not self.isPosOutOfBounds(p1):
                            self.map[p1[0]][p1[1]].antinode = True
                        p2: tuple[int, int] = locations[a2][0] - vector[0], locations[a2][1] - vector[1]
                        if not self.isPosOutOfBounds(p2):
                            self.map[p2[0]][p2[1]].antinode = True

    def countAntinodes(self):
        count = 0

        for l in self.map:
            for case in l:
                if case.antinode:
                    count += 1

        return count

    def dumpVisitedMap(self):
        for l in self.map:
            for case in l:
                if case.antenna != None:
                    if case.antinode:
                        print("!", end="")
                    else:
                        print(case.antenna, end="")
                elif case.antinode:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

def run(input: list[str]):
    map = Map(input)

    map.computeAntinodes()
    map.dumpVisitedMap()
    print(f"There are {map.countAntinodes()} unique locations containing an antinode")
