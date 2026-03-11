import random as rand

white = 255
black = 202
red = 124
green = 84
orange = 215
blue = 25
sky = 75
pink = 134
yellow = 220
brown = 137

fg = lambda n: "\x1b[38:5:"+str(n)+"m"
bg = lambda n: "\x1b[48:5:"+str(n)+"m"
rst = "\x1b[0m"

color = {
    0: fg(white)+"0"+rst,
    1: fg(red)+"1"+rst,
    2: fg(green)+"2"+rst,
    3: fg(orange)+"3"+rst,
    4: fg(blue)+"4"+rst,
    5: fg(sky)+"5"+rst,
    6: fg(pink)+"6"+rst,
    7: fg(yellow)+"7"+rst,
    8: fg(brown)+"8"+rst,
    9: fg(black)+"9"+rst,
}

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

def board_to_domain(board):
    cells = []
    for r in range(0, rows):
        for c in range(0, cols):
            cells.append(board[r][c])

    rand.shuffle(cells)
    return cells

def print_board(board, rows, cols):
    b = board
    for row in range(0, rows*3):
        if (row%3 == 0):
            for c in range(0, cols):
                print("+-------", end='')
            print("+")

        for c in range(0, cols):
            if (c == 0):
                print("| ", end='')
            else:
                print(" | ", end='')

            r = row // 3
            if row % 3 == 0:
                print(f"\\ {color[b[r][c][0]]} /", end='')
            elif row % 3 == 1:
                print(f"{color[b[r][c][3]]} X {color[b[r][c][1]]}", end='')
            else:
                print(f"/ {color[b[r][c][2]]} \\", end='')

        print(" |")

    for c in range(0, cols):
        print("+-------", end='')
    print("+")

rows = 4
cols = 4
board = generate_random_solvable_board(rows, cols)
print_board(board, rows, cols)
