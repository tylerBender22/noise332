import math

class Vector:
    """
    Superclass representing a vector in n-dimensional space.

    This class defines the interface for vector operations and serves as a base 
    for implementations like 2D and 3D vectors.

    [Unit Vector](https://en.wikipedia.org/wiki/Unit_vector#Spherical_coordinates), [Del](https://en.wikipedia.org/wiki/Del_in_cylindrical_and_spherical_coordinates)

    Methods:
    --------
    magnitude():
        Calculates the magnitude of the vector. Overridden in subclasses.
    
    print():
        Prints the vector's components. Overridden in subclasses.
    
    randomGradient():
        Generates a random gradient vector. Overridden in subclasses.
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

    Methods:
    --------
    magnitude():
        Calculates the magnitude of the 2D vector.
    
    print():
        Prints the components of the 2D vector.
    
    randomGradient(seed=None):
        Generates a random normal gradient unit vector (2D) based on a seed.
    """
    def __init__(self, x:float, y:float):
        """
        Contructor for 2D Vector.

        Parameters:
        -----------
        x : float
            The x-component of the vector.
        y : float
            The y-component of the vector.
        """
        super().__init__()
        self.x, self.y = x, y

    def magnitude(self):
        """
        Calculates the magnitude(length) of the 2D vector.

        Returns:
        --------
        float:
            The magnitude of the vector, calculated as the square root of the sum of 
            the squares of its components.
        """
        return math.sqrt(self.x**2 + self.y**2)

    def print(self):
        """
        Prints the components of the 2D vector in the format [x, y].
        """
        print("[" + str(self.x) + ", " + str(self.y) + "]", end=' ')


class Vector3D(Vector):
    """
    Sub-class representing a 3D vector.

    Methods:
    --------
    magnitude():
        Calculates the magnitude of the 2D vector.
    
    print():
        Prints the components of the 2D vector.
    
    randomGradient(seed=None):
        Generates a random normal gradient unit vector (2D) based on a seed.
    """
    def __init__(self, x:float, y:float, z:float):
        """
        Contructor for 3D Vector.

        Parameters:
        -----------
        x : float
            The x-component of the vector.
        y : float
            The y-component of the vector.
        z : float
            The z-component of the vector.
        """
        super().__init__()
        self.x, self.y, self.z = x, y, z

    def magnitude(self):
        """
        Calculates the magnitude(length) of the 3D vector.

        Returns:
        --------
        float:
            The magnitude of the vector, calculated as the square root of the sum of 
            the squares of its components.
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def print(self):
        """
        Prints the components of the 3D vector in the format [x, y, z].
        """
        print("[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) +"]", end=' ')
