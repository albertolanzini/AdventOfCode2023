from typing import List, Tuple, Optional, Dict
from collections import deque

class StepCounter:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)
        self.starting_point = self._find_starting_point()

    def _handle_input(self, inputfile: str) -> List[List[str]]:
        with open(inputfile, 'r') as f:
            content = f.read().splitlines()
        return list(list(line) for line in content)
    
    def _find_starting_point(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] == 'S':
                    return (i, j)
                    break
        return (-1, -1) # if not found (should not be a case with the given input)
    
    def _bfs(self, set_dist):
        count, directions = 0, [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque([(self.starting_point, 0)])
        visited = set(self.starting_point)

        while q:
            cur, dist = q.popleft()
            x, y = cur

            if dist <= set_dist and dist % 2 == 0:
                count += 1

            for dx, dy in directions:
                if (x + dx in range(len(self.data))) and (y + dy in range(len(self.data))) \
                      and (x + dx, y + dy) not in visited and self.data[x+dx][y+dy] == '.':
                    q.append([(x+dx, y+dy), dist + 1])
                    visited.add((x+dx, y+dy))

        return count


def main():
    step_counter = StepCounter('input.txt')

    # Part 1 Usage

    print(step_counter.data)
    print(step_counter._bfs(64))

    # Part 2 Usage



if __name__ == "__main__":
    main()