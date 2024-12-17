import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from noise.interpolation import *
from noise.perlin import Perlin2D
from quadTree.tree import *

print("2D Terrain Generator\n")
sizeIn = input("\nPlease enter the size of the noise array (NxN), (or press Enter...size will default to 32x32)... N: ")
seedIn = input("\nPlease enter a seed value (or press Enter...will generate random seed if not provided): ")

size = int(sizeIn) if sizeIn else 32
seed = int(seedIn) if seedIn else None

depth = 5
perl = Perlin2D(size, seed)
noise = perl.noise()

quadtree = quadTree(size, depth)
quadtree.Tree(noise)

fig, ax = plt.subplots(figsize=(8, 8))

def update(val):
    newDepth = int(slider.val)
    quadtree.maxDepth = newDepth
    quadtree.Tree(noise)
    ax.clear()
    ax.set_title(f"Quadtree(LOD: {depth})")
    quadtree.visualize(quadtree.root, ax)
    plt.draw()

slider_ax = fig.add_axes([0.1, 0.01, 0.8, 0.03])
slider = Slider(slider_ax, 'LOD', 1, 10, valinit=depth, valstep=1)

slider.on_changed(update)
ax.set_title(f"Quadtree(LOD: {depth})")
quadtree.visualize(quadtree.root, ax)

plt.show()
