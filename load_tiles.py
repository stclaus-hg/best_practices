import random
from pygame import image, Rect, Surface
from generate_maze import generate_dot_positions, create_grid_string, create_maze

TILE_POSITIONS = [
    ('#', 0, 0),
    (' ', 0, 1),
    ('.', 2, 0),
    ('*', 3, 0),
]

SIZE = 32


def get_tile_rect(x, y):
    return Rect(x * SIZE, y * SIZE, SIZE, SIZE)


def load_tiles():
    tile_image = image.load('images/tiles.xpm')
    tiles = {}
    for symbol, x, y in TILE_POSITIONS:
        tiles[symbol] = get_tile_rect(x, y)
    return tile_image, tiles


if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    m = Surface((96, 32))
    m.blit(tile_img, get_tile_rect(0, 0), tiles['#'])
    m.blit(tile_img, get_tile_rect(1, 0), tiles[' '])
    m.blit(tile_img, get_tile_rect(2, 0), tiles['*'])
    image.save(m, 'tile_combo.png')
    positions = generate_dot_positions(5, 5)

    print(create_grid_string(positions, 5, 5))

    random.seed(0)
    maze = create_maze(12, 7)
    print(maze)
