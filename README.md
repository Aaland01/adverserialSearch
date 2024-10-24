# adverserialSearch
## Assignment in Introduction to AI - October 2024

Implementation of the adverserial search algorithms minimax and alpha-beta-pruning, and their sub-functions min_value and max_value, for three games;

### Halving Game
Start with a number. A player decides during their turn to either halve the number (/2) or lessen it by one (-1). The goal is to be the first player to start the turn with the number 0. 
Output:

    The number is 5 and it is P1's turn
    P1's action: --
    The number is 4 and it is P2's turn
    P2's action: --
    The number is 3 and it is P1's turn
    P1's action: /2
    The number is 1 and it is P2's turn
    P2's action: --
    The number is 0 and P1 won


### Bucket Game
Simple implementation of three buckets with two numbers each. First player choosed a bucket, second player chooses a number within that bucket. Goal of each player is to get the other player to choose the largest value. 
Output:

    The state is (0, ['A', 'B', 'C']) and it is P1's turn
    P1's action: B
    The state is (1, [3, 1]) and it is P2's turn
    P2's action: 1
    The state is (0, [1]) and P1's utility is 1
### Tic-tac-toe
Simple 3x3, get three in a row. 
Output with minimax and alpha-beta-pruning is the same, with minimax using 30 times more time deciding first move. (~30sec vs ~1sec)


       |   |
    ---+---+---
       |   |
    ---+---+---
       |   |

    It is P1's turn to move
    First move found in: 
     0.9916081428527832 seconds # alpha-beta
    29.523985624313354 seconds # minimax
    P1's action: (0, 0)

     x |   |
    ---+---+---
       |   |
    ---+---+---
       |   |
 
    It is P2's turn to move
    P2's action: (1, 1)

     x |   |
    ---+---+---
       | o |
    ---+---+---
       |   |

    It is P1's turn to move
    P1's action: (0, 1)

     x | x |
    ---+---+---
       | o |
    ---+---+---
       |   |

    It is P2's turn to move
    P2's action: (0, 2)

     x | x | o
    ---+---+---
       | o |
    ---+---+---
       |   |

    It is P1's turn to move
    P1's action: (2, 0)

     x | x | o
    ---+---+---
       | o |
    ---+---+---
     x |   |

    It is P2's turn to move
    P2's action: (1, 0)

     x | x | o
    ---+---+---
     o | o |
    ---+---+---
     x |   |

    It is P1's turn to move
    P1's action: (1, 2)

     x | x | o
    ---+---+---
     o | o | x
    ---+---+---
     x |   |

    It is P2's turn to move
    P2's action: (2, 1)

     x | x | o
    ---+---+---
     o | o | x
    ---+---+---
     x | o |

    It is P1's turn to move
    P1's action: (2, 2)

     x | x | o
    ---+---+---
     o | o | x
    ---+---+---
     x | o | x

    The game is a draw

