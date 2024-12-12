dir_map = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}  # Directions among the axis
facing_dir_map = {
    "^": "up",
    "v": "down",
    ">": "right",
    "<": "left",
}  # Maps the symbol on the input to the direction
rotation_map = {
    "^": ">",
    "v": "<",
    ">": "v",
    "<": "^",
}  # Maps the rotation upon hitting a target

input_map = []
visit_count = 0
bounds = (0, 0)  # The map's bounds among the axis
guard_position = (0, 0)


def find_guard_position():
    for i, row in enumerate(input_map):
        for j, char in enumerate(row):
            if char == '^':
                return (i, j)  # Found the position


def is_inside_map(pos: tuple[int, int]):
    return (pos[0] >= 0 and pos[0] < bounds[0]) and (pos[1] >= 0 and pos[1] < bounds[1])


def is_walkable(pos: tuple[int, int]):
    return input_map[pos[0]][pos[1]] != "#"


def visit_pos(pos: tuple[int, int]):
    global visit_count
    if(input_map[pos[0]][pos[1]]) == ".":
        input_map[pos[0]][pos[1]] = "X"
        visit_count += 1


def theorical_next_position(pos: tuple[int, int], facing):
    dir = dir_map[facing_dir_map[facing]]
    return (pos[0]+dir[0], pos[1]+dir[1])


def print_map():
    for line in input_map:
        print("".join(line))
    print()
        

def main():
    global guard_position, bounds, visit_count, input_map
    with open("input.txt", "r") as input:
        while line := input.readline():
            input_map.append(list(line.strip()))
        
    bounds = (len(input_map), len(input_map[0]))
    guard_position = find_guard_position()
    input_map[guard_position[0]][guard_position[1]] = "."
    curr_position = guard_position
    curr_facing = "^"
    while is_inside_map(curr_position):
        visit_pos(curr_position)
        theorical_next_pos = theorical_next_position(curr_position, curr_facing)
        if not is_inside_map(theorical_next_pos):
            break
        if is_walkable(theorical_next_pos):  # If the position is not a barrier 
            curr_position = theorical_next_pos
        else:
            #print_map()  # Can also show the map every time we hit a barrier
            curr_facing = rotation_map[curr_facing]
            #print(f"Now going {facing_dir_map[curr_facing]}..")

    return visit_count


if __name__ == "__main__":
    res = main()
    print_map()
    print(f"Result: {res}")
    print(f"Visit count: {visit_count}")
    print(f"Guard's position: {guard_position}")
