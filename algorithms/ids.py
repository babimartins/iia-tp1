from helpers.functions import is_final_state, possible_movements

# Algoritmo IDS
def ids(initial_state):
    max_depth = 0
    while True:
        visited = set()
        queue = [(initial_state, [])]

        while queue:
            curr_path, path = queue.pop()

            if is_final_state(curr_path):
                return path

            visited.add(tuple(map(tuple, curr_path)))

            if len(path) < max_depth:
                movements = possible_movements(curr_path)

                for new_state in movements:
                    if tuple(map(tuple, new_state)) not in visited:
                        new_path = path + [new_state]
                        queue.append((new_state, new_path))

        max_depth += 1

def ids_solution(initial_state):
    solucao = ids(initial_state)
    return solucao