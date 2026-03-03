import tkinter as tk

class PuzzleGUI:
    def __init__(self, root, path):
        self.root = root
        self.root.title("8-Puzzle Solver - A* Search")
        self.path = path # The solution path (list of states)
        self.tiles = []  # Stores the tkinter Label objects for the tiles
        self.create_board()
        self.animate_solution()

    # Create the initial 3x3 grid of labels
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                # Create a Label for each tile
                tile = tk.Label(self.root, text="", font=("Helvetica", 32), width=4, height=2, borderwidth=2, relief="ridge")
                tile.grid(row=i, column=j)
                row.append(tile)
            self.tiles.append(row)

    # Update the board labels to reflect a new state
    def update_board(self, state):
        for i in range(3):
            for j in range(3):
                # State is a string of 9 characters
                val = state[i * 3 + j]
                # Set text to empty string for '0' (the blank tile)
                self.tiles[i][j].config(text="" if val == '0' else val)

    # Animate the solution path step-by-step
    def animate_solution(self):
        delay = 500  # Delay in milliseconds between steps
        for i, state in enumerate(self.path):
            # Schedule the board update for each state in the path
            self.root.after(i * delay, lambda s=state: self.update_board(s))