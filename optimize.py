from scipy.optimize import dual_annealing
from count_triangles import count_triangle_flat_in_neg_out
import numpy as np

def optimize(lines):
    return dual_annealing(count_triangle_flat_in_neg_out, bounds=[[-(2**32)+1,2**32-1]]*lines.size, x0=lines.flatten())

if __name__ == '__main__':
    lines = np.array([
        [[0., 0.], [8., 0.]],
        [[0., -1.], [6., 5.]],
        [[0., 7.], [8., -1.]],
        [[0., 3.], [5., -2.]],
        [[3., -2.], [8., 3.]],
        #[[0., -4.], [8., 2.]],
        #[[0., 8.], [8., -5.]],
        #[[0., 6.], [8., 4.]],
        #[[0., -3.], [8., 1.]],
        #[[0., 1.], [8., -3.]],
        #[[0., 2.], [8., -4.]],
    ])
    opt = optimize(lines)
    print("Found {} trianges with {} lines with lines:\n{}".format(int(-1 * opt.fun), len(lines), opt.x.reshape(opt.x.size // 4, 2, 2)))
