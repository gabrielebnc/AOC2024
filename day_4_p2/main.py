
def counter(puzzle: list[str], line):
    count = 0
    # We only loop from the second letter to the second-last
    for i in range(1, len(puzzle[line])-1):
        # If the letter is 'A', it could be the center of an X
        if puzzle[line][i] == "A": 
            count += check_x(puzzle, line, i)
    return count
    
def check_x(puzzle, line, idx):
    right_diag = (puzzle[line-1][idx-1] == "M" and puzzle[line+1][idx+1] == "S") or (puzzle[line-1][idx-1] == "S" and puzzle[line+1][idx+1] == "M")
    left_diag = (puzzle[line-1][idx+1] == "M" and puzzle[line+1][idx-1] == "S") or (puzzle[line-1][idx+1] == "S" and puzzle[line+1][idx-1] == "M")
    return right_diag and left_diag

def main():
    puzzle = []
    with open("input.txt", "r") as input:
        while line:=input.readline().strip():
            puzzle.append(line)
        input.close()

    count = 0
    # We only loop from the second column to the second-last
    for line in range(1, len(puzzle)-1):
        count += counter(puzzle, line)
    
    return count


if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
