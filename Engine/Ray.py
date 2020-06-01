import numpy
import math

class Ray:

    def __init__(self, position, direction, error=0):
        self.direction = direction
        self.position = position
        self.error = error

    def move(self, t):
        self.position = self.position + self.direction * t

    def set_position(self, position):
        self.position = position

    def get_speed(self):
        return math.sqrt(self.direction[0]**2 + self.direction[1]**2)

    def negate(self):
        self.direction = -self.direction

    def reflect(self, normal):
        scalar = numpy.dot(self.direction, normal)
        self.direction = self.direction - 2 * scalar * normal

    def transform(self, matrix):
        self.direction = self.direction * matrix

    def copy(self):
        return Ray(self.position, self.direction, self.error)
