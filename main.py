import random


class Game:
    grid = None

    def __init__(self, cols: int = 10, rows: int = 10):
        self.cols = cols
        self.rows = rows
        self.grid = [[random.randint(0, 1) for i in range(self.cols)] for j in range(self.rows)]

    def __str__(self):
        return '\n'.join(map(' '.join, [list(map(str, suba)) for suba in self.grid]))

    def generate(self):
        next_grid = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(self.cols):
            for j in range(self.rows):
                cell_state = self.grid[i][j]

                live_neighbors = self.count_live_neighbors(i, j)
                if cell_state == 0 and live_neighbors == 3:
                    next_grid[i][j] = 1
                elif cell_state == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    next_grid[i][j] = 0
                else:
                    next_grid[i][j] = cell_state

        self.grid = next_grid

    def count_live_neighbors(self, x: int, y: int) -> int:
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == x and j == y:
                    continue
                col = (x + i + self.cols) % self.cols
                row = (y + j + self.rows) % self.rows
                live_neighbors += self.grid[col][row]

        return live_neighbors


if __name__ == '__main__':
    grid = Game(cols=10, rows=10)
    print(grid)

    for i in range(100):
        grid.generate()
        print('\n')
        print(f'Generation {i}')
        print(grid)
