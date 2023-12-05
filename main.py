import pygame
import sys

pygame.init()

width, height = 300, 300
cell_size = width // 3

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            row = y // cell_size
            col = x // cell_size
            if grid[row][col] == 0:
                grid[row][col] = 1

    screen.fill((255, 255, 255))

    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size), 1)
            if grid[row][col] == 1:
                pygame.draw.line(screen, (255, 0, 0), (col * cell_size, row * cell_size), ((col + 1) * cell_size, (row + 1) * cell_size), 2)
                pygame.draw.line(screen, (255, 0, 0), ((col + 1) * cell_size, row * cell_size), (col * cell_size, (row + 1) * cell_size), 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
