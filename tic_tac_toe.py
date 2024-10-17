from copy import deepcopy
from time import time

State = tuple[int, list[list[int | None]]]  # Tuple of player (whose turn it is),
                                            # and board
Action = tuple[int, int]  # Where to place the player's piece

class Game:
    """Game class for Tic-Tac-Toe
    """
    def initial_state(self) -> State:
        return (0, [[None, None, None], [None, None, None], [None, None, None]])

    def to_move(self, state: State) -> int:
        player_index, _ = state
        return player_index

    def actions(self, state: State) -> list[Action]:
        _, board = state
        actions = []
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    actions.append((row, col))
        return actions

    def result(self, state: State, action: Action) -> State:
        _, board = state
        row, col = action
        next_board = deepcopy(board)
        next_board[row][col] = self.to_move(state)
        return (self.to_move(state) + 1) % 2, next_board

    def is_winner(self, state: State, player: int) -> bool:
        _, board = state
        for row in range(3):
            if all(board[row][col] == player for col in range(3)):
                return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        return all(board[i][2 - i] == player for i in range(3))

    def is_terminal(self, state: State) -> bool:
        _, board = state
        if self.is_winner(state, (self.to_move(state) + 1) % 2):
            return True
        return all(board[row][col] is not None for row in range(3) for col in range(3))

    def utility(self, state, player):
        assert self.is_terminal(state)
        if self.is_winner(state, player):
            return 1
        if self.is_winner(state, (player + 1) % 2):
            return -1
        return 0

    def print(self, state: State):
        _, board = state
        print()
        for row in range(3):
            cells = [
                ' ' if board[row][col] is None else 'x' if board[row][col] == 0 else 'o'
                for col in range(3)
            ]
            print(f' {cells[0]} | {cells[1]} | {cells[2]}')
            if row < 2:
                print('---+---+---')
        print()
        if self.is_terminal(state):
            if self.utility(state, 0) > 0:
                print(f'P1 won')
            elif self.utility(state, 1) > 0:
                print(f'P2 won')
            else:
                print('The game is a draw')
        else:
            print(f'It is P{self.to_move(state)+1}\'s turn to move')
# ! My code ----------------------------------------------------------------------------

def minimax_search(game: Game, state: State) -> Action | None:
    value, move = max_value(game, state) #(value, move)
    return move # move

def max_value(game: Game, state: State) -> tuple | None:
    if game.is_terminal(state):
        return (game.utility(state, player), None)
    value, move = (float('-inf'), float('-inf'))
    for action in game.actions(state):
        value2, action2 = min_value(game, game.result(state,action))
        if value2 > value:
            value, move = (value2, action)
    return (value, move)

def min_value(game: Game, state: State) -> tuple | None:
    if game.is_terminal(state):
        return (game.utility(state, player), None)
    value, move = (float('inf'), float('inf'))
    for action in game.actions(state):
        value2, action2 = max_value(game, game.result(state,action))
        if value2 < value:
            value, move = (value2, action)
    return (value, move)

def alpha_beta_search(game: Game, state: State) -> Action | None:
    value, move = max_value_ab(game, state, float('-inf'), float('-inf'))
    return move

def max_value_ab(game: Game, state: State, alpha: float | int, beta: float | int) -> tuple | None:
    if game.is_terminal(state):
        return (game.utility(state, player), None)
    value = float('-inf')
    for action in game.actions(state):
        value2, action2 = min_value_ab(game, game.result(state,action), alpha, beta)
        if value2 > value:
            value, move = (value2, action)
            alpha = max(alpha, value)
        if value >= beta:
            return (value, move)
    return (value, move)

def min_value_ab(game: Game, state: State, alpha: float | int, beta: float | int) -> tuple | None:
    if game.is_terminal(state):
        return (game.utility(state, player), None)
    value = float('inf')
    for action in game.actions(state):
        value2, action2 = max_value_ab(game, game.result(state,action), alpha, beta)
        if value2 < value:
            value, move = (value2, action)
            beta = min(beta, value)
        if value <= beta:
            return (value, move)
    return (value, move)

game = Game()
state = game.initial_state()
firstmove = True
game.print(state)
while not game.is_terminal(state):
    firstMoveTimer = time() if firstmove else 0
    player = game.to_move(state)
    action = minimax_search(game, state) # The player whose turn it is
                                         # is the MAX player
    #action = alpha_beta_search(game, state)
    if firstmove:
        firstMoveTimer = time()-firstMoveTimer
        print(f'First move found in: {firstMoveTimer} seconds')
        firstmove = False
    print(f'P{player+1}\'s action: {action}')
    assert action is not None
    state = game.result(state, action)
    game.print(state)