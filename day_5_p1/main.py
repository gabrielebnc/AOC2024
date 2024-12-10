from collections import defaultdict


def is_correct(update, rules):
    for i, x in enumerate(update):
        for j, y in enumerate(update):
            if i < j and y in rules[x]:
                print(f"{update} not correct: {update[i]} - {update[j]} are in wrong order")
                return False
    return True


def main():
    rules = defaultdict(set)
    updates = []

    with open("input.txt", "r") as input:
        while line := input.readline():
            if line.count("|"):
                split = line.strip().split("|")
                rules[int(split[1])].add(int(split[0]))
            elif len(line.strip()):
                split = line.strip().split(",")
                updates.append(list(map(int, split)))
    
    sum = 0
    for update in updates:
        if is_correct(update, rules):
            print(f"Correct update: {update}")
            sum += update[len(update) // 2]

    return sum


if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
