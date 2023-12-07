from typing import List, Dict, Tuple
from collections import Counter

class CamelCards:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)
        self.card_strength = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, 
                              '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, 
                              '4': 4, '3': 3, '2': 2, 'J':1}
        """
        Part 1 Definition

        self.card_strength = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, 
                              '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, 
                              '4': 4, '3': 3, '2': 2}

        """
    def _handle_input(self, inputfile: str) -> List[Tuple[str, int]]:
        with open(inputfile, 'r') as file:
            content = file.read().split('\n')
        ret_list = []
        for game in content:
            cards, bid = game.split(' ')
            ret_list.append((cards, int(bid)))
        return ret_list
    
    def _get_card_strength(self, card: str) -> int:
        return self.card_strength[card]
    
    def _calculate_pair_p1(self, pair: Tuple[str, int]) -> Tuple[int, str]:
        cards, bid = pair

        hash_cards = Counter(cards)
        counts = list(hash_cards.values())
        counts.sort(reverse=True)

        if counts[0] == 5:
            return 6, cards
        elif counts[0] == 4:
            return 5, cards
        elif counts[0] == 3 and counts[1] == 2:
            return 4, cards
        elif counts[0] == 3:
            return 3, cards
        elif counts[0] == 2 and counts[1] == 2:
            return 2, cards
        elif counts[0] == 2:
            return 1, cards
        else:
            return 0, cards
        
    def _calculate_pair_p2(self, pair: Tuple[str, int]) -> Tuple[int, str]:
        cards, bid = pair

        hash_cards = Counter(cards)

        if 'J' in hash_cards:
            j = hash_cards['J']
        else:
            return self._calculate_pair_p1(pair)
        
        counts = [count for card, count in hash_cards.items() if card != 'J']
        counts.sort(reverse=True)

        if counts:
            if counts[0] + j == 5:
                return 6, cards
            elif counts[0] + j == 4:
                return 5, cards
            elif counts[0] == 2 and counts[1] == 2:
                return 4, cards
            elif counts[0] + j == 3:
                return 3, cards
            elif counts[0] + j == 2:
                return 1, cards
        else:
            return 6, cards
    

    def _sort_pairs(self) -> List[int]:
        pairs_dict = {}
        total = 0

        for pair in self.data:
            card, bid = pair
            val, cards = self._calculate_pair_p2(pair)

            if val not in pairs_dict:
                pairs_dict[val] = [(bid, cards)]
            else:
                pairs_dict[val].append((bid, cards))

        print(pairs_dict)
        
        sorted_keys = list(pairs_dict.keys())
        sorted_keys.sort()
        
        count = 0
        for key in sorted_keys:

            sorted_pairs = sorted(pairs_dict[key], key=lambda x: [self._get_card_strength(card) for card in x[1]])
            print(sorted_pairs)
            
            for a, b in sorted_pairs:
                total += (a * (count+1))
                count += 1
        return total

def main():
    camel_cards = CamelCards('input.txt')

    # Part 1 usage

    # print(camel_cards._sort_pairs())

    # Part 2 usage

    print(camel_cards._sort_pairs())
    


if __name__ == "__main__":
    main()