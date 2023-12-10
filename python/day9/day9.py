from typing import List, Dict, Tuple

class SequenceSolver:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)
        
    def _handle_input(self, inputfile: str) -> List[List[int]]:
        with open(inputfile, 'r') as file:
            content = file.read().split('\n')
        ret_list = []
        for line in content:
            ret_list.append(list(int(i) for i in line.split(' ')))
        return ret_list
    
    def _calculate_sequences(self, sequence: List[int]) -> List[int]:
        sequences = [sequence]

        while not all(x == sequences[-1][0] for x in sequences[-1]):
            new_seq = [sequences[-1][i+1] - sequences[-1][i] for i in range(len(sequences[-1])-1)]
            sequences.append(new_seq)
        return sequences
    
    def _calculate_next_el(self, sequence: List[int]) -> int:
        
        sequences = self._calculate_sequences(sequence)
        i = len(sequences)-2

        while i >= 0:
            sequences[i].append(sequences[i+1][-1] + sequences[i][-1])
            i -= 1

        return sequences[0][-1]
    
    def _calculate_first_el(self, sequence: List[int]) -> int:

        sequences = self._calculate_sequences(sequence)
        i = len(sequences)-2

        while i >= 0:
            sequences[i].insert(0, sequences[i][0] - sequences[i+1][0])
            i -= 1

        return sequences[0][0]


    
    def _calculate_result_p1(self) -> int:
        total = 0

        for sequence in self.data:
            total += self._calculate_next_el(sequence)

        return total
    
    def _calculate_result_p2(self) -> int:
        total = 0

        for sequence in self.data:
            total += self._calculate_first_el(sequence)

        return total

def main():
    sequence_solver = SequenceSolver('input.txt')

    # Part 1 usage

    print(sequence_solver._calculate_result_p1())

    # Part 2 usage

    print(sequence_solver._calculate_result_p2())
    

if __name__ == "__main__":
    main()