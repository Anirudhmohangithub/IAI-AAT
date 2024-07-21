def nextMove(player, board):
    # Check for immediate win opportunities for the current player
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r][c] = player
                if checkWin(player, board):
                    print(r, c)
                    return
                board[r][c] = '_'  # Undo move for simulation
    
    # Check for immediate block opportunities for the opponent
    opponent = 'O' if player == 'X' else 'X'
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r][c] = opponent
                if checkWin(opponent, board):
                    print(r, c)
                    board[r][c] = player  # Place our move to block
                    return
                board[r][c] = '_'  # Undo move for simulation
    if board[0][0]==board[2][2]==opponent:
        if board[1][1]==player and board[0][1]=='_':
            print(0,1)
            board[0][1]=player
            return
    if board[0][2]==board[2][0]==opponent:
        if board[1][1]==player and board[0][1]=='_':
            print(0,1)
            board[0][1]=player
            return

    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r][c] = opponent
                f = 0
                for rr in range(3):
                    for cc in range(3):
                        if board[rr][cc] == '_':
                            board[rr][cc] = player
                            if checkWin(opponent, board):
                                f += 1
                            board[rr][cc] = '_'
                if f > 1:
                    print(r, c)
                    return
                board[r][c] = '_'  # Undo move for simulation
    
    # Check for moves that lead to multiple win opportunities (forks)
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r][c] = player
                f = 0
                for rr in range(3):
                    for cc in range(3):
                        if board[rr][cc] == '_':
                            board[rr][cc] = opponent
                            if checkWin(player, board):
                                f += 1
                            board[rr][cc] = '_'
                if f > 1:
                    print(r, c)
                    return
                board[r][c] = '_'  # Undo move for simulation
    
    # Default: Choose the center spot if available
    if board[1][1] == '_':
        print(1, 1)
        return
    
    # Choose a corner spot if center is taken
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for (r, c) in corners:
        if board[r][c] == '_':
            print(r, c)
            return
    
    # Choose a side spot if all corners are taken (should not happen if board is valid)
    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for (r, c) in sides:
        if board[r][c] == '_':
            print(r, c)
            return

def checkWin(player, board):
    # Check rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == player:
            return True
    
    # Check columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

# Example of usage
if _name_ == "_main_":
    player = input().strip()  # Read the current player (X or O)
    board = []
    for _ in range(3):
        board.append(list(input().strip()))  # Read each row of the board as a list of characters
    
    nextMove(player, board)