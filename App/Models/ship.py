from Images import images
from Models.laser import Laser
import pygame as pg


"""
This is the file for the class Ship.
"""


class Ship:
    """
    This is the class Ship.
    """

    cooldown = 30

    def __init__(self, x, y, health=100):
        """
        This is the constructor for the class Ship.
        """
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        """
        This is the draw method for the class Ship.
        """
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def get_width(self):
        """
        Gets the with of the ship image
        """
        return self.ship_img.get_width()

    def get_hight(self):
        """
        This is the get_hight method for the class Ship.
        """
        return self.ship_img.get_height()

    def move_lasers(self, vel, obj):
        """
        Check if the laser is off_screen
        """
        self.cooldown_laser()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(500):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown_laser(self):
        """
        Cooldown function 
        """
        if self.cool_down_counter >= self.cooldown:
            self.cool_down_counter = 0
        elif self.cool_down_counter >= 1:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x+16, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


# class Player(Ship):
#     """
#     This is the class Player.
#     """

#     def __init__(self, x, y, health=100):
#         super().__init__(x, y, health)
#         self.ship_img = images.space_ship
#         self.laser_img = images.red_laser
#         self.mask = pg.mask.from_surface(self.ship_img)
#         self.max_health = health

#     def move_lasers(self, vel, objs):
#         """
#         Check if the laser is off_screen
#         """
#         self.cooldown()
#         for laser in self.lasers:
#             laser.move(vel)
#             if laser.off_screen():
#                 self.lasers.remove(laser)
#             else:
#                 for obj in self.objs:
#                     if laser.collision(obj):
#                         objs.remove(obj)
#                         if laser in self.lasers:
#                             obj.remove(obj)
#                             self.lasers.remove(laser)


# player = Player(300, 400)
