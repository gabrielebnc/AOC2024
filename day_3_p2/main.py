import re
from functools import reduce

# Match the mul string, capturing the numbers
PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"

# Remove all instructions after don't() and keep all after do()
def filter_instructions(matches):
    i = 0
    to_delete = False
    while i < len(matches):
        if matches[i][2] != '': # do()
            to_delete = False
            i+=1
            continue
        if matches[i][3] != '': # don't()
            to_delete = True
            i+=1
            continue
        if to_delete:
            del matches[i]
        else:
            i += 1


# Takes the current sum, adds the result of mul(x,y)
def reducer(partial, mul_group):
    if mul_group[0] == "" or mul_group[1] == "": # Skip
        return partial
    return partial + int(mul_group[0]) * int(mul_group[1])

def main():
    with open("input.txt", "r") as input:
        matches = re.findall(PATTERN, input.read())
    input.close()
    filter_instructions(matches)
    return reduce(reducer, matches, 0)
    

if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
