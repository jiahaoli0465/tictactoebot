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
            return None  # Invalid move
        self.process(action)
        # return action
    

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
            # winner = self.player if value == 1 else None  # None indicates a draw
            # status = 'won' if value == 1 else 'draw'
            # return self.state, winner, status

        self.player = self.tictactoe.get_opponent(self.player)
        # return self.state, None, 'continue'
    




    # def start_game(self ):
    #     while True:
    #         # print(self.state)

    #         if self.player == 1:
    #             #player moves
    #             valid_moves = self.tictactoe.get_valid_moves(self.state)
    #             # print("valid_moves", [i for i in range(self.tictactoe.action_size) if valid_moves[i] == 1])

    #             # inp = input(f'{self.player}:')

    #             # if (inp == ' ' or not inp.isdigit()):
    #             #     print('input not valid')
    #             #     continue
    #             # action = int(inp)

    #             # action = make_move()

    #             # if valid_moves[action] == 0:
    #             #     print('action not valid')
    #             #     continue

    #         else:
    #             #computer moves
    #             neutral_state = self.tictactoe.change_perspective(self.state, self.player)
    #             mcts_probs = self.mcts.search(neutral_state)        
    #             action = np.argmax(mcts_probs)

    #         self.state = self.tictactoe.get_next_state(self.state, action, self.player)

    #         value, is_terminal = self.tictactoe.get_value_and_terminated(self.state, action)

    #         if is_terminal:
    #             print(self.state)
    #             if value == 1:
    #                 print (self.player, 'won')
    #             else:
    #                 print('draw')
                
    #             break

    #         self.player = self.tictactoe.get_opponent(self.player)





# class TTCgame:
#     def __init__(self):
#         self.tictactoe = TicTacToe()
#         self.player = 1
#         self.args = args
#         self.mcts = MCTS(self.tictactoe, self.args)
#         self.state = self.tictactoe.get_initial_state()

#     def start_game(self ):
#         while True:
#             print(self.state)

#             if self.player == 1:
#                 valid_moves = self.tictactoe.get_valid_moves(self.state)
#                 print("valid_moves", [i for i in range(self.tictactoe.action_size) if valid_moves[i] == 1])
#                 inp = input(f'{self.player}:')
#                 if (inp == ' ' or not inp.isdigit()):
#                     print('input not valid')
#                     continue
#                 action = int(inp)

#                 if valid_moves[action] == 0:
#                     print('action not valid')
#                     continue

#             else:
#                 neutral_state = self.tictactoe.change_perspective(self.state, self.player)
#                 mcts_probs = self.mcts.search(neutral_state)        
#                 action = np.argmax(mcts_probs)

#             self.state = self.tictactoe.get_next_state(self.state, action, self.player)

#             value, is_terminal = self.tictactoe.get_value_and_terminated(self.state, action)

#             if is_terminal:
#                 print(self.state)
#                 if value == 1:
#                     print (self.player, 'won')
#                 else:
#                     print('draw')
                
#                 break

#             self.player = self.tictactoe.get_opponent(self.player)









# ttc = TTCgame()

# ttc.start_game()





# tictactoe = TicTacToe()
# player = 1

# args = {
#     'C': 3,
#     'num_searches': 10000
# }

# mcts = MCTS(tictactoe, args)
# state = tictactoe.get_initial_state()

# while True:
#     print(state)

#     if player == 1:
#         valid_moves = tictactoe.get_valid_moves(state)
#         print("valid_moves", [i for i in range(tictactoe.action_size) if valid_moves[i] == 1])
#         inp = input(f'{player}:')
#         if (inp == None or not inp.isdigit()):
#             print('input not valid')
#             continue
#         action = int(inp)

#         if valid_moves[action] == 0:
#             print('action not valid')
#             continue

#     else:
#         neutral_state = tictactoe.change_perspective(state, player)
#         mcts_probs = mcts.search(neutral_state)        
#         action = np.argmax(mcts_probs)

#     state = tictactoe.get_next_state(state, action, player)

#     value, is_terminal = tictactoe.get_value_and_terminated(state, action)

#     if is_terminal:
#         print(state)
#         if value == 1:
#             print (player, 'won')
#         else:
#             print('draw')
         
#         break

#     player = tictactoe.get_opponent(player)
    