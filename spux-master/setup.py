#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

build_commands = (
    "build",
    "build_ext",
    "build_py",
    "build_clib",
    "build_scripts",
    "bdist_wheel",
    "bdist_rpm",
    "bdist_wininst",
    "bdist_msi",
    "bdist_mpkg",
    "build_sphinx",
    "develop",
)

readme = "\
SPUX is a modular framework for Bayesian inference and uncertainty quantification. \
SPUX can be coupled with linear and nonlinear, deterministic and stochastic models. \
SPUX supports model in any programming language (e.g. Python, R, Julia, C/C++, Fortran, Java). \
SPUX scales effortlessly from serial run to parallel high performance computing clusters. \
SPUX is application agnostic, with current examples in environmental data sciences. \
\
SPUX is actively developed at Eawag, Swiss Federal Institute of Aquatic Science and Technology, \
by researchers in the High Performance Scientific Computing Group, https://www.eawag.ch/sc. \
For the scientific website of the SPUX project, please refer to https://eawag.ch/spux. \
\
Documentation is available at https://spux.readthedocs.io. \
Source code respository is available at https://gitlab.com/siam-sc/spux. \
\
You are welcome to browse through the results gallery of the models already coupled to spux at https://spux.readthedocs.io/en/stable/gallery.html. \
\
This is free software, distributed under Apache (v2) License."

# if any(command in build_commands for command in sys.argv[1:]):

#     # reading package files here is dangerous, pip e.g. only reads setup.py to
#     # find dependendies, and at this time README.rst and or HISTORY.rst might
#     # not be present at all. The effect is that pip fails, this gets even more
#     # dangerous when spux is declared as requiremnts in other packages.

#     with open("README.rst") as readme_file:
#         readme = readme_file.read()

#     with open("HISTORY.rst") as history_file:
#         history = history_file.read()

requirements = [
    "numpy",
    "sympy",
    "mpi4py",
    "pandas",
    "setuptools",
    "Cython",
    "scipy",
    "matplotlib",
    "cloudpickle",
    "pycallgraph",
    "numba",
    "gprof2dot",
    "suftware",
    "pygit2",
    "reprozip",
    "pylatex",
]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setuptools.setup(
    author = "Jonas Šukys, Marco Bacci, Uwe Schmitt, Mikołaj Rybiński",
    author_email="jonas.sukys@eawag.ch, marco.bacci@eawag.ch, "
                 "uwe.schmitt@id.ethz.ch, mikolaj.rybinski@id.ethz.ch",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    description="SPUX: Scalable Package for Uncertainty Quantification",
    install_requires=requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="Bayesian inference using hpc",
    name="spux",
    packages=setuptools.find_packages(include=["spux"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://gitlab.com/siam-sc/spux/",
    ext_modules=[],
    version="0.4.0",
    zip_safe=False,
)
