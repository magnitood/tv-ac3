import random as rand

# TODO: shuffle the solved board to make a proper solution
def generate_random_solvable_board(rows, cols):
    board = []
    for r in range(0, rows):
        row = []
        for c in range(0, cols):
            col = []

            if (r == 0):
                col.append(rand.randint(0, 9))
            else:
                col.append(board[r-1][c][2])

            col.append(rand.randint(0, 9))
            col.append(rand.randint(0, 9))

            if (c == 0):
                col.append(rand.randint(0, 9))
            else:
                col.append(row[c-1][1])

            row.append(col)
        board.append(row)

    return board

def print_board(board, rows, cols):
    b = board
    for row in range(0, rows*3):
        for c in range(0, cols):
            r = row // 3
            if row % 3 == 0:
                print(f"\\ {b[r][c][0]} /", end='')
            elif row % 3 == 1:
                print(f"{b[r][c][3]} X {b[r][c][1]}", end='')
            else:
                print(f"/ {b[r][c][2]} \\", end='')

            if (c < cols-1):
                print(" | ", end='')
        print()
        if row % 3 == 2 and row//3 < rows-1:
            for c in range(0, cols):
                print("-----", end='')
                if (c < cols-1):
                    print("-+-", end='')
            print()

rows = 4
cols = 4
board = generate_random_solvable_board(rows, cols)
print_board(board, rows, cols)
