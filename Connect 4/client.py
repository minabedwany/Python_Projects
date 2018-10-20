import socket

################ MESSAGE HANDLING ############################
def _read_host() -> str:
	""" Asks the user what host they want to connect to.
	"""

	while True:
		host = input("Host: ").strip()

		if host == "":
			print("That is not a valied host; please try again")
		else:
			return host


def _read_port() -> int:
	""" Asks the user for the port
	"""

	while True:
		try:
			port = (int)(input("Port: "))

			if port < 0 or port > 65535:
				print("Ports are integers from 0-65535, please try again")
			else:
				return port
		except ValueError:
			print("Ports are integers from 0-65535, please try again")

def _print_response(resp: str) -> None:
	""" Prints a response from a string
	"""

	print("Response:", resp)

def _check_username_response(response: str, name: str) -> bool:
	return response.find("WELCOME " + name) == 0

def _check_server_response(resp: str) -> bool:
	if (resp.find("DROP") == 0 or resp.find("POP") == 0
		or resp.find("OKAY") == 0 or resp.find("READY") == 0
		or resp.find("WINNER_YELLOW") == 0 or resp.find("INVALID") == 0):
		return True
	return False

def _check_user_name(name: str) -> bool:
	return (name == "" or name.find(" ") >= 0
		or name.find("\t") >= 0 or name.find("\n") >= 0
		or name.find("\r") >= 0)

################# ONLINE ##################################

def _connect(host: str, port:int) -> 'Connection':
	""" Connects to the host and port given through the arguments
	"""

	echo_socket = socket.socket()
	echo_socket.connect((host, port))

	echo_socket_in = echo_socket.makefile("r")
	echo_socket_out = echo_socket.makefile("w")
	
	return echo_socket, echo_socket_in, echo_socket_out


def close(connection: "Connection") -> None:
	""" Closes the connection between a client and server
	"""

	echo_socket, echo_socket_in, echo_socket_out = connection

	echo_socket.close()
	echo_socket_in.close()
	echo_socket_out.close()


def send_message(connection: "Connection", message:str) -> None:
	""" Sends a message to the server from the client
	"""

	echo_socket, echo_socket_in, echo_socket_out = connection

	echo_socket_out.write(message + "\r\n")
	echo_socket_out.flush()


def _receive_response(connection: 'Connection') -> str:
	""" Receives the response from a server
	"""

	echo_socket, echo_socket_in, echo_socket_out = connection

	return echo_socket_in.readline()[:-1]


def start_network_game() -> "Connection":
	""" Starts a game with the UCI network against an AI
	"""

	choice = input("Do you want to connect to the UCI network? Y/N\n")
	if choice.upper() == "Y":
		host = "woodhouse.ics.uci.edu"
		port = 4444
	else:
		host = _read_host()
		port = _read_port()

	print("Connecting to {} on port {}...".format(host, port))
	connection = _connect(host, port)

	username = input("Enter a username: ").strip()
	while _check_user_name(username):
		username = input("Invalid username, try again: ").strip()
	send_message(connection, "I32CFSP_HELLO " + username)

	response = _receive_response(connection)
	if not _check_username_response(response, username):
		print("Unexpected response (username), exiting now")
		connection.close()
		return None
	_print_response(response)
	print("Starting game...")
	send_message(connection, "AI_GAME")
	_print_response(_receive_response(connection))

	return connection

def receive_messages(connection: "Connection") -> str:
	""" Receives the moves that the server makes
	"""

	response = _receive_response(connection)
	_print_response(response)
	if (not _check_server_response(response)):
		return None
	result = None
	while response.upper() != "READY" or response == "":
		if response.upper().find("DROP") == 0 or response.upper().find("POP") == 0:
			result = response
		elif response.find("WINNER") == 0:
			result += response
			break
		elif response == "INVALID":
			result = response
		response = _receive_response(connection)
		_print_response(response)
		if (not _check_server_response(response)):
			return None
	return result

def send_move(connection: "Connection", move: str) -> None:
	""" Sends a move to the server if it is valied
	"""
	if move.upper().find("DROP") != 0 or move.upper().find("POP") != 0:
		print("INVALID MOVE")
	else:
		send_message(connection, move)


if __name__ == "__main__":
	username = input("Enter a username: ").strip()
	while _check_user_name(username):
		username = input("Enter a valid username: ").strip()
	print(username)