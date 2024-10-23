from vector import *
from interpolation import *
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
        """
        Constructor for 2D Perlin Noise.

        Parameters:
        -----------
        size : int
            The size of the grid for generating Perlin noise. If less than 2, it is set to 2.
        interpolationFunction : callable, optional
            The function used to interpolate between grid points. If None, smoothstep is used.
        seed : any, optional
            Seed for generating random gradients for consistent noise generation.
        """
        if size < 2:
            self.size = 2
        else:
            self.size = size
        
        if interpolationFunction is None:
             self._interpFunc = interpolation.smoothstep
        else: self._interpFunc = interpolationFunction

        if seed is None:
            self._seed = np.random.randint(-2147483648, 2147483647)
        random = np.random.RandomState(seed)

        _gradients = np.array([[self.randomGradient(random) for _ in range(self.size + 1)] for _ in range(self.size + 1)])
        self.noise = np.zeros((self.size, self.size))

        for x in range(size):
            for y in range(size):
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
                self.noise[x, y] = interpolation.interpolate(i0, i1, sy, self._interpFunc)

    def randomGradient(self, seed) -> Vector2D:
        """
        Generates a random normal gradient unit vector (2D) based on a seed.

        Parameters:
        seed (int, optional): A seed for the random number generator. If None, 
        it will use the current random state.

        Returns:
        Vector2D: A random normal gradient unit vector with components in the range [-1, 1].
        """
        angle = seed.uniform(0, 2 * np.pi)
        return Vector2D(np.cos(angle), np.sin(angle))

    def _dotP(self, gradientVector:Vector2D, sx, sy) -> float:
        """
        Computes the dot product between a gradient vector and a relative position vector.

        Parameters:
        -----------
        gradientVector : Vector2D
            The gradient vector at a specific grid point.
        sx : float
            The relative position in the x-direction
        sy : float
            The relative position in the y-direction

        Returns:
        --------
        float:
            The result of the dot product between the gradient vector and the relative position 
            vector.
        """
        return (sx * gradientVector.x) + (sy * gradientVector.y)