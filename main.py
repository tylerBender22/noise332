from matplotlib import pyplot as plt
import numpy as np
import noise.perlin as perlin
from noise.interpolation import *
from scipy.ndimage import gaussian_filter


def _plotPerlinCartesian(perlin:perlin.Perlin2D):
    #noise = gaussian_filter(perlin.noise, sigma=1) # smooth it out a bit
    plt.imshow(perlin.noise, cmap='viridis')
    plt.colorbar()
    plt.title('Perlin Noise')
    plt.show()


def _plotPerlin3D(perlin:perlin.Perlin2D):
        x = np.linspace(0, perlin.noise.shape[1] - 1, perlin.noise.shape[1])
        y = np.linspace(0, perlin.noise.shape[0] - 1, perlin.noise.shape[0])
        x, y = np.meshgrid(x, y)
        noise = gaussian_filter(perlin.noise, sigma=1) # smooth it out a bit
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        surf = ax.plot_surface(x, y, noise, cmap='viridis', edgecolor='none')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Noise Value')
        ax.set_title('Perlin Height Map')

        color_bar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

        ax.view_init(elev=30, azim=210)

        plt.show()



perl = perlin.Perlin2D(16, 87692, interpolation.smootherstep, 1, 0.8, 0.3, False, 0.3)
perl.doChunk(0, 0)