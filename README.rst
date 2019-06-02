=============================
circpacker : Circle Packer
=============================

.. |made-with-python| image:: https://img.shields.io/badge/Made%20with-Python-brightgreen.svg?style=flat-square
   :target: https://www.python.org/
   
.. |License| image:: https://img.shields.io/badge/License-BSD%202--Clause-brightgreen.svg?style=flat-square
   :target: https://github.com/aarizat/circpacker/blob/master/LICENS

.. |docs| image:: https://readthedocs.org/projects/pc4bims/badge/?version=latest
   :target: https://circpacker.readthedocs.io/en/latest/?badge=latest

.. |orcid| image:: https://img.shields.io/badge/id-0000--0003--0619--8735-brightgreen.svg?style=flat-square
   :target: https://orcid.org/0000-0003-0619-8735

|made-with-python| |docs| |License| |ORCID|

``CircPacker`` is an application software in **Python 3** to create circle packing
in closed polygons.


.. figure:: https://raw.githack.com/aarizat/circpacker/master/figures/polygon_Irreg.svg
        :alt: plot example1


Features
--------

* Free software: `BSD-2-Clause <https://opensource.org/licenses/BSD-2-Clause>`_.
* Documentation: https://circpacker.readthedocs.io.

Requirements
------------

The code was written in Python 3. The packages `numpy <http://www.numpy.org/>`_,
`scipy <https://www.scipy.org/>`_, `matplotlib <https://matplotlib.org/>`_
and `triangle <http://dzhelil.info/triangle/index.html#>`_ are
required for using ``circpacker``. All of them are
downloadable from the PyPI repository by opening a terminal and typing the
following code lines:


::

    pip install numpy
    pip install scipy
    pip install matplotlib
    pip install triangle


Installation
------------


To install ``circpacker`` open a terminal and type:

::

    pip install circpacker


Examples
-------

To produce the plot shown above execute the following script

::

    from numpy import array
    from circpacker.basegeom import Polygon
    from circpacker.packer import CircPacking as cp
    coordinates = array([[1, 1], [2, 5], [4.5, 6], [8, 3], [7, 1],
                         [4, 0]])
    polygon = Polygon(coordinates)
    boundCoords = polygon.boundCoords
    CircPack = cp(boundCoords, depth=10)
    CircPack.plot(plotTriMesh=True)


Now, let's see an example for a autosimilar ``bimsoil`` model.


::

    from numpy import array
    import matplotlib.pyplot as plt
    from circpacker.basegeom import Polygon
    from circpacker.packer import CircPacking as cp
    from circpacker.slopegeometry import AnthropicSlope

    h = 15 # slope height
    slopeGeometry = AnthropicSlope(h, [1, 1.5], 2/3*h, 2/3*h, 1/3*h)
    boundCoords = slopeGeometry.boundCoords
    polygon = Polygon(boundCoords)
    CircPack = cp(boundCoords, minAngle=20, maxArea=0.35*polygon.area, length=0.05*h)
    CircPack.plot(plotTriMesh=True)

For a simple slope with h=15 m, inclination H:V of 1:1.5, crown and foot lengths of 2/3h, and
depth 1/3h. Minimum angle and maximum area for each Delaunay triangle of 20° and 35% of slope area, respectively.

.. figure:: https://raw.githack.com/aarizat/circpacker/master/figures/autosim_slope.svg
        :alt: plot example2

