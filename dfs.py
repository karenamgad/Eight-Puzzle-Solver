import time
from helpers import *

# DFS with a simple state-visited check and a depth limit
def dfs(start, depth_limit=50):
    start_time = time.time()
    # Stack stores paths (list of states) to explore using a LIFO structure
    stack = [[start]] 
    # Visited set to prevent re-exploring states
    visited = set() 
    nodes_expanded = 0
    max_depth = 0

    while stack:
        path = stack.pop()
        node = path[-1]

        # Check if state has already been visited
        if node in visited:
            continue
        visited.add(node)
        max_depth = max(max_depth, len(path))
     
        # Goal check
        if node == GOAL_STATE:
            end_time = time.time()
            # Return solution path and statistics
            return path, {
                'cost': len(path) - 1,
                'nodes_expanded': nodes_expanded,
                'search_depth': len(path) - 1,
                'running_time': end_time - start_time
            }

        nodes_expanded += 1

        # Expand children only if the current path length is within the limit
        if len(path) <= depth_limit:
            # Push neighbors onto the stack in reverse order for standard DFS expansion order
            for neighbor in reversed(states(node)):
                if neighbor not in visited:
                    stack.append(path + [neighbor])
    
    # No solution found
    return None, {}