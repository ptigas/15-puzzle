from neural_network import *
from intelligence import *
from board import *
import random
import numpy as np
import time
import itertools

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
puzzle = random_state(N, 50)
print(puzzle)
t0 = time.time()
path, _ = a_star(puzzle, neural_heuristic)
print("Solved using neural network in {}".format(time.time() - t0))

with open("solution.txt", "w") as f:
    for p in path:
        f.write("{}\n".format(list(itertools.chain.from_iterable(p.board))))

#a_star(puzzle, manhattan_heuristic)
#print("Solved using heuristics in {}".format(time.time() - t0))