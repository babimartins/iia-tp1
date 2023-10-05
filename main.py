import sys

from algorithms.bfs import bfs_solution
from algorithms.ids import ids_solution
from algorithms.ucs import ucs_solution

from algorithms.astar import astar_solution
from algorithms.gbfs import gbfs_solution

from algorithms.hc import hc_solution

from helpers.constants import HEURISTIC
from helpers.functions import print_steps, print_solution

algorithm = sys.argv[1]
initial_state = [list(map(int, sys.argv[i*3+2:i*3+5])) for i in range(3)]
should_print = len(sys.argv) > 11 and sys.argv[11] == 'PRINT'

result = None
if algorithm == 'B':
    result = bfs_solution(initial_state)
elif algorithm == 'I':
    result = ids_solution(initial_state)
elif algorithm == 'U':
    result = ucs_solution(initial_state)
elif algorithm == 'A':
    result = astar_solution(initial_state, HEURISTIC)
elif algorithm == 'G':
    result = gbfs_solution(initial_state, HEURISTIC)
elif algorithm == 'H':
    result = hc_solution(initial_state, HEURISTIC)
else:
    print("Algoritmo fornecido inválido.")

if result != None:
    if should_print:
        print_steps(result, initial_state)
    else:
        print_solution(result)
