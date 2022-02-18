from ship import Ship
import images
import pygame as pg


class Player(Ship):
    """
    This is the class Player.
    """

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = images.img
        self.laser_img = images.red_laser
        self.mask = pg.mask.from_surface(self.ship_img)
        self.max_health = health


player = Player(300, 400)
