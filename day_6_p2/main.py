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

bounds = (0, 0)  # The map's bounds among the axis
cells_count = 0


class LoopDetectedException(Exception):
    pass


def find_guard_position(map):
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == "^":
                return (i, j)  # Found the position


def is_inside_map(pos: tuple[int, int]):
    return (pos[0] >= 0 and pos[0] < bounds[0]) and (pos[1] >= 0 and pos[1] < bounds[1])


def is_walkable(pos: tuple[int, int], map):
    spot = map[pos[0]][pos[1]]
    return spot != "#" and spot != "O"


def is_visited(char):
    return char == "X"


def visit_pos(pos: tuple[int, int], map):
    if (map[pos[0]][pos[1]]) == ".":
        map[pos[0]][pos[1]] = "X"
        return True
    return False


def theorical_next_position(pos: tuple[int, int], facing):
    dir = dir_map[facing_dir_map[facing]]
    return (pos[0] + dir[0], pos[1] + dir[1])


def print_map(map):
    for line in map:
        print("".join(line))
    print()


def visit(map, cells_count):
    curr_position = find_guard_position(map)
    map[curr_position[0]][curr_position[1]] = "."
    curr_facing = "^"
    move_count = 0
    visit_count = 0
    while is_inside_map(curr_position):
        if move_count > cells_count:  # LOOP DETECTED
            raise LoopDetectedException(
                f"move count: {move_count}, cells count: {cells_count}"
            )

        visit_count += visit_pos(curr_position, map)
        theorical_next_pos = theorical_next_position(curr_position, curr_facing)
        if not is_inside_map(theorical_next_pos):
            break
        if is_walkable(theorical_next_pos, map):  # If the position is not a barrier
            curr_position = theorical_next_pos
            move_count += 1
        else:
            # print_map(map)  # Can also show the map every time we hit a barrier
            curr_facing = rotation_map[curr_facing]
            # print(f"Now going {facing_dir_map[curr_facing]}..")

    return visit_count


def main():
    global bounds, cells_count

    input_map = []
    with open("day_6_p2/input.txt", "r") as input:
        while line := input.readline():
            input_map.append(list(line.strip()))

    starting_position = find_guard_position(input_map)
    backup_map = [line[:] for line in input_map]
    bounds = (len(input_map), len(input_map[0]))
    cells_count = bounds[0] * bounds[1]

    visit(input_map, cells_count)
    loop_positions = 0

    for x, line in enumerate(input_map):
        for y, char in enumerate(line):
            if is_visited(char) and (x, y) != starting_position:
                map_plus_barrier = [line[:] for line in backup_map]
                map_plus_barrier[x][y] = "O"  # Add a barrier
                try:
                    visit(map_plus_barrier, cells_count)
                except LoopDetectedException:
                    loop_positions += 1

    return loop_positions


if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
