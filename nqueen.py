# def is_safe(board, row, col):
#     for i in range(row):
#         if board[i] == col or abs(board[i] - col) == abs(i - row):
#             return False
#     return True

# def solve_n_queens(board, row, n):
#     if row == n:
#         print_board(board, n)
#         return True

#     for col in range(n):
#         if is_safe(board, row, col):
#             board[row] = col
#             if solve_n_queens(board, row + 1, n):
#                 return True
#             board[row] = -1  # Backtrack
#     return False

# def print_board(board, n):
#     for i in range(n):
#         row = ['Q' if j == board[i] else '.' for j in range(n)]
#         print(' '.join(row))
#     print()

# def n_queens(n):
#     board = [-1] * n  # Initialize the board with -1
#     if not solve_n_queens(board, 0, n):
#         print("No solution exists")

# # User input for N
# n = int(input("Enter the value of N for N-Queens: "))
# n_queens(n)



def print_board(board, n):
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(' '.join(row))
    print()

def solve_n_queens_bnb_bt(n):
    def backtrack(row):
        if row == n:
            print_board(board, n)
            return

        for col in range(n):
            if not cols[col] and not diag1[row - col + n - 1] and not diag2[row + col]:
                # Branch: Place the queen
                board[row] = col
                cols[col] = diag1[row - col + n - 1] = diag2[row + col] = True

                # Recurse to next row
                backtrack(row + 1)

                # Backtrack: Remove the queen and try next column
                cols[col] = diag1[row - col + n - 1] = diag2[row + col] = False
                board[row] = -1

    # Initialize tracking structures
    board = [-1] * n
    cols = [False] * n             # Columns
    diag1 = [False] * (2 * n - 1)  # \ Diagonal
    diag2 = [False] * (2 * n - 1)  # / Diagonal

    backtrack(0)

# User input
n = int(input("Enter the value of N for N-Queens: "))
solve_n_queens_bnb_bt(n)
