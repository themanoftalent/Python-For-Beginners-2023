
.. _contributing:

============
Contributing
============

| The source code is available at the GitLab repository: https://gitlab.com/siam-sc/spux.
| Contributions are welcome, and they are greatly appreciated!
| Every little bit helps, and credit will always be given.

The SPUX'onic way
-----------------

When contributing, please always make an effort to adhere the SPUX'onic coding style and ethics:

* think (at least) twice about proper variable names:
    * avoid abbreviations and slang,
    * prioritize descriptive single-word variables to lengthy "sentence"-variables,
* use docstrings for each class and method you implement,
* place technical methods into ``spux.utils`` or ``spux.io``,
* always use the ``verbosity`` level filter for any (carefully formatted, of course) output to console,
* always clean up (remove debug code and unnecessary comments) before merging to test branch.

Types of contributions
----------------------

You can contribute in many ways, listed in the following paragraphs.

Report bugs
~~~~~~~~~~~

Report bugs at https://gitlab.com/siam-sc/spux/issues

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix bugs
~~~~~~~~

Look through the GitLab issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement features
~~~~~~~~~~~~~~~~~~

Look through the GitLab issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write documentation
~~~~~~~~~~~~~~~~~~~

SPUX could always benefit from more documentation, whether as part of the
official spux docs, in docstrings, or even on the web in blog posts,
articles, and such.

To contribute to the official spux docs, checkout the the spux repository
and look through all the files listed in the ``MANIFEST.in`` file.
The auto-generated documentation from all these files is placed under the ``docs/`` directory,
where static files such as plots, tables, etc. are located under ``docs/_static`` (please respect the current directory structure).
When adding your new contributions to the documentation, please follow the current style and make sure that:

* Code snippet uses the code block (instead of a standard paragraph text).
* Code snippet has no remaining programmer comments, notes, or legacy code.
* The line lengths of the code snippet do not protrude beyond the right margin of the paragraph.

Submit feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://gitlab.com/siam-sc/spux/issues

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Contributions are very welcome and will make the framework better for you and other users.

Get started!
------------

Ready to contribute? Here's how to set up `spux` for local development.

1. Fork the `spux` repo on GitLab.
2. Clone your fork locally::

    $ git clone git@gitlab.com:siam-sc/spux.git
    $ cd spux/

3. (Optional) Install virtualenv and virtualenvwrapper (and source paths, if needed)::

    $ pip install virtualenvwrapper

4. (Optional) Install your local copy into a virtualenv::

    $ mkvirtualenv spux
    $ workon spux

5. Set up your fork for local development (use `--user` at the end if needed)::

    $ pip install -r requirements_dev.txt
    $ python setup.py develop

6. Create a branch for local development (name it dev_username for private development branch)::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

   You can run tests within your environment::

    $ flake8 spux tests examples
    $ pytest -m "not mpi" tests
    $ mpiexec -n 1 --oversubscribe pytest -m "mpi" tests

   Or, alternatively (a slower approach), using tox to include testing with Python and MPI versions::

    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

7. Commit your changes and push your branch to GitLab::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

8. Make sure all tests pass in the `GitLab-CI <https://gitlab.com/siam-sc/spux/pipelines>`_ as well.

9. Submit a merge request (e.g. to the "test" branch) through the GitLab website.

10. Maintainers: review merge request and activate "Merge automatically when pipeline succeeds".

Merge requests
--------------

Before you submit a merge request, check that it meets these guidelines:

1. The merge request should include tests.
2. If the merge request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The merge request should work for Python 3.7.

Tips
----

* To run only non-MPI tests::

  $ pytest -m "not mpi" tests

  or only short module tests, excluding long integration tests::

  $ pytest -m "not mpi and not integration" tests

  or only long integration tests using MPI::

  $ pytest -m "mpi and integration" tests

* To run tests from a single file::

  $ pytest tests/test_spux.py

  or a single test function::

  $ pytest tests/test_spux.py::test_imports

* To add dependency, edit appropriate ``*requirements`` variable in the
  ``setup.py`` file and re-run::

  $ python setup.py develop

  Check if this requirement should be also included in the ``requirements_dev.txt`` file.

Deploying
---------

A reminder for the maintainers on how to deploy.

* Make sure all issues on GitLab associated with this release milestone are:
    * either fixed and closed with changes merged into the ``test`` branch,
    * or re-assigned to future release milestones.
* Review documentation and make sure all examples and statements are up to date:
    * run ``make docs_html`` in the terminal and check generated html pages carefully,
    * check all source code snippets that use specific line numbers and fix them,
    * check if additional examples, results, or publications should be added for the gallery,
    * check if additional contributions should be added in the credits.
* Verify all filenames listed in :code:`MANIFEST.in`, including all needed package directories.
* Merge the release version of the code to the :code:`release` branch, make sure all tests pass.
* Make sure all your changes are COMMITTED (!), including:
    * an entry in ``HISTORY.rst``,
    * (optionally) the development status change in ``setup.py`` (see `here <https://pypi.org/classifiers/>`_ for options).
* Make sure you have ``texlive-science``,  ``latexmk``, and ``image-magick`` installed for PDF documentation.
* Make sure your working branch is :code:`release`.

Then run in the terminal::

    $ pip install -U -r requirements_rtd.txt
    $ make docs
    $ make clean
    $ bumpversion patch # possible: major / minor / patch; might need --allow-dirty
    $ git push
    $ git push --tags

Afterwards, GitLab-CI will automatically deploy the release to PyPI and ReadTheDocs if `tests <https://gitlab.com/siam-sc/spux/pipelines>`_ pass.
Then merge the :code:`release` branch into the :code:`master` and :code:`test` branches.
