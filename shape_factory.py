"""
    factory pattern
"""
import pygame


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        raise NotImplementedError

    def move(self, direction):
        if direction == 'up':
            self.y -= 4
        elif direction == 'down':
            self.y += 4
        elif direction == 'left':
            self.x -= 4
        elif direction == 'right':
            self.x += 4

    @staticmethod
    def factory(type):
        if type == "Circle":
            return Circle(100, 100)
        elif type == "Square":
            return Square(100, 100)
            assert 0, type


class Square(Shape):

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 20, 20))


class Circle(Shape):

    def draw(self):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 20)


if __name__ == '__main__':
    pygame.init()
    size = 1200, 800
    screen = pygame.display.set_mode(size)

    obj = Shape.factory("Square")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: obj.move('up')
        if pressed[pygame.K_DOWN]: obj.move('down')
        if pressed[pygame.K_LEFT]: obj.move('left')
        if pressed[pygame.K_RIGHT]: obj.move('right')

        screen.fill((0, 0, 0))
        obj.draw()
        pygame.display.update()
