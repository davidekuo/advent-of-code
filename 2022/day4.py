# AOC 2022 Day 4

import pathlib
import re


def parse(data):
    """Parse input"""
    parsed = []
    for line in data.splitlines():  
        # Each line has form 'A-B,C-D' 
        a, b, c, d = re.split('[-,]', line)  # split string line with any char delimiters within brackets []
        first = set(range(int(a), int(b)+1))  # range: [x, y)
        second = set(range(int(c), int(d)+1))
        parsed.append((first, second))
    return parsed


def part1(data):
    count = 0
    for parsed_line in data:  
        first, second = parsed_line
        if first.issubset(second) or first.issuperset(second):
            count += 1
    return count


def part2(data):
    count = 0
    for parsed_line in data:
        first, second = parsed_line
        if not first.isdisjoint(second):
            count += 1
    return count

def main():
    # Read inputs
    example_input = pathlib.Path("./inputs/day4_example_input.txt").read_text().strip()
    input = pathlib.Path("./inputs/day4_input.txt").read_text().strip()

    # Test example input/solution
    example_solution = part1(parse(example_input))
    assert example_solution == 2
    print(f"Part 1 test example: output = {example_solution}, solution = 2")

    # Solve Part 1
    part1_solution = part1(parse(input))
    print(part1_solution)

    # Solve Part 2
    example_part2_solution = part2(parse(example_input))
    assert example_part2_solution == 4
    print(f"Part 2 test example: output = {example_part2_solution}, solution = 4")
    part2_solution = part2(parse(input))
    print(part2_solution)


if __name__ == "__main__":
    main()
    