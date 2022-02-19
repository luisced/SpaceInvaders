import os
import pygame as pg

# (Player): This is player image

space_ship_png = pg.image.load(os.path.join("images", "space-invaders.png"))
space_ship = pg.transform.scale(space_ship_png, (50, 50))

# (Enemy 1): SpaceInvaders\images\space_invaders_red.png
space_ship_red_png = pg.image.load(
    os.path.join("images", "space_invaders_red.png"))
space_ship_red = pg.transform.scale(space_ship_red_png, (50, 50))


# (Enemy 2): SpaceInvaders\images\space_invaders_blue.png
space_ship_glue_png = pg.image.load(
    os.path.join("images", "space_invaders_blue.png"))
space_ship_glue = pg.transform.scale(space_ship_glue_png, (50, 50))

# (Enemy 3): SpaceInvaders\images\space_invaders_green.png
space_ship_green_png = pg.image.load(
    os.path.join("images", "space_invaders_green.png"))
space_ship_green = pg.transform.scale(space_ship_green_png, (50, 50))

# (Red laser): SpaceInvaders\images\SpaceInvadersLaserDepiction.png
red_laser_png = pg.image.load(os.path.join("images", "laser.png"))
red_laser = pg.transform.smoothscale(red_laser_png, (2, 2))

# (Lightning): SpaceInvaders\images\SpaceInvadersLaserDepiction.png
lightning_png = pg.image.load(os.path.join("images", "Lighning.png"))
lightning = pg.transform.smoothscale(lightning_png, (50, 50))

# background: SpaceInvaders\images\SpaceInvadersBackground.png

background = pg.image.load(os.path.join(
    "images", "SpaceInvadersBackground.jpg"))
