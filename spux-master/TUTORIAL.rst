
.. _tutorial:

========
Tutorial
========

This section guides you through a tutorial for an example model and usage pattern of SPUX.
For peculiarities regarding the coupling your model with the SPUX framework, refer to :ref:`customization`.

Overview
--------

Commands should be executed in Python terminal, or inside a Python script, or in a Jupyter notebook.
To learn how to write your own custom scripts and configure spux,
first read through the rest of this section and take a look at the
`examples <https://gitlab.com/siam-sc/spux/tree/test/examples>`_
suite.

Editor
~~~~~~

Try one of the following cross-platform editors (you can also use Vim or Emacs, of course):

* Spyder - similar UI as R,
* PyCharm - proprietary,
* VS Code - works very well with GitLab integration extensions - give it a try!

Model stochasticity
~~~~~~~~~~~~~~~~~~~

SPUX supports two types of models for the Bayesian inference:

* Deterministic - model evaluation is uniquely determined by the inputset and parameters,
* Stochastic - model evaluation is additionally driven by a random variable/process.

Bayesian inference of model parameters for deterministic models is often less difficult,
since a simple so-called ``Direct`` likelihood can be used,
which, for any given parameters, is analytically computed from the specified error model.
Error model describes a probabilistic distribution for observational data,
conditional on the true model evaluation (referred to as model prediction).

For stochastic models, in addition to uncertain model parameters,
also the uncertain model evaluations (predictions, sometimes referred to as states) need to be inferred.
To this end, the error model alone is often not sufficient to analytically compute
the marginal likelihood of a given dataset and model parameters.
Currently SPUX supports the Particle Filter approximation of such marginal likelihood, used in this tutorial.

As SPUX framework has a focus on the Bayesian inference in stochastic models,
in the present tutorial we also focus on the stochastic models, with an example of a ``Randomwalk``.
``Straightwalk`` is another educational model available in SPUX,
which is simply a stripped down version (with the randomness eliminated) of the stochastic ``Randomwalk`` model.
To learn more about the ``Straightwalk`` and how to use SPUX with deterministic models,
we recommend to read the tutorial below and then
refer to analogous example scripts in the respective example directory at:
`examples/straightwalk/ <https://gitlab.com/siam-sc/spux/tree/test/examples/straightwalk/>`_.

Replicate datasets
~~~~~~~~~~~~~~~~~~

In some applications, multiple replicates of observational datasets are available,
with each replicate dataset corresponding to the same (assumed to be unknown) model parameter values,
but different independent stochastic model evaluations (for instance, w.r.t. the seed of the pseudo-random number generator.)
Examples of such replicates could be independent datasets from several consecutive sufficiently separated time periods,
or even several simultaneously collected measurements from independent experimental sites.

If this is the case, each dataset (and the respective model inputset) can be treated statistically independently
but at the same time fully integrated into the SPUX framework by simply merging
individual respective (direct or marginal) likelihoods into a single ``Replicates`` likelihood.
For the sake of simplicity, this tutorial only considers a single dataset.
To learn more about how to use SPUX with multiple independent replicate datasets,
we recommend to read the tutorial below and then
refer to analogous example scripts in the respective example directory at:
`examples/randomwalk-replicates/ <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk-replicates/>`_.

Randomwalk (serial)
-------------------

Here we provide an elaborate description of the SPUX framework
setup and simulation execution for an example of a simple Randomwalk model.

Model description
~~~~~~~~~~~~~~~~~

The model describes a stochastic one-dimensional walk on integers,
with a prescribed (let's say, genetically) :code:`stepsize`.
Starting at the location given by the :code:`origin` parameter,
a randomwalk takes a random step of size :code:`stepsize` either to the left or to the right,
with direction distribution depending on the :code:`drift` parameter.
Inaccurate observations at several times of the randomwalk's position are available,
with unknown observational error distribution,
assumed to be Gaussian with zero mean and standard deviation given by the parameter :code:`$\sigma$`.

All files required throughout this example (and some more) could be found in
`examples/randomwalk/ <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/>`_,
which we assume is the current working directory where commands are executed.
This means that all :code:`import module` statements will import the corresponding :code:`module.py` script from this directory (or an already installed external Python module).
All imports starting with :code:`from spux import ...` import modules that are built-in in the spux module,
and we use relative links starting with `spux/ <https://gitlab.com/siam-sc/spux/tree/test/spux/>`_ for a corresponding file in the GitLab repository.

The randomwalk model is a built-in module in spux and can be found at
`spux/models/randomwalk.py <https://gitlab.com/siam-sc/spux/tree/test/spux/models/randomwalk.py>`_:

.. literalinclude:: ../spux/models/randomwalk.py
   :language: python
   :lines: 10-

In the source code above, :code:`Randomwalk` class has a constructor (note the underscores!) :code:`__init__ (self, ...)`,
which is called when constructing model by :code:`model = Randomwalk (stepsize=1)`.
The argument :code:`self` is a pointer to the object itself, analogous to :code:`this` in C/C++.
Additional methods include:

* :code:`init (self, inputset, parameters)` - initialize model with the specified :code:`inputset` and :code:`parameters`,
* :code:`run (self, time)` - run model from the current time up to the specified :code:`time`.

Note, that the "current time" in the above is set in :code:`init (...)` or the previous call of :code:`run (...)`
and is handled differently in different models (in this example: simply saving it to :code:`self.time`).

The :code:`annotate (values, labels, time)` method packages model predictions stored in :code:`values` to a :code:`pandas.DataFrame`
with the specified list of :code:`labels` for the elements if the :code:`values` and with the requested :code:`time`.

SPUX configuration
~~~~~~~~~~~~~~~~~~

Apart from the actual model, we also need to specify several auxiliary configuration files for observational datasets,
statistical error model (i.e. a probabilistic distribution of the observations conditional on the specified model prediction),
and prior distribution of the parameters.
Actual dataset files are located in the datasets directory at
`examples/randomwalk/datasets/ <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/datasets/>`_.

The script to load the dataset into :code:`pandas` DataFrames (a default container for dataset management in SPUX, see https://pandas.pydata.org) is located in
`examples/randomwalk/dataset.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/dataset.py>`_.

.. literalinclude:: ../examples/randomwalk/dataset.py
   :language: python
   :lines: 1-

Error model is defined in
`examples/randomwalk/error.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/error.py>`_
as an object with a method :code:`distribution (prediction, parameters)`
which returns a distribution of the model observations (dataset):

.. literalinclude:: ../examples/randomwalk/error.py
   :language: python
   :lines: 1-

Prior distribution is defined in `examples/randomwalk/prior.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/prior.py>`_:

.. literalinclude:: ../examples/randomwalk/prior.py
   :language: python
   :lines: 1-

Within the context if this illustrative ``Randomwalk`` example, we also make use of the (optional) exact ("the truth")
parameter values as well as the model predictions (without the observational noise) which are set at
`examples/randomwalk/exact.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/exact.py>`_:

.. literalinclude:: ../examples/randomwalk/exact.py
   :language: python
   :lines: 1-

The datasets (and the predictions) in the
`examples/randomwalk/datasets/ <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/datasets/>`_
directory were generated using the above exact model parameters from
`examples/randomwalk/exact.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/exact.py>`_
by the synthesis script based on the built-in SPUX data generation method:
`examples/randomwalk/script_synthesize.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/script_synthesize.py>`_

.. literalinclude:: ../examples/randomwalk/script_synthesize.py
   :language: python
   :lines: 1-

We would also like to emphasize, that in the above scripts we generously use LaTeX syntax
within labels for parameters, predictions, and observations.
The benefit of such scrupulous naming will become evident from the generated plots
within this tutorial, where all axes labels are LaTeX-formatted mathematical symbols.
Notice, that for a LaTeX syntax to be supported in Python,
one must prepend the string with the ``r`` letter (as in "raw").

In order to give you a better overview of the datasets, the error model, the prior distribution,
and (optional) exact parameters values for a reference, consider running a preparation script
`examples/randomwalk/plot_config.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/plot_config.py>`_:

.. literalinclude:: ../examples/randomwalk/plot_config.py
   :language: python
   :lines: 1-

The above script plots model observations (datasets),
marginal prior distributions of model parameters,
and marginal error model distributions for specified model prediction and parameters
and by default saves them in the ``fig`` directory under multiple file formats (PDF, EPS, SVG, PNG),
additionally including a caption file ``*.cap`` containing the description of the figure contents:

.. figure:: _static/randomwalk/randomwalk_dataset.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_dataset.cap

.. figure:: _static/randomwalk/randomwalk_distributions-prior.png
   :align: center

   .. include:: _static/randomwalk/randomwalk_distributions-prior.cap

.. figure:: _static/randomwalk/randomwalk_errors.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_errors.cap

In addition to the plots,
an auxiliary ``report`` directory is created
(can be changed by setting :code:`reportdir` in :code:`sampler.setup (...)`),
including information regarding SPUX framework setup.
Each report file in the ``report`` directory is saved using three different formats:

* ``.dat`` - a (cloudpickle) binary dump of the respective Python object or dictionary,
* ``.txt`` - a formatted ASCII table to be easily read directly,
* ``.tex`` - a formatted LaTeX table to be included in a LaTeX report.
* ``.cap`` - a caption with the table title and description of the table contents.

At the end of the ``plot_config.py`` script all generated plots are compiled into a LaTeX report under directory ``latex``,
where a PDF report is also generated if the ``pdflatex`` can be found in the system (which is not a SPUX dependency).
The PDF report for this example can be downloaded `here <_static/randomwalk/randomwalk_report.pdf>`_.
The report is continuously overwritten with the newest plots and tables,
and contains separate sections for the SPUX framework setup, and, as described in the following sections,
the results of the inference run and the computational performance amd runtime profiling reports.

As already hinted in the report above, the main script
`examples/randomwalk/script.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/script.py>`_,
uses the above auxiliary scripts to configure SPUX:

.. literalinclude:: ../examples/randomwalk/script.py
   :language: python
   :lines: 1-

In this script, different additional components, such as model, likelihood, and sampler, are created.
Afterwards, all these components are merged together by assigning according to the logical dependencies.
In the future, SPUX will provide a :code:`spux.utils.assign` module containing a :code:`assign` function,
which takes a list of components (in any order) as an argument, tries to "automagically" perform all needed assignments
(assuming all components are directly derived from the respective SPUX component base classes)
and returns the resulting top-level component (in this example, the :code:`sampler`):

.. code-block:: python

    from spux.utils.assign import assign
    components = [model, error, dataset, likelihood, prior]
    sampler = assign (sampler, components)

The corresponding SPUX configuration table from ``report/randomwalk_config.txt`` reports
the selected class for each SPUX component, together with the selected constructor arguments:

.. literalinclude:: _static/randomwalk/randomwalk_config.txt
   :language: console

In the SPUX configuration above, in the constructor arguments of the ``PF`` marginal likelihood estimator,
the number of particles, instead of being a fixed number,
is set to a list indicating the minimum and maximum number of particles to be used adaptively,
starting with the minumum number of particles and then iteratively
taking into account the feedback from the empirical standard deviations of these estimates.

SPUX results
~~~~~~~~~~~~

It is a good idea to keep this main :code:`script.py` separate from the scripts that will actually run SPUX,
in order to have flexibility for the later customization of output location, sampling duration, and the targeted hardware resources.

To achieve this, we import the main configuration script and initiate the execution of the framework
in a separate script named (you will see later why such name)
`examples/randomwalk/script_serial.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/script_serial.py>`_:

.. literalinclude:: ../examples/randomwalk/script_serial.py
   :language: python
   :lines: 1-

Within ``sampler.setup (...)``, various additional (optional) sampling options can be set, including:

* ``sandbox`` instance - target filesystem and directory for the SPUX sandbox,
* ``verbosity`` - [0 to infinity] limits the depth of verbosity in the hierarchy of SPUX components,
* ``seed`` instance - initial seed array for the pseudo random number generators,
* ``lock`` - batch index to lock sampler's feedback to likelihood (e.g. adaptive ``PF``) [default: ``None``],
* ``thin`` period - to save only every ``thin``-th sample batch and information [default: ``None``].

The adaptive number of particles in ``PF`` is meant to be used only during the initial burn-in period,
after which, if the number of particles is not completely stationary, the adaptation should be locked.
The optional ``lock`` argument in the ``sampler.setup (...)`` can be used
to stop the adaptation of the number of particles in ``PF`` and lock the most recent value until the end of sampling.

The ``sandbox`` in this example script is configured to use the fast virtual node-local RAM-based Linux filesystem called ``tmpfs``.
Note, that the exact path to the local ``tmpfs`` might differ depending on the Linux distribution.
For local testing, a user might prefer to temporarily switch to a conventional filesystem and set a different desired sandbox ``path``, leaving ``target=None``.
For production runs on high performance computing clusters, we recommend either to use the default ``tmpfs``,
or, if the amount of system memory is a limiting factor, to set ``target`` to the scratch file system of the cluster.
Node-local (not shared) scratch filesystems are preferable, due to their better performance and the lack of restrictions regarding any storage quotas.
If target is a shared (hence not a node-local) filesystem (the worst case scenario, for development only), you can also set ``path``, where a corresponding symlink pointing to the specified ``target`` will be created.

Regarding the auxiliary calls :code:`sampler.executor.init ()` and :code:`sampler.executor.exit ()`,
you must have them, and in this particular order, i.e. wrapping every other call of the SPUX framework
(apart from the calls in the main configurations script).

The main script then generates an :code:`output/` directory
(can be changed by setting :code:`outputdir` in :code:`sampler.setup (...)`)
with files containing posterior samples and supporting information;
multiple files of each type will be generated for each checkpoint,
with the default period being 10 minutes:

* :code:`samples-*.csv` - a CSV file containing comma-separated posterior samples of parameters,
* :code:`samples-*.dat` - a binary file (:code:`cloudpickle`) containing posterior samples of parameters,
* :code:`infos-*.dat` - a binary file (:code:`cloudpickle`) containing a :code:`list` of supporting information,
* :code:`pickup-*.dat` - a binary file (:code:`cloudpickle`) containing a dictionary of sampler pickup information.

The supporting files :code:`infos-*.dat` contain detailed information about
each component in the hierarchical assignment structure specified by the main configuration script.
In the particular example, when loaded (see following paragraphs) will contain a list of dictionaries for each draw of the posterior parameters from the sampler.
For samplers supporting multiple MCMC chains, each draw provides as many samples as there are chains,
and hence the list in the :code:`infos-*.dat` will be shorter than the list of all posterior parameters by a factor of the number of chains.
The structure of each element in the list of loaded :code:`infos-*.dat` can be inferred from the corresponding info generation routines for each SPUX component (look for :code:`info = {...}`).

The sampler pickup files :code:`pickup-*.dat` contain all information
needed to continue sampling past the respective checkpoint
(will be discussed in detail in the following sections).

In addition to the ``output`` directory, the auxiliary ``report`` directory is also updated,
appending information regarding
computational environment (in ``report/randomwalk_environment.txt``):

.. literalinclude:: _static/randomwalk/randomwalk_environment.txt
   :language: console

required computational resources (in ``report/randomwalk_resources.txt``):

.. literalinclude:: _static/randomwalk/randomwalk_resources.txt
   :language: console

sampler setup (in ``report/randomwalk_setup.txt``):

.. literalinclude:: _static/randomwalk/randomwalk_setup.txt
   :language: console

the cumulative number of model evaluations in each SPUX component (in ``report/randomwalk_evaluations.txt``):

.. literalinclude:: _static/randomwalk/randomwalk_evaluations.txt
   :language: console

and the structure of the information available in :code:`infos-*.dat`:

.. literalinclude:: _static/randomwalk/randomwalk_infos.txt
   :language: console

If :code:`self.sandboxing == 1` is set for the model,
a :code:`sandbox` directory is created (or a custom name, if custom sandbox is specified).
This directory is populated with nested sandboxes for each sample, chain, replicate, likelihood, and model.
For sandboxes in the ``local`` mode (for non-shared filesystems), nested directories are replaced by a single directory with a long name indicating the underlying hierarchy.
Please also note, that sandboxes in ``local`` mode are tentative, meaning that they are only created once ``self.sandbox ()`` is executed for the first time.
If :code:`trace=True` is additionally specified in the :code:`sampler.setup (...)`,
this directory contains the stored sandboxes of all samplers,
likelihoods and models, including all the generated results. However, these results would be easily accessible only if sandboxes are placed in a shared filesystem and a non-local mode is used.

In the future, SPUX will explicitly save the sandbox with a complete trace of the model output
(independently of the value set to ``trace``)
for the approximated joint maximum a posteriori (MAP) model parameters and states
under the directory specified in ``sampler.setup (...)`` by ``MAPdir`` with the default being ``'MAP'``.
In addition, there will be an option to save only a (possibly thinned) collection
of posterior sandboxes by specifying ``trace = 'posterior'`` in ``sampler.setup (...)``.

.. Before we proceed to the results, please note,
.. that all following plots were generated with the production settings,
.. which are more computationally demanding compared to the example scripts above.
.. In particular, 16 particles were used in the PF likelihood, and 16 chains were used in the EMCEE sampler.
.. We used in total 129 cores, with 8 workers for the ``EMCEE`` sampler,
.. and 4 workers for the ``PF`` likelihood.
.. In total, 50'000 samples were requested, with the ``lock`` set to be at 50 sample batches (800 samples).

An example analysis script to load and visualize results from the :code:`output/` directory is available at
`examples/randomwalk/plot_results.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/plot_results.py>`_:

.. literalinclude:: ../examples/randomwalk/plot_results.py
   :language: python
   :lines: 1-

This script uses some built-in plotting routines available in `spux/plot/mpl.py <https://gitlab.com/siam-sc/spux/tree/test/spux/plot/mpl.py>`_ module.
However, the user is free to use only the loading parts and choose how to visualize the results using other established data visualization libraries,
including the built-in visualization module :code:`pandas.plotting` in :code:`pandas` for the visualization of the :code:`pandas.DataFrame` objects.
Also check out `NumFOCUS <https://numfocus.org/sponsored-projects?_sft_project_category=python-interface+visualization>`_.

Note, that for runtime saving purposes,
actual linked example scripts in repository usually could be setup for smaller computational resources (i.e. fewer particles, chains, samples, etc.),
and hence the following example plots for SPUX results could differ from your versions
(please check the corresponding entries in the provided configuration and setup tables above).

The above analysis script generates multiple plots of the results, but firstly it is most useful to look at the ``unsuccessfuls`` and ``resets`` plots.

.. figure:: _static/randomwalk/randomwalk_unsuccessfuls.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_unsuccessfuls.cap

Note, that skipped likelihoods are not scheduled in the executor and might result in a temporary (for that particular parameter proposal)
parallelization imbalances due to the lack of tasks to process.

.. figure:: _static/randomwalk/randomwalk_resets.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_resets.cap

From the diagnostic plot above, we determine that the inference was (tentatively) successful:
not many failed (NaN) or skipped (zero prior) likelihood evaluations, and a negligible amount of total chain resets (likelihood re-estimations).

The next most important plots are the ``parameters`` plot, reporting the sampling progress of all sampler chains,

.. figure:: _static/randomwalk/randomwalk_parameters.png
   :align: center
   :scale: 15 %

   .. include:: _static/randomwalk/randomwalk_parameters.cap

and the progress of the corresponding likelihood, accuracies, particles, redraw, and acceptances plots
providing diagnostic information of the algorithmic technicalilies within the ``PF`` likelihood estimation
and Markov chain sampling:

.. figure:: _static/randomwalk/randomwalk_likelihoods.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_likelihoods.cap

.. figure:: _static/randomwalk/randomwalk_max_avg_errs.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_max_avg_errs.cap

.. figure:: _static/randomwalk/randomwalk_accuracies.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_accuracies.cap

.. figure:: _static/randomwalk/randomwalk_particles.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_particles.cap

.. figure:: _static/randomwalk/randomwalk_redraw.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_redraw.cap

.. figure:: _static/randomwalk/randomwalk_acceptances.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_acceptances.cap

We estimate the burnin period to last for approximately 70 batches of EMCEE samples from multiple chains.
We use this information to generate all subsequent plots with the initial bias already removed
by setting ``burnin=70`` in the ``reconstruct`` method for loading results in the ``plot_results.py`` script above.
We note, that ``lock`` sample batch reported in the ``setup`` table above must not exceed the selected ``burnin``
to ensure that the number of particles in ``PF`` likelihood is fixed throught the posterior sampling
(and hence avoid any potential bias due to the adaptivity process).
The resulting inference plots provide a detailed insight into posterior parameters and model predictions distributions,
as well as the performance of the overall Bayesian inference.

.. figure:: _static/randomwalk/randomwalk_posteriors.png
   :align: center
   :scale: 15 %

   .. include:: _static/randomwalk/randomwalk_posteriors.cap

.. figure:: _static/randomwalk/randomwalk_posteriors2d.png
   :align: center
   :scale: 15 %

   .. include:: _static/randomwalk/randomwalk_posteriors2d.cap

.. figure:: _static/randomwalk/randomwalk_posterior2d-origin-drift.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_posterior2d-origin-drift.cap

.. figure:: _static/randomwalk/randomwalk_predictions-posterior.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_predictions-posterior.cap

.. figure:: _static/randomwalk/randomwalk_qq.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_qq.cap

In addition to the plots in the ``fig`` directory, the auxiliary ``report`` directory is also updated,
appending information regarding
the approximate maximum a posterior parameters values (in ``report/randomwalk_MAP.txt``):

.. literalinclude:: _static/randomwalk/randomwalk_MAP.txt
   :language: console

and various metrics for inference efficiency (in ``report/randomwalk_metrics.txt``):

.. literalinclude:: _static/randomwalk/randomwalk_metrics.txt
   :language: console

As with the ``plot_config.py`` script, at the end of the ``plot_results.py`` script
all generated plots are compiled into a LaTeX report under directory ``latex``.

SPUX performance
~~~~~~~~~~~~~~~~

The table of inference runtimes is available in ``report/randomwalk_runtimes.txt``:

.. literalinclude:: _static/randomwalk/randomwalk_runtimes.txt
   :language: console

Even without explicitly specifying ``informative = 1`` in ``sampler.setup (...)``,
the informative output is enable for the first and the last sample batches.
This allows us to generate a simplified and a standard ``timestamps`` plots,
providing an inisight into the runtimes profiles of the very last sample.

.. figure:: _static/randomwalk/randomwalk_timestamps-last-cherrypicked.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_timestamps-last-cherrypicked.cap

.. figure:: _static/randomwalk/randomwalk_timestamps-last.png
   :align: center
   :scale: 20 %

   .. include:: _static/randomwalk/randomwalk_timestamps-last.cap

Continue sampling
~~~~~~~~~~~~~~~~~

It is possible to continue the sampling process where it finished without any additional re-evaluation of the likelihoods,
since all the needed information is already available.
The easiest way to continue sampling is to increase the number of samples as needed
and then execute the sampling script with the additional command line option ``--continue``, for example:

.. code-block:: console

    $ python script_serial.py --continue

This automatically loads the most recent pickup file (see above).

An alternative and a more flexible way to manually customize the ``sampler.setup (...)`` method by providing

* sample batch ``index`` - from which to continue (usually incremented last sampled batch index),
* ``feedback`` - from the previous sample batch ``index`` (only for ``PF`` likelihood),

and the ``sampler.init (...)`` method by providing (for the sampele batch ``index`` specified above)

* ``initial`` parameters - respective loaded parameter samples for each sampler chain,
* ``posteriors`` - the posteriors of the above parameters.

An example of such advanced manual continuation script is available at
`examples/randomwalk/script_serial_continue.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/script_serial_continue.py>`_.

.. .. literalinclude:: ../examples/randomwalk/script_serial_continue.py
..    :language: python
..    :lines: 1-

Informative output
~~~~~~~~~~~~~~~~~~

By default, the computation performance measurements
and the additional :code:`infos` from each SPUX component
are incorporated into ``infos-*.dat`` for the first and the last sample batches.
Alternatively, you can choose to enable or disable such informative output
by setting :code:`informative = 1` or :code:`informative = 0` flag in the :code:`sampler.setup (...)`.
Note, however, that :code:`informative = 1` results in an overhead for your inference,
and is only advised for the non-production runs during the development stages.
You can then use the sample script
`examples/randomwalk/plot_performance.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/plot_performance.py>`_
to generate plots for timings and scaling for each sample batch,
in addition to the timings plots generated by ``plot_results`` above.

Profiling
~~~~~~~~~

If you would like to have more detailed information about the execution process,
you can enable the profiling by setting :code:`profile=1` in :code:`sampler.sample (...)`.
The profiling information after the execution of the framework will be saved in :code:`output/profile.pstats`.
You can then use the sample script
`examples/randomwalk/plot_profiler.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/plot_profiler.py>`_
to generate a report and a callgraph plot, which will be saved under the :code:`fig/` directory.

Randomwalk (parallel)
---------------------

With minimal effort, the above example configuration could be parallelized
either on a local machine or on high performance computing clusters.

Note, that NO MODIFICATIONS are needed for this particular ``Randomwalk`` model class.
For a more detailed discussion for other user-specific models written not in pure Python, refer to :ref:`customization`.

SPUX executors
~~~~~~~~~~~~~~

To enable parallel execution, each SPUX component in the main configuration script :code:`script.py`
can be optionally assigned a parallel executor, specifying the number of parallel workers (for that particular component).
In this example, we use a separate script
`examples/randomwalk/script_executors.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/script_executors.py>`_:

.. literalinclude:: ../examples/randomwalk/script_executors.py
   :language: python
   :lines: 1-

The additional lines at the end of the script regarding the :code:`table` estimate the needed computational resources,
which are determined by the number of workers requested in each executor.
Note, that a separate core is used for the manager process of each executor.
The table with estimated computational resources can be printed to the terminal simply by executing this script
(parallel inference is NOT launched at this point):

.. code-block:: console

    $ python script_executors.py

An example output of such table (for this particular configuration) is provided below,
where the cumulative number of 31 cores are needed (bottom left cell, scroll horizontally to see everything).

.. literalinclude:: _static/randomwalk/randomwalk_resources.txt
   :language: console

Launching parallel SPUX
~~~~~~~~~~~~~~~~~~~~~~~

To launch a parallel inference using SPUX with the attached parallel executors as above,
we use a separate script for parallel runs which additionally initializes a parallel connector
and passes it to the ``sampler.executor.init (...)``, as given in
`examples/randomwalk/script_parallel.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/script_parallel.py>`_:

.. literalinclude:: ../examples/randomwalk/script_parallel.py
   :language: python
   :lines: 1-

Note the initialization of the connector as the very first item in the script.
We emphasize, that such ordering of the connector and remaining SPUX components is mandatory to ensure efficient startup.

Assuming you have MPI installed (see :ref:`installation`),
the above script can be executed with:

.. code-block:: console

    $ python script_parallel.py

Note, that this is the shortest way to run it, but not the best.
In particular, if the simulation crashes, the backtrace of the crash source will be complicated
and the parallel processes cleanup will not be as desired.
Hence, please consider using a more extensive command for production runs:

.. code-block:: console

    $ mpiexec -n 1 python -m mpi4py script_parallel.py

Note, that any needed additionally required MPI processes will be spawned automatically according to the resource table above,
hence for this configuration always use :code:`-n 1`, independently of the workers in executors.

When ``script_parallel.py`` is executed, the computational resources table described in the preceding section
is printed to the terminal and also written to ``report/randomwalk_resources.txt``.

Remark on MPI libraries
~~~~~~~~~~~~~~~~~~~~~~~

Note, that different MPI libraries provide different implementations,
which have different configuration capabilities and might not completely follow the MPI standard.

Here we try to provide a list of useful advices to address any issues that you could encounter.

For ``OpenMPI`` (launched with ``mpirun`` or ``mpiexec``):

* Specify ``--mca mpi_warn_on_fork 0`` to avoid annoying warnings (only for ``Spawn`` connector).
* Specify ``--mca pmix_server_max_wait 3600`` and ``--mca pmix_base_exchange_timeout 3600``
  to avoid connection failures (not relevant for ``Legacy`` connector).
* For local testing, specify ``--oversubscribe`` to use more MPI ranks than you have cores.

For ``CrayMPI`` (launched with ``srun``):

* Specify ``--hint=nomultithread`` and ``--cpu-bind=rank``.

Remark on executors
~~~~~~~~~~~~~~~~~~~

Note, that multiple serial (``Serial``) and parallel (``Pool``/``Ensemble``) executors
can be freely selected (that is, serial or parallel) for every SPUX component (``Model``, ``Likelihood``, ``Sampler``, etc.).

This freedom to use individual parallel executors of arbitrary size for every SPUX component provides a lot of flexibility,
but also leaves ample of space for computationally inefficient parallel configurations.
Hence, for large production runs, we strongly advice to take the following guidelines into consideration (decreasing in priority):

* Allocate most workers to the executors of the outer-most SPUX component(s) (e.g. ``sampler``).
* Avoid parallel executors with few workers (less than 4) - replace them with ``Serial`` executors.

SPUX will report the percentage of the number of manager cores w.r.t. the total number of all (manager and worker) cores.
If the above guidelines are not properly implemented, this fraction could be larger than 20%,
in which case SPUX will display an explicit inefficiency warning.
Such warning will be skipped for jobs that requested not more than 8 cores in total,
to filter out local debug and development runs, where parallelization efficiency is not of the highest importance.

Remark on connectors
~~~~~~~~~~~~~~~~~~~~

The default way of initializing a connector is given by

.. code-block:: python

    from spux.executors.mpi4py.connectors import utils
    connector = utils.select ('auto')

checks how many MPI ranks are available in ``MPI_COMM_WORLD`` intra-communicator
and automatically selects ``Spawn`` connector if only one rank is found (and all other workers need to be spawned.)

Since some HPC systems do not allow dynamically spawning new MPI processes,
to run SPUX in parallel on 21 cores with MPI, simply execute:

.. code-block:: console

    $ mpiexec -n 21 python -m mpi4py script_parallel.py

Note, that :code:`-n 21` MUST match the total amount of required resources (bottom right cell) reported by running
`examples/randomwalk/script_executors.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/script_executors.py>`_:
and stored in ``report/randomwalk_resources.txt``.

In this case,
more than one MPI rank is available in ``MPI_COMM_WORLD`` intra-communicator,
and hence the :code:`Split` connector is automatically selected.

Some HPC systems not only disallow dynamically spawning new MPI processes,
but also do not support modern dynamical MPI process management features such as inter-communicator creation
between two existing MPI intra-communicators using :code:`MPI_Comm_accept ()` and :code:`MPI_Comm_connect ()` methods.
In this case, you will simply need to use a legacy :code:`Legacy` connector
instead of the :code:`Split` connector.
Any such specific connector can be also specified manually either by replacing ``auto`` with ``spawn``/``split``/``legacy``
in the connector initialization, or by specifying such connector name as a command line argument to the ``script_parallel.py``, for example:

.. code-block:: console

    $ mpiexec -n 21 python -m mpi4py script_parallel.py --connector legacy

Remark on replicates
~~~~~~~~~~~~~~~~~~~~

For parallel runs with replicate datasets (e.g. ``randomwalk-replicates`` example),
the :code:`Replicates` likelihood performs guided load balancing
by evaluating the lengths of the associated datasets together and sorting likelihood evaluations,
taking into account adaptive number of particles in the ``PF`` likelihood as well, if used.
Higher priorities are assigned to the likelihoods with longer datasets and large number of particles (if applicable),
and lower priorities are assigned to the likelihoods with shorter datasets and smaller number of particles (if applicable).
If needed, one can disable such behavior by setting :code:`sort=0`
in the constructor :code:`Replicates (...)`.
We warn, however, that depending on the executor configuration,
disabling sorting (and hence reverting to non-guided load balancing)
might lead to inefficient parallelization.

Performance progress
~~~~~~~~~~~~~~~~~~~~

The performance plots of the last sample from a parallel simulation are also generated with ``plot_results.py``.
Additional highly technical parallel performance plots can be generated by executing ``plot_performance.py``,
provided that ``informative = 1`` was used in ``sampler.setup (...)``,
and provide a summarized insight into the computation and communication balance within the parallel ``PF`` resampling stages,
over the evolution of the entire sampling process.

As with the ``plot_config.py`` and ``plot_results.py`` scripts, at the end of the ``plot_performance.py`` script
all generated plots are compiled into a LaTeX report under directory ``latex``.

Parallel scaling
~~~~~~~~~~~~~~~~

The template for post-processing results from multiple independent SPUX runs
using a different cumulative amount of processor cores and generating the
strong scaling plot is available in
`examples/randomwalk/plot_scaling.py <https://gitlab.com/siam-sc/spux/tree/test/examples/randomwalk/plot_scaling.py>`_.

Profiling (parallel)
~~~~~~~~~~~~~~~~~~~~

Currently no special scripts for parallel profiling are packaged with SPUX.