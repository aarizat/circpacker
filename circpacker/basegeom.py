# -*- coding: utf-8 -*-
'''Module to define the ``Triangle``, ``Circle`` and ``Polygon`` classes. Some
properties related to the geometry of these classes are determined.
These classes are the basic inputs to pack circular particles in a
closed polygon in :math:`\\mathbb{R}^2`.
'''


import numpy as np
import numpy.typing as npt
# import matplotlib.pyplot as plt

Point = npt.ArrayLike[float, float]
Vertices = npt.ArrayLike[Point, Point, Point]


class Circle:
    '''Creates instances of circes objects.

    Attributes:
        center (`tuple` or `list`): (x, y)-cartesian coordinates of\
            circle center.
        radius (`float` or `int`): Length of the segment that joins the center\
            with any point of the circumference.

    Examples:
        >>> center, radius = (0, 0), 1
        >>> circle = Circle(center, radius)
        >>> circle.__dict__
        {'area': 3.141592653589793,
         'center': array([0, 0]),
         'curvature': 1.0,
         'diameter': 2,
         'perimeter': 6.283185307179586,
         'radius': 1}

        >>> center, radius = (2, 5), 2.5
        >>> circle = Circle(center, radius)
        >>> circle.__dict__
        {'area': 19.634954084936208,
        'center': array([2, 5]),
        'curvature': 0.4,
        'diameter': 5.0,
        'perimeter': 15.707963267948966,
        'radius': 2.5}

    Note:
        The class ``Circle`` requires `NumPy <http://www.numpy.org/>`_
    '''

    def __init__(self, center: Point = np.array([0.0, 0.0]), radius: float = np.inf):
        self.center = center
        self.radius = radius
        self._curvature = None
        self._diameter = None
        self._area = None
        self._perimeter = None

    @property
    def curvature(self):
        self._curvature = 1 / self.radius
        return self._curvature

    @property
    def diameter(self):
        self._diameter = 2 * self.radius
        return self._diameter

    @property
    def area(self):
        self._area = np.pi * self.radius**2
        return self._area

    @property
    def perimeter(self):
        self._perimeter = 2 * self.radius * np.pi
        return self._perimeter


class Triangle:
    '''Creates an instance of an object that defines a Triangle once the
    coordinates of its three vertices in cartesian :math:`\\mathbb{R}^2` space
    are given.

    It considers the usual notation for the triangle ``ABC`` in which `A`, `B`
    and `C` represent the vertices and ``a``, ``b``, ``c`` are the
    lengths of `the segments BC`, `CA` and `AB` respectively.

    Attributes:
        coordinates ((3, 2) `numpy.ndarray`): Coordinates of three vertices\
            of the triangle.

    Note:
        The class ``Triangle`` requires `NumPy <http://www.numpy.org/>`_,
        `SciPy <https://www.scipy.org/>`_\
        and `Matplotlib <https://matplotlib.org/>`_.

    Examples:
        >>> from numpy import array
        >>> from circpacker.basegeom import Triangle
        >>> coords = array([(2, 1.5), (4.5, 4), (6, 2)])
        >>> triangle = Triangle(coords)
        >>> triangle.__dict__.keys()
        dict_keys(['vertices', 'area', 'sides', 'perimeter', 'distToIncenter',
                   'incircle'])

        >>> from numpy import array
        >>> from circpacker.basegeom import Triangle
        >>> coords = array([[2, 1], [6, 1], [4, 5.5]])
        >>> triangle = Triangle(coords)
        >>> triangle.__dict__.keys()
        dict_keys(['vertices', 'area', 'sides', 'perimeter', 'distToIncenter',
                   'incircle'])
    '''

    def __init__(self, vertices: Vertices):
        self.vertices = vertices
        self._area = None
        self._perimeter = None

    @property
    def area(self) -> float:
        v1 = self.vertices[0] - self.vertices[1]
        v2 = self.vertices[0] - self.vertices[2]
        self._area = 0.5 * abs(np.linalg.norm(np.cross(v1, v2)))
        return self._area

    @property
    def perimeter(self) -> float:
        self._perimeter = sum(self._triangle_side_lengths(self.vertices).values())
        return self._perimeter

    @property
    def incircle(self) -> Circle:
        radius = 2 * self.area / self.perimeter
        x = sum(
                np.array(v) * length 
                for v, length in self._triangle_side_lengths(self.vertices)
        )
        center = x / self.perimeter
        return Circle(center, radius)

    @staticmethod
    def _triangle_side_lengths(vertices: Vertices) -> dict[tuple, float]:
        return {
            tuple(vertices[0]): np.linalg.norm(vertices[1] - vertices[2]),
            tuple(vertices[1]): np.linalg.norm(vertices[0] - vertices[2]),
            tuple(vertices[2]): np.linalg.norm(vertices[0] - vertices[1]),
        }


def _mutually_tangent(c1: Circle, c2: Circle, c3: Circle) -> bool:
    ...
    # TODO


def get_descartes_circles(c1: Circle, c2: Circle, c3: Circle) -> list[Circle]:
    """ Applying Descartes' theorem
    """
    ...
    # TODO


def incircles_triangle(tri: Triangle) -> list[Circle]:
    ...
    # TODO


class Polygon:
    '''Creates an instance of an object that defines a Polygon once the
    cartesian coordinates of its vertices are given.

    Attributes:
        coordinates ((n, 2) `numpy.ndarray`): Coordinates of the vertices\
            of the polygon.
    '''

    def __init__(self, coordinates):
        '''Method for initializing the attributes of the class.'''
        self.coordinates = coordinates
        self.boundCoords = np.vstack((coordinates, coordinates[0]))
        self.area()

    def area(self):
        '''Method for determine the area of the polygon.

        Returns:
            area (`float`): area of the polygon surface.

        Examples:
            >>> from numpy import array
            >>> from circpacker.basegeom import Polygon
            >>> coords = array([(1, 1), (4, 8), (8, 5)])
            >>> polygon = Polygon(coords)
            >>> polygon.area
            18.5

            >>> from numpy import array
            >>> from circpacker.basegeom import Polygon
            >>> coords = array([[1, 1], [2, 5], [4.5, 6], [8, 3],
                                [7, 1], [4, 0]])
            >>> polygon = Polygon(coords)
            >>> polygon.area
            27.5
        '''
        # polygon area by applying the gauss equation
        area = 0.5*abs(sum(self.boundCoords[:-1, 0] * self.boundCoords[1:, 1] -
                           self.boundCoords[:-1, 1] * self.boundCoords[1:, 0]))
        setattr(self, 'area', area)
        return area

    def plot(self):
        '''Method for show the graph of the polygon.

        Examples:

            .. plot::

                from numpy import array
                from circpacker.basegeom import Polygon
                coords = array([[1, 1], [2, 5], [4.5, 6], [8, 3],
                                [7, 1], [4, 0]])
                polygon = Polygon(coords)
                polygon.plot()
        '''

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self.boundCoords[:, 0], self.boundCoords[:, 1], '-k', lw=2)
        ax.plot(self.coordinates[:, 0], self.coordinates[:, 1], 'ok', ms=5)
        ax.grid(ls='--', lw=0.5)
        ax.axis('equal')
        return


# %%
'''
BSD 2 license.

Copyright (c) 2018, Universidad Nacional de Colombia, Andres Ariza-Triana
and Ludger O. Suarez-Burgoa.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
