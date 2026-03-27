# Conway's Game of Life
A Python implementation of Conway's game of life using Pygame.
Interact with the simulation using mouse and keyboard.

## How to Install:
1. Clone the repository
```bash 
git clone https://github.com/uftabyya/Conways-game-of-life
```
2. Install required packages (If you don't have **Pygames** installed)
```bash 
pip install -r requirements.txt
```

## Requirements
Python 3.10 or higher

## Instructions
- `Space` / `K` - Pause/Unpause the simulation
- `T` - Clear all cells
- `ESC` - Quit the simulation
- **Left mouse click** - Add new live cells

You may change colour of the live cells by editing the RGB value of the `COLOUR_ALIVE` constant in `main.py`.

## Known Limitations
- The simulation currently stops at the borders.
- The program may crash if the cursor crosses the border while placing live tiles with the mouse.
