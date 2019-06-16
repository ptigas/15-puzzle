from neural_network import *
from intelligence import *
from board import *
import random
import numpy as np
import time


def random_state(N, moves):
    state = Board()
    state.scramble(moves)
    return state

def group(a, d):
    print(a)
    res = []
    for i in range(d):
        res.append(a[i*d:i*d+d])
    return np.array(res)

N = 4
puzzle = random_state(N, 60)
print(puzzle)
t0 = time.time()
a_star(puzzle, neural_heuristic)
print(time.time() - t0)