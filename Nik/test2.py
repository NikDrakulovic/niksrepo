game = []

import itertools

#horizontal
def win(current_game):
	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	for row in game:
		if all_same(row):
			print(f"Player{row[0]} is the winner horizontally")
			return True

#diag
	diags = []
	for col, row, in zip (cols, rows):
		diags.append(game[row][col])
	if all_same(diags):
		print(f"Player{diags[0]} is the winner diagonally (/)")
		return True

	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if all_same(diags):
		print(f"Player{diags[0]} is the winner diagonally (\\)")
		return True
#vertical
	check = []
	for col in range(len(game)):
		for row in game:
			check.append(row[col])
		if all_same(check):
			print(f"Player{check[0]} is the winner vertically ()")
			return True


def game_board(game_map, player=0, row=0,column=0,just_display=False):
	try:
		if game_map[row][column] != 0:
			print ("This position is occupied! God you are stupid!")
			return game_map, False
		print("   "+"  ".join([str(i) for i in range(len(game_map))]))
		if not just_display:
			game_map [row][column]=player
		for count, row in enumerate(game_map):
			print(count,row)
		return game_map, True

	except IndexError as e:
		print("Error you fuck")
		return game_map, False
	except Exception as e:
		print("Something went wrong u dumb")
		return game_map, False

play = True
players = [1,2]
while play:
	
	game_size = int(input("what size game of tic tav toe dipshit?  "))
	game= [[0 for i in range(game_size)] for i in range(game_size)]

	cols = list(reversed(range(len(game))))
	rows = list(range(len(game)))

	game_won=False
	game, _ = game_board(game,just_display=True)
	player_choice = itertools.cycle([1,2])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current Player: {current_player}")
		played = False

		while not played:
			column_choice=int(input ("what column do you want to play (0,1,2): "))
			row_choice=int(input ("what row do you want to play (0,1,2): "))
			game, played = game_board(game, current_player, row_choice, column_choice)

		if win(game):
			game_won = True
			again = input("The game is over, would you like to play again? (y/n) ")
			if again.lower() == "y":
				print("restarting")
			elif again.lower() == "n":
				print("bye bitch")
				play = False
			else:
				print("not a valid answer dipshit")
				play = False

#game = game_board(game, just_display=True)
#game = game_board(game_board, player=1, row=3, column=1)