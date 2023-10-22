
.. _CUSTOMIZATION:

=============
Customization
=============

This section discusses the peculiarities of coupling your model with the framework
(the most common use case of SPUX),
including some guidelines on writing a custom posterior sampler
or a custom likelihood module and using it within SPUX.
You are welcome to browse through the results of the models already coupled to spux in the :ref:`gallery`.

Adding a model
--------------

In the most common use scenario of SPUX, you will want to implement your own Python model class,
which will wrap your existing application to the SPUX framework.
To avoid any confusion between these two concepts, we try to refer to your existing application (in any pogramming language)
as the "application", and to the Python class coupling your application to the SPUX framework as the "model".
While reading these instructions, make sure to take a look at the base Model class at
`spux/models/model.py <https://gitlab.com/siam-sc/spux/tree/test/spux/models/model.py>`_.
There, extensive comments describe the requirements and many additional helper variables
available within all model methods from the base model class.

You will need to create a new file with your model class derived from this base :code:`Model` class.
To have an idea what is required, take a look at the code
for the Randomwalk model used in :ref:`tutorial`.

Model test script
~~~~~~~~~~~~~~~~~

To test any modifications or new additions to the model class,
we recommend to use a dataset synthesis script for debugging purposes.
We recommend to adapt a respective ``script_synthesize.py`` script from any of these examples:

* `examples/strightwalk/script_synthesize.py <https://gitlab.com/siam-sc/spux/tree/test/examples/straightwalk/script_synthesize.py>`_
  for a deterministic model,
* `examples/randomwalk/script_synthesize.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/script_synthesize.py>`_
  for a stochastic model,
* `examples/randomwalk-replicates/script_synthesize.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk-replicates/script_synthesize.py>`_
  as above, but with replicate datasets.

As explained in :ref:`tutorial`, these scripts only need the exact parameters to be specified.
No need for exact model predictions - these will be generated.
At this point, we also suggest to start with no error model, that is ``error = None``.
The error model will become relevant only once the model is fully implemented,
and you will switch from dataset synthesis using ``script_synthesize.py`` to running complete
Bayesian inference using SPUX as described in :ref:`tutorial`.
Note, that even if the synthetically generated dataset(s) (that is, by specifying the error model)
are usually scientifically irrelevant (since you want to perform the Bayesian inference using the real dataset(s)),
the inference using such dataset(s) still provides an invaluable resource for making sure the correctness of your implementation.

If your model is (or is intended to become) stochastic and you will be using the ``PF`` likelihood,
we do recommend to start with resampling disabled by setting ``noresample=1`` in its constructor.
This will skip the resampling procedures that require properly functioning ``save/load/state`` methods in your model,
allowing you to fully develop your model's ``init`` and ``run`` methods first.
Make sure to remove ``noresample=1`` once you move to the implementation and testing of the ``save/load/state`` methods.

An alternative option is to start with a deterministic version of your model first (provided such version is possible),
and to use the ``Direct`` likelihood, which does not perform any resampling and does not use ``save/load/state`` methods of your model.

Model execution control
~~~~~~~~~~~~~~~~~~~~~~~

In your custom model class (inherited from the base ``Model`` class), you will need to modify two mandatory methods:

* :code:`init (self, inputset, parameters)` - initialize model for the specified inputset and parameters
* :code:`run (self, time)` - run model until the specified time and return the prediction

In the method declarations above, the arguments have the following meanings:

* :code:`inputset` - an optional arbitrary object specified in the :code:`likelihood` (default is :code:`None`)
* :code:`parameters` - a :code:`pandas.Dataframe` object with model parameters (as in the :code:`prior` of the :code:`sampler`)
* :code:`time` - an entry from the :code:`index` of the :code:`pandas.Dataframe` object :code:`dataset` specified in the :code:`likelihood`

Within these two main methods, you have two alternative options to execute your actual application:

* Basic (easy but less efficient) - run application execution command with arguments in a shell,
* Advanced (an efficient SPUX'onic way) - call application methods from Python using "drivers".

The "basic" method is very similar to the way you are most probably already executing your application,
and hence is recommended as the starting option for the first coupling of your application to the SPUX framework.
In particular, the application execution command (name it "mymodel") with some additional prescribed command line arguments (name them "arg1" and "arg2"),
is often called by

.. code-block:: console

   $ mymodel arg1 arg2

To achieve exactly the same behavior from within any method of your SPUX model class (``init (...)``, ``run (...)``, etc.),
including the isolation of the application to the required sandbox directory if the sandboxing is enabled (see below),
you can simply use the built-in convenience method ``shell``:

.. code-block:: python

   code = self.shell (r'mymodel arg1 arg2')

Note the ``r`` in front of the string to make sure all speciad characters are specified properly.
Internally it uses Python's ``subprocess`` module,
and returns the exit code of your application.

The "advanced" method allows to control the execution stages of your application directly from within the Python model methods,
avoiding the unnecessary overhead of application initialization and finalization inbetween consecutive calls of the model's ``run (...)`` method.
The computational efficiency gains are particularly large for a long time series datasets, where ``run (...)`` needs to be called multiple times,
and for models with small stochastic volatility (including deterministic models), where model states change infrequently (or never) inbetween consecutive ``run (...)`` calls.

Taking into account the additional requirements for respective model drivers (see :ref:`installation`),
you can also start directly from the advanced model execution control template corresponding to the required programming language:

* Python: `spux/models/straightwalk.py <https://gitlab.com/siam-sc/spux/tree/test/spux/models/straightwalk.py>`_
  `spux/models/randomwalk.py <https://gitlab.com/siam-sc/spux/tree/test/spux/models/randomwalk.py>`_,
  `examples/hydro/hydro.py <https://gitlab.com/siam-sc/spux/tree/test/examples/hydro/hydro.py>`_,
* Fortran: `examples/superflex/superflex.py <https://gitlab.com/siam-sc/spux/tree/test/examples/superflex/superflex.py>`_,
* Java: `spux/models/ibm.py <https://gitlab.com/siam-sc/spux/tree/test/spux/models/ibm.py>`_.

Model scope variables
~~~~~~~~~~~~~~~~~~~~~

Any model instance has the following internal variables (some different for each instance) available in all methods:

* ``self.sandbox ()`` - a path to an isolated sandbox directory (if ``self.sandboxing == 1``),
* ``self.verbosity`` - a integer indicating verbosity level for ``print ()`` intensity management,
* ``self.seed ()`` - a list containing all hierarchical seeds,
* ``self.seed.cumulative ()`` - a (large) integer seed obtained by combining all hierarchical seeds,
* ``self.rng`` - a ``numpy.random.RandomState`` instance for ``random_state`` in ``scipy.stats`` distributions.

The detailed usage of these methods is described in the following sections.

Model sandboxing
~~~~~~~~~~~~~~~~

Sandboxing is enabled by default and a default sandbox is created under ``sandbox``.
From within any method of the model, the sandbox path can be retrieved by executing ``self.sandbox ()``.
If certain common files need to be present in every model sandbox,
consider creating and populating a template sandbox directory, for instance named ``input``,
and specifying a custom sandbox by ``sandbox = Sandbox (template = 'input')`` in ``sampler.setup (...)``.
The contents of the template sandbox are always automatically copied (using efficient local caching) to the actual isolated sandbox.
and are accessible under sandbox path retrieved using the same instruction as before, i.e. ``self.sandbox ()``.
During the model development and debugging,
we do recommend to use ``trace = 1`` in ``sampler.setup (...)`` to be able to inspect each sandbox.

Model stochasticity
~~~~~~~~~~~~~~~~~~~

Note, that ``self.seed ()``, ``self.seed.cumulative ()`` and ``self.rng`` change for EACH call of ``self.run ()``.
Make sure that your underlying model is properly configured to implement such frequent updates in the seeding of the random number generator.

Initial model state
~~~~~~~~~~~~~~~~~~~

For some models that do not have a clear starting state,
there are basically only two alternative choices regarding the implementation of the ``init (...)`` method:

* perform computationally expensive "warmup" simulations to obtain (hopefully) valid model states,
* given a prior initial states distribution, infer the posterior initial states distribution.

For the latter choice, the hydrological example is in particularly interesting,
since the initial model state is stochastic (to be inferred using Particle Filter).
For an example usage of such setup, please refer to the hydrological example at:
`examples/hydro <https://gitlab.com/siam-sc/spux/tree/test/examples/hydro>`_.
In short, a probabilistic prior distribution is provided for the initial model state in
`examples/hydro/initial.py <https://gitlab.com/siam-sc/spux/tree/test/examples/hydro/initial.py>`_,
which is then filtered by the ``PF`` likelihood to infer
the posterior distribution of initial model states that are consistent to a respective dataset.

Auxiliary predictions
~~~~~~~~~~~~~~~~~~~~~

The ``run (self, time)`` method of the model returns annotated model predictions.
For the sake of simplicity and to keep the amount of data manageable,
only a list or an array of scalars is allowed to be included for such annotation.
The full state of some complex models, for instance, in computational fluid dynamics,
consists of large multi-dimensional arrays instead of just a couple of scalar values.
The suggested strategy is to cherry-pick a handful of the most important scalar values
(at the most important array locations) and use them for annotation.
This will be sufficient for some simple plots of posterior predictions.
However, the error model might still require the full multi-dimensional array
for the evaluation of the observation likelihood given some multi-dimensional dataset.
To accommodate this, assign any extracted large arbitrary Python objects
to the ``auxiliary`` argument in the ``annotate (...)`` call.
By doing so, the ``predictions`` in the error model's ``distribution (...)`` method
will instead be a dictionary containing :code:`predictions ['scalars']` as a ``pandas.DataFrame`` formed from the provided scalars,
and :code:`predictions ['auxiliary']` as a arbitrary Python object assigned by the model.
This auxiliary object will be accessible only in the error model, and will be discarded immidiately afterwards.

Inputsets for models
~~~~~~~~~~~~~~~~~~~~

If ``Replicates`` likelihood is used to incorporate different observations provided by multiple (replicate) datasets,
some models might also require different inputset configurations for each such dataset.
For instance, each dataset might require a specific starting time and value of the model.
These inputset configurations are not allowed to be set in the model constructor, since this would result in identical inputs across all replicates (which is fine only if there are no different dataset replicates).
Instead, the ``inputsets`` argument provides complementary information for each replicate by passing a respective ``inputset`` to the model's ``init (...)`` method (see description above).
For an example usage of  this setup, please refer to the hydrological example at:
`examples/hydro <https://gitlab.com/siam-sc/spux/tree/test/examples/hydro>`_.

Model state serialization
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``PF`` likelihood estimator for stochastic models requires your model to have a capability of being cloned,
which in SPUX is based on the concept of the model "state" serialization to a binary stream (array).
If you model is written in pure Python or R and you are NOT using the sandbox for any files relevant to your model state,
then the required model state serialization functionality from the model's base class is already sufficient.

However, if you save some part of your model state in the sandbox with snapshot-dependent filenames,
or if your model is not written in pure Python or R,
you will need to specify custom methods for model serialization
into its binary representation (state) and a corresponding de-serialization:

* :code:`save (self)` - save and return a ``bytearray`` representing the current state of the model,
* :code:`load (self, state)` - load model using the ``bytearray`` representing its required state.

The corresponding helper methods ``save (obj)`` and ``load (state)`` are available in the ``spux.utils.serialize`` module,
and are suggested to be used to serialize and de-serialize any arbitrary Python object.

If any files relevant to the model state are saved in the sandbox,
the full state of the ``save`` method must also include the sandbox state,
which is obtained by calling the ``self.sandbox.save (...)`` method of the sandbox.
This functionality is already implemented in the base ``Model`` class (de-)serialization methods,
as long as the list of relevant files (otherwise all sandbox files will be included)
is specified in the ``statefiles`` argument of the ``Sandbox`` constructor.
Note, that the files specified in the ``statefiles`` list do not necessarily
need to exist in the initial template sandbox directory,
since they might be dynamically generated during the ``init (...)`` and ``run (...)`` methods of the model.

If the filenames of the sandbox state files
depend on the snapshot, then they cannot be statically specified in the sandbox constructor,
and a custom model (de-)serialization methods ``save`` and ``load`` need to be implemented.
In such case, the list of relevant state files (otherwise all sandbox files will be included)
needs to be specified in the ``files`` argument of the ``self.sandbox.save (...)`` method.
The obtained sandbox state can then be combined
with any additional required model instance fields (for instance, ``self.time``)
in a dictionary and then passed to the serializer:

.. code-block:: python

   state = {}
   files = ['relevant_file_1', 'relevant_file_2']
   state ['sandbox'] = self.sandbox.save (files)
   state ['model'] = self.time
   state = serialize.save (state)

The corresponding model ``load`` method must then extract the relevant model and sandbox states from the full serialized model state and write back the correponding files into the new sandbox:

.. code-block:: python

   state = serialize.load (state)
   self.sandbox.load (state ['sandbox'])
   self.time = state ['model']

If your model is not written in Python or R, then for some of the other most common programming languages, SPUX contains built-in driver modules in
`spux/drivers <https://gitlab.com/siam-sc/spux/tree/test/spux/drivers/>`_,
which can be used to implement the above model state saving and loading routines quickly and efficiently.
We recommend to look at the provided example codes in
`examples/ <https://gitlab.com/siam-sc/spux/tree/test/examples/>`_.

Serialization test script
~~~~~~~~~~~~~~~~~~~~~~~~~

To test your custom implementation of the model state (de-)serialization using ``save ()`` and ``load ()`` routines,
we recommend to use a clone testing script for debugging purposes.
We recommend to adapt the example ``script_clone.py`` script from
`examples/randomwalk/script_clone.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/script_clone.py>`_.
The script runs the specified model up to the specified clone time
and makes a clone of the original model by saving its state.
Then, a second model is created by loading the saved state of the original model
and both models are run using the same RNG and seed up to the specified compare time.
If the ``save ()`` and ``load ()`` methods work as expected,
the predictions of both models must be identical.

SPUX executors
--------------

Any set of independent tasks within any of the SPUX components can be executed in parallel using built-in SPUX executors.
As described in the tutorial, the default exectutor is a ``Serial`` executor.

Currently, the parallel executors of each type ("pool" and "ensemble") are implemented in SPUX using MPI.
Different types of executors support different functionality and are usually meant to be used in different SPUX components:

- "pool" - dynamically executes a set of independent tasks; changes in task "states" are discarded,
- "ensemble" - statically executes a set of independent tasks in an ensemble (keeping task "states").

The "pool" type executor can be used by calling its ``map (...)`` method and passing one of the three sets of arguments:

- a callable object (for instance, a function) and a list of arguments for the evaluations,
- a list of callable objects (with an optional list of common fixed arguments),
- a list of callable objects and a corresponding list of arguments for the evaluations.

The "ensemble" type executor does not accept a list of tasks directly,
but requires and instance of an ``Ensemble`` class.
Currently the only implemented ensemble class is for an ensemble of SPUX models (to be used in the ``PF`` likelihood),
available at
`spux/likelihoods/ensemble.py <https://gitlab.com/siam-sc/spux/tree/test/spux/likelihoods/ensemble.py>`_.

Given an ``ensemble`` instance as above,
the "ensemble" type executor can be used by issuing a sequence of executor method calls for control
of the ensemble initialization, iterative execution of multiple stages for all tasks, and (optional) resampling:

- ``connect (ensemble, indices)`` - initialize ensemble with tasks enumerated by the specified indices,
- ``call (method, args)`` - call a specified (as a string) ``method`` of each task and return the results,
- ``resample (indices)`` - resample tasks according to the specified indices (clone and/or delete),
- ``disconnect ()`` - finalize ensemble and discard any changes in the task "states".

Inbetween the ``connect`` and ``disconnect``,
the ensemble executor methods ``call`` and ``resample`` can be called multiple times,
each time advancing all tasks to the next execution stage and performing any needed resampling of tasks.
During the resampling, tasks are allowed to be cloned (duplicate indices) and deleted (missing indices).
In the resampling call, load re-balancing across the resulting resampled ensemble is performed.

Parallel models
---------------

Most probably you have already noticed, that in the tutorial,
no parallel executor is attached to the model object.
This is because our implementation Randomwalk model does not support parallelization.
However, a custom user model might be very computationally expensive and need further parallelization.

Parallelize serial model
~~~~~~~~~~~~~~~~~~~~~~~~

Provided that the content of the pure Python model :code:`init (...)` and/or :code:`run (...)` methods
can be split into a list of independent computationally intensive tasks,
one could attach a :code:`spux.executors.mpi4py.pool` executor to the model.
The instruction how to make use of the ``Mpi4pyPool`` executor are provided in the preceding sections.
A more complicated option to potentially achieve a better performance
is to attach a :code:`spux.executors.mpi4py.ensemble` executor to the model
by splitting the model into independent sub-models and treating all of them as an ensemble of sub-models.
The instruction how to make use of the ``Mpi4pyEnsemple`` executor are provided in the preceding sections as well.

For more information, take a look at the corresponding documentation files in :ref:`documentation`.

Parallel model executor
~~~~~~~~~~~~~~~~~~~~~~~

In some cases, a custom user model might be either already parallelized,
or the model might be written in another programming language rather than Python.
SPUX framework does support such models too.

The easiest, but also the least efficient way to run parallel models is
to rely on model evolution through file system (saving model states as files in sandboxes),
and simply calling ``os.system ('myparallelmodel <some args ...>')``
from within the ``self.init (...)`` and ``self.run (...)``.
This requires sufficient allocated computation resources such that all processes
from both the SPUX framework and the parallel model run on separate cores.

An alternative way is a bit more complicated and only minimally itrusive,
and can be used provided that MPI is used for model parallelization.
In particular, one can attach the built-in parallel MPI model executor from
`spux/executors/mpi4py/mpimodel.py <https://gitlab.com/siam-sc/spux/tree/test/spux/executors/mpi4py/mpimodel.py>`_:

.. code-block:: python

    from spux.executors.mpi4py.mpimodel import Mpi4pyModel

With the :code:`Mpi4pyModel (workers=<workers>)` executor attached to the model,
in the model :code:`init (...)` and :code:`run (...)` methods,
the call :code:`self.executor.connect (command)` returns an MPI inter-communicator
connected to the parallel workers, each executing the provided shell command :code:`command` in parallel,
analogous to the manual launch of an MPI:

.. code-block:: console

    $ mpiexec -n <workers> command

You can use this manager-side MPI inter-communicator to workers for simulation control,
parameters specification, predictions retrieval, and saving/loading of the model state,
completely circumventing the need for any unnecessary filesytem related operations.

Model communicators
~~~~~~~~~~~~~~~~~~~

The connection procedure from the parallel workers (model) to the manager
depends on the selected connector (see explanation in the :ref:`tutorial`) as described below.
Independently of the selected connector, in each parallel worker you will have an access
to a corresponding inter-communicator with the manager.
You can use this worker-side MPI inter-communicator to manager for simulation control,
parameters acquisition, predictions reporting, and saving/loading of the model state.

For :code:`spawn` connector, on the workers (model) side,
you have access to an inter-communicator with the manager returned by calling :code:`MPI_Comm_get_parent ()`.
Within the model, the standard ``MPI_COMM_WORLD`` MPI intra-communicator is available, as in a normal MPI run.
Currently ``spawn`` is the only fully supported connector for parallel models using MPI.

.. EXPERIMENTAL:
.. For :code:`split` and ``legacy`` connectors, what can we do to create the ``peers`` MPI intra-communicator
.. within each parallel MPI model?
.. For :code:`split`, on the workers (model) side,
.. you have access to an inter-communicator with the manager returned by calling :code:`MPI_Comm_connect (...)`
.. with the :code:`port` provided by :code:`self.executor.port`.
.. For :code:`legacy`, on the workers (model) side,
.. you have access to an inter-communicator with the manager returned by calling :code:`MPI_Intracomm_create (...)`
.. with the ``remote`` set to :code:`port` provided by :code:`self.executor.port`.
.. Hence, for both such connectors, you need to pass the value of the :code:`self.executor.port` to the model binary,
.. by including it within the :code:`command` in :code:`self.executor.connect (command)`.
.. Within the model, the standard ``MPI_COMM_WORLD`` MPI intra-communicator is available
.. but it refers to the entire SPUX pool of MPI processes, and hence is NOT the same as for a normal MPI run.

For more information, take a look at the corresponding documentation files in :ref:`documentation`.

Adding a distribution
---------------------

The easiest way to specify a multivariate distribution is to use a tensor
`spux/distributions/tensor.py <https://gitlab.com/siam-sc/spux/tree/test/spux/distributions/tensor.py>`_
of selected univariate distributions from the :code:`scipy.stats` module; see an example in :ref:`tutorial`.

An example of how to have a joint parameters distribution with correlations,
possibly by selecting a multivariate distribution from the :code:`scipy.stats` module,
can be found in
`spux/distributions/multivariate.py <https://gitlab.com/siam-sc/spux/tree/test/spux/distributions/multivariate.py>`_.

Adding an error
---------------

One custom scenario would be when the observations (both the predictions or the dataset) need to be transformed
before the density of the distribution can be evaluated.
To support this, one can provide a custom :code:`transform (self, observations, parameters)` method in the error class
which performs the required transformations using the (optional) specified parameters and returns the result.

For an example, look at the :code:`error.py` in
`examples/hydro/error.py <https://gitlab.com/siam-sc/spux/tree/test/examples/hydro/error.py>`_.

Setting variable types
----------------------

Sometimes either some of the model parameters or some of the model predictions are represented by integers instead of floating point numbers.
This is often the case if the quantity of interest represents a count of some occurrences, or a discrete categorical class.

By default, all parameters and predictions are assumed to be of type ``float``.
However, optional respective ``parameters.types`` and/or ``predictions.types`` files can be provided
in the implementations of the ``prior.py/error.py/<model>.py`` scripts
and in the constructor of the plotting class ``MatPlotLib``.

The format of the files requires to specify two columns, with entries listing ``<variable name>`` and ``<variable type>``, for instance:

.. code-block:: console

    prey int
    prey_kFood double

The ``parameters.types`` file is used in the
`examples/IBM_2species <https://gitlab.com/siam-sc/spux/tree/test/examples/IBM_2species>`_
example to round integer valued parameters in ``prior.py``, ``error.py`` and ``ibm.py``,
since inconsistencies can arise depending on the type of sampler.

The ``predictions.types`` file is used in the plotting routines in the constructor of the ``MatPlotLib`` class.
This is useful, for example, to plot the error distributions for integer-valued observations (model predictions or collected dataset).

Please refer to
`examples/IBM_2species <https://gitlab.com/siam-sc/spux/tree/test/examples/IBM_2species>`_
for a specific usage example of these files.

Adding a sampler
----------------

In order to add a custom sampler (in addition to existing samplers, e.g. MCMC and EMCEE),
you need to derive a new sampler class the base ``Sampler`` class in ``spux.samplers.sampler``.
For the source code of the sampler base class, please refer to
`spux/samplers/sampler.py <https://gitlab.com/siam-sc/spux/tree/test/spux/samplers/sampler.py>`_.

In particular, the new sampler class must have the following methods:

- ``__init__ (self, ...)`` - constructor to set sampler properties (can be skipped),
- ``init (self, ...)`` - sampler initialization routine (can be empty),
- ``pickup (self)`` - return sampler pickup information (e.g. a dictionary with needed entries),
- ``draw (self, sandbox, seed)`` - return samples as ``pandas.Dataframe`` and the associated ``info``.

In most use cases, sampler will need to have an assigned likelihood
(which is assigned in the base class method ``sampler.assign (...)``).
The ``init (...)`` method can be used to initialize as many
likelihoods as the number of needed concurrent chains (assuming ``self.chains`` is set in the constructor):

.. code-block:: python

    self.likelihoods = [copy (self.likelihood) for index in range (self.chains)]

The following code can be used to properly set up likelihoods in ``draw (...)``:

.. code-block:: python

    for chain, likelihood in enumerate (self.likelihoods):
        label = 'C%05d' % chain
        chain_sandbox = sandbox.spawn (label) if self.sandboxing else None
        chain_seed = seed.spawn (chain, name=label)
        likelihood.setup (chain_sandbox, self.verbosity - 2, chain_seed, self.informative, self.trace, self._feedback)

Finally, the list of all likelihoods can be passed to the executor for evaluation,
together with the list of corresponding parameters for each of them:

.. code-block:: python

    results, timings = self.executor.map (likelihoods, parameters)

Note, that to allow maximum flexibility,
the ``self.executor`` is avaible within both ``init (...)`` and ``draw (...)`` methods.

For an example implementation, please refer to the source code of the EMCEE sampler at
`spux/samplers/emcee.py <https://gitlab.com/siam-sc/spux/tree/test/spux/samplers/emcee.py>`_.

Work in progress.

Adding a likelihood
-------------------

Work in progress.
