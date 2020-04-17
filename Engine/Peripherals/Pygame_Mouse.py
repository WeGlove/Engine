import pygame
from src.Backends.Peripherals.Mouse import Mouse


class Pygame_Mouse(Mouse):

    def get_position(self):
        return pygame.mouse.get_pos()

    def clicked(self):
        return pygame.mouse.get_pressed()

    def left_clicked(self):
        return pygame.mouse.get_pressed()[0]

    def middle_clicked(self):
        return pygame.mouse.get_pressed()[1]

    def right_clicked(self):
        return pygame.mouse.get_pressed()[2]

    def update(self):
        pygame.event.get()
