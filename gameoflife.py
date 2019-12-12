import random
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))

#sets board state equal to all zeros
def dead_state(rows, cols):
    board_state = [["0" for i in range(cols)] for j in range(rows)]
    return board_state

def random_state(rows, cols):
    board_state = dead_state(rows, cols)

    for i in range(rows):
        for j in range(cols):
            random_num = random.random()
            if random_num >= 0.5:
                board_state[i][j] = 1
            else:
                board_state[i][j] = 0

    return board_state

def render(board_state):
    for i in range(rows):
        for j in range(cols):
            if board_state[i][j]==0:
                print(" ", end=" ")
            else:
                print("#", end=" ")
        print("\n")

def next_board_state(board_state):

def find_nearby_cells():



board_state = random_state(rows, cols)
render(board_state)



