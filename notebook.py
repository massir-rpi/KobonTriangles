import marimo

__generated_with = "0.9.16"
app = marimo.App(width="medium")


@app.cell
def __():
    from poly_point_isect import isect_segments, isect_segments_impl
    import numpy as np
    import seaborn as sns
    import itertools
    return isect_segments, isect_segments_impl, itertools, np, sns


@app.cell
def __():
    N = 3
    zoom_factor = 10
    return N, zoom_factor


@app.cell
def __(itertools):
    counter = itertools.count()

    class IdxTuple(tuple):
        def __new__(self, tup):
            #if 'idx' in kwargs:
            #    self.idx = kwargs['idx']
            obj = tuple.__new__(IdxTuple, tup)
            obj.idx = counter.__next__()
            #super().__init__(*args, **kwargs)
            return obj
    return IdxTuple, counter


@app.cell
def __(IdxTuple, N, np, zoom_factor):
    def totuple(a):
        if a.shape == ():
            return a.item()
        else:
            return IdxTuple(map(totuple, a))

    def generate_point_pairs_on_circle():
        angles = np.random.uniform(0, 2 * np.pi, (N, 2))
        angles_point2 = np.random.uniform(0, 2 * np.pi, (N, 4))

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

    return generate_point_pairs_on_circle, totuple


@app.cell
def __(generate_point_pairs_on_circle):
    line_segments = generate_point_pairs_on_circle()
    return (line_segments,)


@app.cell
def __(line_segments, zoom_factor):
    line_segments * zoom_factor
    return


@app.cell
def __(N, line_segments, zoom_factor):
    import matplotlib.pyplot as plt

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

    ax.set_xlim(-1.1*zoom_factor, 1.1*zoom_factor)
    ax.set_ylim(-1.1*zoom_factor, 1.1*zoom_factor)
    ax.set_aspect('equal', adjustable='box')

    plt.gca()
    return ax, circle, circle2, fig, i, plt, x1, x2, y1, y2


@app.cell
def __(line_segments, np):
    idx_dct = {l.tobytes(): i for i, l in enumerate(line_segments)}

    def to_idx(point_pair):
        return idx_dct[np.array(point_pair).tobytes()]
    return idx_dct, to_idx


@app.cell
def __(line_segments, totuple):
    [(l[0].idx, l[1].idx) for l in totuple(line_segments)]
    return


@app.cell
def __(line_segments, totuple):
    type(totuple(line_segments)[0][0][0])
    return


@app.cell
def __(isect_segments_impl, line_segments, totuple):
    tups = totuple(line_segments)
    idxs = [(l[0].idx, l[1].idx) for l in totuple(line_segments)]
    isects = isect_segments_impl(tups, include_segments=True)
    isect_coords = [i[0] for i in isects]
    isect_idx_pairs = [((i[1][0][0].idx, i[1][0][1].idx), (i[1][1][0].idx, i[1][1][1].idx)) for i in isects]
    return idxs, isect_coords, isect_idx_pairs, isects, tups


@app.cell
def __(isects):
    isect = isects[0][1]
    isect
    type(isect[0][1])
    return (isect,)


@app.cell
def __():
    return


@app.cell
def __(idxs, isect_idx_pairs):
    isect_idx_pairs, idxs
    return


@app.cell
def __(isects, tups):
    [i[1] for i in isects], tups
    return


@app.cell
def __(isects, tups):
    seti = set()
    for _i in isects:
        seti.add(_i[1][0])
        seti.add(_i[1][1])

    seti - set(tups)
    return (seti,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
