def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    if [board[i][i] for i in range(3)].count(player) == 3 or [board[i][2-i] for i in range(3)].count(player) == 3:
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for _ in range(9):
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter row and column (0, 1, 2): ").split())
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move, try again.")
    print_board(board)
    print("It's a draw!")
tic_tac_toe()
