
.. _gallery:

=======
Gallery
=======

Here we provide a gallery containing selected example results of several applications (a non-exhaustive list)
using SPUX framework for Bayesian inference and uncertainty quantification.

Randomwalk
----------

| Domain: demo.
| Authors: Jonas Šukys (Eawag, Switzerland).
| Model: one-dimensional random walk (built-in).
| Language: Python.
| Cluster: EULER (ETH Zurich, Switzerland) - 129 cores.

A simple one-dimensional randomwalk with uncertain origin, drift, and the observation error.

.. figure:: _static/randomwalk/randomwalk_predictions-posterior.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_predictions-posterior.cap

.. figure:: _static/randomwalk/randomwalk_posterior2d-origin-drift.png
   :align: center
   :scale: 15 %

   .. include:: _static/randomwalk/randomwalk_posterior2d-origin-drift.cap

Linear bucket
-------------

| Domain: hydrology.
| Authors: Andreas Scheidegger (Eawag, Switzerland).
| Model: linear bucket model with stochastic forcing.
| Language: R, with :code:`rpy2` bindings to Python.

Work in progress.

Stochastic inputs
-----------------

| Domain: hydrology.
| Authors: Jonas Šukys (Eawag, Switzerland).
| Model: hydrological model with stochastic inputs (built-in).
| Language: Python, with :code:`numba` compiled C code for computationally expensive parts.
| Cluster: EULER (ETH Zurich, Switzerland) - 1121 cores.

Publication: Del Giudice, D. et al., (2016) "Describing the catchment-averaged precipitation as a stochastic process improves parameter and input estimation;
Water Resources Research. John Wiley & Sons, Ltd, 52(4), pp. 3162–3186. doi: 10.1002/2015WR017871.

.. figure:: _static/hydro/hydro_errors-dataset-2.png
   :align: center
   :scale: 20 %

   The first dataset and the associated heteroscedastic error model for the input (precipitation) and the output (discharge) measurements.

.. figure:: _static/hydro/hydro_predictions-posterior-dataset-2-unbiased.png
   :align: center

   Plots of the posterior distribution of model predictions for an observational dataset above,
   including auxiliary posterior distributions for rainfall potential ``$\xi$``, reservoir level ``S``, and the water volume discrepancy ``$\Delta V$``.

Work in progress.

Stochastic parameters
---------------------

| Domain: hydrology.
| Authors: Marco Bacci, Jonas Šukys (Eawag, Switzerland).
| Model: hydrological model with stochastic time-dependent parameters (Superflex).
| Language: Fortran, with :code:`ctypes` bindings of the compiled Fortran model library to Python.

Work in progress.

Prey-Predator
-------------

| Domain: aquatic ecology.
| Authors: Jonas Šukys, Nele Schuwirth, Peter Reichert (Eawag, Switzerland), Mira Kattwinkel (University of Koblenz-Landau, Germany).
| Model: prey-predator model using stochastic individual based model with synthetic dataset (IBM-Bugs).
| Language: Java, with :code:`JPype` bindings to Python.
| Cluster: EULER (ETH Zurich, Switzerland) - up to 1000 cores.

Publication (preprint available at http://arxiv.org/abs/1711.01410):

.. code::

        Šukys, J. and Kattwinkel, M.
        "SPUX: Scalable Particle Markov Chain Monte Carlo
        for uncertainty quantification in stochastic ecological models".
        Advances in Parallel Computing - Parallel Computing is Everywhere,
        IOS Press, (32), pp. 159–168, 2018.

.. figure:: _static/ibm-bugs/predator-prey/mcmc-ibm-2000p-100s-200c_posterior_prey_kDens_predator_kDens.png
   :align: center
   :scale: 20 %

   Marginal posterior distribution of :code:`prey_kDens` and :code:`predator_kDens` parameters,
   including the corresponding MCMC chain from the sampler.
   Legend:
   green "+" - initial parameters.

Work in progress.

River invertebrates
-------------------

| Domain: aquatic ecology.
| Authors: Marco Bacci, Nele Schuwirth, Peter Reichert, Jonas Šukys (Eawag, Switzerland) Mira Kattwinkel (U Koblenz-Landau, Germany).
| Model: river invertebrates mesocosm modeling using stochastic IBMs (IBM-Bugs).
| Model: Java, with :code:`JPype` bindings to Python.
| Cluster: EULER (ETH Zurich, Switzerland) - 736 cores.

Work in progress.

DATALAKES
---------

| Domain: hydrology and data science.
| Authors: Artur Safin, Jonas Šukys (Eawag, Switzerland).
| Model: DATALAKES - a scalable UQ framework for predicting lake dynamics (MITgcm).
| Language: Fortran, with :code:`ctypes` bindings of the compiled Fortran model library to Python.
| Cluster: Daint (Swiss Supercomputing Center (CSCS), Switzerland).

Work in progress.

In-stream herbicides
--------------------

| Domain: aquatic ecology.
| Authors: Peter Reichert, Fabrizio Fenizia, Lorenz Ammann, Jonas Šukys (Eawag, Switzerland).
| Model: in-stream herbicide concentration dynamics (Superflex).
| Language: Fortran, with :code:`ctypes` bindings of the compiled Fortran model library to Python.

Work in progress.

Urban hydrology
---------------

| Domain: urban hydrology.
| Authors: Joao Leitao, Andreas Scheidegger, Jörg Rieckermann, Jonas Šukys.
| Model: urban hydrologic model (SWMM).
| Language: C, with :code:`Swig` wrapper for Python.

Work in progress.

Solar dynamo
------------

| Domain: physics and data science

BISTOM - calibration of the solar dynamo simulations.

Work in progress.
