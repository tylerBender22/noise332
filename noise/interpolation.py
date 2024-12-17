import math

class interpolation:
    """
    class that provides various interpolation functions.
    """
    def interpolate(x0:float, x1:float, w:float, interpolationFunction) -> float:
        """
        interpolates between two values using a specified interpolation function.
        """
        w = interpolation.sigmoid(w)
        return x0 * (1.0 - interpolationFunction(w)) + x1 * interpolationFunction(w)

    def smootherstep(x):
        """
        computes the smootherstep interpolation function.
        """
        return x * x * x * (x * (x * 6.0 - 15.0) + 10)

    def smoothstep(x):
        """
        computes the smoothstep interpolation function.
        """
        return 3 * x**2 - 2 * x**3

    def sigmoid(x):
        """
        computes the sigmoid function.
        """
        x = max(-10, min(x, 10))
        return (1 / (1 + (math.pow(math.e, -x))))

