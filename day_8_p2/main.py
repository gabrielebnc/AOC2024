def is_inside_map(pos: tuple[int, int], bounds: tuple[int, int]):
    return (pos[0] >= 0 and pos[0] < bounds[0]) and (pos[1] >= 0 and pos[1] < bounds[1])


def add_positions(pos1: tuple[int, int], pos2: tuple[int, int]):
    return tuple(a + b for a, b in zip(pos1, pos2))


def subtract_positions(pos1: tuple[int, int], pos2: tuple[int, int]):
    return tuple(a - b for a, b in zip(pos1, pos2))


def get_antinodes_positions(pos1: tuple[int, int], pos2: tuple[int, int], bounds):
    def validate_antinode_pos(pos: tuple[int, int]):
        return is_inside_map(pos, bounds)

    an_positions = []
    delta_pos = (pos1[0] - pos2[0], pos1[1] - pos2[1])

    # Compute all the possible antinodes positions, two of these will be the antennas positions themself, we will filter them out
    pos = add_positions(pos1, delta_pos)
    while is_inside_map(pos, bounds):
        an_positions.append(pos)
        pos = add_positions(pos, delta_pos)

    pos = subtract_positions(pos1, delta_pos)
    while is_inside_map(pos, bounds):
        an_positions.append(pos)
        pos = subtract_positions(pos, delta_pos)

    # Now filter, removing the positions identical to pos1 or pos2 and positions outside the map
    return list(set(filter(validate_antinode_pos, an_positions)))


def main():
    input_map = []
    antennas_frequencies = set()
    antinode_positions = set()

    with open("input.txt", "r") as input:
        while line := list(input.readline().strip()):
            input_map.append(line)
            for e in line:
                antennas_frequencies.add(e)
    antennas_frequencies.remove(".")

    bounds = (len(input_map), len(input_map[0]))

    for x1, line1 in enumerate(input_map):
        for y1, elem1 in enumerate(line1):
            if (
                elem1 in antennas_frequencies
            ):  # Skip for each spot which is not an antenna
                for x2, line2 in enumerate(input_map):
                    for y2, elem2 in enumerate(line2):
                        if (x1, y1) != (
                            x2,
                            y2,
                        ) and elem1 == elem2:  # We found two antennas of same frequency
                            antinodes = get_antinodes_positions(
                                (x1, y1),
                                (x2, y2),
                                bounds,  # Add the antenna type to the function
                            )
                            for an in antinodes:
                                antinode_positions.add(an)

    return len(antinode_positions)


if __name__ == "__main__":
    res = main()
    print(f"Result: {res}")
