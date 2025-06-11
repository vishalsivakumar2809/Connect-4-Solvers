from math import inf
import random
import unittest 
from connect4 import Board

def switch_player(player):
	if player == 'X':
		return 'O'
	return 'X'
	
def minimax(board, player, ply):
	"""
	Function receives an instances of the Board class, the player who is to act at this state (either X or O),
	and the maximum search depth given by the variable ply.

	The function returns three values: 
	1. the score of the optimal move for the player who is to act;
	2. the optimal move
	3. the total number of nodes expanded to find the optimal move 
	"""
	expansions = 1

	# if the current board instance is a draw/win for a player, we return [-1, 0, 1], any column, no. of expansions (= 1).
	if board.is_terminal():
		return board.game_value(), board.lastCol, expansions
	
	# if depth is 0 (max depth), we return 0,0,1.
	if ply == 0:
		return 0, 0, expansions
	
	# setting bestScore to -inf if player is X, which means we maximize for X.
	if player == 'X':
		bestScore = -inf

	# setting bestScore to inf if player is O, which means we minimize for O.	
	else:
		bestScore = inf
	
	bestMove = -inf
	
	# traversing all available moves
	for move in board.available_moves():

		# updating our board, then recursively calling minimax to retrieve a score, 
		# with switch(player) switching the player as required, and depth decreasing by 1.
		# board.undo_move will then undo the move we committed, to ensure we can work with 
		# the original board for the next move.

		board.perform_move(move, player)
		score, result_move, expanded = minimax(board, switch_player(player), ply - 1)
		board.undo_move(move)

		expansions = expansions + expanded 		

		# if player is X, we must maximize the score, so we check if score's higher than
		# bestScore, to which we update bestScore and bestMove.
		if player == 'X':
			if score > bestScore:
				bestScore = score
				bestMove = move
		
		# if player is O, we must minimize the score, so we check if score's lesser than
		# bestScore, to which we update bestScore and bestMove.
		else:
			if score < bestScore:
				bestScore = score
				bestMove = move
	
	return bestScore, bestMove, expansions

class TestMinMaxDepth1(unittest.TestCase):

	def test_depth1a(self):
		b = Board()
		player = b.create_board('010101')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 0)

	def test_depth1b(self): 
		b = Board() 
		player = b.create_board('001122')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 3)

	def test_depth1c(self): 
		b = Board() 
		player = b.create_board('335566')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 4)

	def test_depth1d(self):
		b = Board() 
		player = b.create_board('3445655606')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 6)

	def test_depth1e(self):
		b = Board() 
		player = b.create_board('34232210101')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 1)

	def test_depth1f(self):
		b = Board() 
		player = b.create_board('23445655606')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 6)

	def test_depth1g(self): 
		b = Board() 
		player = b.create_board('33425614156')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 2)

class TestMinMaxDepth3(unittest.TestCase):

	def test_depth3a(self):
		b = Board()
		player = b.create_board('303111426551')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 2)

	def test_depth3b(self): 
		b = Board() 
		player = b.create_board('23343566520605001')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 6)

	def test_depth3c(self): 
		b = Board() 
		player = b.create_board('10322104046663')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 0)

	def test_depth3d(self):
		b = Board() 
		player = b.create_board('00224460026466')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 3)

	def test_depth3e(self):
		b = Board() 
		player = b.create_board('102455500041526')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 1)

	def test_depth3f(self):
		b = Board() 
		player = b.create_board('01114253335255')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 2)

	def test_depth3g(self): 
		b = Board() 
		player = b.create_board('0325450636643')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 5)

class TestMinMaxDepth5(unittest.TestCase):
	def test_depth5a(self):
		b = Board()
		player = b.create_board('430265511116')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 3)
		
	def test_depth5b(self):
		b = Board()
		player = b.create_board('536432111330')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 5)

	def test_depth5c(self):
		b = Board()
		player = b.create_board('322411004326')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 3)

	def test_depth5d(self):
		b = Board()
		player = b.create_board('3541226000220')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 4)

	def test_depth5e(self):
		b = Board()
		player = b.create_board('43231033655')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 1)

	def test_depth5f(self):
		b = Board()
		player = b.create_board('345641411335')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 5)

	def test_depth5g(self):
		b = Board()
		player = b.create_board('336604464463')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 3)		
		print('\nMinimax Expansions: ',expansions)

if __name__ == '__main__':
	unittest.main()
	

