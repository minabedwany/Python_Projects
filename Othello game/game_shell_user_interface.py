import game_logic

def run():
    print('FULL')
    row_board, column_board = input_column_row()
    turn = first_player_move()
    game_state = game_logic.game_state(row_board, column_board, turn)
    win_way = winning_way()
    initial_content = read_initial_content(row_board)

    current_board = game_state.pieces_start(initial_content)
    game_state.copy_board(current_board)
    print('TURN: {}'.format(game_state.turnn))
    user_interface(game_state,current_board,win_way,row_board,column_board,turn)

def user_interface(game_state,current_board,win_way,row_board,column_board,turn):
    while True:
        game_state.loc_same_color()
        game_state.flipping()

        if win_way == '>':
            if game_state.game_over() == True:
                winner = game_state.winner_most_points()
                print('WINNER:', winner)
                return

        elif win_way == '<':
            if game_state.game_over() == True:
                winner = game_state.winner_least_points()
                print('WINNER:', winner)
                return
 
        try:
            roww, columnn = user_input(row_board,column_board)
            current_board = game_state.make_move(roww,columnn)
            print("VALID")
            game_state.opposite_turn()
            game_state.copy_board(current_board)
            if game_state.game_over() == False:
                print('TURN: {}'.format(game_state.turnn))
        except(game_logic.Invalid_move):
            print("INVALID")


def input_column_row():
       while True:
        row_input = int(input())
        column_input = int(input())
        return (row_input, column_input)
            

def read_initial_content(num_rows) -> list:
    numlines = num_rows
    input_lines = []
    for i in range(numlines):
        input_lines.append(input().split(" "))
        inputs = input_lines


    return inputs

def first_player_move():
    while True:
        first_player = input()
        if first_player == 'B' or first_player == 'W':
            return first_player
        else:
            print("not a valid command for player's turn.")
            
            
def user_input (board_row, board_col):
    while True:
            inputss= ''
            inputss += input()
            list_of_input = inputss.split(' ')
            row_input = int(list_of_input[0]) -1
            column_input = int(list_of_input[1]) -1

            if 0 <= row_input < board_row and 0 <= column_input < board_col:
                return row_input, column_input
            else:
                print("INVALID")

                  
def winning_way():
    while True:
        input_win= input()
        if input_win == '>': 
            return input_win
        elif input_win =='<': 
            return input_win
        
if __name__ == '__main__':
    run()
