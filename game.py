from tictactoe import TicTacToe
from mcts import MCTS
import numpy as np


args = {
    'C': 3,
    'num_searches': 1000
}
class TTCgame:
    def __init__(self):
        self.tictactoe = TicTacToe()
        self.player = 1
        self.args = args
        self.mcts = MCTS(self.tictactoe, self.args)
        self.state = self.tictactoe.get_initial_state()
        self.game_over = False

    def get_state(self):
        return self.state
    
    def make_move(self, bid):
        action = bid
        valid_moves = self.tictactoe.get_valid_moves(self.state)

        if valid_moves[action] == 0:
            return None  
        self.process(action)
    

    def computer_move(self):
        neutral_state = self.tictactoe.change_perspective(self.state, self.player)
        mcts_probs = self.mcts.search(neutral_state)        
        action = np.argmax(mcts_probs)
        self.process(action)
        if self.game_over:
            return action, 'over'
        return action, 'cont'
        


    def process(self, action):
        self.state = self.tictactoe.get_next_state(self.state, action, self.player)
        value, is_terminal = self.tictactoe.get_value_and_terminated(self.state, action)

        if is_terminal:
            self.game_over = True


        self.player = self.tictactoe.get_opponent(self.player)

    
