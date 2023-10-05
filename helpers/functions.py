from helpers.constants import FINAL_STATE

# Função para encontrar as posições do espaço em branco (0) no quebra-cabeça
def find_empty_pos(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Função para verificar se um state é igual ao state objetivo
def is_final_state(state):
    return state == FINAL_STATE

# Função para gerar os movements possíveis a partir de um state
def possible_movements(state):
    movements = []
    row, column = find_empty_pos(state)

    if row > 0:
        new_state = [list(row) for row in state]
        new_state[row][column], new_state[row - 1][column] = new_state[row - 1][column], new_state[row][column]
        movements.append(new_state)
    if row < 2:
        new_state = [list(row) for row in state]
        new_state[row][column], new_state[row + 1][column] = new_state[row + 1][column], new_state[row][column]
        movements.append(new_state)
    if column > 0:
        new_state = [list(row) for row in state]
        new_state[row][column], new_state[row][column - 1] = new_state[row][column - 1], new_state[row][column]
        movements.append(new_state)
    if column < 2:
        new_state = [list(row) for row in state]
        new_state[row][column], new_state[row][column + 1] = new_state[row][column + 1], new_state[row][column]
        movements.append(new_state)

    return movements


def print_solution(solution):
    print(len(solution))

def print_steps(solution, initial_state):
    if initial_state == FINAL_STATE:
        print(len(solution))
        print()
        for row in initial_state:
            for value in row:
                if value == 0:
                    print('  ', end='')
                else:
                    print(f'{value} ', end='')
            print()
        print()
    elif solution and solution[-1] == FINAL_STATE:
        print(len(solution))
        print()
        for row in initial_state:
            for value in row:
                if value == 0:
                    print('  ', end='')
                else:
                    print(f'{value} ', end='')
            print()
        print()
        for state in solution:
            for row in state:
                for value in row:
                    if value == 0:
                        print('  ', end='')
                    else:
                        print(f'{value} ', end='')
                print()
            print()
    else:
        print("Não foi encontrada uma solução.")

