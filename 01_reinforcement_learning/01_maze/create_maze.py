# -*- coding: utf-8 -*-
from pprint import pprint
from enum import Enum
import numpy as np
import matplotlib.pyplot as plt

# 以下でフリーズする場合の対策
# import matplotlib.pyplot as plt
# http://stackoverflow.com/questions/17490444/import-matplotlib-pyplot-hangs

# 必要？
# brew install freetype


# ダンジョンの自動生成
# http://www5d.biglobe.ne.jp/~stssk/maze/make.html


# class Maze_Algorithm(Enum):
#     stick = 1

# class Maze:

#     def __init__(self, maze_size):
#         self.size = maze_size
#         self.maze = [[0 for i in range(maze_size)] for j in range(maze_size)]

#     def create(self, algorithm=Maze_Algorithm.stick):
#         pass

#     def draw(self):
#         for row in self.maze:
#             for cell in row:
#                 print("■" if cell == 0 else "□", end="")
#             print("")


# if __name__ == "__main__":

#     maze = Maze(10)
#     maze.create()
#     maze.draw()

#     print(Maze_Algorithm.stick)

maze_size = 10
maze = [[(i % 2) for i in range(maze_size)] for j in range(maze_size)]
plt.imshow(np.random.randn(100, 100))
plt.show()

