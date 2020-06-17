import socket
import pickle
import time
import sys
import random
from _thread import *

questions = [("Which team play at Anfield?\n a) Manchester City  b) Aston Villa  c) Liverpool  d) Everton", "c"),("Which English Premier side are known as The Red Devils?\n a) Arsenal  b) Newcastle United  c) Manchester United  d) Chelsea", "c"),("How many lions are on the England badge?\n a) 1  b) 2  c) 3  d) 0", "c"),("Which international club does Paul Pogba play for?\n a) England  b) Brazil  c) France  d) Wales","c"),("England have won the World Cup once. But in which year did they lift the trophy?\n a) 1966  b) 2000  c) 1994  d) 1982","a"),("How long is a game of professional football?\n a) 60 Min  b) 75 Min  c) 45 Min  d) 90 Min","d"),("What happens if a referee shows a player a red card?\n a) They get sent off the pitch  b) They have to do 10 laps of the ground  c) The other team automatically scores a goal  d) They get detention after the game","a"),("How many players of a team are allowed on pitch at any time?\n a) 9  b) 11  c) 15  d) 13","b"),("Who is the current captain of the English women's national team?\n a) Steph Houghton  b) Casey Stoney  c) Fara Williams  d) Toni Duggan","a"),("Which Premier League team are famous for wearing black and white stripes?\n a) Tottenhum Hotspur  b) Crystal Palace  c) Newcastle United  d) Everton","c"),("What kind of animal is featured on Leicester City's badge?\n a) Cat  b) Dog  c) Fox  d) Wolf","c"),("Which England legend is married to Victoria Beckham?\n a) Keith Beckham  b) Sam Beckham  c) David Beckham  d) Stormzy","c"),("How many times have Brazil won the World Cup?\n a) 0  b) 2  c) 3  d) 5","d"),("Which club won the Scottish Premiership in 2017?\n a) Rangers  b) Celtic  c) Motherwell  d) Kilmarnock","b"),("Which team does Harry Kane play for?\n a) Arsenal  b) Derby County  c) Tottenhum Hotspur  d) Birmingham City","c"),("Which team are nicknamed The Canaries?\n a) Norwich City  b) Liverpool  c) Brighton and Hove Albion  d) Celtic","a"),("Which Scottish team has a goal on their club badge?\n a) Celtic  b) Rangers  c) Heart of Midlothian  d) Aberdeen","d"),("Who is currently the English women's national team's most capped player?\n a) Fara Williams  b) Jill Scott  c) Jodie Taylor  d) Isobel Christiansen","a"),("How many teams play in the FIFA World Cup?\n a) 32  b) 16  c) 28  d) 12","a"),("Which football star is on the cover of the FIFA 18 game?\n a) Rooney  b) Ronaldo  c) Pogba  d) Messi","b"),("How many teams have won the World Cup since its inception in 1930?\n a) 8  b) 7  c) 5  d) 4","a"),("Brazil has the most number of World Cup titles to its credit. How many times has it won the World Cup so far?\n a) 5  b) 4  c) 6  d) 7","a"),("In which year was the football World Cup held for the first time?\n a) 1928  b) 1930  c) 1924  d) 1932","b"),(" Which country won the first football World Cup?\n a) Brazil  b) Germany  c) Uruguay  d) Argentina","c"),("Paul, a marine creature, which supposedly predicted the outcome of many matches in World Cup 2010 was?\n a) Jelly Fish  b) Walrus  c) Octopus  d) Seal","c"),("In which country is FIFA World Cup 2018 scheduled to be played?\n a) Qatar  b) Russia  c) South Korea  d) France","b"),(" To which country does the famous player Ronaldo, who held the record for most number of World Cup goals, belong?\n a) France  b) Spain  c) Portugal  d) Brazil","d"),("In which country are the headquarters of FIFA (International Federation of Association Football) located?\n a) Switzerland  b) Brazil  c) France  d) Netherlands","a"),("Who has the record for scoring the most goals in World Cup history?\n a) Ronaldo  b) Maradona  c) Miroslav Klose  d) Messi","c"),("Which trophy was awarded to the winners of World Cup tournament until 1970?\n a) Arsenal Trophy  b) Heisman Trophy  c) Grondona Cup  d) Jules Rimet Trophy","d"),("What kind of animal was Zabivaka, the mascot for FIFA World Cup 2018?\n a) Tiger  b) Cat  c) Polar Bear  d) Wolf","d"),("Who of the following was awarded the Golden Ball or the Best Player Award at the 2018 FIFA World Cup?\n a) Modric  b) Kane  c) Lukaku  d) Ronaldo","a"),("In which year did France win the World Cup earlier?\n a) 1994  b) 1998  c) 2002  d) 2004","b"),("Thibaut Courtois who was awarded the Golden Glove award for the best goalkeeper at the World Cup 2018 is from which country?\n a) Croatia  b) France  c) England  d) Belgium","d"),("Who was the captain of the 2018 World Cup winning team of France?\n a) Lioris  b) Pogba  c) Mbappe  d) Griezmann","a"),("From which confederation did the most number of teams qualify for the World Cup 2018 final 32?\n a) CONCACAF  b) CONMEBOL  c) UEFA  d) CAF","c"),("Who of the following players scored a hat-trick of goals in the World Cup 2018?\n a) Ronaldo  b) Kane  c) Both  d) None","c"),("Luzhniki Stadium which hosted the opening and closing ceremonies in World Cup 2018 is located in which city?\n a) Moscow  b) Volgograd  c) Saint Petersburg  d) Sochi","a"),("Which team was awarded the FIFA Fair Play Award at the World Cup 2018 tournament?\n a) England  b) Japan  c) Spain  d) Croatia","c"),("Which of the following was the official song of the FIFA World Cup 2018?\n a) All in One Rhythm  b) Live it up  c) Go for it  d) Football in Space","b"),("What name has been given to the special font typeface designed by Brandia Central for writing the official logo Russia 2018 of FIFA World Cup 2018?\n a) Kremlin  b) Molot  c) Troika  d) Dusha","d"),("What name was given to the football used for the final match between France and Croatia at the FIFA World Cup 2018?\n a) Telstar Elast  b) Telstar Durlast c) Telstar Mechta d) Telstar Plast","c"),("Which team scored the highest number of goals at the FIFA World Cup 2018?\n a) Belgium  b) France  c) England  d) Croatia","a"),("Who of the following was the manager of the French team at the FIFA World Cup 2018 as well as the captain of the team which won the World Cup in 1998?\n a) Ricardo Gareca  b) Didier Deschamps c) Fernando Hierro d) Juan Carlo Osorio","b"),("Who was selected for the Man of the Match Award in the finals of World Cup 2018?\n a) Griezmann  b) Mbappe  c) Pogba  d) Varane","a"),("How much was the prize money awarded to the World Cup winning team France at the tournament?\n a) $22M  b) $26M  c) $32M  d) $38M","d"),("Who of the following became the second teenager in the history of World Cup football to score a goal in the finals?\n a) Griezmann  b) Mbappe  c) Pogba  d) Varane","b"),(" What kind of animal was Fuleco, the mascot for FIFA World Cup 2014?\n a) Giant Anteater  b) Alpaca  c) Armadillo  d) Otter","c"),(" Who of the following was awarded the Golden Ball or the Best Player Award at the 2014 FIFA World Cup?\n a) Pogba  b) Messi  c) Neymar  d) Gotze","b")]
random.shuffle(questions)

boolean = [False, False, False]

whoPressedBuzz = -1

clients_list = []

score = [0,0,0]

help1 = 0
help2 = 0

class Player():
	def __init__(self, id):
		self.score = 0
		self.id = id
		self.isBuzzerPressed = False
		self.whoPressedBuzzer = id
		self.isPlayerReady = False
		self.isGameReady = False


server = str(sys.argv[1])
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))

except socket.error as e:
	print(e)

s.listen(100)
print("Waiting for Connections, Server has started")

players = [Player(0), Player(1), Player(2)]

def client_thread(conn, current_player):

	conn.send(pickle.dumps(players[current_player]))

	MakeAllReady(conn)

	reply = ""

	Quiz(conn, players[current_player].id)
	conn.close()
	sys.exit()


def MakeAllReady(conn):
	while True:
		try:
			player = pickle.loads(conn.recv(2048))

			if player.isPlayerReady:
				boolean[player.id] = True
				print("Player {} is ready".format(player.id+1))
				conn.send(pickle.dumps(player))
				break

		except:
			pass

	while True:
		try:
			if boolean == [True, True, True]:
				player.isGameReady = True
				print("EVERY PLAYER READY")
				conn.send(pickle.dumps(player))
				break

			conn.send(pickle.dumps(player))

		except:
			pass


def Quiz(conn, player_id):
	global score
	for question in questions:
		if score[0] < 5 and score[1] < 5 and score[2] < 5:
			global whoPressedBuzz
			
			time.sleep(1)
			conn.send(str.encode(question[0]+"\n"))
			start_time = time.time()
			conn.send(str.encode("Press the Buzzer to answer the question within 10 seconds.\n"))
			help3 = 0

			while(time.time()-start_time<=10):
				conn.settimeout(0.5)
				
				try:
					data = conn.recv(2048)
					data = data.decode("utf-8")

				except:
					data = None

				if data and whoPressedBuzz == -1:
					whoPressedBuzz = player_id + 1
					conn.send(str.encode("Be Careful. You have only 10 seconds to choose the right option among a, b, c, d.\n"))
					help3 = 1
					break

				if whoPressedBuzz != player_id + 1 and whoPressedBuzz != -1:
					conn.send(str.encode("Player {} has pressed the Buzzer. Please Wait. He/She will answer the question.\n".format(whoPressedBuzz)))
					help3 = 1
					break

			answer_time = time.time()
			global help1
			global help2
			helper = 0

			if help3==0:
				conn.send(str.encode("Time limit to press the Buzzer has exceeded.\n The right answer is {}\n".format(question[1])))

			while(time.time()-answer_time<=10 and help3==1):
				if whoPressedBuzz == player_id + 1:
					conn.settimeout(10)
					try:
						answer = conn.recv(2048)
						answer = answer.decode("utf-8")

						if answer == question[1] + "\n":
							score[player_id] += 1
							whoPressedBuzz = -1
							helper = 1
							help1 = 1
							help2 = 1
							conn.send(str.encode("Correct Answer! You earn 1 point.\n"))

						else:
							score[player_id] -= 0.5
							help1 = 1
							helper = 1
							help2 = 1
							whoPressedBuzz = -1
							conn.send(str.encode("Wrong answer! You lose 0.5 point.\n"))

					except:
						score[player_id] -= 0.5
						whoPressedBuzz = -1
						help1 = 1
						help2 = 1
						conn.send(str.encode("Time limit has exceeded. You lose 0.5 point.\n"))

				if help1 == 1:
					help1 = 0
					whoPressedBuzz = -1
					break

				if help2 == 1 and help1 == 0:
					help2 = 0
					whoPressedBuzz = -1
					break

				if helper == 1:
					break

			conn.send(str.encode("Scores: \n"))
			conn.send(str.encode("         Player 1 : {} points\n".format(score[0])))
			conn.send(str.encode("         Player 2 : {} points\n".format(score[1])))
			conn.send(str.encode("         Player 3 : {} points\n".format(score[2])))

		else:
			break
	
	if score[player_id] >= 5:
		print("Player {} WON\n".format(player_id+1))
		conn.send(str.encode("YOU WON"))
	else:
		if score[0]>=5 and player_id!=0:
			conn.send(str.encode("YOU LOSE. Player {} has won\n".format(1)))
		if score[1]>=5 and player_id!=1:
			conn.send(str.encode("YOU LOSE. Player {} has won\n".format(2)))
		if score[2]>=5 and player_id!=2:
			conn.send(str.encode("YOU LOSE. Player {} has won\n".format(3)))



current_player = 0

while score[0]<5 and score[1]<5 and score[2]<5:
	s.settimeout(1)

	try:
		conn, addr = s.accept()
		clients_list.append(conn)
		print("Connected to: ", addr)

	except:
		if score[0]>=5 or score[1]>=5 or score[2]>=5:
			print("Quiz Finished")
		continue

	start_new_thread(client_thread, (conn, current_player))
	current_player += 1

s.close()
