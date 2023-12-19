import re
import copy
from pathlib import Path

class LightBeamSolver:
    def __init__(self, file_path):
        self.file_path = file_path
        self.parsed_data = self.parse_input()

    def parse_input(self):
        with open(self.file_path, "r") as f:
            data = f.read()
        data_list = data.splitlines()
        hrz_sym = [[sym.start() for sym in re.finditer(r'[^\.]', line)] for line in data_list]
        vert_sym = [[sym.start() for sym in re.finditer(r'[^\.]', ''.join(line))] for line in zip(*data_list)]
        bool_map = [[False for _ in range(len(line))] for line in data_list]
        for idx, line in enumerate(hrz_sym):
            for sym in line: 
                bool_map[idx][sym] = data_list[idx][sym]
        return (bool_map, hrz_sym, vert_sym)

    def sym_redirect_map(self):
        redirect_map = {
            '\\': {
                'R': 'D',
                'L': 'U',
                'U': 'L',
                'D': 'R'
            },
            '|': {
                'R': 'UD',
                'L': 'UD',
                'U': 'U',
                'D': 'D'
            },
            '/': {
                'R': 'U',
                'L': 'D',
                'U': 'R',
                'D': 'L'
            },
            '-': {
                'R': 'R',
                'L': 'L',
                'U': 'LR',
                'D': 'LR'
            }
        }
        return redirect_map

    def get_range(self, direction, a, z):
        match direction:
            case 'R' | 'D': 
                return range(a, z, 1)
            case 'L' | 'U': 
                return range((z + 1), (a + 1), 1)

    def get_range_edge(self, direction, a, z):
        match direction:
            case 'R' | 'D': return range(a, z, 1)
            case 'L' | 'U': return range(0, (a + 1), 1)

    def get_symbol_value(self, direction, a, m):
        match direction:
            case 'R' | 'D': return iter([idx for idx in m[a[0]] if idx >= a[1]])
            case 'L' | 'U': return iter(reversed([idx for idx in m[a[0]] if idx <= a[1]]))

    def light_beam(self, point, m, bool_map, direction):
        value = next(self.get_symbol_value(direction, point, m), None)
        if value is not None:
            for i in self.get_range(direction, point[1], value):
                if direction in 'LR':
                    bool_map[point[0]][i] = True
                else:
                    bool_map[i][point[0]] = True
            if direction in 'LR':
                next_directions = self.sym_redirect_map()[bool_map[point[0]][value]][direction]
                next_point = (point[0], value) 
            else:
                next_directions = self.sym_redirect_map()[bool_map[value][point[0]]][direction]
                next_point = (value, point[0])
            return next_point, bool_map, list(next_directions)
        else:
            for i in self.get_range_edge(direction, point[1], len(bool_map[point[0]])):
                if direction in 'LR':
                    bool_map[point[0]][i] = True
                else:
                    bool_map[i][point[0]] = True
            return None, bool_map, None

    def move(self, l, h, v, curr_point, curr_dir, mirror_hit):
        match curr_dir:
            case 'R': 
                curr_point, l, new_dir = self.light_beam((curr_point[0], curr_point[1] + 1), h, l, curr_dir)
            case 'L': 
                curr_point, l, new_dir = self.light_beam((curr_point[0], curr_point[1] - 1), h, l, curr_dir)
            case 'D': 
                curr_point, l, new_dir = self.light_beam((curr_point[1], curr_point[0] + 1), v, l, curr_dir)
            case 'U': 
                curr_point, l, new_dir = self.light_beam((curr_point[1], curr_point[0] - 1), v, l, curr_dir)
        if curr_point is not None:
            if curr_dir not in mirror_hit.setdefault(curr_point, []):
                mirror_hit.setdefault(curr_point, []).append(curr_dir)
                for direction in new_dir:
                    l, mirror_hit = self.move(l, h, v, curr_point, direction, mirror_hit)
        return l, mirror_hit

    def get_energized_tiles(self, bool_map, mirror_hit):
        return len(mirror_hit) + sum(1 for line in bool_map for item in line if item and isinstance(item, bool))

    def check_all_options(self, data):
        total_tiles = []
        length = len(data[0])
        for i in range(0, length):
            directions = [(i, -1, 'R'), (i, length, 'L'), (-1, i, 'D'), (length, i, 'U')]
            for entry in directions:
                l, h, v = copy.deepcopy(data)
                l, mirror_hit = self.move(l, h, v, (entry[0], entry[1]), entry[2], {})
                curr_total_tiles = self.get_energized_tiles(l, mirror_hit)
                total_tiles.append(curr_total_tiles)
        return max(total_tiles)

    def part1(self, parsed_data):
        l, h, v = copy.deepcopy(parsed_data)
        l, mirror_hit = self.move(l, h, v, (0, -1), 'R', {})
        energized_tiles = self.get_energized_tiles(l, mirror_hit)
        return energized_tiles

    def part2(self, parsed_data):
        return self.check_all_options(parsed_data)

    def solve(self):
        print(self.part1(self.parsed_data))
        print(self.part2(self.parsed_data))

if __name__ == "__main__":
    solver = LightBeamSolver('input.txt')
    solver.solve()