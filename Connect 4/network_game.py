import connect_four
import client
import move_methods

def play_online() -> None:
	""" Starts and plays an online game
	"""
	try:
		connection = client.start_network_game()
		if connection == None:
			return
	except:
		print("Not a valid address or port, exiting program")
		return
	game = connect_four.new_game()
	move_methods.print_board(game)

	while connect_four.winner(game) == 0:
		move_methods.print_current_player(game)
		player_move = input("Send: ")
		game = move_methods.make_move(game, player_move)
		if move_methods.is_valid_move(player_move):
			client.send_message(connection, player_move.upper())
		else:
			continue
		server_move = client.receive_messages(connection)
		if server_move == None:
			print("Unexpected server response, closing connection")
			client.close(connection)
			return
		elif server_move.find("WINNER") > -1:
			move_methods.make_move(game, server_move[:server_move.find("WINNER")])
			print(server_move[server_move.find("WINNER"):])
			break
		else:	
			game = move_methods.make_move(game, server_move)

	client.close(connection)

if __name__ == "__main__":
	play_online()
