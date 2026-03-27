import pygame
from board import Status, Cell, Board

WIDTH, HEIGHT = 1200, 600
TILE_SIZE = 15

COLOUR_BG = (10, 10, 10)
Colour_GRID = (20, 20, 20)
COLOUR_ALIVE = (57, 255, 20)

#colours 
# Neon Green (57, 255, 20)
# Neon Blue (5, 217, 255)
# Neon Red (255, 0, 0)

def draw_grid(screen):
    for y in range(0, HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, Colour_GRID, (0, y), (WIDTH, y), 1)
    for x in range(0, WIDTH, TILE_SIZE):
        pygame.draw.line(screen, Colour_GRID, (x, 0), (x, HEIGHT), 1)

def cell_display(screen, board: Board):
    for row in range(board.get_row()):
        for col in range(board.get_col()):
            if board.get_cell(row, col).get_status() == Status.ALIVE:
                x = row * TILE_SIZE
                y = col * TILE_SIZE
                pygame.draw.rect(screen, COLOUR_ALIVE, (x, y, TILE_SIZE, TILE_SIZE))

def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    board = Board(WIDTH//TILE_SIZE, HEIGHT//TILE_SIZE)

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_k:
                    running = not running
                elif event.key == pygame.K_r:
                    board = Board(WIDTH//TILE_SIZE, HEIGHT//TILE_SIZE)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                    

        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            row, col = position[0]//TILE_SIZE, position[1]//TILE_SIZE
            board.get_cell(row, col).set_alive()


        screen.fill(COLOUR_BG)
        cell_display(screen, board)
        draw_grid(screen)
        pygame.display.flip()

        if running:
            board.update_neighbours()
            board.update_status()
            cell_display(screen, board)
            draw_grid(screen)
            pygame.display.flip()

        clock.tick(10)

if __name__ == "__main__":
    main()
    


    
