from typing import List

class ScratcherValidator:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)

    def _handle_input(self, inputfile: str) -> List[str]:
        with open(inputfile, 'r') as file:
            return file.read().split('\n')
        
    def _usable_input(self) -> List[tuple[List[int], List[int]]]:
        usable_data = []
        for line in self.data:
            if line:  # to skip empty lines
                parts = line.split('|')
                first_set = list(map(int, parts[0].split()[2:]))  # skip 'Card X:' part
                second_set = list(map(int, parts[1].split()))
                usable_data.append((first_set, second_set))
        return usable_data
    
    def _n_matches_p1(self) -> int:
        games_list = self._usable_input()
        score = 0


        for game in games_list:
            my_card, game_card = game
            intersection_set = set(my_card).intersection(game_card)

            if len(intersection_set) != 0:
                score += (2**(len(intersection_set)-1))

        return score
    
    def _n_scratchcards_p2(self) -> int:
        games_list = self._usable_input()
        games_dict = {}

        for i in range(len(games_list)):
            games_dict[i+1] = 1
        
        for i, game in enumerate(games_list):
            my_card, game_card = game
            intersection_set = set(my_card).intersection(game_card)

            for j in range(len(intersection_set)):
                games_dict[i+1+j+1] += (1*games_dict[i+1])
        
        return sum(val for key, val in games_dict.items())


def main():
    
    scratcher_validator = ScratcherValidator('input.txt')

    # Part 1 usage

    print(scratcher_validator._n_matches_p1())

    # Part 2 usage

    print(scratcher_validator._n_scratchcards_p2())

if __name__ == "__main__":
    main()
        
