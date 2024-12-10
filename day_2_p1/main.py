def is_incr(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


def is_decr(list):
    for i in range(len(list) - 1):
        if list[i] < list[i + 1]:
            return False
    return True


def diff_check(list):
    for i in range(len(list) - 1):
        diff = abs(list[i] - list[i + 1])
        if diff > 3 or diff < 1:
            return False
    return True


def is_safe(report):
    return (is_incr(report) or is_decr(report)) and diff_check(report)


def main():
    safe_count = 0
    with open("input.txt", "r") as input:
        while line := input.readline():
            safe_count += is_safe(list(map(int, line.split())))
    return safe_count


if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
