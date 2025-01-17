import numpy as np

def gen_rand_lines(N, zoom_factor):
    angles = np.random.uniform(0, 2 * np.pi, (N, 2))

    arr = np.column_stack((
        np.cos(angles[:, 0]),
        np.sin(angles[:, 0]),
        np.cos(angles[:, 1]),
        np.sin(angles[:, 1]),
    ))
    arr = arr.reshape(N, 2, 2)

    # zoom out
    slopes = (arr[:, 1, 1] - arr[:, 1, 0]) / (arr[:, 0, 1] - arr[:, 0, 0])
    intercepts = arr[:, 1, 0] - slopes * arr[:, 0, 0]
    new_x1 = -zoom_factor * np.ones(N)
    new_y1 = slopes * new_x1 + intercepts
    new_x2 = zoom_factor * np.ones(N)
    new_y2 = slopes * new_x2 + intercepts

    # back to point-point form
    arr = np.column_stack((
        new_x1,
        new_y1,
        new_x2,
        new_y2
    ))
    arr = arr.reshape(N, 2, 2)
    return arr