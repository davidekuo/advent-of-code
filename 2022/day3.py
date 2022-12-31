# AOC 2022 Day 3

import pathlib


def parse(data):
    """Parse input"""
    return data.splitlines()


def get_priority(item_type: str) -> int:
    """
    Helper function that returns priority of provided item type

    :param str item_type: an alphabetical character (a-z, A-Z)
    :return: priority (int)
    """
    assert item_type.isalpha()
    if item_type.islower():
        return ord(item_type) - ord('a') + 1
    else:  # item_type is uppercase
        return ord(item_type) - ord('A') + 27


def part1(data):
    priority_sum = 0
    for rucksack in data:
        first_compartment = rucksack[:(len(rucksack) // 2)]
        second_compartment = rucksack[(len(rucksack) // 2):]
        intersection = set(first_compartment) & set(second_compartment)
        priority_sum += get_priority(intersection.pop())  # pop to get str from set
    return priority_sum


def part2(data):
    priority_sum = 0
    group_size = 3
    for i in range(0, len(data), group_size):
        group = data[i:i+group_size]
        intersection = set(group[0]) & set(group[1]) & set(group[2])
        priority_sum += get_priority(intersection.pop())
    return priority_sum


def main():
    # Read inputs
    example_input = pathlib.Path("./inputs/day3_example_input.txt").read_text().strip()
    input = pathlib.Path("./inputs/day3_input.txt").read_text().strip()

    # Test example input/solution
    example_solution = part1(parse(example_input))
    assert example_solution == 157

    # Solve Part 1
    part1_solution = part1(parse(input))
    print(part1_solution)

    # Solve Part 2
    part2_solution = part2(parse(input))
    print(part2_solution)


if __name__ == "__main__":
    main()
