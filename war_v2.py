from random import shuffle

class Card():
	"""
	Represents an individual card.
	"""
	suits = ["Spades",
			 "Hearts",
			 "Diamonds",
			 "Clubs"]

	values = [None, None, "2", "3",
			 "4", "5", "6", "7",
			 "8", "9", "10",
			 "Jack", "Queen",
			 "King", "Ace"]

	def __init__(self, v, s):
		"""
		Initial class object
		param: v, s: int
		"""
		self.value = v
		self.suit = s

	def __lt__(self, c2):
		"""
		Overrides the < operator.
		Allows for comparison.
		"""
		if self.value < c2.value:
			return True
		if self.value == c2.value:
			if self.suit < c2.suit:
				return True
			else:
				return False
		return False

	def __gt__(self, c2):
		"""
		Overrides the > operator.
		Allows for comparison.
		"""
		if self.value > c2.value:
			return True
		if self.value == c2.value:
			if self.suit > c2.suit:
				return True
			else:
				return False
		return False

	def __repr__(self):
		"""
		Overides the __repr__
		Allows for return of object description
		"""
		v = self.values[self.value] + " of " + self.suits[self.suit]
		return v

class Deck():
	"""
	Initializes a deck
	Contain 52 individual card objects
	"""
	def __init__(self):
		"""
		Initial deck
		"""
		self.full_deck = []
		for i in range(2, 15):
			for y in range(4):
				self.full_deck.append(Card(i, y))
		shuffle(self.full_deck)

	def rm_card(self):
		"""
		Removes a card
		"""
		if len(self.full_deck) == 0:
			return
		ind_card = self.full_deck.pop()
		return ind_card

class Player():
	"""
	Represents a player.
	Tracks wins, current card and name.
	"""
	def __init__(self, name):
		self.wins = 0
		self.card = None
		self.name = name

class Game():
	"""
	Represents the card game War.
	"""
	def __init__(self):
		"""
		Init game. Collects two player names.
		Init deck, two player objects. 
		"""
		print("Welcome to War: A Grimes Golden Production\n"+ "Press q at any time to quit, thank you.")
		self.deck = Deck()
		name1 = input("Enter player 1 name: ")
		name2 = input("Enter player 2 name: ")
		self.player1 = Player(name1)
		self.player2 = Player(name2)

	def wins(self, winner):
		"""
		Returns the winner of a round
		"""
		w = "{} wins this round."
		w = w.format(winner)
		return(w)

	def draw(self, p1n, p1c, p2n, p2c):
		"""
		Draws card by formatting input from game loop
		"""
		d = "{} drew {} {} drew {}"
		d = d.format(p1n, p1c, p2n, p2c)
		print(d)

	def winner(self, p1, p2):
		"""
		Calculates the winner
		"""
		if p1.wins > p2.wins:
			return "War is over.\n{} wins the game".format(p1.name)
		if p1.wins < p2.wins:
			return "War is over.\n{} wins the game".format(p2.name)
		return "War is over.\nIt was a tie"

	def play_game(self):
		"""
		Begins the game loop
		"""
		cards = self.deck.full_deck
		print("Beginning game")
		while len(cards) >= 2:
			m = "Instructions:\nq: quit t: turbo mode. b: blind turbo\nOr any other keys to play standard: "
			response = input(m)
			if response == 'q':
				break
			elif response == 't':
				# Turbo Mode
				while len(cards) >= 2:
					p1c = self.deck.rm_card()
					p2c = self.deck.rm_card()
					p1n = self.player1.name
					p2n = self.player2.name
					self.draw(p1n, p1c, p2n, p2c)
					if p1c > p2c:
						self.player1.wins += 1
						print(self.wins(p1n))
					else:
						self.player2.wins += 1
						print(self.wins(p2n))
			elif response == 'b':
				while len(cards) >= 2:
					p1c = self.deck.rm_card()
					p2c = self.deck.rm_card()
					p1n = self.player1.name
					p2n = self.player2.name
					if p1c > p2c:
						self.player1.wins += 1
						self.wins(p1n)
					else:
						self.player2.wins += 1
						self.wins(p2n)
			else:
				p1c = self.deck.rm_card()
				p2c = self.deck.rm_card()
				p1n = self.player1.name
				p2n = self.player2.name
				self.draw(p1n, p1c, p2n, p2c)
				if p1c > p2c:
					self.player1.wins += 1
					print(self.wins(p1n))
				else:
					self.player2.wins += 1
					print(self.wins(p2n))

		win = self.winner(self.player1, self.player2)
		print(win)



		
war = Game()
war.play_game()







