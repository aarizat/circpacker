"""Compatibility tests for public import paths."""

import numpy as np

from circpacker.basegeom import Circle as PublicCircle
from circpacker.core.basegeom import Circle as CoreCircle
from circpacker.core.packer import CircPacking as CoreCircPacking
from circpacker.core.slopegeometry import AnthropicSlope as CoreAnthropicSlope
from circpacker.packer import CircPacking as PublicCircPacking
from circpacker.slopegeometry import AnthropicSlope as PublicAnthropicSlope


def test_geometry_public_imports_keep_identity() -> None:
    assert PublicCircle is CoreCircle


def test_packer_public_imports_keep_identity() -> None:
    assert PublicCircPacking is CoreCircPacking


def test_slope_public_imports_keep_identity() -> None:
    assert PublicAnthropicSlope is CoreAnthropicSlope


def test_circpacking_keeps_length_and_lenght_attributes() -> None:
    coordinates = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    model = PublicCircPacking(coordinates, depth=0, length=0.1)

    assert model.length == 0.1
    assert model.lenght == 0.1
