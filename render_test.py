import pygame
import numpy as np

pygame.init()
grid = np.zeros((10, 10), dtype=int)
grid[0, :] = 1
grid[-1, :] = 1
grid[:, 0] = 1
grid[:, -1] = 1
grid[3, 3] = 2   # aag
grid[6, 7] = 3   # insaan
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("FireSwarm")

CELL = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((200, 200, 200))

    for row in range(10):
        for col in range(10):
            if grid[row, col] == 1:
                color = (60, 60, 60)
            elif grid[row, col] == 2:
                color = (220, 50, 50)
            elif grid[row, col] == 3:
                color = (50, 180, 80)
            else:
                color = (230, 230, 230)
            pygame.draw.rect(screen, color, (col * CELL, row * CELL, CELL - 1, CELL - 1))

    pygame.display.flip()

pygame.quit()