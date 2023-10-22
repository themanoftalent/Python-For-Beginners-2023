
.. _parallelization:

===============
Parallelization
===============

Here we briefly describe parallelization algorithms,
including communication patterns, load balancing strategies,
and experimental results for parallelization profiling and scaling.

Communication patterns
----------------------

.. figure:: _static/schemes/PF_resample.png
   :align: center

   Adaptive parallel resampling algorithm used in the SPUX framework.

Profiling and scaling
---------------------

.. figure:: _static/ibm-bugs/predator-prey/mcmc-ibm-2000p-100s-200c_timestamps-S00050-all.png
   :align: center

   Timestamps of within a single Particle Filter likelihood evaluation.

.. figure:: _static/ibm-bugs/predator-prey/mcmc-ibm-2000p-100s_scaling.png
   :align: center
   :scale: 20 %

   Strong parallel scaling on Euler supercomputer at ETH Zurich, Switzerland.
