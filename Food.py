from Constants import *
import pygame
import random


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, x_squares_number - 1) * grid_square_size, random.randint(0, y_squares_number - 1) * grid_square_size)

    def draw(self, surface):
        fruit_rect = pygame.Rect((self.position[0], self.position[1]), (grid_square_size, grid_square_size))
        pygame.draw.rect(surface, self.color, fruit_rect)
