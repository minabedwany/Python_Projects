import connect_four

def print_board(game: "Gameboard") -> None:
	""" Prints the current state of the game board
	"""

	for col in range(connect_four.BOARD_COLUMNS):
		print(col + 1, end = " ")
	print()

	for row in range(connect_four.BOARD_ROWS):
		for col in range(connect_four.BOARD_COLUMNS):
			if (game[0][col][row] == 1):
				print("R ", end = "")
			elif (game[0][col][row] == 2):
				print("Y ", end = "")
			else:
				print(".","", end = "")
		print()

def print_winner(game: "Gameboard") -> None:
	""" Prints the winner of the current game
	"""

	print("The winner is ", end = "")
	if game[1] == connect_four.RED:
		print("Yellow")
	elif game[1] == connect_four.YELLOW:
		print("Red")

def print_current_player(game: "Gameboard") -> None:
	""" Prints the current player
	"""

	if game[1] == connect_four.RED:
		print("The current player is Red ")
	elif game[1] == connect_four.YELLOW:
		print("The current player is Yellow ")

def is_valid_move(move: str):
	if move.upper().find("DROP") == 0 or move.upper().find("POP") == 0:
		return True
	return False

def make_move(game: "Gameboard", move: str) -> "Gameboard":
	""" Makes a move on the game board
	"""

	if move == None:
		return game
	if connect_four.winner(game) != 0:
		return game
	if move.upper().find("DROP") == 0:
		try:
			game = connect_four.drop(game, int(move.split(" ")[-1]) - 1)
			print_board(game)
		except connect_four.InvalidMoveError:
			print("Invalid move")
		except ValueError:
			print("Invalid move")
		except connect_four.GameOverError:
			print("Game is already over")
		except Exception:
			print("Please enter a valid input")
	elif move.upper().find("POP") == 0:
		try:
			game = connect_four.pop(game, int(move.split(" ")[-1]) - 1)
			print_board(game)
		except connect_four.InvalidMoveError:
			print("Invalid move")
		except ValueError:
			print("Invalid move")
		except connect_four.GameOverError:
			print("Game is already over")
		except Exception:
			print("Please enter a valid input")
	elif move == "INVALID":
		pass
	else:
		print("Please enter if you would like to drop a piece or pop a piece")
	return game
