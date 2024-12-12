from noise.perlin import *
from quadTree import *

class World:
    def __init__(self, worldId, size:int, perlin:Perlin2D):
        self.worldId = worldId
        self.size = size
        self.perlin = perlin
        self.world = None


    def newWorld(self):
        pass