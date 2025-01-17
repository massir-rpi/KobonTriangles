from scipy.optimize import dual_annealing
from count_triangles import count_triangle_flat_in_neg_out
from random_lines import gen_rand_lines
from view import plot_lines_in_circle

def optimize(lines_segments):
    return dual_annealing(
        func=count_triangle_flat_in_neg_out,
        bounds=[[-(2**32)+1,2**32-1]] * lines_segments.size,
        x0=lines_segments.flatten()
    )

if __name__ == '__main__':
    # lines = np.array([
    #     [[0., 0.], [8., 0.]],
    #     [[0., -1.], [6., 5.]],
    #     [[0., 7.], [8., -1.]],
    #     [[0., 3.], [5., -2.]],
    #     [[3., -2.], [8., 3.]],
    #     #[[0., -4.], [8., 2.]],
    #     #[[0., 8.], [8., -5.]],
    #     #[[0., 6.], [8., 4.]],
    #     #[[0., -3.], [8., 1.]],
    #     #[[0., 1.], [8., -3.]],
    #     #[[0., 2.], [8., -4.]],
    # ])
    N = 5
    zoom = 3
    lines = gen_rand_lines(N, zoom)
    opt = optimize(lines)
    opt_num_triangles = int(-1 * opt.fun)
    opt_lines = opt.x.reshape(opt.x.size // 4, 2, 2)
    plot_lines_in_circle(lines, zoom, "{}_seed.png".format(N))
    plot_lines_in_circle(opt_lines, zoom, "{}_opt_{}.png".format(N, opt_num_triangles))

    print("Found {} trianges with {} lines with:\n{}\n\nwith random seed:\n{}".format(opt_num_triangles, len(lines), opt_lines, lines))
    # print("Found {} trianges with {} lines with:\n{}\n\nwith random seed:\n{}".format(int(-1 * opt[1]), len(lines), opt[0].reshape(opt[0].size // 4, 2, 2), lines))
