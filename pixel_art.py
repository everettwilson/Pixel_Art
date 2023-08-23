import tkinter as tk
from itertools import cycle
import argparse

class ColorCyclingCanvas(tk.Canvas):
    def __init__(self, master, colors, **kwargs):
        super().__init__(master, **kwargs)
        self.colors = cycle(colors)
        self.current_color = next(self.colors)
        self.configure(bg=self.current_color)
        self.bind("<Button-1>", self.change_color)

    def change_color(self, event=None):
        self.current_color = next(self.colors)
        self.configure(bg=self.current_color)

class PixelArtApp(tk.Tk):
    def __init__(self, grid_size):
        super().__init__()
        self.title("Pixel Art Creator")

        # Define a list of colors to cycle through
        self.colors = ["red", "green", "blue", "yellow", "white"]

        # Create grid of Canvas widgets based on provided grid size
        self.pixels = [
            [ColorCyclingCanvas(self, self.colors, width=20, height=20, highlightthickness=1, highlightbackground="gray") for _ in range(grid_size)]
            for _ in range(grid_size)
        ]

        for i, row in enumerate(self.pixels):
            for j, canvas in enumerate(row):
                canvas.grid(row=i, column=j, sticky="nsew")

        # Ensure grid cells expand to fill window
        for i in range(grid_size):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a grid for pixel art.")
    parser.add_argument("grid_size", type=int, help="Size of the grid. For example, '5' produces a 5x5 grid.")
    args = parser.parse_args()

    app = PixelArtApp(args.grid_size)
    app.mainloop()

