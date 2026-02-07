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

``circpacker`` now targets Python 3.12+ and uses `uv <https://docs.astral.sh/uv/>`_
for environment and dependency management.


Installation and development
----------------------------

Clone the repository and sync dependencies:

::

    uv sync

Run tests:

::

    uv run pytest -q

Run format and lint checks:

::

    uv run ruff format --check .
    uv run ruff check .

Run static type checks:

::

    uv run mypy

Run Python examples/scripts:

::

    uv run python -c "import circpacker; print(circpacker.__version__)"


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

More information
----------------

Here is a list of papers based on ``circpacker``.

* `Revista de la Facultad de Ciencias de la Universidad Nacional de Colombia <https://revistas.unal.edu.co/index.php/rfc/article/view/72343>`_
* `Challenges and Innovations in Geomechanics <https://link.springer.com/chapter/10.1007%2F978-3-030-64518-2_87>`_

