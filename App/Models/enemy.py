from Images import images
from Models.ship import Ship
from Models.laser import Laser
import pygame as pg


class Enemy(Ship):
    """
    This is the class Enemy.
    """

    enemy_color = {
        "red": (images.space_ship_red, images.red_laser),
        "blue": (images.space_ship_glue, images.red_laser),
        "green": (images.space_ship_green, images.red_laser)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.enemy_color[color]
        self.mask = pg.mask.from_surface(self.ship_img)

    def move(self, vel):

        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x+19, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    # funcion that checks if enemy collides with player
