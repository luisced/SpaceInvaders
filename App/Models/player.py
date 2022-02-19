
from Models.ship import Ship
import Images.images as images
import pygame as pg


class Player(Ship):
    """
    This is the class Player.
    """

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = images.space_ship
        self.laser_img = images.red_laser
        self.mask = pg.mask.from_surface(self.ship_img)
        self.max_health = health
        self.score = 0

    def move_lasers(self, vel, objs):
        """
        Check if the laser is off_screen
        """
        self.cooldown_laser()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(500):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.score += 10
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.health_bar(window)
        self.score_banner()

    def health_bar(self, screen):
        """
        Draw the health bar
        """
        self.screen = screen

        pg.draw.rect(self.screen, (255, 255, 0), (self.x, self.y +
                     self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pg.draw.rect(self.screen, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() +
                     10, self.ship_img.get_width() * (self.health / self.max_health), 10))

    # function that add 10 to the score

    def score_banner(self):
        """
        This function draws the score banner
        """
        self.font = pg.font.SysFont('comicsans', 50)
        self.text = self.font.render(
            'Score: ' + str(self.score), True, (255, 255, 255))
        self.screen.blit(self.text, (10, 60))


player = Player(300, 400)
