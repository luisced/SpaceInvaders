from Models.enemy import Enemy
from Models.player import Player
from Models.laser import *
import pygame as pg
import random

pg.init()

"""
This is the main file for the Space Invaders game.
"""

width, height = 800, 500
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
    level = 0  # level is the current level.
    lives = 5  # lives is the number of lives the player has.
    main_font = pg.font.SysFont("comicsans", 50)
    lost = False
    lost_count = 0
    laser_velocity = 5
    score = 0

    # Player features

    velocity = 5  # velocity is the speed of the enemies.
    player = Player(300, 300)  # player is the player's player.

    # Enemy features

    enemies = []  # enemies is a list of enemies.
    wave_length = 5  # wave_length is the number of enemies in a wave.
    enemy_vel = 1  # enemy_vel is the speed of the enemies.

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
        enemies_banner = main_font.render(
            f"Enemies Left: {len(enemies)}", True, (255, 255, 255))

        # This draws the lives, level, score and enemies on the window.
        Win.blit(images.background, (0, 0))
        Win.blit(lives_banner, (10, 10))
        Win.blit(level_banner, (width - level_banner.get_width() - 10, 10))
        Win.blit(enemies_banner, (10, 110))

        # This draws the player on the window.
        for enemy in enemies:
            enemy.draw(Win)

        player.draw(Win)

        if lost:
            lost_banner = main_font.render(
                f"You Lost!", True, (255, 255, 255))
            Win.blit(lost_banner, (width / 2 - lost_banner.get_width() / 2, 300))

        # This updates the display.
        pg.display.update()

    while run:
        clock.tick(fps)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > fps * 10:
                run = False

            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(100, width - 100), random.randrange(
                    -1500,  - 150), random.choice(["red", "blue", "green"]), health=100)
                enemies.append(enemy)

        # If the user quits the game, the game loop will stop.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        # Key presses are checked.

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and player.x - velocity > 0:  # Move Left
            player.x -= velocity
        if keys[pg.K_RIGHT] and player.x + velocity + player.get_width() < width:  # Move Right
            player.x += velocity
        if keys[pg.K_UP] and player.y - velocity > 0:  # Move Up
            player.y -= velocity  # Move Up
        if keys[pg.K_DOWN] and player.y + velocity + player.get_hight() + 15 < height:
            player.y += velocity

        if keys[pg.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_velocity, player)

            if random.randrange(0, 2 * 60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_hight() > height:
                lives -= 1
                enemies.remove(enemy)

            # add 10 points to score if enemy is destroyed

        player.move_lasers(-laser_velocity, enemies)


def main_menu():
    """
    This function will display the main menu.
    """

    # This creates the main menu.
    menu_font = pg.font.SysFont("comicsans", 30)
    run = True
    while run:
        Win.blit(images.background, (0, 0))
        title = menu_font.render(
            "Press any key to begin...", True, (255, 255, 255))
        Win.blit(title, (width / 2 - title.get_width() / 2, height / 2))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                game()


main_menu()


game()
