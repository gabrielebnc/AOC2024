def counter(puzzle: list[str], line):
    count = 0
    # Count horizontal (also backwards)
    count += puzzle[line].count("XMAS") + puzzle[line].count("SAMX")

    if line <= len(puzzle) - 4:
        count += vertical_counter(puzzle, line)
        count += diagonal_right(puzzle, line)
        count += diagonal_left(puzzle, line)

    return count


# Count horizontal (also backwards)
def vertical_counter(puzzle, line):
    count = 0
    for i in range(len(puzzle[line])):
        count += (
            puzzle[line][i] == "X"
            and puzzle[line + 1][i] == "M"
            and puzzle[line + 2][i] == "A"
            and puzzle[line + 3][i] == "S"
        )
        count += (
            puzzle[line][i] == "S"
            and puzzle[line + 1][i] == "A"
            and puzzle[line + 2][i] == "M"
            and puzzle[line + 3][i] == "X"
        )
    return count


# Diagonal right count (also backwards)
def diagonal_right(puzzle, line):
    count = 0
    for i in range(len(puzzle[line]) - 3):
        count += (
            puzzle[line][i] == "X"
            and puzzle[line + 1][i + 1] == "M"
            and puzzle[line + 2][i + 2] == "A"
            and puzzle[line + 3][i + 3] == "S"
        )
        count += (
            puzzle[line][i] == "S"
            and puzzle[line + 1][i + 1] == "A"
            and puzzle[line + 2][i + 2] == "M"
            and puzzle[line + 3][i + 3] == "X"
        )
    return count


# Diagonal left count (also backwards)
def diagonal_left(puzzle, line):
    count = 0
    for i in range(3, len(puzzle[line])):
        count += (
            puzzle[line][i] == "X"
            and puzzle[line + 1][i - 1] == "M"
            and puzzle[line + 2][i - 2] == "A"
            and puzzle[line + 3][i - 3] == "S"
        )
        count += (
            puzzle[line][i] == "S"
            and puzzle[line + 1][i - 1] == "A"
            and puzzle[line + 2][i - 2] == "M"
            and puzzle[line + 3][i - 3] == "X"
        )
    return count


def main():
    puzzle = []
    with open("input.txt", "r") as input:
        while line := input.readline().strip():
            puzzle.append(line)
        input.close()

    count = 0
    for line in range(len(puzzle)):
        count += counter(puzzle, line)

    return count


if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
