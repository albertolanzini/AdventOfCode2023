from typing import List
import numpy as np

class StringCalculator:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)

    def _handle_input(self, inputfile: str) -> None:
        with open(inputfile, 'r') as f:
            content = f.read().split(',')
        return content
    
    def _ascii_calc(self, char, total):
        char_val = ord(char)
        total += char_val
        total *= 17
        total = total % 256

        return total
    
    def _s_string_ascii_calc(self, string):
        tot_str = 0
        for ch in string:
            tot_str = self._ascii_calc(ch, tot_str)
        return tot_str
    
    def _string_ascii_calc(self):
        total = 0
        for str in self.data:
            tot_str = 0
            for ch in str:
                tot_str = self._ascii_calc(ch, tot_str)
            total += tot_str
            # print(f"The total for {str} is {tot_str}")
        return total
    
    def _empty_fill_box(self):
        hashmap = {i: [] for i in range(256)}
        replaced = False
        for str in self.data:

            if '=' in str:
                string, focal_len = str.split('=')
                box = self._s_string_ascii_calc(string)
                for tupl in hashmap[box]:
                    if string == tupl[0]:
                        tupl[1] = focal_len
                        replaced = True
                        break
                    else:
                        continue
                
                if replaced == False:
                    hashmap[box].append([string, focal_len])

                replaced = False
            
            if '-' in str:
                string = str.replace('-', '')
                box = self._s_string_ascii_calc(string)
                for tupl in hashmap[box]:
                    if string == tupl[0]:
                        hashmap[box].remove(tupl)

        return hashmap
    
    def _calculate_focal_total(self):
        box_map = self._empty_fill_box()
        total = 0

        for box in box_map.keys():

            for i, tup in enumerate(box_map[box]):
                total += ((box + 1) * (i + 1) * int(tup[1]))

        return total







            

def main():
    string_calculator = StringCalculator('input.txt')
    print(string_calculator._empty_fill_box())
    print(string_calculator._calculate_focal_total())

if __name__ == "__main__":
    main()