import math

# The desired goal state for the 8-puzzle
GOAL_STATE = "012345678"

# Print the 8-puzzle board in a 3x3 format
def print_board(state):
    # Ensure the state is a string
    s = "".join(map(str, state)) if isinstance(state, list) else state
    for i in range(0, 9, 3):
        print(s[i:i+3])
    print("-" * 10)

# Find the index of the blank tile ('0')
def find_zero(state):
    # Ensure the state is a string
    s = "".join(map(str, state)) if isinstance(state, list) else state
    return s.index('0')

# Generate all valid next states (moves) from the current state
def states(current_state):
    # Ensure state is a string
    s = "".join(map(str, current_state)) if isinstance(current_state, list) else current_state
    pos = s.index('0')
    moves = []
    # Possible tile movements: up, down, left, right
    directions = [(-3, 'up'), (3, 'down'), (-1, 'left'), (1, 'right')]

    for move, _ in directions:
        new_pos = pos + move
        if 0 <= new_pos < 9:
            # Prevent illegal moves like wrapping around rows (left/right moves at edge)
            if (pos % 3 == 0 and move == -1) or (pos % 3 == 2 and move == 1):
                continue
            # Swap the blank tile with the new position to create the neighbor state
            lst = list(s)
            lst[pos], lst[new_pos] = lst[new_pos], lst[pos]
            moves.append(''.join(lst))
    return moves