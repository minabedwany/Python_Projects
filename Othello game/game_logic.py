
Black_player= 'B'
White_player= 'W'
none='.'

all_directions=[[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

class Invalid_move(Exception):
    pass

class gameover_error(Exception):
    pass

class game_state:

    def __init__(self,column,row,turn:'B or W'):
        self.board_row = row
        self.board_column = column
        self.turnn = turn
        self.valid=[]
        self.board =[]


    def pieces_start(self, lst) -> list:

        self.board.extend(lst)
        return self.board
    

    def print_board(self):
        print('B: {}  W: {}'.format(self.black_score, self.white_score))
    
        for x in range(0, self.board_row):
            for i in self.board[x]:
                print(i, end = ' ')
            print()

    

    def copy_board(self, current_board):
        board_copy=[]
        for row in range(self.board_row):
            board_copy.append([])
            for column in range(self.board_column):
                board_copy[-1].append(current_board[row][column])
        self.black_score,self.white_score = self.total_score()
        self.print_board()
        return board_copy





    def opposite_turn(self):
        if self.turnn == Black_player:
            self.turnn = White_player
        elif self.turnn == White_player:
            self.turnn = Black_player
            return self.turnn



    def loc_same_color(self):
        self.location_list=[]
        for row in range(0, self.board_row):
            for column in range(0, self.board_column):
                if self.board[row][column]== self.turnn:
                    self.location_list.append([row, column])
        return self.location_list


    def change_player(self):
        self.other_piece= White_player
        if self.turnn == Black_player:
            self.other_piece = White_player
        elif self.turnn == White_player:
            self.other_piece = Black_player
        return self.other_piece
    

    def flipping(self):
        adjacent_list =[]
        self.piece_flip_list=[]
        self.valid=[]
        self.other_piece = self.change_player()
        
        for xdirection, ydirection in all_directions:
            for each_spot in self.location_list:
                self.adjacent_row = each_spot[0] + xdirection
                self.adjacent_column = each_spot[1] + ydirection
                if self.valid_position(self.adjacent_row,self.adjacent_column) and self.board[self.adjacent_row][self.adjacent_column] == self.other_piece:
                    adjacent_list.append([self.adjacent_row, self.adjacent_column])

                    while self.board[self.adjacent_row][self.adjacent_column] == self.other_piece:
                        
                        self.adjacent_row = self.adjacent_row + xdirection
                        self.adjacent_column = self.adjacent_column + ydirection
                        if not self.valid_position(self.adjacent_row,self.adjacent_column): 
                            break

                        if self.valid_position(self.adjacent_row,self.adjacent_column):
                            if self.board[self.adjacent_row][self.adjacent_column] == none: 
                                self.valid.append([self.adjacent_row,self.adjacent_column])
                                
                            elif self.board[self.adjacent_row][self.adjacent_column] == self.turnn:
                                while True:
                                    self.adjacent_row = self.adjacent_row - xdirection
                                    self.adjacent_column = self.adjacent_column - ydirection
                                    if self.board[self.adjacent_row][self.adjacent_column] == self.turnn:
                                        break
                                    self.piece_flip_list.append([self.adjacent_row,self.adjacent_column])


  
    def make_move(self,row_select,column_select):        
        while True:
            if [row_select ,column_select] not in self.valid:
                raise Invalid_move
            elif [row_select ,column_select] in self.valid:
                self.board[row_select][column_select] = self.turnn
                self.flipping()
                current_board = self.flip_pieces()
                return current_board
            
    def valid_position(self,row_select,column_select):
        return 0 <= row_select < self.board_row and 0 <= column_select < self.board_column



    def flip_pieces (self):
        for pieces in self.piece_flip_list:
            self.board[pieces[0]][pieces[1]] = self.turnn
        return self.board

    def total_score(self):
        total_score_black= 0
        total_score_white= 0
        for row in range(int(self.board_row)):
            for column in range(int(self.board_column)):
                if self.board[row][column] == Black_player:
                    total_score_black += 1
                elif self.board[row][column] == White_player:
                    total_score_white += 1
        return (total_score_black,total_score_white)


    def game_over(self):
        x = len(self.valid)
        if x == 0:
            return True
        elif x > 0 :
            return False

    def winner_least_points(self):
        winner=Black_player
        if self.game_over():
            if self.black_score > self.white_score:
                winner = White_player
            elif self.white_score > self.black_score:
                winner = Black_player
            elif self.white_score == self.black_score:
                winner = "NONE"
        return winner

    def winner_most_points(self):
        winner= Black_player
        if self.game_over():
            if self.black_score > self.white_score:
                winner = Black_player
            elif self.white_score > self.black_score:
                winner = White_player
            elif self.white_score == self.black_score:
                winner = "NONE"
        return winner




