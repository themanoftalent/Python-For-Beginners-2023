
.. _installation:

============
Installation
============

Python package spux is available at PyPI repository: https://pypi.org/project/spux.

Main prerequisites
------------------

- Python, we recommend using Python 3.

  - in macOS, pre-installed
  - in Debian/Ubuntu, pre-installed
  - in Windows, follow instructions in https://www.python.org/downloads/windows/
  - to test, run in terminal: :code:`python3 -V`

- Open MPI:

  - in macOS with Homebrew, in terminal: :code:`brew open-mpi`
  - in Debian/Ubuntu with Apt, in terminal:
    :code:`apt-get install openmpi-bin libopenmpi-dev`
  - in Windows, the parallel version of the framework has not been tested yet

- SPUX Package, in terminal:

  .. code-block:: console

      $ pip3 install --user --upgrade pip
      $ pip3 install --user spux

Remember, that if you reinstall or somehow else change your MPI library,
you must reinstall :code:`mpi4py` package by running in terminal:

.. code-block:: console

    $ pip3 install --user --upgrade pip
    $ pip3 install --user --upgrade --force-reinstall --no-cache-dir mpi4py

Additional prerequisites
------------------------

Depending on the programming language of your model, additional prerequisites might be needed:

- R driver: R package, and in terminal: :code:`$ pip3 install --user rpy2`,
- Julia driver: Julia package :code:`PyCall`, and in terminal: :code:`$ pip3 install --user julia`,
- Fortran driver: Fortran compiler (if needed), and in terminal: :code:`$ pip3 install --user ctypes`,
- C/C++ driver: C/C++ compiler (if needed), and Swig (http://www.swig.org/) code wrapper,
- Java driver: Java SDK, and in terminal: :code:`$ pip3 install --user Jpype1`.

If you additionally want the generated LaTeX report source files to be compiled to the PDF files,
then you will need to have the ``pdflatex`` installed
(the procedure varies depending on the OS and distribution and hence is not described here).

Stable release
--------------

To install spux, run this command in your terminal:

.. code-block:: console

    $ pip install spux

This is the preferred method to install spux, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

To update when a newer release becomes available, run in your terminal:

.. code-block:: console

    $ pip install --user --upgrade spux

Latest release
--------------

To install the latest development version of spux, run these commands in your terminal:

.. code-block:: console

    $ git clone --single-branch --branch test https://gitlab.com/siam-sc/spux.git
    $ cd spux
    $ python setup.py install --user

To update when a newer version of the :code:`test` branch becomes available,
run in your terminal (within the :code:`spux` directory from above):

.. code-block:: console

    $ git pull
    $ python setup.py install --user

If you use latest version of SPUX, please also
refer to the latest version of documentation at: https://spux.readthedocs.io/en/latest/.

From sources
------------

The sources for spux can be downloaded from the https://gitlab.com/siam-sc/spux.

You can also clone the public repository:

.. code-block:: console

    $ git clone https://gitlab.com/siam-sc/spux.git
