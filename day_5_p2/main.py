from collections import defaultdict
from functools import cmp_to_key

rules = defaultdict(set)


def is_ordered(update):
    for i, x in enumerate(update):
        for j, y in enumerate(update):
            if i < j and x in rules[y]:
                print(
                    f"{update} not correct: {update[i]} - {update[j]} are in wrong order"
                )
                return False
    return True


def rules_compare(a, b):
    if b in rules[a]:
        return -1
    else:
        return 1


def main():
    updates = []

    with open("input.txt", "r") as input:
        while line := input.readline():
            if line.count("|"):
                split = line.strip().split("|")
                rules[int(split[0])].add(int(split[1]))
            elif len(line.strip()):
                split = line.strip().split(",")
                updates.append(list(map(int, split)))

    sum = 0
    for update in updates:
        if not is_ordered(update):
            update = sorted(update, key=cmp_to_key(rules_compare))
            print(f"Sorted update: {update}")
            sum += update[len(update) // 2]

    return sum


if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
