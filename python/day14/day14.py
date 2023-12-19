from typing import List
import numpy as np

class RockTilter:
    def __init__(self, inputfile: str) -> None:
        self.data = None

    def _handle_input(self, inputfile: str) -> None:
        with open(inputfile, 'r') as f:
            matrix = [list(line) for line in f.read().splitlines()]
        self.data = matrix
        self.load_history = []
    
    def transpose(self) -> None:
        self.data = list(map(list, zip(*self.data)))

    def _calculate_row(self, row: List[str]) -> int:
        total, count = 0, 0

        for i in range(len(row)-1, -1, -1):

            if row[i] == 'O':
                count += 1
            
            if row[i] == '#':
                if count == 0:
                    continue
                else:
                    incr = len(row) - i - 1
                    while count > 0:
                        total += incr
                        incr -= 1
                        count -= 1
        
        if count > 0:
            incr = len(row)
            while count > 0:
                total += (incr)
                incr -= 1
                count -= 1

        return total
    
    def _calculate_matrix_p1(self):
        total = 0
        for row in self.data:
            # print(row)
            total += self._calculate_row(row)
        return total
    
    def move_north(self) -> None:
        for y, row in enumerate(self.data):
            for x, char in enumerate(row):
                if char != 'O':  # skip non-moving rocks
                    continue
                obstacles_y = [y for y in range(y) if self.data[y][x] in '#O']
                new_y = max(obstacles_y, default=-1) + 1
                if new_y != y:
                    self.data[y][x] = '.'
                    self.data[new_y][x] = 'O'

    def turn_clockwise(self) -> None:
        self.data = [list(row) for row in zip(*self.data[::-1])]

    def calculate_load(self) -> int:
        height = len(self.data)
        return sum(row.count('O') * (height - y) for y, row in enumerate(self.data))

    def run_cycles(self, num_cycles: int) -> None:
        for i in range(num_cycles):
            for _ in range(4):
                self.move_north()
                self.turn_clockwise()
            self.load_history.append(self.calculate_load())

            # cycle detection
            for cycle_size in range(2, 100):
                cycle = self.load_history[-cycle_size:]
                if self.load_history[-cycle_size*2:-cycle_size] == cycle:  # cycle found
                    mysterious_offset = -2  # not quite about this one to be honest...
                    remaining_iterations = num_cycles - i + mysterious_offset
                    final_load = cycle[remaining_iterations % cycle_size]
                    print(final_load)
                    return

def main():
    rock_tilter = RockTilter('input.txt')
    rock_tilter._handle_input('input.txt')

    # Part 1 Usage

    rock_tilter.transpose()
    print(rock_tilter._calculate_matrix_p1())

    # Part 2 Usage

    rock_tilter._handle_input('input.txt')
    rock_tilter.run_cycles(1_000_000_000)



if __name__ == "__main__":
    main()