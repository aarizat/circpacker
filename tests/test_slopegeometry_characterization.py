"""Characterization tests for slope geometry helpers."""

import numpy as np

from circpacker.slopegeometry import AnthropicSlope, NaturalSlope


def test_anthropic_slope_outputs_stable_geometry() -> None:
    slope = AnthropicSlope(12, [1, 1.5], 10, 10)

    assert np.isclose(slope.maxDepth, 4.571428571428573)
    assert slope.boundCoords.shape == (7, 2)
    assert np.array_equal(slope.boundCoords[0], np.array([0, 0]))
    assert np.array_equal(slope.boundCoords[-1], np.array([0, 0]))


def test_natural_slope_outputs_stable_geometry() -> None:
    surface_coords = np.array(
        [
            [0.0, 16.57142857],
            [10.0, 16.57142857],
            [18.0, 4.57142857],
            [28.0, 4.57142857],
        ]
    )
    slope = NaturalSlope(surface_coords)

    assert np.isclose(slope.maxDepth, 4.571428571428575)
    assert slope.boundCoords.shape == (7, 2)
    assert np.array_equal(slope.boundCoords[0], np.array([0.0, 0.0]))
    assert np.array_equal(slope.boundCoords[-1], np.array([0.0, 0.0]))
