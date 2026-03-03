import heapq
import time
from helpers import *


# Calculate the Manhattan distance heuristic (h(n))
def manhattan_distance(state, goal="012345678"):
    distance = 0
    # Ensure state is a string
    s = "".join(map(str, state)) if isinstance(state, list) else state

    for i, val_char in enumerate(s):
        if val_char != '0':
            # Find the goal position of the current tile
            goal_pos = goal.index(val_char)
            # Calculate current (x1, y1) and goal (x2, y2) coordinates
            x1, y1 = i % 3, i // 3
            x2, y2 = goal_pos % 3, goal_pos // 3
            # Add Manhattan distance for this tile
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


# A* Search using Manhattan distance as the heuristic
def astar_manhattan(start, goal="012345678"):
    start_time = time.time()
    frontier = []
    # Heap stores (f_score, cost_g, state_string, path_list_of_strings)
    heapq.heappush(frontier, (manhattan_distance(start), 0, start, [start]))
    # Visited set to prevent cycles and redundant exploration
    visited = set()
    nodes_expanded = 0

    while frontier:
        # Pop state with the lowest f_score
        est_total, cost, state, path = heapq.heappop(frontier)
        
        if state in visited:
            continue
        visited.add(state)
        nodes_expanded += 1

        # Goal check
        if state == goal:
            end_time = time.time()
            # Return solution path and statistics
            return path, {
                'cost': cost,
                'nodes_expanded': nodes_expanded,
                'search_depth': cost, # Search depth is the cost (g)
                'running_time': end_time - start_time
            }

        # Expand neighbors
        for neighbor in states(state):
            if neighbor not in visited:
                new_cost = cost + 1
                est = new_cost + manhattan_distance(neighbor) # f(n) = g(n) + h(n)
                heapq.heappush(frontier, (est, new_cost, neighbor, path + [neighbor]))

    # No solution found
    return None, {}