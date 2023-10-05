import random

from helpers.functions import find_empty_pos

def possible_movements(state):
    movements = []
    row, column = find_empty_pos(state)

    if row > 0:
        movements.append((row - 1, column))
    if row < 2:
        movements.append((row + 1, column))
    if column > 0:
        movements.append((row, column - 1))
    if column < 2:
        movements.append((row, column + 1))

    return movements

# Algoritmo Hill Climbing com movements laterais
def hill_climbing(initial_state, heuristic, max_iter=1000):
    curr_state = initial_state
    best_heuristic = heuristic(curr_state)
    solution = []

    for _ in range(max_iter):
        all_movements = possible_movements(curr_state)
        random.shuffle(all_movements)

        best_neighbor = None
        best_neighbor_heuristic = float('inf')

        for movement in all_movements:
            new_state = [list(row) for row in curr_state]
            curr_row, curr_column = find_empty_pos(new_state)
            final_row, final_column = movement
            new_state[curr_row][curr_column], new_state[final_row][final_column] = new_state[final_row][final_column], new_state[curr_row][curr_column]

            neighbor_heuristic = heuristic(new_state)

            if neighbor_heuristic < best_neighbor_heuristic:
                best_neighbor = new_state
                best_neighbor_heuristic = neighbor_heuristic

        if best_neighbor_heuristic >= best_heuristic:
            break

        curr_state = best_neighbor
        best_heuristic = best_neighbor_heuristic
        solution.append(curr_state)

    return solution

def hc_solution(initial_state, heuristic):
    solucao = hill_climbing(initial_state, heuristic)
    return solucao