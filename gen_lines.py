import numpy as np

def gen_rand_angles(N):
    return np.random.uniform(0, 2 * np.pi, 2 * N)

def angles_to_lines(zoom_factor, angles):
    '''
    angles: an (N, 2) ndarray of floats between 0 and 2pi
    '''

    n = len(angles) // 2

    arr = np.column_stack((
        np.cos(angles[:n]),
        np.sin(angles[:n]),
        np.cos(angles[n:]),
        np.sin(angles[n:]),
    ))
    arr = arr.reshape(n, 2, 2)

    # zoom out
    slopes = (arr[:, 1, 1] - arr[:, 1, 0]) / (arr[:, 0, 1] - arr[:, 0, 0])
    intercepts = arr[:, 1, 0] - slopes * arr[:, 0, 0]

    # truncate at edges of big circle - solve x^2+y^2=r^2 && y=mx+b
    m = slopes
    b = intercepts
    r = zoom_factor
    new_x1 = - (np.sqrt((m ** 2 + 1) * r ** 2 - b ** 2) + b * m) / (m ** 2 + 1)
    new_x2 = (np.sqrt((m ** 2 + 1) * r ** 2 - b ** 2) - b * m) / (m ** 2 + 1)
    new_y1 = slopes * new_x1 + intercepts
    new_y2 = slopes * new_x2 + intercepts

    # back to point-point form
    arr = np.column_stack((
        new_x1,
        new_y1,
        new_x2,
        new_y2
    ))
    arr = arr.reshape(n, 2, 2)
    return arr


if __name__ == '__main__':
    angles = np.random.uniform(0, 2 * np.pi, (5, 2))
    print(angles_to_lines(2, angles))
