# KobonTriangles

This is a small computational geometry project whose goal is to make progress on the Kobon Triangle problem. 

For an input number of lines, `optimize.py` will use dual annealing to maximize the number of non-intersecting triangles that can be formed. It does this by rotating the endpoints of the lines around a circle.

## Highlights
- Generate random lines from angle parameters and clip them to a circle.
- Count triangles formed by segment intersections using a robust segment intersection routine.
- Optimize line angles (using simulated annealing) to search for arrangements with many triangles.
- Output PNG visualizations of seed and optimized layouts.

## Requirements
- Python 3.8+ (development used CPython 3.8/3.9)
- numpy
- scipy
- matplotlib

The project depends on the bundled segment intersection implementation (isect_segments-bentley_ottmann). You can either install that package in editable mode or ensure the package directory is on your PYTHONPATH.

## Install
From the repository root, create a virtual environment and install the Python dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install numpy scipy matplotlib

# Option 1: install the bundled intersection package in editable mode
pip install -e ./isect_segments-bentley_ottmann

# Option 2: add the package folder to PYTHONPATH (quick, for experiments)
export PYTHONPATH="$PYTHONPATH:$(pwd)/isect_segments-bentley_ottmann"
```

## Quick usage

Count triangles in a small hard-coded example:

```bash
python count_triangles.py
```

Generate a random arrangement and run the optimizer (this produces PNG files):

```bash
python optimize.py
```

By default `optimize.py` will:
- generate N random lines (controlled by the `N` variable in the script)
- run a dual annealing optimizer to (locally) maximize the number of triangles
- save two PNG images: `<N>_seed.png` and `<N>_opt_<triangles>.png`

Files of interest
- `count_triangles.py` — counts triangles from a list of line segments; also exposes helpers to count from angle parameters.
- `gen_lines.py` — generate lines from angles and utility functions to sample random angles.
- `optimize.py` — runs an optimizer (scipy.dual_annealing) over angle parameters to maximize triangle counts and writes visualization PNGs.
- `view.py` — plotting helper (`plot_lines_in_circle`) that makes PNGs with high DPI.
- `util.py` — small helper utilities.
- `isect_segments-bentley_ottmann/` — bundled third-party segment intersection implementation used to find segment intersections. See that folder for its tests and license.

Development notes
- The optimizer is configured for experimentation; parameters like `maxiter` and `accept` are set in `optimize.py` and can be tuned.
- When iterating on large N or heavy optimization, expect long run times; use smaller N to iterate quickly.
- The plotting function saves at 600 DPI by default in `view.py` — adjust `dpi` or `plot_lines_in_circle` if you need lower-res images.
