import random


def get_neighbors(x, y):
    return [
        (x, y-1), (x, y+1), (x-1, y), (x+1, y),
        (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)
    ]


def get_all_dot_positions(xsize, ysize):
    return [(x, y) for x in range(1, xsize-1) for y in range(1, ysize-1)]


def generate_dot_positions(xsize, ysize):
    positions = get_all_dot_positions(xsize, ysize)

    dots = set()
    while positions != []:
        x, y = random.choice(positions)
        neighbors = get_neighbors(x, y)
        free = [nb in dots for nb in neighbors]
        if free.count(True) < 5:
            dots.add((x, y))
        positions.remove((x, y))
    return dots


def create_grid_string(dots, xsize, ysize):
    grid = ""
    for y in range(ysize):
        for x in range(xsize):
            grid += "." if (x, y) in dots else "#"
        grid += "\n"
    return grid


def create_maze(xsize, ysize):
    dots = generate_dot_positions(xsize, ysize)
    maze = create_grid_string(dots, xsize, ysize)
    return maze
