# Project imports
from libs.common.types import AxisType, PointTable2DType, is_of_type


class PointTable2D:

    def __init__(self, point_table: PointTable2DType) -> None:
        self.points = point_table

    @property
    def x_axis(self) -> AxisType:
        return [point[0] for point in self.points]
        
    @property
    def y_axis(self) -> AxisType:
        return [point[1] for point in self.points]

    @property
    def size(self) -> int:
        return len(self.points)

    def sort_by_axis(self, axis: str = 'x') -> None:
        axis_mapping = {
            'x': 0,
            'y': 1,
        }

        axis_index = axis_mapping.get(axis.lower())

        sorted_table = sorted(
            self.points,
            key=lambda point: point[axis_index]
        )

        self.points = sorted_table

    def __iadd__(self, input_table: PointTable2DType) -> object:
        if not is_of_type(input_table, PointTable2DType):
            raise ValueError(
                'You must provide a valid PointTable2DType in order to sum tables!'
            )

        summed_table = list(set(self.points + input_table))

        instance = PointTable2D(summed_table)
        instance.sort_by_axis()
        
        return instance
