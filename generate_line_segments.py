import numpy as np

N_POINTS = 3
ZOOM_FACTOR = 10


def generate_point_pairs_on_circle(angles):
    '''
    angles: an (N, 2) ndarray of floats between 0 and 2pi
    '''

    arr = np.column_stack((
      np.cos(angles[:, 0]),
      np.sin(angles[:, 0]),
      np.cos(angles[:, 1]),
      np.sin(angles[:, 1]),
    ))
    arr = arr.reshape(N_POINTS, 2, 2)

    # zoom out
    slopes = (arr[:, 1, 1] - arr[:, 1, 0]) / (arr[:, 0, 1] - arr[:, 0, 0])
    intercepts = arr[:, 1, 0] - slopes * arr[:, 0, 0]
    new_x1 = -ZOOM_FACTOR * np.ones(N_POINTS)
    new_y1 = slopes * new_x1 + intercepts
    new_x2 = ZOOM_FACTOR * np.ones(N_POINTS)
    new_y2 = slopes * new_x2 + intercepts

    # back to point-point form
    arr = np.column_stack((
        new_x1,
        new_y1,
        new_x2,
        new_y2
    ))
    arr = arr.reshape(N_POINTS, 2, 2)
    return arr


if __name__ == '__main__':
    angles = np.random.uniform(0, 2 * np.pi, (N_POINTS, 2))
    print(generate_point_pairs_on_circle(angles))
