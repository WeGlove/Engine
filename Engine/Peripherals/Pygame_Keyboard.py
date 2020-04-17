import pygame
from src.Backends.Peripherals.Keyboard import Keyboard


class Pygame_Keyboard(Keyboard):

    def isPressed(self, key):
        return pygame.key.get_pressed()

    def getPressed(self):
        return pygame.key.get_pressed()

    def arePressed(self, keys):
        all([pygame.key.get_pressed(key) for key in keys])

    def __pygame_key_to_key(self, key):
        pass

    def update(self):
        pygame.event.get()
