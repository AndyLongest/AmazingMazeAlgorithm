from maze.grid import MazeGrid


def render_ascii(grid: MazeGrid) -> str:
    lines: list[str] = []

    top = "+" + "---+" * grid.width
    lines.append(top)

    for y in range(grid.height):
        middle = ["|"]
        bottom = ["+"]

        for x in range(grid.width):
            cell = grid.cell(x, y)
            middle.append("   ")
            middle.append("|" if cell.walls["E"] else " ")

            bottom.append("---" if cell.walls["S"] else "   ")
            bottom.append("+")

        lines.append("".join(middle))
        lines.append("".join(bottom))

    return "\n".join(lines)
