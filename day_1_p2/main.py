from collections import defaultdict

def main():
    similarity_score = 0
    left, right = [], defaultdict(lambda: 0)
    with open("input.txt", "r") as input:
        while line:= input.readline():
            split = line.split()
            left.append(int(split[0]))

            # Map with counts of occurrences
            right[int(split[1])] += 1
    for elem in left:
        similarity_score += elem * right[elem]
    
    return similarity_score


if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
