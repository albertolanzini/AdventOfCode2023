from typing import List, Dict, Tuple
from collections import Counter
import itertools
import math

class CamelTravel:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)
        
    def _handle_input(self, inputfile: str) -> List[Tuple[str, int]]:
        with open(inputfile, 'r') as file:
            lines = [i for i in file.read().split('\n') if i != '']
            return lines
    
    def _build_hash(self, lines: List[str]) -> Dict[str, Tuple[str, str]]:
        return {line.split(' = ')[0]: tuple(line.split(' = ')[1].strip('()').split(', ')) for line in lines if line != lines[0]}
    
    def _travel_hash(self):
        data, dir_hash = self.data, self._build_hash(self.data)
        direction = data[0]

        iterator = itertools.cycle(direction)

        cur_str = 'AAA'

        i = 1

        # from the input we are sure there always is a solution
        while True: 
            dir = next(iterator)

            if dir == 'R':
                cur_str = dir_hash[cur_str][1]
            else:
                cur_str = dir_hash[cur_str][0]

            if cur_str == 'ZZZ':
                return i
            i += 1

    def _find_all_starting_points(self) -> List[str]:
        dir_hash = self._build_hash(self.data)
        starting_points = list()

        for key in dir_hash.keys():
            if key.endswith('A'):
                starting_points.append(key)

        return starting_points

    def _travel_hash_p2(self):
        dist = list()
        direction, dir_hash = self.data[0], self._build_hash(self.data)
        
        for starting_point in self._find_all_starting_points():
            iterator = itertools.cycle(direction)
            i = 0

            while True: 
                dir = next(iterator)

                if dir == 'R':
                    starting_point = dir_hash[starting_point][1]
                else:
                    starting_point = dir_hash[starting_point][0]

                i += 1

                if starting_point.endswith('Z'):
                    break

            dist.append(i)
            
        return math.lcm(*dist)

def main():
    camel_travel = CamelTravel('input.txt')

    # Part 1 usage

    # print(camel_travel.data)
    # print(camel_travel._build_hash(camel_travel.data))
    print(camel_travel._find_all_starting_points())

    print(camel_travel._travel_hash_p2())

if __name__ == "__main__":
    main()