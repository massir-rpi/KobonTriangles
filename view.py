import matplotlib.pyplot as plt

def plot_lines_in_circle(line_segments, zoom_factor, filepath):
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

    ax.set_xlim(-1.1 * zoom_factor, 1.1 * zoom_factor)
    ax.set_ylim(-1.1 * zoom_factor, 1.1 * zoom_factor)
    ax.set_aspect('equal', adjustable='box')

    plt.savefig(filepath)