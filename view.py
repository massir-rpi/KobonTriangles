import matplotlib.pyplot as plt
from typing import Optional, Tuple

def plot_lines_in_circle(line_segments, zoom_factor, filepath, limits: Optional[Tuple[Tuple[float]]] = None):
    """
    Args:
        limits:
            nested tuples ((xmin, xmax), (ymin, ymax))
            if not provided, zoom_factor will be used
    """

    if limits is None:
        limit = 1.1 * zoom_factor
        limits = ((limit, limit), (limit, limit))

    N = len(line_segments)
    fig, ax = plt.subplots()

    # Plotting the unit circle
    circle = plt.Circle((0, 0), 1, fill=False, color='blue', linestyle='--')
    circle2 = plt.Circle((0, 0), zoom_factor, fill=False, color='red', linestyle='--')
    ax.add_artist(circle)
    ax.add_artist(circle2)

    # Plotting the line segments
    for i in range(N):
        x1, y1 = line_segments[i][0]
        x2, y2 = line_segments[i][1]
        ax.plot([x1, x2], [y1, y2], marker='o')

    ax.set_xlim(**limits[0])
    ax.set_ylim(**limits[1])
    ax.set_aspect('equal', adjustable='box')

    plt.savefig(filepath)
