import os
import pygame as pg


space_ship = pg.image.load(os.path.join("images", "space-invaders.png"))

# (Enemy 1): SpaceInvaders\images\space_invaders_red.png
space_ship_red = pg.image.load(
    os.path.join("images", "space_invaders_red.png"))

# (Enemy 2): SpaceInvaders\images\space_invaders_blue.png
space_ship_glue = pg.image.load(
    os.path.join("images", "space_invaders_blue.png"))

# (Enemy 3): SpaceInvaders\images\space_invaders_green.png
space_ship_green = pg.image.load(
    os.path.join("images", "space_invaders_green.png"))

# (Red laser): SpaceInvaders\images\SpaceInvadersLaserDepiction.png
red_laser = pg.image.load(os.path.join("images", "laser.png"))

# (Lightning): SpaceInvaders\images\SpaceInvadersLaserDepiction.png
lightning = pg.image.load(os.path.join("images", "Lighning.png"))

# background: SpaceInvaders\images\SpaceInvadersBackground.png

background = pg.image.load(os.path.join(
    "images", "SpaceInvadersBackground.jpg"))
