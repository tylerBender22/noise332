import math

class Vector:
    """
    Superclass representing a vector in n-dimensional space.
    """
    def __init__(self):
        pass

    def magnitude(self):
        raise NotImplementedError()

    def print(self):
        raise NotImplementedError()

    def randomGradient(self):
        raise NotImplementedError()


class Vector2D(Vector):
    """
    Sub-class representing a 2D vector.
    """
    def __init__(self, x:float, y:float):
        super().__init__()
        self.x, self.y = x, y

    def magnitude(self):
        """
        magnitude of vector
        """
        return math.sqrt(self.x**2 + self.y**2)

    def print(self):
        """
        Print the vector in the format [x, y].
        """
        print("[" + str(self.x) + ", " + str(self.y) + "]", end=' ')


class Vector3D(Vector):
    """
    Sub-class representing a 3D vector.

    """
    def __init__(self, x:float, y:float, z:float):
        super().__init__()
        self.x, self.y, self.z = x, y, z

    def magnitude(self):
        """
        magnitude of vector
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def print(self):
        """
        Print the vector in the format [x, y, z].
        """
        print("[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) +"]", end=' ')
