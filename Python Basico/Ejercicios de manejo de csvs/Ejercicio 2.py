import csv

def populate_game_list ():
	game_limit = int(input("How many games would you like to enter?"))
	video_games_list = []
	for number_of_games in range(game_limit):
		current_game_list = {}
		current_game_list['game_name'] = input("Enter the name of the game:")
		current_game_list['game_genre'] = input("Enter the genre of the game:")
		current_game_list['game_developer'] = input("Enter the name of the game developer:")
		current_game_list['game_classification'] = input("Enter the ESRB classification for the game:")

		video_games_list.append(current_game_list)

	return video_games_list


def write_csv_file(file_path, data):
	headers = data[0].keys()
	with open(file_path, 'w', encoding='utf-8') as file:
		writer = csv.DictWriter(file, headers,delimiter='\t')
		writer.writeheader()
		writer.writerows(data)


game_collection = populate_game_list()
write_csv_file('videogameslist.csv', game_collection)