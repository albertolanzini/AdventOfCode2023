from typing import List, Tuple, Optional

class DigCalculator:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)

    def _handle_input(self, inputfile: str) -> List[List[str]]:
        with open(inputfile, 'r') as f:
            content = f.read().strip().split('\n')
        res = []
        for line in content:
            res.append(line.split(' '))
        return res

    def _solve(self, lines: List[Tuple[str, int, Optional[None]]]) -> int:
        x, y, a, l = 0, 0, 0, 0
        for d, n, c in lines:
            match d:
                case "0" | "R":
                    x += n
                    a += y * n
                case "1" | "D":
                    y += n
                case "2" | "L":
                    x -= n
                    a -= y * n
                case "3" | "U":
                    y -= n
            l += n   
        return abs(a) + l // 2 + 1

    def part1(self) -> None:
        solved_values = []

        for line in self.data:
            if len(line) >= 2:
                first_word = line[0]
                second_word_as_int = int(line[1])
                solved_values.append((first_word, second_word_as_int, None))
        print(self._solve(solved_values))

    def convert_hex_to_instructions(self, data: List[List[str]]) -> List[Tuple[str, int, Optional[None]]]:
        instructions = []
        for line in data:
            hex_code = line[2].replace('#', '').replace('(', '').replace(')', '')
            distance = int(hex_code[:-1], 16)  
            direction_code = int(hex_code[-1], 16)  
            direction_map = {0: "R", 1: "D", 2: "L", 3: "U"}
            direction = direction_map[direction_code]
            instructions.append((direction, distance, None))
        return instructions

    def part2(self) -> None:
        preprocessed_data = self.convert_hex_to_instructions(self.data)
        print(self._solve(preprocessed_data))

def main():
    dig_calculator = DigCalculator('input.txt')
    dig_calculator.part1()
    dig_calculator.part2()

if __name__ == "__main__":
    main()