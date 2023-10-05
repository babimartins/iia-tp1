import heapq

from helpers.functions import is_final_state, possible_movements

# Algoritmo UCS
def ucs(initial_state):
    row = []
    heapq.heappush(row, (0, initial_state, []))
    visited = set()

    while row:
        _, curr_path, path = heapq.heappop(row)

        if is_final_state(curr_path):
            return path

        visited.add(tuple(map(tuple, curr_path)))
        movements = possible_movements(curr_path)

        for new_state in movements:
            if tuple(map(tuple, new_state)) not in visited:
                new_path = path + [new_state]
                cost_path = len(new_path)
                heapq.heappush(row, (cost_path, new_state, new_path))

def ucs_solution(initial_state):
    solucao = ucs(initial_state)
    return solucao
