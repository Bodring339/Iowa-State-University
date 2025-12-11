#!/usr/bin/env python3
# chimpRefactor.py
# Your Name
# 19 November 2025
# Lab Number
# Refactored chimp.py following assignment requirements only.

import os
import sys
import pygame
import random


class NoneSound:
    def play(self):
        pass


def load_sound(path):
    try:
        return pygame.mixer.Sound(path)
    except (pygame.error, FileNotFoundError):
        print(f"Warning: unable to load sound '{path}'")
        return NoneSound()


class Entity(pygame.sprite.Sprite):
    def __init__(self, data_dir, image_name, colorkey=None, scale=None):
        super().__init__()

        fullpath = os.path.join(data_dir, image_name)
        try:
            image = pygame.image.load(fullpath)
        except pygame.error:
            raise SystemExit(f"Cannot load image: {fullpath}")

        image = image.convert()

        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)

        if scale is not None:
            w = int(image.get_width() * scale)
            h = int(image.get_height() * scale)
            image = pygame.transform.scale(image, (w, h))

        self.image = image
        self.rect = self.image.get_rect()


class Fist(Entity):
    def __init__(self, data_dir, image_name="fist.png", colorkey=-1, scale=None):
        super().__init__(data_dir, image_name, colorkey, scale)
        self.punching = False

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos

    def punch(self, target):
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)
        return False

    def unpunch(self):
        self.punching = False


class Chimp(Entity):
    def __init__(self, data_dir, image_name="chimp.png", colorkey=-1, scale=None):
        super().__init__(data_dir, image_name, colorkey, scale)
        self.rect = self.image.get_rect()
        self.rect.move_ip(100, 100)
        self.speed = [9, 9]

    def update(self):
        screen = pygame.display.get_surface()
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > screen.get_height():
            self.speed[1] = -self.speed[1]


def main():
    pygame.init()

    if not pygame.font:
        print("Warning, fonts disabled")
    if not pygame.mixer:
        print("Warning, sound disabled")

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")

    # Corrected screen size ONLY
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Chimp")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Pummel the Chimp!", True, (10, 10, 10))
        textpos = text.get_rect(center=background.get_rect().center)
        background.blit(text, textpos)

    punch_sound = load_sound(os.path.join(data_dir, "punch.wav"))
    whiff_sound = load_sound(os.path.join(data_dir, "whiff.wav"))

    chimp = Chimp(data_dir)
    fist = Fist(data_dir)

    allsprites = pygame.sprite.RenderPlain((chimp, fist))

    clock = pygame.time.Clock()
    going = True

    while going:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()
                    chimp.speed[0] = -chimp.speed[0]
                    chimp.speed[1] = random.choice([-9, 9])
                else:
                    whiff_sound.play()
            elif event.type == pygame.MOUSEBUTTONUP:
                fist.unpunch()

        allsprites.update()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
