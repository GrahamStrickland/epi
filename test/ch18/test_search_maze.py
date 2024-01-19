#!/usr/bin/env python3


import itertools
from search_maze import Coordinate, search_maze


def test_search_maze() -> None:
    maze = [[1,0,0,0,0,0,1,1,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [1,0,1,0,0,1,1,0,1,1],
            [0,0,0,1,1,1,0,0,1,0],
            [0,1,1,0,0,0,0,0,0,0],
            [0,1,1,0,0,1,0,1,1,0],
            [0,0,0,0,1,0,0,0,0,0],
            [1,0,1,0,1,0,1,0,0,0],
            [1,0,1,1,0,0,0,1,1,1],
            [0,0,0,0,0,0,0,1,1,0]]
    s = Coordinate(x=9,y=0)
    e = Coordinate(x=0,y=9)
    print(search_maze(maze, s, e))


test_search_maze()

