import heapq

from helpers.functions import is_final_state, possible_movements

# Função GBFS
def gbfs(initial_state, heuristic):
    row = []
    heapq.heappush(row, (heuristic(initial_state), initial_state, []))
    visited = set()

    while row:
        _, curr_state, path = heapq.heappop(row)

        if is_final_state(curr_state):
            return path

        visited.add(tuple(map(tuple, curr_state)))
        movements = possible_movements(curr_state)

        for new_state in movements:
            if tuple(map(tuple, new_state)) not in visited:
                new_path = path + [new_state]  
                heapq.heappush(row, (heuristic(new_state), new_state, new_path))

    return None

def gbfs_solution(initial_state, heuristic):
    solucao = gbfs(initial_state, heuristic)
    return solucao