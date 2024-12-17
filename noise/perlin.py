from noise.vector import *
from noise.interpolation import *
import math
import numpy as np

"""
Sources: 
    https://en.wikipedia.org/wiki/Perlin_noise
    https://en.wikipedia.org/wiki/Smoothstep -> Smoother Step
"""


class Perlin2D:
    """
    A class to generate 2D Perlin noise.
    """
    def __init__(self, size: int, seed:int=None, interpolationFunction=None):
        if size < 2:
            self.size = 2
        else:
            self.size = size
        
        if interpolationFunction is None:
             self._interpFunc = interpolation.smoothstep
        else: self._interpFunc = interpolationFunction
        if not seed:
            self._seed = np.random.randint(-2147483648, 2147483647)
        self.random = np.random.RandomState(seed)

    """
    return np.array[(self.size)x(self.size)] or perlin noise
    """
    def noise(self):
        _nodeNoise = np.zeros((self.size, self.size))
        _gradients = np.array([[self.randomGradient(self.random) for _ in range(self.size + 1)] for _ in range(self.size + 1)])
        self.noise = np.zeros((self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                #grid cell cords
                x0 = math.floor(x)
                x1 = min(x0 + 1, self.size - 1)
                y0 = math.floor(y)
                y1 = min(y0 + 1, self.size - 1)
                #rel pos
                sx = x - x0
                sy = y - y0
                #interpolate between gradients and distance
                n0 = self._dotP(_gradients[x0, y0], sx, sy)
                n1 = self._dotP(_gradients[x1, y0], sx - 1, sy)
                i0 = interpolation.interpolate(n0, n1, sx, self._interpFunc)
                n0 = self._dotP(_gradients[x0, y1], sx, sy - 1)
                n1 = self._dotP(_gradients[x1, y1], sx - 1, sy - 1)
                i1 = interpolation.interpolate(n0, n1, sx, self._interpFunc)
                #final interpolation
                _nodeNoise[x, y] = interpolation.sigmoid(interpolation.interpolate(i0, i1, sy, self._interpFunc))
        return _nodeNoise

    def randomGradient(self, seed) -> Vector2D:
        """
        generates random gradient vector
        """
        angle = seed.uniform(0, 2 * np.pi)
        return Vector2D(np.cos(angle), np.sin(angle))
    def _dotP(self, gradientVector:Vector2D, sx, sy) -> float:
        """
        dot product between a gradient vector and a relative position vector.
        """
        return (sx * gradientVector.x) + (sy * gradientVector.y)
    
