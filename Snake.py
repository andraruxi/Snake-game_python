from Constants import *
import pygame
import random
import sys


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (0, 0, 0)
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def grow(self):
        self.length += 1
        self.score += 1
        self.positions.insert(0, self.get_new_snake_head())

    def move(self):
        new_snake_head = self.get_new_snake_head()
        if len(self.positions) > 2 and new_snake_head in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new_snake_head)
            self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def get_new_snake_head(self):
        current_position = self.get_head_position()
        x_direction, y_direction = self.direction
        new_snake_head = (((current_position[0] + (x_direction * grid_square_size)) % screen_width),
                          (current_position[1] + (y_direction * grid_square_size)) % screen_height)
        return new_snake_head

    def draw(self, surface):
        for snake_part in self.positions:
            snake_rect = pygame.Rect((snake_part[0], snake_part[1]), (grid_square_size, grid_square_size))
            pygame.draw.rect(surface, self.color, snake_rect)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
