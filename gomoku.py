import operator #Required for the tuple addition function to work properly 

def is_empty(board):  #Checks to ensure that at the start of the game the entire board contains only blank spaces
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != " ":
                return False
    return True
    
def is_bounded(board, y_end, x_end, length, d_y, d_x): #Needs to be references by detect rows - checks if the sequence can continue or not
    c = " "
    if board[y_end][x_end] == "b": #Helper function that compares the end colour to the starting colour, if they don't match, then the sequence...
        if (d_x == 1) and (d_y==0): #... is not checked if it is bound, since it is not a valid sequence of that length 
            if board[y_end][x_end-length +1] == "b":
                c = "w"
        if (d_x == 0) and (d_y==1):
            if board[y_end - length + 1][x_end] == "b":
                c = "w"
        if (d_x == 1) and (d_y==1):
            if board[y_end - length + 1][x_end - length + 1] == "b":
                c = "w"
        if (d_x == -1) and (d_y==1):
            if board[y_end - length + 1][x_end + length - 1] == "b":
                c = "w"
    if board[y_end][x_end] == "w":
        if (d_x == 1) and (d_y==0):
            if board[y_end][x_end-length +1] == "w":
                c = "b"
        if (d_x == 0) and (d_y==1):
            if board[y_end - length + 1][x_end] == "w":
                c = "b"
        if (d_x == 1) and (d_y==1):
            if board[y_end - length + 1][x_end - length + 1] == "w":
                c = "b"
        if (d_x == -1) and (d_y==1):
            if board[y_end - length + 1][x_end + length - 1] == "w":
                c = "b"
    if c != " ":
        if (d_x == 1) and (d_y==0): #Checks end case for horizontal 
            if (board[y_end][x_end+1] != " ") and (board[y_end][x_end - length] != " "): 
                return ("CLOSED")
            if (x_end - length < 0) and (board[y_end][x_end + 1] != " "):
                return ("CLOSED")
            if (board[y_end][x_end - length] != " ") and (x_end == 7):
                return ("CLOSED")
            if (board[y_end][x_end-length] == " ") and (board[y_end][x_end + 1] == " "):
                if x_end - length < 0:
                    return ("SEMIOPEN")
                else:
                    return ("OPEN")
            else:
                return ("SEMIOPEN")
        if (d_x == 0) and (d_y == 1): #Checks end case for vertical 
            if (y_end == 7) and (board[y_end - length][x_end] == " "):
                 return ("SEMIOPEN")
            if (board[y_end - length + 1][x_end] != " ") and (board[y_end+1][x_end] != " "): 
                return ("CLOSED")
            if (y_end - length < 0) and (board[y_end+1][x_end] != " "):
                return ("CLOSED")
            if (board[y_end - length][x_end] != " ") and (y_end == 7):
                return ("CLOSED")
            if (board[y_end - length][x_end] == " ") and (board[y_end + 1][x_end] == " "):
                return ("OPEN")
            else:
                return ("SEMIOPEN")
        if (d_x == 1) and (d_y == 1): #Checks case for negative diagonal 
            if (y_end - length < 0) and (x_end == 7):
                return ("CLOSED") 
            if (y_end == 7) and (x_end - length < 0):
                return ("CLOSED")
            if (board[y_end+1][x_end+1] != " ") and (x_end - length < 0):
                return ("CLOSED")
            if (y_end == 7) and (board[y_end - length - 1][x_end - length - 1] != " "):
                return ("CLOSED")
            if (x_end == 7) and (board[y_end - length - 1][x_end - length - 1] != " "):
                return ("CLOSED")
            if (board[y_end+1][x_end+1] != " ") and (y_end - length < 0):
                return ("CLOSED")
            if (board[y_end + 1][x_end + 1] == " ") and (board[y_end - length + 1][x_end - length + 1] == " "):
                return ("OPEN")
            if (board[y_end + 1][x_end + 1] != " ") and (board[y_end - length - 1][x_end - length - 1] != " "):
                return ("CLOSED")
            else:
                return ("SEMIOPEN")
        if (d_x == -1) and (d_y == 1): #Checks case for positive diagonal 
            if (y_end == 7) and (x_end + length > 7):
                return ("CLOSED") 
            if (y_end - length < 0 ) and (x_end == 0):
                return ("CLOSED")
            if (y_end == 7) and (board[y_end - length][x_end + length] != " "):
                return ("CLOSED")
            if (x_end + length > 7) and (board[y_end + 1][x_end - 1] != " "):
                return ("CLOSED")
            if (x_end == 0) and (board[y_end - length][length+1] != " "):
                return ("CLOSED")
            if (y_end - length < 0) and (board[y_end + 1][x_end-1] != " "):
                return ("CLOSED")
            if (board[y_end + 1][x_end - 1] != " ") and (board[y_end - length][x_end + length] != " "):
                return ("CLOSED")
            if (board[y_end + 1][x_end - 1] == " ") and (y_end - length < 0):
                return ("CLOSED")
            if (board[y_end + 1][x_end - 1] == " ") and (x_end + length > 7):
                return ("CLOSED")
            if (board[y_end + 1][x_end - 1] == " ") and (board[y_end - length][x_end + length] == " "):
                return ("OPEN")
            else:
                return ("SEMIOPEN")
            
    
        
def detect_row(board, col, y_start, x_start, length, d_y, d_x): #Checks for the number of open and semi open sequences for a given colour in a given direction
    open_c = 0 # Counters used to record the amount of open, semi open sequences
    semi_c = 0
    hole_c = 0 # Counter used to detect if there are any holes along the length of a sequence - if greater than 1, the sequence is not continous
    if (d_y == 0) and (d_x == 1):
        if x_start + length <= 7:
            if is_bounded(board, y_start, x_start+length-1, length, 0, 1) == "OPEN": #Checks to see if the sequence is open
                for i in range(x_start, x_start + length - 1):
                    if board[y_start][i] != col: #Checks to make sure that the sequence is continous along that length 
                        hole_c += 1
                if hole_c < 1:
                    open_c += 1
            if is_bounded(board, y_start, x_start+length-1, length, 0, 1) == "SEMIOPEN":
                for i in range(x_start, x_start + length - 1):
                    if board[y_start][i] != col:
                        hole_c += 1
                if hole_c < 1:
                    semi_c += 1
    if (d_y == 1) and (d_x == 0): # Checks each direction for every length along a single tile
        if y_start + length <= 7:
            if is_bounded(board, y_start + length-1, x_start, length, 1, 0) == "OPEN":
                for j in range(y_start, y_start + length - 1):
                    if board[j][x_start] != col:
                        hole_c += 1
                if hole_c < 1:
                    open_c += 1
            if is_bounded(board, y_start + length-1, x_start, length, 1, 0) == "SEMIOPEN":
                for j in range(y_start, y_start + length - 1):
                    if board[j][x_start] != col:
                        hole_c += 1
                if hole_c < 1:
                    semi_c += 1
    if (d_y == 1) and (d_x == 1):  
        if (x_start + length <= 7) and (y_start + length <= 7): 
            if is_bounded(board, y_start + length - 1, x_start+length - 1, length, 1, 1) == "OPEN":
                for i in range(x_start, x_start + length - 1):
                    for j in range(y_start, y_start + length -1):
                        if board[j][i] != col:
                            hole_c += 1
                if hole_c < 1:
                    open_c += 1
            if is_bounded(board, y_start + length - 1, x_start+length - 1 , length, 1, 1) == "SEMIOPEN":
                for i in range(x_start, x_start + length - 1):
                    for j in range(y_start, y_start + length -1):
                        if board[j][i] != col:
                            hole_c += 1
                if hole_c < 1:
                    semi_c += 1
    if (d_y == 1) and (d_x == -1):
        if (x_start - length >= 0) and (y_start + length <= 7): 
            if is_bounded(board, y_start + length - 1, x_start-length + 1, length, 1, -1) == "OPEN":
                for i in range(x_start, x_start - length + 1):
                    for j in range(y_start, y_start + length -1):
                        if board[j][i] != col:
                            hole_c += 1
                if hole_c < 1:
                    open_c += 1
            if is_bounded(board, y_start + length - 1, x_start-length + 1, length, 1, -1) == "SEMIOPEN":
                for i in range(x_start, x_start - length + 1):
                    for j in range(y_start, y_start + length -1):
                        if board[j][i] != col:
                            hole_c += 1
                if hole_c < 1:
                    semi_c += 1
    return open_c, semi_c
    
    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length): #sums the amount of open/semi open sequences of a particular direction in the entire board
    s_open = 0
    open = 0
    for i in range(len(board)):
        for j in range(len(board[i])): #The map(operator.add,  allows tuples to be added to each other similar to the method of matrix addition 
            open, s_open = (tuple(map(operator.add, (open, s_open), detect_row(board, col, i, j, length, 0, 1)))) #Adding the positions of the tuples together allows the... 
            open, s_open = (tuple(map(operator.add, (open, s_open), detect_row(board, col, i, j, length, 1, 0)))) #...total amount of open/closed sequences to be computed 
            open, s_open = (tuple(map(operator.add, (open, s_open), detect_row(board, col, i, j, length, 1, 1))))
            open, s_open = (tuple(map(operator.add, (open, s_open), detect_row(board, col, i, j, length, 1, -1))))
    return open, s_open
    
def search_max(board):  #Deterime the location of the best move based on scores from sequences created
    x = 0
    y = 0
    board_copy = []
    temp_score = 0
    for board_copier in board: #Creates deep copy of the board
        board_copy.append(board_copier[:]) #A deep copy of the list is required to prevent entanglement when temporary "b" stones are added to the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                board_copy[i][j] = "b"
                temp_score2 = score(board_copy)
                if temp_score2 >= temp_score: #Compares the score for each square agaist the highest found score at a given position 
                    x = i
                    y = j
                    temp_score = temp_score2
                    board_copy[i][j] = " " # resets the tested position back to blank on the copied board - prevents entanglement 
                else: 
                    board_copy[i][j] = " "
    return x, y
                
def score(board):
    MAX_SCORE = 100000
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    for i in range(2, 6): #Looping through lengths of sequences from 2 to 5
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i) #Adds the amount of each length of each colour sequence to a dictionary 
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
    #Score function is missing the case where it detects a closed bounded row of 5
    if open_b[5] >= 1 or semi_open_b[5] >= 1: #Black wins if a length 5 sequence is found
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1: #White wins if a length 5 sequence is found
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_win(board):  #checks if there are five stones in a row, anywhere in the board
    if (score(board)) <= -100000: 
        return "White won"
    if (score(board)) >= 100000:
        return "Black won"
    for i in range(len(board)):
        for j in range(len(board[i])): #Checks to see if there are open tiles, if there are, the game can continue
            if board[i][j] == " ":
                return "Continue playing"
    else:
        return "Draw" #If there are no open tiles, then the board is a draw

def print_board(board): #Prints the board when required - will show the updated board with the correct postions of stones
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    print(s) #Part of starter code 
    
def make_empty_board(sz): #Creates and empty board of size sz
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                
def analysis(board): #Helper function to display the amout of open, semi open rows for a given length and colour
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);  #Uses dectect_rows to find open and semi open sequences 
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
def play_gomoku(board_size): #Computer will always move first
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    if is_empty(board) == True: #Checks to make sure the board is empty 
        print("Empty")
        
    while True:
        print_board(board)
        if is_empty(board):  #Evaluates if true - computer starts on 4,4 
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board) #Forces program to check where ideal move is
            
        print("Computer move: (%d, %d)" % (move_y, move_x)) #Statement showing computer's move
        board[move_y][move_x] = "b" #Places a b in the location chosen by search max
        print_board(board)
        analysis(board)

        game_res = is_win(board) #Checks to see if black has won after black's turn
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
        print("Your move:")
        move_y = int(input("y coord: ")) #Requests the player choose their next move
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w" #Sets the position of the players move to a white stone
        print_board(board)
        analysis(board) #Computes the number of open and semi open sequences
        
        game_res = is_win(board) #Checks to see if the game has been won after white's turn
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
    
def put_seq_on_board(board, y, x, d_y, d_x, length, col): #Not used in the actual gameplay, used for testing purposes below
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

##Used to tests student created functions - not part of program - Included with the starter code - left incase needed for marking purposes


'''

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    y = 6; x = 0; d_x = 0; d_y = 1; length =2
   # put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    y_end = 7
    x_end = 0
    board[6][0] = "w"
    board[7][0] = "w"
    print_board(board)
   


    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 3; y = 1; d_x = 0; d_y = 1; length = 2
    #put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    board[1][3] = "b"
    #board[3][3] = "b"
    board[2][3] = "b"
    board[4][3] = "b"
    print_board(board)
    if detect_row(board, "b",y,x,length,d_y,d_x) == (1,0):
        print(detect_row(board, "b",y,x,length,d_y,d_x))
        print("TEST CASE for detect_row PASSED")
    else:
        print(detect_row(board, "b",y,x,length,d_y,d_x))
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 0; y = 6; d_x = 0; d_y = 1; length = 2; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    if detect_rows(board, col,length) == (0,1):
        print(detect_rows(board, col,length))
        print("TEST CASE for detect_rows PASSED")
    else:
        print(detect_rows(board, col,length))
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][7] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


 ''' 
            
if __name__ == '__main__':
    play_gomoku(8)   #Specifically told to not print anything, so this will not actually display who won, only return the value, as specified 