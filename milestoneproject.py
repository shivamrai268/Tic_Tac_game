board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]
player_symbol = ["X", "O"]

#count=0
def print_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("--|---|---")
    print(board[3], "|", board[4], "|", board[5])
    print("--|---|---")
    print(board[6], "|", board[7], "|", board[8])


def player_input(player,board):
    #correct_input = True
    position = (input("Player {player} chance! Choose position  {symbol} '1-9' : ".format(player=player + 1,
                                                                                               symbol=player_symbol[
                                                                                                   player])))
    if position == "":
        print("Enter a valid input")
        player_input(player,board)
    else:
        #position=int(position)-1
        position = int(position)
        print("position details: ",position)
        #print("kunl")

        if board[position] == player_symbol[0] or board[position] == player_symbol[1]:
            print("Already full")
            player_input(player,board)

        else:
            board[position] = player_symbol[player]
            print(board[position])
            #print("shivam")


def win(board_win,board,player):
    for i in board_win:
        win_symbol = board[i[0]]
        print("win symbol: ",win_symbol)
        if win_symbol !="":
            won=True
            print("board win data : ",i)
            for j in i:
                #print("board[j] data",board[j])
                if board[j] != win_symbol:
                    won=False
                    break
            if won:
                if win_symbol == player_symbol[0]:

                    print("Player 1 won")
                    #print(print_board())
                    #print("won player win symbol : ",win_symbol)
                else:
                    print("Player 2 won")
                break
        else:
            False


    return won
board_win=[[0, 1, 2],[3, 4, 5],[6, 7, 8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
#win()

#print(win())

player = 0

def Board_check(board):

    #if board["X"]+ board["0"] !=9:
    if board.count(player_symbol[0]) + board.count(player_symbol[1]) !=9 :
        #print(board.count(player_symbol[0]))
        #print(board.count(player_symbol[1]))

        return True
    else:
        #print(False)
        return False

while True:


    iswin = win(board_win,board,player)
    #isfull = Board_check(board)
    isemptyboard=Board_check(board)
    #print("player 1 attempt : {} time".format(board.count(player_symbol[0])))


    if (not iswin) and (isemptyboard):
        print_board(board)
        player_input(player,board)
        player = int(not player)
        #count +=1

        #print_board()
    elif iswin:
        print("congrats you win !!!")
        break
    elif not isemptyboard:
        print("Board full,Match Tie !!!")
        break
#print("count: ",count)


