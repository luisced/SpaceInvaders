import pygame as pg


class Movement:
    """
    This is the class Movement.
    """

    def __init__(self, x, y):
        """
        This is the constructor for the class Movement.
        """
        self.x = x
        self.y = y

    def move_left(self):
        """
        This is the move_left method for the class Movement.
        """
        self.x -= 10

    def move_right(self):
        """
        This is the move_right method for the class Movement.
        """
        self.x += 10

    def move_up(self):
        """
        This is the move_up method for the class Movement.
        """
        self.y -= 10

    def move_down(self):
        """
        This is the move_down method for the class Movement.
        """
        self.y += 10

    def draw(self, window):
        """
        This is the draw method for the class Movement.
        """
        pg.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))
