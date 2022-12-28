# AOC 2022 Day 2

import pathlib


def parse(data):
    """Parse input"""
    return data.splitlines()


def part1(data):
    """
    Part 1 notes:
    A, X, 1 = rock
    B, Y, 2 = paper
    C, Z, 3 = scissors

    Round score: {rock = 1, paper = 2, scissors = 3} + {lost = 0, draw = 3, win = 6}
    Total score = sum(round_scores)
    """
    shape_score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    total_score = 0

    for rd in data:
        opponent_shape_score = shape_score[rd[0]]  # first char
        your_shape_score = shape_score[rd[-1]]  # last char
        total_score += your_shape_score

        difference = opponent_shape_score - your_shape_score
        if difference == 0:  # draw
            total_score += 3
        elif difference == -1 or difference == 2:  # won
            total_score += 6
        else:  # lost
            pass

    return total_score


def part2(data):
    """
    Part 2 notes:
    X = lose (0), Y = draw (3), Z = win (6)
    """
    get_score = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
    total_score = 0

    for rd in data:
        opponent_shape_score = get_score[rd[0]]  # first char
        result_score = get_score[rd[-1]]  # last char
        total_score += result_score

        if result_score == 6:  # win
            total_score += 1 if opponent_shape_score == 3 else opponent_shape_score + 1
            # if opponent is scissors (3), you need rock (1) to win
        elif result_score == 0:  # lose
            total_score += 3 if opponent_shape_score == 1 else opponent_shape_score - 1
            # if opponent is rock (1), you need scissors (3) to lose
        else:  # draw
            total_score += opponent_shape_score

    return total_score


def main():
    # Read inputs
    example_input = pathlib.Path("./inputs/day2_example_input.txt").read_text().strip()
    input = pathlib.Path("./inputs/day2_input.txt").read_text().strip()

    # Test example input/solution
    example_solution = part1(parse(example_input))
    assert example_solution == 15

    # Solve Part 1
    part1_solution = part1(parse(input))
    print(part1_solution)

    # Solve Part 2
    part2_solution = part2(parse(input))
    print(part2_solution)


if __name__ == "__main__":
    main()
