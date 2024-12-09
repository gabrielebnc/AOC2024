import re
from functools import reduce

# Match the mul string, capturing the numbers
PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"

# Takes the current sum, adds the result of mul(x,y)
def reducer(partial, mul_group):
    return partial + int(mul_group[0]) * int(mul_group[1])

def main():
    with open("input.txt", "r") as input:
        matches = re.findall(PATTERN, input.read())
    input.close()
    return reduce(reducer, matches, 0)
    

if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
