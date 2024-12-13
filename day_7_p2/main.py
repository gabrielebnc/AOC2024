from itertools import product
from functools import reduce

operators = ["*", "+", "||"]


def compute(acc, current):
    num, op = current
    if op == "+":
        return acc + num
    if op == "*":
        return acc * num
    if op == "||":
        return int(str(acc) + str(num))


def is_achievable(nums: list[int], result: int):
    operators_combs = list(product(operators, repeat=len(nums) - 1))
    for comb in operators_combs:
        operations = zip(nums[1:], comb)
        red = reduce(compute, operations, nums[0])

        if red == result:
            return True
    return False


def main():
    equations = {}
    with open("input.txt", "r") as input:
        while line := input.readline():
            result, nums = line.strip().split(":")
            nums = list(map(int, nums.split()))
            equations[int(result)] = nums

    sum = 0
    for res, nums in equations.items():
        if is_achievable(nums, res):
            sum += res

    return sum


if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
