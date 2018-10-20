# Mina Bedwany  

import tkinter
import game_logic

NONE = '.'
Black = 'B'
White = 'W'

FONT = ('Helvetica', 14)



class OthelloApplication:
    def __init__(self):

        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = 'purple')
        
        self._canvas.grid(
            row = 1, column = 0, rowspan = 3, columnspan = 3, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        
        self._root_window.bind('<Return>', self.specs)
        self._canvas.bind('<Configure>', self.on_canvas_resized)
        self._canvas.bind('<Button-3>',self.on_canvas_right_clicked)


        #self.button_pressed = False
        #if self.button_pressed == True:
        self._canvas.bind('<Button-1>', self.when_canvas_clicked)
        #if self.button_pressed == False:
        self._canvas.bind('<Button-1>', self.on_canvas_clicked)


        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)

        self._NONE = []
        self._BLACK = []
        self._WHITE = []


        self._board = []
        self.new_board = []

        self._current_turn = tkinter.StringVar()
        self._disc_count = tkinter.StringVar()

        self._input_box = tkinter.Entry(master= self._root_window,font= FONT)
        self._input_box.grid(row= 1, column=1,sticky= tkinter.E)

        self._input_instructions = tkinter.StringVar()
        self._input_instructions.set("Enter Row between 4-16 ---> \n then click here")

        self._game_initial_inputs = []
        self._counter = 0


        self._button = tkinter.Button(master = self._root_window, textvariable= self._input_instructions,
                                      command= self.specs,
                                      font= FONT)
        self._button.grid(row=1,column=0,sticky=tkinter.W)

        
##    def color_switch(self, event: tkinter.Event):
##
##        if event.char == 'b':
##            self.color = 'Black'
##        if event.char == 'w':
##            self.color = 'White'
##        #print(event.char)
##        return self.color

    def begin_button(self):
        self.begin_buttonn =  tkinter.Button(
            master = self._root_window,
            text = 'BEGIN', font = FONT,
            command= self.start_game)

        
        self.begin_buttonn.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.N)
        self.lines(int(self._game_initial_inputs[0]), int(self._game_initial_inputs[1]))
        self.shapes()

    def start_game(self):
        #self.button_pressed == True
        lst = self.return_newboard()
        self.make_board()
 
        self.make_discs()
        self.lines(int(self._game_initial_inputs[0]), int(self._game_initial_inputs[1]))

        self.score_turn()


    def when_canvas_clicked(self, event: tkinter.Event):
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        inputs = self._game_initial_inputs

        x = 1/ int(inputs[1])
        y = 1/ int(inputs[0])

        col_frac = event.x /width
        row_frac = event.y /height

        col = round(col_frac/x - 0.5)
        row = round(row_frac/y - 0.5)


        if self.return_newboard() in self._game.valid:
        #if valid == True :
            self._game.make_move([row,col])
            self.make_discs()
            self.shapes()
            self.score_turn_new()
            self._game.turnn = self._game.change_player()
            

        

    def new_list(self):

        num_rows = int(self._game_initial_inputs[0])
        num_cols = int(self._game_initial_inputs[1])
        
        for i in range(num_rows):
            self._board.append([])
            for j in range(num_cols):
                self._board[-1].append(NONE)

    def on_canvas_resized(self, event: tkinter.Event) -> None:
        self.redraw()

    def redraw(self):
        self._canvas.delete(tkinter.ALL)
        self.lines(int(self._game_initial_inputs[0]), int(self._game_initial_inputs[1]))
        self.shapes()
        
    def on_canvas_clicked(self, event:tkinter.Event):
        self._canvas_clicked = True
        self.x_loc = event.x
        self.y_loc = event.y

        num_rows = int(self._game_initial_inputs[0])
        num_cols = int(self._game_initial_inputs[1])

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        row = int((self.y_loc/height)*num_rows)
        col = int((self.x_loc/width)*num_cols)
        self.discs(row, col, num_rows, num_cols, 'Black')
        
        self.new_board.extend(self._board)
        
        self.new_board[row][col] = Black

    def return_newboard(self):
        return self.new_board

    def on_canvas_right_clicked(self, event:tkinter.Event):
        self._canvas_clicked = True
        self.x_loc = event.x
        self.y_loc = event.y

        num_rows = int(self._game_initial_inputs[0])
        num_cols = int(self._game_initial_inputs[1])

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        row = int((self.y_loc/height)*num_rows)
        col = int((self.x_loc/width)*num_cols)
        self.discs(row, col, num_rows, num_cols, 'White')

        self.new_board = []
        self.new_board.extend(self._board)


        self.new_board[row][col] = White

    def specs(self):

        conditions = ["Enter Column between 4-16 ---> \n then click here", "Enter who goes first (B or W) ---> \n then click here", "Enter Win method (> or <) ---> \n then click here ",""]
        user_inputs = self._input_box.get()
        self._game_initial_inputs.append(user_inputs)
        self._input_box.delete(0, 'end')
        self._input_instructions.set(conditions[self._counter])
        self._counter += 1
        if self._counter > 3:
            self._root_window.unbind('<Return>')
            self._input_box.grid_forget()
            self._button.grid_forget()

            self.lines(int(self._game_initial_inputs[0]), int(self._game_initial_inputs[1]))
            self.shapes()

            self.begin_button()
            self._dialog_window = tkinter.Toplevel()
            self.label = tkinter.Label(
                master = self._dialog_window, text = 'Enter initial content of the game: Left click for Black disks; Right click for White disks; Then click BEGIN to start game',
                font = FONT)
            self.label.grid(row=0, column=0, columnspan = 2, padx = 10, pady = 10,
                sticky = tkinter.N)
            self.shapes()
            self.lines(int(self._game_initial_inputs[0]), int(self._game_initial_inputs[1]))
            self.logic()
            self.new_list()


    def logic(self):

        inputs = self._game_initial_inputs
        self._game = game_logic.game_state(inputs[1], inputs[0], inputs[2])

    def make_board(self):

        inputs = self._game_initial_inputs
        col = 1/ int(inputs[1])
        row = 1/ int(inputs[0])
        for roww in range(int(inputs[0])):
            for column in range(int(inputs[1])):
                box = [col*column, row*roww, col*(column+1), row*(roww+1)]
                self._NONE.append(box)

    def make_discs(self):

        self._BLACK = []
        self._WHITE = []
        inputs = self._game_initial_inputs
        self._game = game_logic.game_state(inputs[1], inputs[0], inputs[2])

        col = 1/ int(inputs[1])
        row = 1/ int(inputs[0])

        convert_row = row/ 10
        convert_column = col/ 10
        self._game.board = self._game.pieces_start((self.return_newboard()))
        for roww in range(int(inputs[0])):
            for column in range(int(inputs[1])):
                result = [col*column + convert_column, row*roww + convert_row, col*(column+1) -convert_column, row*(roww+1) -convert_row]
                if self._game.board[roww][column] == "B":
                    self._BLACK.append(result)
                elif self._game.board[roww][column] == "W":
                    self._WHITE.append(result)



        
    def score_turn_new(self):

        self._current_turn.set(self._game.change_player())
        self._disc_count.set(self._game.total_score())

    def lines(self, num_row, num_col):
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        for row in range(num_row):
            x1 = 0
            y1 = (row*height)/num_row
            x2 = width
            y2 = y1

            self._canvas.create_line(x1, y1, x2, y2, fill = 'Yellow')

        for column in range(num_col):
            x1 = (column*width)/num_col
            y1 = 0
            x2 = x1
            y2 = height

            self._canvas.create_line(x1, y1, x2, y2, fill = 'Yellow')



    def discs(self, row, col, num_rows, num_cols, player):
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        row_height = height / num_rows
        col_width = width / num_cols
        
        frac_rad = 0.9

        x0 = (col + (1 - frac_rad)) * col_width
        y0 = (row + (1 - frac_rad)) * row_height
        x1 = (col + frac_rad) * col_width
        y1 = (row + frac_rad) * row_height



        self._canvas.create_oval(x0, y0, x1, y1, fill = player)

    def shapes(self):

        self._canvas.delete(tkinter.ALL)
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        for item in self._NONE:
            self._canvas.create_rectangle(obj[0]*width, obj[1]*height, obj[2]*width, obj[3]*height, outline= 'Yellow')
        for item in self._BLACK:
            self._canvas.create_oval(obj[0]*width, obj[1]*height, obj[2]*width, obj[3]*height, fill= 'Black')
        for item in self._WHITE:
            self._canvas.create_oval(obj[0]*width, obj[1]*height, obj[2]*width, obj[3]*height, fill= 'White')


    def score_turn(self):

        self._current_turn.set("Turn: " + self._game.turnn)
        self._turn_print =  tkinter.Label(master = self._root_window, textvariable = self._current_turn, font = FONT)
        self._turn_print.grid(row = 0, column = 0)

        self.display_score = "B: "+str(self._game.total_score()[0])+ "   W: " + str(self._game.total_score()[1])

        self._disc_count.set(self.display_score)
        self._count_print = tkinter.Label(master = self._root_window, textvariable = self._disc_count, font = FONT)
        self._count_print.grid(row = 0, column = 1)
        

    def run(self) -> None:
        self._root_window.mainloop()


if __name__ == '__main__':
    OthelloApplication().run()
