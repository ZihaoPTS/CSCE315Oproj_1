import sys
import re
#import readline

players = [];
#players contain player
#player ID;player Name;Game played(by an empty [])
#each game is a copy of Game from games, which then contain
#1. Game ID; 2.Game Name 3.points won in this game 4. total # of achievement
#5. # of achievement get so far 6. IGN
games = [];
#games contain 
#Game ID,Game Name,
#Player Played(by an empty [])
#each contain a list of dictionary for game's victoires
#which then contain victories's point, name, ID, and a list 
# that records player who achieved this victory

flag = 0
print("Steam(fake) initialized, please enter your command:")
while flag == 0:
	if sys.stdin.isatty():
		input = sys.stdin.readline()
	else:
		input = raw_input()
	if not input:
		token = 0
	else:
		if input[0].isalpha():
			input_seperate = input.split()
			#AddPlayer <Player ID> <Player Name>
			if input_seperate[0] == "AddPlayer":
				name = re.search('"(.+?)"',input).group(1)
				players.append({					\
					"playerID":input_seperate[1],	\
					"playerName":name,				\
					"playerGames":[],				\
					"friends":[],					\
					"points":0 })
			#AddGame <Game ID> <Game Name>
			elif input_seperate[0] == "AddGame":
				name = re.search('"(.+?)"',input).group(1)
				games.append({"gameID":input_seperate[1],	\
					"gameName":name,			\
					"gameVictory":[],						\
					"victoryGet":0,							\
					"points":0,								\
					"gamePlayer":[],							\
					"IGN":""})
			#AddVictory <Game ID> <Victory ID> <Victory Name> <Victory Points>
			elif input_seperate[0] == "AddVictory":
				name = re.search('"(.+?)"',input).group(1)
				for i in range(len(games)):
					if games[i]["gameID"] == input_seperate[1]:
						games[i]["gameVictory"].append({	\
							"victoryID":input_seperate[2],	\
							"victoryName":name,\
							"victoryPoints":int(input_seperate[len(input_seperate)-1]),\
							"vicotryPlayer":[]})
						break
			#Plays <Player ID> <Game ID> <Player IGN>
			elif input_seperate[0] == "Plays":
				name = re.search('"(.+?)"',input).group(1)
				gameindex = 0
				for i in range(len(games)):
					if games[i]["gameID"] == input_seperate[2]:
						gameindex = i
						games[i]["gamePlayer"].append(input_seperate[1]);
						break
				for i in range(len(players)):
					if players[i]["playerID"] == input_seperate[1]:
						players[i]["playerGames"].append(games[gameindex])
						players[i]["playerGames"][len(players[i]	\
							["playerGames"])-1]["IGN"] = name
						break
			#AddFriends <Player ID1> <Player ID2>
			elif input_seperate[0] == "AddFriends":
				for i in range(len(players)):
					if players[i]["playerID"] == input_seperate[1]:
						players[i]["friends"].append(input_seperate[2])
						break
				for i in range(len(players)):		
					if players[i]["playerID"] == input_seperate[2]:
						players[i]["friends"].append(input_seperate[1])
						break
			#WinVictory <Player ID> <Game ID> <Victory ID>
			elif input_seperate[0] == "WinVictory":
				points_won = 0
				for i in range(len(games)): #seek games
					if games[i]["gameID"] == input_seperate[2]:
						for j in range(len(games[i]["gameVictory"])): #seek victory in games
							if games[i]["gameVictory"][j]["victoryID"] == input_seperate[3]:
								games[i]["gameVictory"][j]["vicotryPlayer"].append(input_seperate[1])
								points_won += games[i]["gameVictory"][j]["victoryPoints"]
								break
						break
				for i in range(len(players)): #seeking player
					if players[i]["playerID"] == input_seperate[1]:
						players[i]["points"] += points_won
						for j in range(len(players[i]["playerGames"])): #seeking game in player
							if players[i]["playerGames"][j]["gameID"] == input_seperate[2]:
								players[i]["playerGames"][j]["victoryGet"]+=1 #increment victory count
								players[i]["playerGames"][j]["points"] += points_won
								break
						break
			#FriendsWhoPlay <Player ID> <Game ID>
			elif input_seperate[0] == "FriendsWhoPlay":
				player_index = 0
				game_index = 0
				friend_list = []
				for i in range(len(players)):#seek player
					if players[i]["playerID"] == input_seperate[1]:
						player_index = i
						break
				print("{0}'s Friend who play this game are:".format(players	\
					[player_index]["playerName"]))
				for i in range(len(games)):#seek game index
					if games[i]["gameID"] == input_seperate[2]:
						game_index = i;
						break
				for i in range(len(players[player_index]["friends"])):
					for j in range(len(games[game_index]["gamePlayer"])):#look up friend's index in players
						if players[player_index]["friends"][i] == games[game_index]["gamePlayer"][j]:
							friend_list.append(games[game_index]["gamePlayer"][j])
							break
				for i in range(len(friend_list)):
					for j in range(len(players)):
						if friend_list[i] == players[j]["playerID"]:
							print("{0}".format(players[j]["playerName"]))
							break
				flag = 1
				print("Terminating Program After report command FriendsWhoPlay Called")
			#ComparePlayers <Player ID1> <Player ID2> <Game ID>
			elif input_seperate[0] == "ComparePlayers":
				player_1_index = 0
				player_2_index = 0
				player_1_g_index = 0
				player_2_g_index = 0
				game_index = 0
				player_1_vic = []
				player_2_vic = []
				for i in range(len(players)):#seek player 1
					if players[i]["playerID"] == input_seperate[1]:
						player_1_index = i;
						break
				for i in range(len(players)):#seek player 2
					if players[i]["playerID"] == input_seperate[2]:
						player_2_index = i;
						break
				for i in range(len(players[player_1_index]["playerGames"])):#seek player 1 game
					if players[player_1_index]["playerGames"][i] == input_seperate[3]:
						player_1_g_index = i;
						break
				for i in range(len(players[player_2_index]["playerGames"])):#seek player 2 game
					if players[player_2_index]["playerGames"][i] == input_seperate[3]:
						player_2_g_index = i;
						break
				for i in range(len(games)):#seek game index
					if games[i]["gameID"] == input_seperate[2]:
						game_index = i;
						break
				for i in range(len(games[game_index]["gameVictory"])):#list out each player's victory
					for j in range(len(games[game_index]["gameVictory"][i]["vicotryPlayer"])):
						if games[game_index]["gameVictory"][i]["vicotryPlayer"][j]	\
							== input_seperate[1]:
							player_1_vic.append(i)
						if games[game_index]["gameVictory"][i]["vicotryPlayer"][j]	\
							== input_seperate[2]:
							player_2_vic.append(i)
				#player 1 :
				print("{0}'s Total point is {1}".format(players[player_1_index]		\
					["playerName"],players[player_1_index]["playerGames"]				\
					[player_1_g_index]["points"]))#print player name & score
				if players[player_1_index]["playerGames"][player_1_g_index]["victoryGet"] != 0:
					print("And here is his/her victories:")
				for i in player_1_vic:#print victoires
					print("{0}".format(games[game_index]["gameVictory"][i]["victoryName"]))
				#player 2 :
				print("{0}'s Total point is {1}".format(players[player_2_index]		\
					["playerName"],players[player_2_index]["playerGames"]				\
					[player_2_g_index]["points"]))#print player name & score
				if players[player_2_index]["playerGames"][player_2_g_index]["victoryGet"] != 0:
					print("And here is his/her victories:")
				for i in player_2_vic:#print victoires
					print("{0}".format(games[game_index]["gameVictory"][i]["victoryName"]))
				#print termination line
				print("Terminating Program After report command ComparePlayers Called")
				flag = 1
			
			#SummarizePlayer <Player ID>
			elif input_seperate[0] == "SummarizePlayer":
				player_index = 0
				friend_list = []
				for i in range(len(players)):#seek player index
					if players[i]["playerID"] == input_seperate[1]:
						player_index = i
						break
				print("{0}'s total point gain so far is {1}".format(players[player_index]	\
					["playerName"],players[player_index]["points"]))
				if len(players[player_index]["friends"])!=0:
					print("{0}'s Friends are:".format(players[player_index]["playerName"]))
					for i in range(len(players[player_index]["friends"])):#look up friend's name in players
						for j in range(len(players)):
							if players[player_index]["friends"][i] == players[j]["playerID"]:
								friend_list.append(players[j]["playerName"])
								break
					for i in range(len(friend_list)):
						print("{0}".format(friend_list[i]))
				else:
					print("{0} have no friends".format(players[player_index]["playerName"]))
				if len(players[player_index]["playerGames"])!= 0 :
					print("{0} played these game(s):".format(players[player_index]["playerName"]))
					for i in range(len(players[player_index]["playerGames"])):
						print("{0}	{1} Victorie(s)	IGN:{2} Points:{3}".format(players[player_index]		\
						["playerGames"][i]["gameName"],players[player_index]["playerGames"][i]["victoryGet"],	\
						players[player_index]["playerGames"][i]["IGN"],players[player_index]["playerGames"]	\
						[i]["points"]))
				else:
					print("{0} played no games".format(players[player_index]["playerName"]))
				print("Terminating Program After report command SummarizePlayer Called")
				flag = 1
			#SummarizeGame <Game ID>
			elif input_seperate[0] == "SummarizeGame":
				game_index = 0
				player_index = []
				for i in range(len(games)):#seek game index
					if games[i]["gameID"] == input_seperate[1]:
						game_index = i
						break
				for i in range(len(games[game_index]["gamePlayer"])):#seek game's player list
					for j in range(len(players)):
						if players[j]["playerID"] == games[game_index]["gamePlayer"][i]:
							player_index.append(j)
							break
				#print out player list
				print("Following players played {0}:".format(games[game_index]["gameName"]))
				for i in player_index:
					print("{0}".format(players[i]["playerName"]))
				#print out victory condition
				print("Victory Sum:")
				for i in range(len(games[game_index]["gameVictory"])):
					print("{0}:{1}".format(games[game_index]["gameVictory"][i]	\
						["victoryName"],len(games[game_index]["gameVictory"][i]	\
						["vicotryPlayer"])))
				print("Terminating Program After report command SummarizeGame Called")
				flag = 1
			#SummarizeVictory <Game ID> <Victory ID>
			elif input_seperate[0] == "SummarizeVictory":
				game_index = 0
				virctory_index = 0
				player_index = []
				for i in range(len(games)):#seek game index
					if games[i]["gameID"] == input_seperate[1]:
						game_index = i
						break
				for i in range(len(games[game_index]["gameVictory"])):#seek victory index
					if games[game_index]["gameVictory"][i]["victoryName"] == input_seperate[2]:
						virctory_index = i
						break
				for i in range(len(games[game_index]["gameVictory"][virctory_index]["vicotryPlayer"])):#seek game's player list
					for j in range(len(players)):
						if players[j]["playerID"] == games[game_index]["gameVictory"][virctory_index]["vicotryPlayer"][i]:
							player_index.append(j)
							break
				print("Following player achieved {0} in {1}:".format(games[game_index]	\
					["gameVictory"][virctory_index]["victoryName"],games[game_index]	\
					["gameName"]))
				for i in player_index:
					print("{0}".format(players[i]["playerName"]))
				percentage = 0
				if len(games[game_index]["gameVictory"][virctory_index]["vicotryPlayer"])!=0:
					percentage = 100.0*float(len(games[game_index]["gamePlayer"]))	\
						/float(len(games[game_index]["gameVictory"][virctory_index]["vicotryPlayer"]))	
				print("{0}% of player achieved this victory".format(str(percentage)));
				print("Terminating Program After report command SummarizeVictory Called")
				flag = 1
			#VictoryRanking
			elif input_seperate[0] == "VictoryRanking":
				player_list = []
				for i in range(len(players)): #creating a list with player's name corresp to their score
					player_list.append({"name":players[i]["playerName"],"points":players[i]["points"]})
				player_list = sorted(player_list,key=lambda k: k["points"],reverse=True)#sorting the list
				for i in range(len(player_list)):#printing the list
					print("#{0}:{1},{2} points".format(i+1,player_list[i]["name"],player_list[i]["points"]))
				print("Terminating Program After report command VictoryRanking Called")
				flag = 1
			else:
				print("Terminating program for bad input")
				flag=1
