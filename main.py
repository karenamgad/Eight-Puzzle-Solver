import time
import heapq
import collections
from astar_euclidean import *
from astar_Manhattan import *
from bfs import *
from dfs import *
from idfs import *
from helpers import *
from gui import *

if __name__ == "__main__":
    # Get the starting state from the user
    start_state=input("enter the first state: ")
    
    # Get the desired search method from the user
    search_choice = int(input("Choose search method:\n1. BFS\n2. DFS\n3. IDS\n4. A* Euclidean\n5. A* Manhattan\n"))

    # Execute the chosen search algorithm
    if search_choice == 1:
        path, stats = bfs(start_state)
    elif search_choice == 2:
        path, stats = dfs(start_state)
    elif search_choice == 3:
        path, stats = idfs(start_state)
    elif search_choice == 4:
        path, stats = astar_euclidean(start_state)
    elif search_choice == 5:
        path, stats = astar_manhattan(start_state)
    else:
        print("Invalid choice.")
        path, stats = None, {}

   
    # Print results if a solution was found
    if path:
        print(" Path to goal:")
        # Print each step of the solution path
        for step in path:
            print_board(step)

        print("Report:")
        print(f"Cost of path: {len(path) - 1}")
        print(f"Nodes expanded: {stats['nodes_expanded']}")
        print(f"Search depth: {stats['search_depth']}")
        print(f"Running time: {stats['running_time']:.4f} seconds")

        # Launch the GUI to animate the solution
        root = tk.Tk()
        gui = PuzzleGUI(root, path)
        root.mainloop()
    else:
        print("No solution found.")