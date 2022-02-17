
from black import main
import pygame as pg
import os
import time
import random

pg.init()

"""
This is the main file for the Space Invaders game.
"""


# (Player): SpaceInvaders\images\spacehip.png
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


Win = pg.display.set_mode((800, 600))


def game():
    """
    This is the main game loop.
    """

    # run is a boolean variable that will be used to control the game loop.
    run = True
    fps = 60  # fps is the frames per second.
    # clock is a variable that will be used to control the game loop.
    clock = pg.time.Clock()
    level = 1  # level is the current level.
    lives = 5  # lives is the number of lives the player has.
    score = 0  # score is the player's score.
    enemies = []  # enemies is a list of enemies.
    # main_font is the font used for the score and level.
    main_font = pg.font.SysFont("comicsans", 50)

    # Main loop

    def redraw_window():
        """
        This function will redraw the window.
        """

        lives_banner = main_font.render(
            f"Lives: {lives}", True, (255, 255, 255))
        level_banner = main_font.render(
            f"Level: {level}", True, (255, 255, 255))
        score_banner = main_font.render(
            f"Score: {score}", True, (255, 255, 255))
        enemies_banner = main_font.render(
            f"Enemies Left: {len(enemies)}", True, (255, 255, 255))

        Win.blit(background, (0, 0))
        Win.blit(lives_banner, (10, 10))
        Win.blit(level_banner, (10, 60))
        Win.blit(score_banner, (10, 110))
        Win.blit(enemies_banner, (10, 160))
        pg.display.update()

    while run:
        clock.tick(fps)
        redraw_window()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False


game()
