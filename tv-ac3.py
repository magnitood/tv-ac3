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
# fg = lambda n: "\x1b[0m"
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
    None: " ",
}

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


def generate_random_solved_board(rows, cols):
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

def board_to_domain(board, rows, cols):
    cells = []
    for r in range(0, rows):
        for c in range(0, cols):
            cells.append(board[r][c])
    rand.shuffle(cells)

    domain = []
    for r in range(0, rows):
        row = []
        for c in range(0, cols):
            row.append(cells.copy())
        domain.append(row)
    return domain

def generate_random_solvable_domain(rows, cols):
    board = generate_random_solved_board(rows, cols)
    return board_to_domain(board, rows, cols)

def init_board(rows, cols):
    board = []
    for r in range(0, rows):
        row = []
        for c in range(0, cols): 
            col = [None, None, None, None]
            row.append(col)
        board.append(row)
    return board


def is_board_full(board, rows, cols):
    for r in range(0, rows):
        for c in range(0, cols):
            if (board[r][c][0] == None):
                return False
    return True

def is_board_valid(board, rows, cols):
    for r in range(0, rows):
        for c in range(0, cols):
            if (board[r][c][0] == None):
                return False
            if (r != 0):
                if (board[r][c][0] != board[r-1][c][2]):
                    return False
            if (c != 0):
                if (board[r][c][3] != board[r][c-1][1]):
                    return False
    return True

def next_unassigned_var(board, rows, cols):
    for r in range(0, rows):
        for c in range(0, cols):
            if (board[r][c][0] == None):
                return r, c

# AC-3
# returns True and alters domain if arc-consistent
# returns False
def apply_inference(domain, board, rows, cols):
    return True

# board, rows and cols together is the assignement
# domain is the csp

count = 0
def backtracking_solver(domain, board, rows, cols):
    if (is_board_full(board, rows, cols)):
        return True

    r, c = next_unassigned_var(board, rows, cols)
    for value in domain[r][c]:
        board[r][c] = value
        old_domain = domain.copy()
        if apply_inference(domain, board, rows, cols):
            result = backtracking_solver(domain, board, rows, cols)
            if result:
                return True
            domain = old_domain
        board[r][c] = [None, None, None, None]
    return False

rows = 5
cols = 5
domain = generate_random_solvable_domain(rows, cols)
print(domain[0][0])
board = init_board(rows, cols)
result = backtracking_solver(domain, board, rows, cols)
if result:
    print_board(board, rows, cols)
else:
    print("No Solution", count)
