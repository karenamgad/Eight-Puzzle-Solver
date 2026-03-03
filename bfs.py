from collections import deque
import time
from helpers import *

def bfs(start):
    start_time = time.time()
    # Frontier stores paths (list of states) to explore using a queue (FIFO)
    frontier = deque([[start]]) 
    # Visited set to keep track of explored states
    visited = {start} 
    nodes_expanded = 0
    max_depth = 0

    while frontier:
        path = frontier.popleft()
        node = path[-1]
        
        # Track the maximum depth reached
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
        # Generate and add unvisited neighbors to the frontier
        for neighbor in states(node):
            if neighbor not in visited:
                frontier.append(path + [neighbor])
                visited.add(neighbor)
    
    # No solution found
    return None, {}