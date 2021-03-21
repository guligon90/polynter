# Project imports
from libs.common.types import AxisType, NumberType, PointTable2DType
from libs.points.plane import PointTable2D


class Lagrange:
    """
    Performs the the interpolation of the points
    using the Lagrange polynomial method:
    https://en.wikipedia.org/wiki/Lagrange_polynomial
    """

    @staticmethod
    def _eval_product_sum(
        x_value: NumberType,
        fixed_x_index: int,
        known_x_axis: AxisType
    ) -> NumberType:
        """
        Helper function that calculates the product,
        i.e., L_(n,k)(x),  for each summation term
        """
        i = 0
        product_value = 1.0

        while i < len(known_x_axis):
            if i != fixed_x_index:
                product_value *= (x_value - known_x_axis[i])/(known_x_axis[fixed_x_index] - known_x_axis[i])
            i += 1

        return product_value

    @staticmethod
    def interpolate(known_points: PointTable2D, new_points: PointTable2D) -> PointTable2D:
        """
        Do the interpolation.
        """
        known_x_axis = known_points.x_axis
        known_y_axis = known_points.y_axis
        interpolated_table = PointTable2D(known_points.points)

        for point in new_points.points:
            sum = 0.0
            for k in range(0, known_points.size):
                sum += known_y_axis[k]*Lagrange._eval_product_sum(point[0], k, known_x_axis)

            interpolated_table += [(point[0], sum)]

        return interpolated_table


class NewtonDividedDifferences:
    """
    Performs the the interpolation of the points
    using the Newton method of divided differences:
    https://en.wikipedia.org/wiki/Newton_polynomial
    """
    pass
