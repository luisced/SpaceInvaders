import pygame as pg
import os

"""
This is the file for the class Ship.
"""


class Ship:
    """
    This is the class Ship.
    """

    def __init__(self, x, y, color, health=100):
        """
        This is the constructor for the class Ship.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
        self.lives = 3
        self.score = 0
        self.ship_image = pg.image.load(
            os.path.join("images", "space-invaders.png"))
        self.ship_image_red = pg.image.load(
            os.path.join("images", "space_invaders_red.png"))
        self.ship_image_glue = pg.image.load(
            os.path.join("images", "space_invaders_blue.png"))
        self.ship_image_green = pg.image.load(
            os.path.join("images", "space_invaders_green.png"))
        self.laser_image = pg.image.load(os.path.join("images", "laser.png"))
        self.lightning_image = pg.image.load(
            os.path.join("images", "Lighning.png"))
        self.background = pg.image.load(os.path.join(
            "images", "SpaceInvadersBackground.jpg"))
        self.laser_list = []
        self.lightning_list = []
        self.enemy_list = []
        self.enemy_list_red = []
        self.enemy_list_glue = []
        self.enemy_list_green = []
        self.enemy_list_lightning = []
        self.enemy_list_lightning_red = []
        self.enemy_list_lightning_glue = []
        self.enemy_list_lightning_green = []
        self.enemy_list_laser = []
        self.enemy_list_laser_red = []
        self.enemy_list_laser_glue = []
        self.enemy_list_laser_green
