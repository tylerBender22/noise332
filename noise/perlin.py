from noise.vector import *
from noise.interpolation import *
from world.quadTree.tree import *
import math
import numpy as np
from scipy.ndimage import gaussian_filter

"""
Sources: 
    https://en.wikipedia.org/wiki/Perlin_noise
    https://en.wikipedia.org/wiki/Smoothstep -> Smoother Step
"""


class Perlin2D:
    def __init__(self, size: int, seed: int = None, interpolationFunction=None, 
                 apply_smoothing: bool = False, smoothing_sigma: float = 1.0):
        
        self.size = max(size, 2)  #min size 2

        #all of these are just used to tweak generation.
        #------------
        self.apply_smoothing = apply_smoothing
        self.smoothing_sigma = smoothing_sigma
        self.tempGradients = {}  #store prev gradients for dynamic chunk gen
        #-----------
        
        if interpolationFunction is None:
             self._interpFunc = interpolation.smoothstep
        else: self._interpFunc = interpolationFunction

        if seed is None:
            self._seed = np.random.randint(-2147483648, 2147483647)
        else:   self._seed = seed
        
        self.random = np.random.RandomState(self._seed)

    def doChunk(self, chunkX: int, chunkY: int) -> quadTree:
        noise = self._doPerlin(chunkX, chunkY, 1.0)

        if self.apply_smoothing:
            noise = gaussian_filter(noise, sigma=self.smoothing_sigma)

        chunk = quadTree.doTree(chunkX, chunkY, noise.size)
        return chunk


    def _doPerlin(self, chunkX: int, chunkY: int, frequency: float) ->np.array:
        _gradients = np.empty((self.size + 1, self.size + 1), dtype=object)

        #check if old gradients need to be used
        for gx in range(self.size + 1):
            for gy in range(self.size + 1):
                tempX = int((chunkX * self.size + gx) * frequency)
                tempY = int((chunkY * self.size + gy) * frequency)

                if (tempX, tempY) in self.tempGradients:
                    _gradients[gx, gy] = self.tempGradients[(tempX, tempY)]
                else:
                    _gradients[gx, gy] = self.randomGradient()
                    self.tempGradients[(tempX, tempY)] = _gradients[gx, gy]

        #noise
        _noise = np.zeros((self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                #rel pos
                px = x * frequency / self.size
                py = y * frequency / self.size

                x0, x1 = int(px), int(px) + 1
                y0, y1 = int(py), int(py) + 1
                sx, sy = px - x0, py - y0

                g00 = _gradients[x0, y0]
                g10 = _gradients[x1, y0]
                g01 = _gradients[x0, y1]
                g11 = _gradients[x1, y1]

                n0 = self._dotP(g00, sx, sy)
                n1 = self._dotP(g10, sx - 1, sy)
                ix0 = interpolation.interpolate(n0, n1, sx, self._interpFunc)

                n0 = self._dotP(g01, sx, sy - 1)
                n1 = self._dotP(g11, sx - 1, sy - 1)
                ix1 = interpolation.interpolate(n0, n1, sx, self._interpFunc)

                _noise[x, y] = interpolation.interpolate(ix0, ix1, sy, self._interpFunc)
        return _noise
    

    def randomGradient(self, seed) -> Vector2D:
        angle = seed.uniform(0, 2 * np.pi)
        return Vector2D(np.cos(angle), np.sin(angle))

    def _dotP(self, gradientVector:Vector2D, sx, sy) -> float:
        return (sx * gradientVector.x) + (sy * gradientVector.y)