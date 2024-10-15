State = tuple[int, list[str | int]]  # Tuple of player (whose turn it is),
                                     # and the buckets (as str)
                                     # or the number in a bucket
Action = str | int  # Bucket choice (as str) or choice of number


class Game:
    def __init__(self, N: list[str]):
        self.N = N

    def initial_state(self) -> State:
        return 0, self.N

    def to_move(self, state: State) -> int:
        player, _ = state
        return player

    def actions(self, state: State) -> list[Action]:
        _, actions = state
        return actions

    def result(self, state: State, action: Action) -> State:
        if action == 'A':
            return (self.to_move(state) + 1) % 2, [-50, 50]
        elif action == 'B':
            return (self.to_move(state) + 1) % 2, [3, 1]
        elif action == 'C':
            return (self.to_move(state) + 1) % 2, [-5, 15]
        assert type(action) is int
        return (self.to_move(state) + 1) % 2, [action]

    def is_terminal(self, state: State) -> bool:
        """
        returns true if State[1].len (list choices) == 0
        Meaning, the player only has one choice, and searching is not needed
        Since State = tuple(int player, list choices)
        """
        _, actions = state
        return len(actions) == 1

    def utility(self, state: State, player: int) -> float:
        assert self.is_terminal(state)
        _, actions = state
        assert type(actions[0]) is int
        return actions[0] if player == self.to_move(state) else -actions[0]

    def print(self, state):
        print(f'The state is {state} and ', end='')
        if self.is_terminal(state):
            print(f'P1\'s utility is {self.utility(state, 0)}')
        else:
            print(f'it is P{self.to_move(state)+1}\'s turn')

def minimax_search(game: Game, state: State) -> Action | None:
    # ! MY CODE HERE ----------------------------------------------------------------------
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

buckets = ['A', 'B', 'C']
# val (-50,50) (3,1) (-5, 15)
game = Game(buckets)

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


# OUTPUT 
# The state is (0, ['A', 'B', 'C']) and it is P1's turn
# P1's action: B
# The state is (1, [3, 1]) and it is P2's turn
# P2's action: 1
# The state is (0, [1]) and P1's utility is 1