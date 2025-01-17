from scipy.optimize import dual_annealing
from count_triangles import count_triangles_angles_in_neg_out
from gen_lines import angles_to_lines, gen_rand_angles
from view import plot_lines_in_circle

def optimize(angles):
    return dual_annealing(
        func=count_triangles_angles_in_neg_out,
        bounds=[[-100,100]] * angles.size,
        x0=angles.flatten(),
        # maxiter=10000,
        # restart_temp_ratio=2.e-2,
        # accept=-500,
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
    zoom = 2
    # lines = gen_rand_lines(N, zoom)
    angles = gen_rand_angles(N)
    lines = angles_to_lines(zoom, angles)
    opt = optimize(angles)
    opt_num_triangles = int(-1 * opt.fun)
    # opt_lines = opt.x.reshape(opt.x.size // 4, 2, 2)
    opt_lines = angles_to_lines(zoom, opt.x)
    plot_lines_in_circle(lines, zoom, "{}_seed.png".format(N))
    plot_lines_in_circle(opt_lines, zoom, "{}_opt_{}.png".format(N, opt_num_triangles))

    print("Found {} trianges with {} lines with:\n{}\n\nwith random seed:\n{}".format(opt_num_triangles, len(lines), opt_lines, lines))
    # print("Found {} trianges with {} lines with:\n{}\n\nwith random seed:\n{}".format(int(-1 * opt[1]), len(lines), opt[0].reshape(opt[0].size // 4, 2, 2), lines))
