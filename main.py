#!/usr/bin/env python

# Base imports
from pprint import pprint

# Project imports
from libs.common.types import PointTable2DType
from libs.graphics.plotting import plot_interpolation
from libs.interpolation.methods import Lagrange
from libs.points.plane import PointTable2D


# Edit the known points here
INITIAL_CURVE_POINTS: PointTable2DType = [
    (2, 2),
    (5, 8),
    (8, 2),
]

# Include the points to be interpolated here
NEW_POINTS: PointTable2DType = [
    (3, None),
    (4, None),
    (6, None),
    (7, None),
]


if __name__ == '__main__':
    try:
        # Fixed points with known values of f(x)
        known_points = PointTable2D(INITIAL_CURVE_POINTS)

        # Points to be included in the interpolation
        new_points = PointTable2D(NEW_POINTS)

        # Interpolated points
        interpolated_points = Lagrange.interpolate(known_points, new_points)

        pprint(interpolated_points.points)

        plot_interpolation(interpolated_points, known_points)

    except Exception as exc:
        print(f'{exc.__class__.__name__}: {str(exc)}')
