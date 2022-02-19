import pygame as pg
import Images.images as images


class Laser:
    def __init__(self, x, y, laser_img):
        self.x = x
        self.y = y
        self.laser_img = images.red_laser_png
        self.mask = pg.mask.from_surface(self.laser_img)

    def draw(self, window):
        window.blit(self.laser_img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):

        return collide(self, obj)

# Check if the player collides with the enemy


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
