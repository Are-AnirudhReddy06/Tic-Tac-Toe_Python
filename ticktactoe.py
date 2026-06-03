# tic tac toe game with AI

# whos playing
player = 'X'   # thats me
computer = 'O'  # thats the AI
blank = ' '


# this just shows the board on screen
def show_board(board):
    print("")
    print("", board[0], "|", board[1], "|", board[2])
    print(" --|---|--")
    print("", board[3], "|", board[4], "|", board[5])
    print(" --|---|--")
    print("", board[6], "|", board[7], "|", board[8])
    print("")


# checks if someone won
def check_winner(board, who):
    # check all the rows first
    if board[0] == who and board[1] == who and board[2] == who:
        return True
    if board[3] == who and board[4] == who and board[5] == who:
        return True
    if board[6] == who and board[7] == who and board[8] == who:
        return True

    # now columns
    if board[0] == who and board[3] == who and board[6] == who:
        return True
    if board[1] == who and board[4] == who and board[7] == who:
        return True
    if board[2] == who and board[5] == who and board[8] == who:
        return True

    # diagonals (the ones going corner to corner)
    if board[0] == who and board[4] == who and board[8] == who:
        return True
    if board[2] == who and board[4] == who and board[6] == who:
        return True

    # nobody won yet
    return False


# see if the board is full and no more moves
def board_is_full(board):
    full = True
    for i in range(9):
        if board[i] == blank:
            full = False  # found an empty spot so not full
    return full


# this is the minimax thing, it looks at all possible moves
# i dont fully understand it but it works 
def minimax(board, depth, my_turn):

    # if computer won give it a good score
    if check_winner(board, computer) == True:
        return 10 - depth

    # if i won give a bad score (bad for computer)
    if check_winner(board, player) == True:
        return depth - 10

    # nobody won and board is full = draw
    if board_is_full(board) == True:
        return 0

    if my_turn == True:
        # computer is trying to get highest score
        best = -1000  # start very low

        for i in range(9):
            if board[i] == blank:
                board[i] = computer  # try putting O here
                score = minimax(board, depth + 1, False)
                board[i] = blank  # put it back
                if score > best:
                    best = score

        return best

    else:
        # player is trying to get lowest score (bad for computer)
        best = 1000  # start very high

        for i in range(9):
            if board[i] == blank:
                board[i] = player  # try putting X here
                score = minimax(board, depth + 1, True)
                board[i] = blank  # undo it
                if score < best:
                    best = score

        return best


# figure out which square is best for the computer to play
def get_computer_move(board):
    best_score = -1000
    best_spot = -1  # -1 means we havent found anything yet

    # try every empty square
    for i in range(9):
        if board[i] == blank:
            board[i] = computer
            this_score = minimax(board, 0, False)
            board[i] = blank  # undo


            if this_score > best_score:
                best_score = this_score
                best_spot = i

    return best_spot


# main game starts here
def main():

    # make the empty board (9 spots, all blank)
    board = [blank, blank, blank, blank, blank, blank, blank, blank, blank]

    print("============================")
    print("   TIC TAC TOE vs AI")
    print("============================")
    print("you are X the computer is O")
    print("pick a number 1-9 to play")
    print("")

    # show numbered board so player knows what number = what spot
    show_board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    game_over = False

    while game_over == False:

        # players turn
        got_valid_move = False
        while got_valid_move == False:
            try:
                user_input = input("your move (1-9): ")
                move = int(user_input)
                move = move - 1  # convert to 0-8 for the list

                if move >= 0 and move <= 8:
                    if board[move] == blank:
                        board[move] = player
                        got_valid_move = True
                    else:
                        print("that spot is taken!! try another")
                else:
                    print("number must be between 1 and 9")
            except:
                print("thats not a number, please type a number")

        show_board(board)

        # check if player won 
        if check_winner(board, player) == True:
            print("wait you actually won??? that shouldnt happen")
            game_over = True
            break

        if board_is_full(board) == True:
            print("its a draw!!")
            game_over = True
            break

        # Computers turn
        print("computer is thinking...")

        ai_spot = get_computer_move(board)
        board[ai_spot] = computer
        print("computer played spot", ai_spot + 1)  # +1 so it shows 1-9 not 0-8

        show_board(board)

        if check_winner(board, computer) == True:
            print("computer wins... you lose sorry")
            game_over = True
            break

        if board_is_full(board) == True:
            print("its a draw!!")
            game_over = True
            break


# run it
main()