# Mina Bedwany

import connect_four
import client
import move_methods

def play_local() -> None:
	""" Starts and plays a local game
	"""

	game = connect_four.new_game()
	move_methods.print_board(game)
	while connect_four.winner(game) == 0:
		game = move_methods.make_move(game, input("Make your move\n"))
	move_methods.print_winner(game)


if __name__ == "__main__":
	play_local()