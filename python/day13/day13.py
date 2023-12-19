from typing import List
import numpy as np

class MirrorCalculator:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)

    def _handle_input(self, inputfile: str) -> List[str]:
        with open(inputfile, 'r') as f:
            data = f.read().split('\n\n')  # split the input into matrices
        return [[list(row) for row in matrix.split('\n')] for matrix in data]
    
    def _check_mirrors_cols(self, cols):
        transposed_cols = np.array(cols).T.tolist()
        return self._check_mirrors_rows(transposed_cols, row=False)

    def _check_mirrors_rows(self, rows, row=True):
        found = False

        for i in range(len(rows)-2):
            if np.array_equal(rows[i], rows[i+1]):
                found = True
                l, r = i, i+1
                break

        if not found:
            return False, 0

        r_l = l+1
        len_mir = min(l, len(rows) - r)
        

        l -= 1
        r += 1
        len_mir -= 1

        while len_mir > 0:
            if np.array_equal(rows[l], rows[r]):
                l -= 1
                r += 1
                len_mir -= 1
            else:
                return False, 0
                    
        if row:
            print(r_l, row)
            return True, r_l*100
        else:
            print(r_l, row)
            return True, r_l

    
    def _check_all(self):
        total = 0
        for matrix in self.data:
            print(matrix)
            rows_result, rows_value = self._check_mirrors_rows(matrix)
            if rows_result:
                total += rows_value
            else:
                cols_result, cols_value = self._check_mirrors_cols(matrix)
                if cols_result:
                    total += cols_value
            print(total)
        return total



def main():
    mirror_calculator = MirrorCalculator("input.txt")
    matrix = [
        ['.', '.', '#', '#', '.', '#', '.', '.', '.', '#', '#', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.'],
        ['.', '#', '#', '.', '.', '#', '.', '.', '.', '#', '#', '.', '.', '.', '#'], 
        ['#', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '#', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '#', '.', '.', '#', '#', '#', '#', '.', '.', '#'], 
        ['#', '#', '.', '.', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.'], 
        ['.', '#', '#', '#', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.'], 
        ['.', '#', '#', '.', '#', '.', '#', '#', '#', '.', '.', '#', '#', '#', '.'], 
        ['.', '#', '#', '.', '#', '.', '.', '#', '.', '#', '#', '.', '#', '.', '.'], 
        ['#', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.'], 
        ['#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#'], 
        ['#', '#', '#', '.', '.', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#'], 
        ['#', '#', '.', '.', '.', '#', '.', '.', '#', '#', '#', '#', '.', '.', '#'], 
        ['#', '#', '.', '.', '.', '#', '.', '.', '#', '#', '#', '#', '.', '.', '#']]

    print(mirror_calculator._check_mirrors_cols(matrix))
    print(mirror_calculator._check_mirrors_rows(matrix))
    
    print(mirror_calculator._check_all())

if __name__ == "__main__":
    main()