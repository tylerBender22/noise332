import math

class interpolation:
    """
    A class that provides various interpolation functions.

    This class includes methods for smootherstep, smoothstep, and sigmoid functions 
    commonly used in interpolation and smoothing operations.

    Methods:
    --------
    smootherstep(x):
        Computes the smootherstep interpolation function for a given input x.
    
    smoothstep(x):
        Computes the smoothstep interpolation function for a given input x.
    
    sigmoid(x):
        Computes the sigmoid function for a given input x, clamped between -10 and 10.
    """
    def interpolate(x0:float, x1:float, w:float, interpolationFunction) -> float:
        """
        Interpolates between two values using a specified interpolation function.

        Parameters:
        -----------
        x0 : float
            The value at the lower bound.
        x1 : float
            The value at the upper bound.
        w : float
            The interpolation weight (generally between 0 and 1).
        interpolationFunction : callable
            The interpolation function to be used (e.g., smoothstep, sigmoid).

        Returns:
        --------
        float:
            The interpolated value between x0 and x1.
        """
        w = interpolation.sigmoid(w)
        return x0 * (1.0 - interpolationFunction(w)) + x1 * interpolationFunction(w)

    def smootherstep(x):
        """
        Computes the smootherstep interpolation function.

        The smootherstep function is a smooth transition function that interpolates
        between 0 and 1 over the interval [0, 1]. It is defined to be 0 for x < 0,
        1 for x > 1, and has an even smooth transition in between, compared to normal smoothstep.

        Parameters:
        -----------
        x : float
            A value between 0 and 1. Values outside this range are not clamped.

        Returns:
        --------
        float:
            The result of the smootherstep interpolation function, which smoothly transitions 
            from 0 to 1 as x goes from 0 to 1.
        """
        return x * x * x * (x * (x * 6.0 - 15.0) + 10)

    def smoothstep(x):
        """
        Computes the smoothstep interpolation function.

        The smoothstep function is a smooth transition function that smoothly interpolates 
        between 0 and 1 over the interval [0, 1]. It is defined to be 0 for x < 0,
        1 for x > 1, and has a smooth transition in between.

        Parameters:
        -----------
        x : float
            A value between 0 and 1. Values outside this range are not clamped.

        Returns:
        --------
        float:
            The result of the smoothstep interpolation function, which smoothly transitions 
            from 0 to 1 as x goes from 0 to 1.
        """
        return 3 * x**2 - 2 * x**3

    def sigmoid(x):
        """
        Computes the sigmoid function.

        The sigmoid function is a logistic function that outputs values between 0 and 1.
        The input x is clamped to be between -10 and 10 to prevent overflow errors.

        Parameters:
        -----------
        x : float
            The input value to the sigmoid function.

        Returns:
        --------
        float:
            The output of the sigmoid function, clamped to the range [0, 1].
        """
        x = max(-10, min(x, 10))
        return (1 / (1 + (math.pow(math.e, -x))))

