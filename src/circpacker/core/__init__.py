"""Core algorithms and domain models for circpacker."""

from circpacker.core.basegeom import Circle, Polygon, Triangle
from circpacker.core.packer import CircPacking
from circpacker.core.slopegeometry import AnthropicSlope, NaturalSlope

__all__ = [
    "AnthropicSlope",
    "Circle",
    "CircPacking",
    "NaturalSlope",
    "Polygon",
    "Triangle",
]
