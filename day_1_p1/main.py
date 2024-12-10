from sortedcontainers import SortedList


def main():
    difference = 0
    left, right = SortedList(), SortedList()
    with open("input.txt", "r") as input:
        while line := input.readline():
            split = line.split()
            left.add(int(split[0]))
            right.add(int(split[1]))
    for l, r in zip(left, right):
        difference += abs(l - r)
    return difference


if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
