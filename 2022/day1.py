# AOC 2022 Day 1

# from aocd import get_data
import pathlib
import math


def parse(data):
    """Parse input"""
    calorie_list_per_elf = [[]]

    input_list = data.split('\n')
    for element in input_list:
        if element == "":
            calorie_list_per_elf.append([])
        else:
            calorie_list_per_elf[-1].append(int(element))

    return calorie_list_per_elf


def part1(data):
    """Solve Part 1"""
    calories_per_elf = [math.fsum(calorie_list) for calorie_list in data]
    return max(calories_per_elf), calories_per_elf


def part2(data):
    """Solve Part 2"""
    top3 = sorted(data, reverse=True)[:3]
    return math.fsum(top3)


def main():
    # Read inputs
    example_input = pathlib.Path("./inputs/day1_example_input.txt").read_text().strip()
    input = pathlib.Path("./inputs/day1_input.txt").read_text().strip()  # get_data(day=1, year=2022)

    # Test example input/solution
    example_solution, _ = part1(parse(example_input))
    assert example_solution == 24000

    # Solve Part 1
    part1_solution, part2_input = part1(parse(input))
    print(part1_solution)

    # Solve Part 2
    part2_solution = part2(part2_input)
    print(part2_solution)


if __name__ == "__main__":
    main()
