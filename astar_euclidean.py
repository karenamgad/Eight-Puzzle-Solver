import heapq
import time
from helpers import *
import math

# Calculate the Euclidean distance heuristic (h(n))
def euclidean_distance(state):
    distance = 0
    # Ensure state is a string
    s = "".join(map(str, state)) if isinstance(state, list) else state
    
    for i, val_char in enumerate(s):
        if val_char != '0':
            val = int(val_char)
            # Goal position for the tile 'val'
            goal_index = val 
            
            # Calculate current and goal row/column
            cur_row, cur_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_index, 3) 
            
            # Add Euclidean distance for this tile
            distance += math.sqrt((goal_row - cur_row)**2 + (goal_col - cur_col)**2)
    return distance

# A* Search using Euclidean distance as the heuristic
def astar_euclidean(start):
    start_time = time.time()
    frontier = []
    
    # Heap stores (f_score, cost_g, state_string, path_list_of_strings)
    # f_score = g_score + h_score
    heapq.heappush(frontier, (euclidean_distance(start), 0, start, [start])) 
    
    # Visited set to prevent cycles and redundant exploration
    visited = set()
    nodes_expanded = 0

    while frontier:
        # Pop state with the lowest f_score
        est_total, cost, node, path = heapq.heappop(frontier)

        if node in visited:
            continue
        visited.add(node)
        nodes_expanded += 1

        # Goal check
        if node == GOAL_STATE:
            end_time = time.time()
            # Return solution path and statistics
            return path, {
                'cost': cost,
                'nodes_expanded': nodes_expanded,
                'search_depth': len(path) - 1,
                'running_time': end_time - start_time
            }

        # Expand neighbors
        for neighbor in states(node):
            if neighbor not in visited:
                new_cost = cost + 1 # g(n) = cost to reach the neighbor
                est = new_cost + euclidean_distance(neighbor) # f(n) = g(n) + h(n)
                heapq.heappush(frontier, (est, new_cost, neighbor, path + [neighbor]))

    # No solution found
    return None, {}