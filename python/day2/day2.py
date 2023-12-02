from typing import List, Dict
import re

class GameValidator:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)
        self.max_red = 12
        self.max_green = 13
        self.max_blue = 14

    def _handle_input(self, inputfile: str) -> List[str]:
        with open(inputfile, 'r') as file:
            return file.read().split('\n')
        
    def _split_line(self, line: str) -> List[str]:
        return re.split(';|,|:', line)
    
    def _handle_draw(self, draw):
        draw = draw.strip()

        color = ''.join(l for l in draw if l.isalpha())
        num = int(''.join(i for i in draw if i.isdigit()))

        return (color, num)

    def _validate_line_p1(self, line):
        line = self._split_line(line)

        for draw in line[1:]:
            color, num = self._handle_draw(draw)

            if (color == "green" and num > self.max_green) or (color == "red" and num > self.max_red) or (color == "blue" and num > self.max_blue):
                return False
        return True
    
    def _min_numbers_p2(self, line):
        line = self._split_line(line)

        min_green, min_blue, min_red = 0, 0, 0

        for draw in line[1:]:
            color, num = self._handle_draw(draw)

            if color == "green":
                min_green = max(min_green, num)
            if color == "blue":
                min_blue = max(min_blue, num)
            if color == "red":
                min_red = max(min_red, num)
        
        return min_green*min_red*min_blue
     
        
def main():
    input_file = 'input.txt'
    game_validator = GameValidator(input_file)
    total_num_ids = 0
    total_power_sum = 0

    # Part 1 usage
    
    for i, line in enumerate(game_validator.data):
        if game_validator._validate_line_p1(line):
            total_num_ids += (i + 1)
        
    # Part 2 usage

    for line in game_validator.data:
        total_power_sum += game_validator._min_numbers_p2(line)
    
    print(f"The total sum of IDs is {total_num_ids}")
    print(f"The total sum for Part 2 is: {total_power_sum}")

if __name__ == "__main__":
    main()
