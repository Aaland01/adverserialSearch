import math

State = tuple[int, int] # Tuple of player (whose turn it is),
                        # and the number to be decreased
Action = str  # Decrement (number <- number-1) or halve (number <- number / 2)

class Game:
    def __init__(self, N: int):
        self.N = N

    def initial_state(self) -> State:
        return 0, self.N

    def to_move(self, state: State) -> int:
        """
        returns State[0] (int player)
        Since State = tuple(int player, int number)
        """
        player, _ = state
        return player

    def actions(self, state: State) -> list[Action]:
        return ['--', '/2']

    def result(self, state: State, action: Action) -> State:
        _, number = state
        if action == '--':
            return (self.to_move(state) + 1) % 2, number - 1
        else:
            return (self.to_move(state) + 1) % 2, number // 2  # Floored division

    def is_terminal(self, state: State) -> bool:
        """
        returns true if State[1] (int number) == 0
        The win condition.
        Since State = tuple(int player, int number)
        """
        _, number = state
        return number == 0

    def utility(self, state: State, player: int) -> float:
        assert self.is_terminal(state)
        return 1 if self.to_move(state) == player else -1

    def print(self, state: State):
        _, number = state
        print(f'The number is {number} and ', end='')
        if self.is_terminal(state):
            if self.utility(state, 0) > 0:
                print(f'P1 won')
            else:
                print(f'P2 won')
        else:
            print(f'it is P{self.to_move(state)+1}\'s turn')
"""
function MINIMAX-SEARCH(game, state) returns an action
	player = game.to-move(state)
	moveValue = MAX-VALUE(game, state) # Tuple (value, move)
	return moveValue[1]                # move
	
"""
def minimax_search(game: Game, state: State) -> Action | None:
    # ! MY CODE HERE ----------------------------------------------------------------------
    player = game.to_move(state)
    value, move = max_value(game, state) #(value, move)
    return move # move
"""

"""
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

game = Game(5)

state = game.initial_state()
game.print(state)
while not game.is_terminal(state):
    player = game.to_move(state)
    action = minimax_search(game, state) # The player whose turn it is
                                         # is the MAX player
    print(f'P{player+1}\'s action: {action}')
    assert action is not None
    state = game.result(state, action)
    game.print(state)

# Expected output:
# The number is 5 and it is P1's turn
# P1's action: --
# The number is 4 and it is P2's turn
# P2's action: --
# The number is 3 and it is P1's turn
# P1's action: /2
# The number is 1 and it is P2's turn
# P2's action: --
# The number is 0 and P1 won

# Actual output:
# The number is 5 and it is P1's turn
# P1's action: --
# The number is 4 and it is P2's turn
# P2's action: --
# The number is 3 and it is P1's turn
# P1's action: /2
# The number is 1 and it is P2's turn
# P2's action: --
# The number is 0 and P1 won