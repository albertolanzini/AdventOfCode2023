from typing import List, Dict
import string

class EngineChecker:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)

    def _handle_input(self, inputfile: str) -> List[str]:
        with open(inputfile, 'r') as file:
            return file.read().split('\n')
        
    def _num_to_idx_hashmap(self) -> Dict[str, List[tuple[int, int, int]]]:
        num_to_idx = {}

        for n_line, line in enumerate(self.data):
            
            length_line = len(line)
            i = 0

            while i < length_line:

                if line[i].isdigit():
                    cur_str = ""
                    cur_str += line[i]
                    st_idx = i
                    i+=1
                
                    while i < length_line and line[i].isdigit():
                        cur_str += line[i]
                        i += 1
                    end_idx = i-1

                    if cur_str not in num_to_idx:
                        num_to_idx[cur_str] = []
                    num_to_idx[cur_str].append((n_line, st_idx, end_idx))
                else:
                    i += 1
        return num_to_idx
    
    def _identify_symbols(self) -> set[str]:
        symbols_set = set()

        for line in self.data:
            for char in line:
                if not char.isdigit() and char != ".":
                    symbols_set.add(char)

        return symbols_set

    def _close_to_symbol(self, idx_tuple: tuple[int, int, int]) -> bool:
        
        n_line, start, end = idx_tuple
        data = self.data
        data_len, line_len = len(data), len(data[n_line])
        symbol_set = self._identify_symbols()

        start = max(0, start - 1)
        end = min(line_len, end + 2)

        for line_offset in (-1, 0, 1):
            adjacent_line = n_line + line_offset
            
            if 0 <= adjacent_line < data_len:
                check_line = data[adjacent_line][start:end]
                for symbol in symbol_set:
                    if symbol in check_line:
                        return True
        return False
    
    def _calculate_gear_ratios(self) -> int:
        gear_ratios_sum = 0
        # Assuming self.data is a list of strings representing each line of the schematic
        for row_index, line in enumerate(self.data):
            for col_index, char in enumerate(line):
                if char == '*':  # Found a gear
                    adjacent_numbers = self._find_adjacent_numbers(row_index, col_index)
                    if len(adjacent_numbers) == 2:  # Make sure there are exactly two numbers
                        gear_ratio = int(adjacent_numbers[0]) * int(adjacent_numbers[1])
                        gear_ratios_sum += gear_ratio
        return gear_ratios_sum

    def _find_adjacent_numbers(self, row_index, col_index) -> List[str]:
        adjacent_numbers = []
        # Directions: (dx, dy)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            new_row, new_col = row_index + dx, col_index + dy
            if 0 <= new_row < len(self.data) and 0 <= new_col < len(self.data[new_row]):
                # Check if the character is part of a number
                if self.data[new_row][new_col].isdigit():
                    number = self._get_whole_number(new_row, new_col)
                    if number not in adjacent_numbers:
                        adjacent_numbers.append(number)
                        if len(adjacent_numbers) == 2:  # Only need two numbers
                            break
        return adjacent_numbers

    def _get_whole_number(self, row_index, col_index) -> str:
        # Get the whole number that a digit is part of
        number = self.data[row_index][col_index]
        # Check left
        i = col_index
        while i > 0 and self.data[row_index][i - 1].isdigit():
            i -= 1
            number = self.data[row_index][i] + number
        # Check right
        i = col_index
        while i < len(self.data[row_index]) - 1 and self.data[row_index][i + 1].isdigit():
            i += 1
            number += self.data[row_index][i]
        return number
       
def main():
    input_file = 'input.txt'
    engine_checker = EngineChecker(input_file)
    total_parts_sum = 0

    # Part 1 usage

    for num, params_list in engine_checker._num_to_idx_hashmap().items():
        for params in params_list:
            if engine_checker._close_to_symbol(params):
                total_parts_sum += int(num)

    print(total_parts_sum)

    # Part 2 usage

    gear_ratios_sum = engine_checker._calculate_gear_ratios()
    print(f"Sum of gear ratios: {gear_ratios_sum}")


if __name__ == "__main__":
    main()