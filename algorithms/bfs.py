from collections import deque

from helpers.functions import is_final_state, possible_movements

# Algoritmo BFS
def bfs(initial_state):
    row = deque()
    visited = set()
    row.append((initial_state, []))

    while row:
        curr_state, path = row.popleft()
        visited.add(tuple(map(tuple, curr_state)))

        if is_final_state(curr_state):
            return path

        movements = possible_movements(curr_state)

        for new_state in movements:
            if tuple(map(tuple, new_state)) not in visited:
                new_path = path + [new_state]  
                row.append((new_state, new_path))  

    return None


def bfs_solution(initial_state):
    solucao = bfs(initial_state)
    return solucao
