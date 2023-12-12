from typing import List

class GalaxyFinder:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)

    def _handle_input(self, inputfile: str) -> List[str]:
        with open(inputfile, 'r') as file:
            return file.read().split('\n')

    def _solve(self, data: List[int]) -> int:
        c, n = 0, 1000000
        for i, a in enumerate(data):
            d = 0
            for b in data[i + 1 :]:
                d += (b != 0) or n
                c += d * a * b
        return c

    def part_one(self) -> None:
        line_count = [line.count("#") for line in self.data]
        result = self._solve(line_count)
        column = []
        for x in range(len(self.data[0])):
            count = sum(line[x : x + 1] == "#" for line in self.data)
            column.append(count)   
        result += self._solve(column)
        print(result)

def main():
    galaxy_finder = GalaxyFinder("input.txt")
    galaxy_finder.part_one()

if __name__ == "__main__":
    main()