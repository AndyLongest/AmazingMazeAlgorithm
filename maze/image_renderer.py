from __future__ import annotations

from PIL import Image, ImageDraw

from maze.grid import MazeGrid


def render_grid_image(
    grid: MazeGrid,
    cell_size: int = 16,
    wall_width: int = 2,
    wall_color: tuple[int, int, int] = (20, 20, 20),
    background_color: tuple[int, int, int] = (255, 255, 255),
) -> Image.Image:
    if cell_size <= 0:
        raise ValueError("cell_size must be positive")
    if wall_width <= 0:
        raise ValueError("wall_width must be positive")

    image_width = grid.width * cell_size + wall_width
    image_height = grid.height * cell_size + wall_width

    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    for y in range(grid.height):
        for x in range(grid.width):
            cell = grid.cell(x, y)

            x1 = x * cell_size
            y1 = y * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            if cell.walls["N"]:
                draw.line((x1, y1, x2, y1), fill=wall_color, width=wall_width)
            if cell.walls["W"]:
                draw.line((x1, y1, x1, y2), fill=wall_color, width=wall_width)
            if cell.walls["E"]:
                draw.line((x2, y1, x2, y2), fill=wall_color, width=wall_width)
            if cell.walls["S"]:
                draw.line((x1, y2, x2, y2), fill=wall_color, width=wall_width)

    return image
