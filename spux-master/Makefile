VERSION=$(shell grep "^\s*version" setup.py | sed -e 's/[^\.0-9]//g')
PIP?=pip3
PYTHON?=python3
DEBUG?=0
DISTUTILS?=$(PYTHON) setup.py
.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define OPEN_PYSCRIPT
import os, subprocess, sys

filepath = sys.argv[1]
if sys.platform.startswith('darwin'): # macOS
    subprocess.call(('open', filepath))
elif os.name == 'posix': # Linux etc.
    subprocess.call(('xdg-open', filepath))
elif os.name == 'nt': # Windows
    os.startfile(filepath)
endef
export OPEN_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := $(PYTHON) -c "$$BROWSER_PYSCRIPT"
OPEN := $(PYTHON) -c "$$OPEN_PYSCRIPT"

help:
	@$(PYTHON) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

version: ## current package version
	@echo $(VERSION)

clean: clean-docs clean-build clean-pyc clean-test ## remove all docs, build, test, coverage and Python artifacts

clean-docs: ## remove docs artifacts
	rm -fr docs/_build/

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 spux tests

test: ## run tests quickly with the default Python
	$(DISTUTILS) test

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source spux -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs_api:
	rm -f docs/spux*.rst
	sphinx-apidoc -M -o docs/ spux
	# fix submodules inlined headings: change "-" underline to "~"
	for f in $$(ls -1 docs/spux*.rst); do for n in $$(grep -n "spux.* module" "$${f}" | cut -d : -f 1); do sed -i.tmp "$$((n + 1))s/-/~/g" "$${f}"; done done
	rm -f docs/spux*.rst.tmp

docs: docs_api ## generate Sphinx HTML and PDF documentation, including API docs
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(MAKE) -C docs latexpdf
	$(BROWSER) docs/_build/html/index.html
	$(OPEN) docs/_build/latex/spux.pdf

docs_html: docs_api ## generate Sphinx HTML documentation, including API docs
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	$(DISTUTILS) sdist
	$(DISTUTILS) bdist_wheel
	ls -l dist

install: clean ## install the package in edit mode to the active Python's site-packages
	$(PIP) install -e .

uninstall:
	-$(PIP) uninstall -y 'spux==$(VERSION)'
