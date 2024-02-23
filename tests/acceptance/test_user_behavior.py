import math
import numpy as np
from random import random
import datetime

from uniplot import plot, plot_to_string


def test_normal_plotting():
    x = [math.sin(i / 20) + i / 300 for i in range(600)]
    plot(xs=x, ys=x, title="Sine wave")


def test_normal_plotting_to_string():
    x = [math.sin(i / 20) + i / 300 for i in range(600)]
    plot_to_string(xs=x, ys=x, title="Sine wave")


def test_plotting_with_forced_ascii():
    x = [1, 3, -2]
    strs = plot_to_string(xs=x, ys=x, title="Sine wave in ASCII", force_ascii=True)
    assert "█" in "".join(strs)


def test_normal_plotting_with_x_series():
    x = [math.sin(i / 20) + i / 300 for i in range(600)]
    plot(xs=x, ys=x, title="Diagonal")


def test_logarithmic_plotting():
    xs = range(1, 1000, 20)
    ys = [x**2 + 1e-6 for x in xs]
    plot(xs=xs, ys=ys, x_as_log=True, y_as_log=True)


def test_logarithmic_plotting_should_silently_ignore_invalid_values():
    ys = [-1.0, 0.0, 1.0, np.nan, 20.09, None, 12.2]
    plot(xs=ys, ys=ys, x_as_log=True, y_as_log=True)


def test_logarithmic_plotting_should_silently_ignore_invalid_values_even_in_2dim_case():
    ys = [-1.0, 0.0, 1.0, np.nan, 20.09, None, 12.2]
    plot([ys, ys], x_as_log=True, y_as_log=True)


def test_multi_series_plotting():
    ys = [
        [math.sin(i / (10 + i / 50)) - math.sin(i / 100) for i in range(1000)],
        # Make sure we also support plotting series of different length
        [math.sin(i / (10 + i / 50)) - math.sin(i / 100) - 1 for i in range(800)],
    ]
    plot(ys, title="Double sine wave", color=True)


def test_massively_multi_series_plotting():
    many_single_dot_series = [[math.sin(i / 20) + i / 300] for i in range(600)]
    plot(many_single_dot_series, title="Many colored dots", color=True)


def test_just_single_point_plotting():
    """
    Testing this because this has caused problems since for a single point min == max
    """
    x = [2.34]
    plot(x)


def test_random_line_plotting():
    xs = [random() for _ in range(100)]
    ys = [random() for _ in range(100)]
    plot(xs=xs, ys=ys, lines=True)


def test_plotting_time_series_with_bounds_set_manually():
    dates = np.arange("2024-02-17T09:21", 4 * 60, 60, dtype="M8[m]")
    plot(xs=dates, ys=[1, 2, 3, 2], x_min=dates[0], x_max=dates[-1])


def test_plotting_time_series_with_auto_bounds():
    dates = np.arange("2024-02-17T09:21", 4 * 60, 60, dtype="M8[m]")
    plot(xs=dates, ys=[1, 2, 3, 2], x_min=dates[0], x_max=dates[-1])


def test_plotting_time_series_with_python_date_objects():
    dates = [datetime.date(year=2024, month=2, day=i) for i in range(1, 5)]
    plot(xs=dates, ys=[1, 2, 3, 2])


def test_plotting_time_series_with_python_datetime_objects():
    dates = [
        datetime.datetime(year=2024, month=2, day=i, hour=10, minute=5)
        for i in range(1, 5)
    ]
    plot(xs=dates, ys=[1, 2, 3, 2])


def test_just_pass_objects_as_labels_works_as_well():
    class TestClass:
        def __init__(self, x):
            self.x: int = int(x)

        def __str__(self) -> str:
            return f"TestClass via str(x={self.x})"

        def __repr__(self) -> str:
            return f"TestClass via repr(x={self.x})"

    objects = [TestClass(1), TestClass(12), TestClass(123)]
    values = [[0, instance.x] for instance in objects]
    plot(values, title=objects[0], legend_labels=objects, lines=True)
