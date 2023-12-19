import functools

class SpringFinder:
    def __init__(self, raw_data):
        self.data = [self.parse(line) for line in raw_data]

    def parse(self, line):
        s, groups = line.strip().split(" ")
        lookup = {"#": 2, "?": 1, ".": 0}
        return tuple(lookup[char] for char in s), tuple(int(g) for g in groups.split(","))

    def match_beginning(self, data, length):
        return all(x > 0 for x in data[:length]) and (
            (len(data) == length) or data[length] < 2
        )

    @functools.cache
    def count(self, data, blocks):
        total = sum(blocks)
        minimum = sum(x == 2 for x in data)
        maximum = sum(x > 0 for x in data)
        if minimum > total or maximum < total:
            return 0
        if total == 0:
            return 1
        if data[0] == 0:
            return self.count(data[1:], blocks)
        if data[0] == 2:
            l = blocks[0]
            if self.match_beginning(data, l):
                if l == len(data):
                    return 1
                return self.count(data[l + 1:], blocks[1:])
            return 0
        return self.count(data[1:], blocks) + self.count((2,) + data[1:], blocks)

    def solve_p1(self):
        return sum(self.count(*line) for line in self.data)
    
    def solve_p2(self):
        return sum(self.count(((chars + (1,)) * 5)[:-1], blocks * 5) for chars, blocks in self.data)


def main():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')
    finder = SpringFinder(data)
    result1 = finder.solve_p1()
    result2 = finder.solve_p2()
    print(f"Result: {result2}")

if __name__ == "__main__":
    main()
