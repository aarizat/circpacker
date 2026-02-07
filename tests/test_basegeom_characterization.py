"""Characterization tests for geometric primitives."""

import numpy as np
import pytest

from circpacker.basegeom import Circle, Polygon, Triangle


def test_circle_properties_are_stable() -> None:
    circle = Circle(center=(2, 5), radius=2.5)

    assert circle.curvature == 0.4
    assert circle.diameter == 5.0
    assert circle.area == 19.634954084936208
    assert circle.perimeter == 15.707963267948966


def test_descartes_special_case_keeps_tangency() -> None:
    circle = Circle((4.405957, 2.67671461), 0.8692056336001268)
    circle1 = Circle((3.22694724, 2.10008003), 0.4432620600509628)
    c2, c3 = circle.descartesTheorem(circle1)

    assert c2.radius == c3.radius
    assert np.isclose(
        np.linalg.norm(c2.center - circle.center),
        circle.radius + c2.radius,
    )
    assert np.isclose(
        np.linalg.norm(c2.center - circle1.center),
        circle1.radius + c2.radius,
    )


def test_triangle_incircle_and_depth_zero_output() -> None:
    triangle = Triangle(np.array([(2, 1.5), (4.5, 4), (6, 2)]))

    assert triangle.area == 4.375
    assert triangle.perimeter == 10.066662780082012
    assert triangle.incircle.radius == 0.8692056336001268
    assert np.allclose(triangle.incircle.center, np.array([4.405957, 2.67671461]))
    assert len(triangle.circInTriangle(depth=0)) == 1


def test_triangle_length_alias_is_backward_compatible() -> None:
    coords = np.array([(2, 1.5), (4.5, 4), (6, 2)])
    legacy = Triangle(coords).circInTriangle(lenght=0.5)
    preferred = Triangle(coords).circInTriangle(length=0.5)

    assert len(legacy) == len(preferred)


def test_triangle_length_alias_rejects_conflicting_values() -> None:
    triangle = Triangle(np.array([(2, 1.5), (4.5, 4), (6, 2)]))

    with pytest.raises(ValueError):
        triangle.circInTriangle(lenght=0.5, length=0.25)


def test_polygon_area_is_stable() -> None:
    polygon = Polygon(np.array([[1, 1], [2, 5], [4.5, 6], [8, 3], [7, 1], [4, 0]]))

    assert polygon.area == 27.5
