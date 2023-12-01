from typing import List

class NumberFinder:
    def __init__(self, inputfile: str):
        self.data = self._handle_input(inputfile)
        self.number_word_to_digit = {
            'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
        }

    def _handle_input(self, inputfile: str) -> List[str]:
        with open(inputfile, 'r') as file:
            return file.read().split('\n')

    def _map_number_words(self, input_string: str) -> str:
        result, i = '', 0

        while i < len(input_string):
            replaced = False

            for number_word in sorted(self.number_word_to_digit, key=len, reverse=True):
                if input_string[i:i + len(number_word)] == number_word:
                    result += self.number_word_to_digit[number_word]
                    i += len(number_word) - 1
                    replaced = True
                    break

            if not replaced:
                result += input_string[i]
            i += 1

        return result

    def _find_single_sum(self, line: str) -> str:
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        left, right = 0, len(line) - 1
        found_left, found_right = False, False

        while left < right:
            if line[left] in num_list:
                found_left = True
            if line[right] in num_list:
                found_right = True

            if found_left and found_right:
                return line[left] + line[right]

            if not found_left:
                left += 1
            if not found_right:
                right -= 1

        if line[left].isdigit():
            return line[left] + line[left]

    def find_total_sum(self) -> int:
        total_sum = 0
        for line in self.data:
            if line:
                new_line = self._map_number_words(line)
                total_sum += int(self._find_single_sum(new_line))
        return total_sum


def main():
    input_file = 'input.txt'
    number_finder = NumberFinder(input_file)
    total_sum = number_finder.find_total_sum()
    print(f"The total sum calculated from {input_file} is: {total_sum}")

if __name__ == "__main__":
    main()
