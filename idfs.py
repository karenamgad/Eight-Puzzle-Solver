import time
import sys
from helpers import GOAL_STATE, states

# Allow deeper recursion (needed for big puzzles)
sys.setrecursionlimit(5000)

def dls(state, goal, depth, path, stats, seen_path):
    stats['nodes_expanded'] += 1
    if state == goal:
        return path + [state]
    if depth == 0:
        return None
    for neighbor in states(state):
        # Avoid looping back to a previously seen state in current path
        if neighbor in seen_path:
            continue
        result = dls(neighbor, goal, depth - 1, path + [neighbor], stats, seen_path | {neighbor})
        if result:
            return result
    return None

def idfs(start, max_seconds=30):
    goal = GOAL_STATE
    stats = {'nodes_expanded': 0, 'start_time': time.time()}
    start_time = stats['start_time']

    for depth in range(1, 60):  # You can increase max depth if needed
        # Stop if it takes too long
        if time.time() - start_time > max_seconds:
            print(f"\n⚠️ IDFS stopped after {max_seconds}s (depth={depth-1}, nodes={stats['nodes_expanded']})")
            return None, {}

        print(f"🔎 Searching with depth limit = {depth} (nodes expanded = {stats['nodes_expanded']})")
        path = dls(start, goal, depth, [start], stats, {start})
        if path:
            stats['end_time'] = time.time()
            return path, {
                'cost': len(path) - 1,
                'nodes_expanded': stats['nodes_expanded'],
                'search_depth': len(path) - 1,
                'running_time': stats['end_time'] - stats['start_time']
            }

    print("⚠️ IDFS reached max depth without finding solution.")
    return None, {}