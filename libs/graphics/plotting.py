# Third-party imports
import matplotlib.pyplot as plotter

# Project imports
from libs.points.plane import (
    is_of_type,
    PointTable2D,
)


def plot_interpolation(
    interpolated_table: PointTable2D,
    known_table: PointTable2D,
    plot_img_file_path: str = 'img/interpolations.png',
    show_plot: bool = False,
) -> None:
    """
    Function that receives the known intial and interpolated
    points tables and generates a x-y plot.
    """
    type_condition = is_of_type(interpolated_table, PointTable2D) \
        and is_of_type(known_table, PointTable2D)

    if not type_condition:
        raise TypeError('Interpolated table must be of type PointTable2D!')

    # Creating plotting handlers
    figure_handler, axis_handler = plotter.subplots()

    # Plotting the interpolated points
    axis_handler.plot(
        interpolated_table.x_axis,
        interpolated_table.y_axis,
        'go',
        label='Método de Lagrange'
    )

    # Plotting the known points
    axis_handler.plot(
        known_table.x_axis,
        known_table.y_axis,
        'ko',
        label='Pontos originais'
    )

    # Setting axis labels
    axis_handler.set(
        xlabel='x',
        ylabel='y = f(x)',
        title='Interpolação das posições do sprite'
    )

    # Creating legend
    axis_handler.legend(
        loc='lower center',
        shadow=True,
    )

    # Setting plot grid
    axis_handler.grid()

    figure_handler.savefig(plot_img_file_path)
    print(f'Plot image succesfully generated in {plot_img_file_path}')

    if show_plot:
        plotter.show()
