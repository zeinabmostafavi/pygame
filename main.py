import pygame
import random


class Apple():
    def __init__(self):
        self.r = 10
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.color = (255, 0, 0)

    def show(self):
        img = pygame.image.load("SnakeGame/apple.png")
        img = pygame.transform.scale(img, (40, 40))
        d.blit(img, (self.x, self.y))


class Snake():
    def __init__(self):
        self.w = 16
        self.h = 16
        self.x = width/2
        self.y = height/2
        self.name = "snake"
        self.color = (0, 127, 0)
        self.speed = 3
        self.score = 0
        self.x_change = 0
        self.y_change = 0

    def eat(self):
        if apple.x - apple.r <= self.x <= apple.x + apple.r and apple.y - apple.r <= self.y <= apple.y + apple.r:
            self.score += 1
            self.speed += 0.5
            return True
        else:
            return False

    def show(self):
        pygame.draw.rect(d,  self.color, [self.x, self.y, self.w, self.h])

    def move(self):
        if self.x_change == -1:
            self.x -= self.speed
        elif self.x_change == 1:
            self.x += self.speed
        elif self.y_change == - 1:
            self.y -= self.speed
        elif self.y_change == 1:
            self.y += self.speed


if __name__ == "__main__":
    width = 600
    height = 600

    d = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.x_change = -1
                    snake.y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake.x_change = 1
                    snake.y_change = 0

                elif event.key == pygame.K_UP:
                    snake.y_change = -1
                    snake.x_change = 0

                elif event.key == pygame.K_DOWN:
                    snake.y_change = 1
                    snake.x_change = 0

        bg = pygame.image.load("SnakeGame/g.png")
        d.blit(bg, (0, 0))
        snake.move()
        if snake.eat == True:
            apple = Apple()
            self.score = + 1
            text = self.score.text
            font = pygame.font.Font(None, 28)
            t_s = font.render(text, True, (0, 255, 255))
            d.blit(t_s, (100, 100))

        snake.show()
        apple.show()

        pygame.display.update()
        clock.tick(30)
