import heapq

from helpers.functions import is_final_state, possible_movements

# Algoritmo A*
def astar(initial_state, heuristic):
    row = []
    heapq.heappush(row, (0, initial_state, []))  
    visited = set()

    while row:
        cost, curr_state, path = heapq.heappop(row)  
        visited.add(tuple(map(tuple, curr_state)))

        if is_final_state(curr_state):
            return path

        movements = possible_movements(curr_state)

        for new_state in movements:
            if tuple(map(tuple, new_state)) not in visited:
                new_path = path + [new_state]  
                cost_f = len(new_path) + heuristic(new_state) 
                heapq.heappush(row, (cost_f, new_state, new_path)) 

    return None


def astar_solution(initial_state, heuristic):
    solucao = astar(initial_state, heuristic)
    return solucao