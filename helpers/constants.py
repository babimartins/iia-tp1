FINAL_STATE = [[1, 2, 3],       
                  [4, 5, 6],
                  [7, 8, 0]]

# Função de heurística 1 (distância de Manhattan)
def heuristic_manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                final_row, final_column = divmod(state[i][j] - 1, 3)
                distance += abs(i - final_row) + abs(j - final_column)
    return distance

# Função de heurística 2 (número de peças fora do lugar)
def heuristic_out_of_place(state):
    count_out_of_place = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != FINAL_STATE[i][j]:
                count_out_of_place += 1
    return count_out_of_place

HEURISTIC = heuristic_out_of_place