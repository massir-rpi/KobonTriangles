from scipy.optimize import minimize
from count_triangles import count_triangle_flat_in_neg_out
import numpy as np

def optimize(lines):
    return minimize(count_triangle_flat_in_neg_out, lines.flat, method='Nelder-Mead')

if __name__ == '__main__':
    lines = np.array([
        [[0., 0.], [8., 0.]],
        [[0., -1.], [6., 5.]],
        [[0., 7.], [8., -1.]],
        [[0., 3.], [5., -2.]],
        [[3., -2.], [8., 3.]]
    ])
    opt = optimize(lines)
    print("Found {} trianges with {} lines with lines:\n{}".format(int(-1 * opt.fun), len(lines), opt.x.reshape(opt.x.size // 4, 2, 2)))
