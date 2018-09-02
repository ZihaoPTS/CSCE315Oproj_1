import sys
import re
#import readline

players = [];
games = [];

#testying whether variable can be use in dictionary

# players.append({"Name": a, "ID" :1})

# print(players[0]["Name"]);

# input = raw_input("test: ")
# input_seperate = input.split()
# test_dict = {"test_sub":input_seperate[0],"test_sub_2":input_seperate[1]}
# print(test_dict["test_sub"])
# print("\n")
# print(test_dict["test_sub_2"])

flag = 0
while flag == 0:
	input = raw_input("Test: ")
	if input[0].isalpha():
		input_seperate = input.split()
		if input_seperate[0] == "AddPlayer":
			players.append({					\
				"playerID":input_seperate[1],	\
				"playerName":input_seperate[2],	\
				"playerGames":[],				\
				"friends":[],					\
				"points":0 })
		elif input_seperate[0] == "AddGame":
			games.append({"gameID":input_seperate[1],	\
				"gameName":input_seperate[2],			\
				"gameVictory":[],						\
				"gameVictoryN":0})
		elif input_seperate[0] == "AddVictory":
			for i in range(len(games)):
				if games[i]["gameID"] == input_seperate[1]:
					games[i]["gameVictory"].append({	\
						"victoryID":input_seperate[2],	\
						"victoryName":input_seperate[3],\
						"victoryPoints":input_seperate[4] })
					games[i]["gameVictoryN"]+=1
					break
		#Plays <Player ID> <Game ID> <Player IGN>
		elif input_seperate[0] == "Plays":
			gameindex = 0
			for i in range(len(games)):
				if games[i]["gameID"] == input_seperate[2]:
					gameindex = i
					break
			for i in range(len(players)):
				if players[i]["playerID"] == input_seperate[1]:
					players[i]["playerGames"].append(games[gameindex])
					players[i]["playerGames"][len(players[i]	\
						["playerGames"])-1]["victoryGet" : 0]
					players[i]["playerGames"][len(players[i]	\
						["playerGames"])-1]["IGN" : input_seperate[3]]
					break
		# elif input_seperate[0] == "AddFriends":
		
		# elif input_seperate[0] == "WinVictory":
		
		# elif input_seperate[0] == "FriendsWhoPlay":
		
		# elif input_seperate[0] == "ComparePlayers":
		
		# elif input_seperate[0] == "SummarizePlayer":
		
		# elif input_seperate[0] == "SummarizeGame":
		
		# elif input_seperate[0] == "SummarizeVictory":
		
		# elif input_seperate[0] == "VictoryRanking":
		else:
			print("terminating fucntion")
			flag=1
	
		
	
#testing Addplayer
#print(players[0]["playerID"])
#print(players[0]["playerName"])

#print(games[0]["gameVictory"][0]["victoryName"]);

# player suppose to have ID, Name, List of Game(player IGN,achieved/achievement )they played,
# points, and friends(array of ID)
