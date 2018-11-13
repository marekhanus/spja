import random
from tkinter import Tk, Canvas, ALL

from tasks import shortest_path

"""
Here you can test your BFS algorithm.
Left click a cell = set starting point
Left click another cell = set end point
The shortest path between the cells should be highlighted.
"""


class Maze(Tk):
    def __init__(self, dimension, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Maze")

        self.dimension = dimension
        self.cell_width = 15

        self.start = None
        self.end = None
        self.path = []

        self.canvas = Canvas(self, width=601, height=601)
        self.canvas.bind("<Button-1>", self.handle_canvas_click)
        self.canvas.pack()

        self.graph = self.generate_maze()
        self.draw_maze(self.graph)

    def handle_canvas_click(self, event):
        mouse_x = event.x
        mouse_y = event.y
        cell_x, cell_y = self.get_cell_location(mouse_x, mouse_y)

        if cell_x > self.dimension or cell_y > self.dimension:
            return

        location = (cell_x, cell_y)

        if not self.start:
            self.start = location
        elif not self.end and location != self.start:
            self.end = location
            self.path = self.get_shortest_path() or []
            print("Shortest path: {}".format(self.path or None))
        else:
            self.start = location
            self.end = None
            self.path = []

        self.draw_maze(self.graph)

    def get_shortest_path(self):
        return shortest_path(self.graph,
                             self.linearize(self.start),
                             self.linearize(self.end))

    def create_graph(self):
        graph = []
        increments = ((1, 0), (0, 1), (-1, 0), (0, -1))

        for y in range(self.dimension):
            for x in range(self.dimension):
                vertex = []
                graph.append(vertex)
                for (i_x, i_y) in increments:
                    pos_x = x + i_x
                    pos_y = y + i_y
                    if self.is_valid(pos_x, pos_y):
                        vertex.append(self.linearize((pos_x, pos_y)))

        return graph

    def is_valid(self, x, y):
        return 0 <= x < self.dimension and 0 <= y < self.dimension

    def linearize(self, pos):
        x, y = pos
        return y * self.dimension + x

    def get_cell_location(self, mouse_x, mouse_y):
        x = int(mouse_x / self.cell_width)
        y = int(mouse_y / self.cell_width)
        return (x, y)

    def draw_maze(self, graph):
        self.canvas.delete(ALL)

        for i in range(self.dimension * self.dimension):
            y = int(i / self.dimension)
            x = int(i % self.dimension)
            pos_x = x * self.cell_width
            pos_y = y * self.cell_width
            pos_x += 1
            pos_y += 1

            path_index = self.path.index(i) if i in self.path else None
            fill = None
            if self.start == (x, y):
                fill = 'green'
            elif self.end == (x, y):
                fill = 'red'
            elif path_index:
                fill = 'blue'

            vertex = graph[i]
            neighbours = (
                ((-1, 0), (pos_x, pos_y, pos_x, pos_y + self.cell_width)),
                ((0, 1), (pos_x, pos_y + self.cell_width, pos_x + self.cell_width,
                          pos_y + self.cell_width)),
                ((1, 0), (pos_x + self.cell_width, pos_y + self.cell_width,
                          pos_x + self.cell_width, pos_y)),
                ((0, -1), (pos_x + self.cell_width, pos_y, pos_x, pos_y)),
            )

            for ((i_x, i_y), bbox) in neighbours:
                if self.linearize((x + i_x, y + i_y)) not in vertex:
                    self.canvas.create_line(*bbox)

            offset = 2
            self.canvas.create_rectangle(pos_x + offset, pos_y + offset,
                                         pos_x + self.cell_width - offset,
                                         pos_y + self.cell_width - offset,
                                         fill=fill,
                                         width=0)
            if path_index is not None:
                self.canvas.create_text(pos_x + 8, pos_y + 8, fill='white', text=str(path_index))

    def generate_maze(self):
        graph = self.create_graph()

        sets = {}
        for i in range(len(graph)):
            sets[i] = {i}

        walls = []
        for index, v in enumerate(graph):
            for edge in v:
                if (edge, index) not in walls:
                    walls.append((index, edge))

        rand = random.Random()
        rand.shuffle(walls)

        for (src, dest) in walls[:int(len(walls) / 2)]:
            src_set = sets[src]
            dst_set = sets[dest]
            if src_set is not dst_set:
                graph[src].remove(dest)
                graph[dest].remove(src)
                src_set.add(dest)
                sets[dest] = src_set

        return graph


if __name__ == "__main__":
    maze = Maze(40)
    maze.mainloop()
