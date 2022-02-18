from movement import Movement
from ship import *
from player import Player
import images
import movement
import pygame as pg
import time
import random

pg.init()

"""
This is the main file for the Space Invaders game.
"""

width, height = 800, 600
Win = pg.display.set_mode((width, height))


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
    velocity = 5  # velocity is the speed of the enemies.
    # main_font is the font used for the score and level.
    main_font = pg.font.SysFont("comicsans", 50)
    player = Player(300, 400)  # player is the player's player.
    movement = Movement(300, 650)  # movement is the player's movement.

    # Main loop

    def redraw_window():
        """
        This function will redraw the window.
        """

        # Lives, score, level and enemies are drawn on the window.
        lives_banner = main_font.render(
            f"Lives: {lives}", True, (255, 255, 255))
        level_banner = main_font.render(
            f"Level: {level}", True, (255, 255, 255))
        score_banner = main_font.render(
            f"Score: {score}", True, (255, 255, 255))
        enemies_banner = main_font.render(
            f"Enemies Left: {len(enemies)}", True, (255, 255, 255))

        # This draws the lives, level, score and enemies on the window.
        Win.blit(images.background, (0, 0))
        Win.blit(lives_banner, (10, 10))
        Win.blit(level_banner, (655, 10))
        Win.blit(score_banner, (10, 60))
        Win.blit(enemies_banner, (10, 110))

        # This draws the player on the window.
        player.draw(Win)

        # This updates the display.
        pg.display.update()

    while run:
        clock.tick(fps)
        redraw_window()

        # If the user quits the game, the game loop will stop.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        # Key presses are checked.

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and player.x - velocity > 0:  # Move Left
            player.x -= velocity
        if keys[pg.K_RIGHT] and player.x + velocity < width:  # Move Right
            player.x += velocity
        if keys[pg.K_UP] and player.y - velocity > 0:  # Move Up
            player.y -= velocity  # Move Up
        if keys[pg.K_DOWN] and player.y + velocity < height:
            player.y += velocity  # Move Down


game()
