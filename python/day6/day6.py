from typing import List, Dict, Tuple

class BoatRacer:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)

    """

    This was the _handle_input method designed for Part1.
    As the requirements changed, I will move to a different method

    def _handle_input(self, inputfile: str) -> List[List[int]]:
        with open(inputfile, 'r') as file:
            content = file.read().split('\n')
        ret_list = list()
        for line in content:
            line = line.split(" ")
            line = [int(i) for i in line if i.isdigit()]
            ret_list.append(line)
        return ret_list
    
    """

    def _handle_input(self, inputfile: str) -> List[List[int]]:
        with open(inputfile, 'r') as file:
            content = file.read().split('\n')
        ret_list = list()
        for line in content:
            new_line = ''.join(i for i in line if i.isdigit())
            print(new_line)
            if new_line:
                ret_list.append(int(new_line))

        return ret_list
    
    def calculate_total_p1(self) -> int:
        total = 1

        for i in range(len(self.data[0])):
            count = 0

            for time in range(self.data[0][i]):
                dis = (self.data[0][i] - time)*time
                if dis > self.data[1][i]:
                    count += 1

            total *= count
        return total
    
    def calculate_total_p2(self) -> int:
        total_count = 0

        for time in range(self.data[0]):
            dis = (self.data[0] - time)*time
            if dis > self.data[1]:
                total_count += 1

        return total_count

def main():
    boat_racer = BoatRacer('input.txt')

    # Part 1 usage

    # print(boat_racer.calculate_total_p1())

    # Part 2 usage

    print(boat_racer.calculate_total_p2())


if __name__ == "__main__":
    main()