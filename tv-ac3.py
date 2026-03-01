import random as rand

def generate_random_board(rows, cols):
    board = []
    for r in range(0, rows):
        row = []
        for c in range(0, cols):
            col = []
            col.append(rand.randint(0, 9))
            col.append(rand.randint(0, 9))
            col.append(rand.randint(0, 9))
            col.append(rand.randint(0, 9))

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
                print(f"{b[r][c][3]} X {b[r//3][c][1]}", end='')
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

rows = 2
cols = 2
board = generate_random_board(rows, cols)
print_board(board, rows, cols)
