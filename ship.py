import pygame as pg
import os

"""
This is the file for the class Ship.
"""


class Ship:
    """
    This is the class Ship.
    """

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
