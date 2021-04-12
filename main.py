from Snake import *
from Food import *
import pygame


def draw_grid(surface):
    for x in range(0, int(x_squares_number)):
        for y in range(0, int(y_squares_number)):
            if (x + y) % 2 == 0:
                grid_rect_lighter = pygame.Rect((x * grid_square_size, y * grid_square_size), (grid_square_size, grid_square_size))
                pygame.draw.rect(surface, (90, 215, 230), grid_rect_lighter)
            else:
                grid_rect_darker = pygame.Rect((x * grid_square_size, y * grid_square_size), (grid_square_size, grid_square_size))
                pygame.draw.rect(surface, (85, 195, 205), grid_rect_darker)


def update(snake, food):
    snake.move()
    if snake.get_head_position() == food.position:
        snake.grow()
        food.randomize_position()


def draw(snake, food, screen, surface, font):
    draw_grid(surface)
    snake.draw(surface)
    food.draw(surface)
    screen.blit(surface, (0, 0))

    text = font.render("Score {0}".format(snake.score), 1, (0, 0, 0))
    screen.blit(text, (5, 10))

    pygame.display.update()


def init():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    draw_grid(surface)

    font = pygame.font.SysFont("monospace", 16)

    snake = Snake()
    food = Food()

    return clock, screen, surface, font, snake, food


def main():
    clock, screen, surface, font, snake, food = init()

    while True:
        clock.tick(8)

        snake.handle_keys()

        update(snake, food)

        draw(snake, food, screen, surface, font)


main()
