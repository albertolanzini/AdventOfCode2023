from typing import List, Dict, Tuple

class SeedPlanter:
    def __init__(self, inputfile: str) -> None:
        self.data = self._handle_input(inputfile)
        self.seeds, self.maps = self._parse_data(self.data)

    def _handle_input(self, inputfile: str) -> List[str]:
        with open(inputfile, 'r') as file:
            return file.read().split('\n\n')
    
    def _parse_data(self, raw_data: List[str]) -> Tuple[List[int], Dict[str, List[Tuple[int, int, int]]]]:
        seeds, maps = [], {}

        for section in raw_data:
            lines = section.split('\n')
            title = lines[0].split(':')[0]
            if title == 'seeds':
                seeds = [int(x) for x in lines[0].split(': ')[1].split()]
            else:
                maps[title] = [tuple(map(int, line.split())) for line in lines[1:]]

        return seeds, maps
    
    def map_elements_to_values(self, element: int, map_name: str) -> int:
        mapping_list = self.maps[map_name]
        for value, initial_element, _range in mapping_list:
            if initial_element <= element < initial_element + _range:
                return value + (element - initial_element)
        return element
    
    def _find_smaller_location_p1(self, seeds: List[int]) -> int:
        min_location = float('inf')
        for seed in seeds:
            mapped_value = seed
            for map_name in ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map', 
                            'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map', 
                            'humidity-to-location map']:
                print(f"Moved to {map_name}")
                mapped_value = self.map_elements_to_values(mapped_value, map_name)
            min_location = min(min_location, mapped_value)
        return min_location
    
    def _find_smaller_location_p2(self) -> int:
        min_location = float('inf')
        for seed in self._seed_range():
            mapped_value = seed
            for map_name in ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map', 
                            'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map', 
                            'humidity-to-location map']:
                mapped_value = self.map_elements_to_values(mapped_value, map_name)
            min_location = min(min_location, mapped_value)
        return min_location

    def _seed_range(self) -> List[int]:
        for i in range(0, len(self.seeds), 2):
            start = self.seeds[i]
            length = self.seeds[i+1]
            for seed in range(start, start + length):
                yield seed

def main():
    seed_planter = SeedPlanter('input.txt')

    # Part 1 usage

    # print(seed_planter._find_smaller_location(seed_planter.seeds))

    # Part 2 usage

    print(seed_planter._find_smaller_location_p2())

if __name__ == "__main__":
    main()