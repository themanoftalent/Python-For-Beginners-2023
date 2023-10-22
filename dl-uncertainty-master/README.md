# Uncertainty estimation methods in deep learning for biomedical imaging

This repository contains (or will contain) a collection of notebooks demonstrating various approaches to estimate uncertainty in biomedical image application of deep learning. 

## Author

**Walter de Back**  
Institute for Medical Informatics and Biometry  
"Carl Gustav Carus" Faculty of Medicine, TU Dresden    
& Center for High Performance Computing, TU Dresden

## Installation 

- Download and install miniconda for python 3.x from

    https://conda.io/miniconda.html

- Clone this git repository

```bash
git clone git@gitlab.com:wdeback/dl-uncertainty.git
```

or

```bash
git clone https://wdeback@gitlab.com/wdeback/dl-IMS.git
```

- Create python 3.5 environment with required packages (keras, scikit-learn, tensorflow, etc.)

```bash
cd dl-uncertainty
conda env create --file environment.yml
```

This will install all dependencies within a virtual environment called 'dl'.

### Start notebook

- Activate environment

```bash
source activate dl
```

- Start jupyter lab 

```bash
jupyter lab
```

- Browse to folder `notebooks` and select notebook to start

### Notebook usage

- Execute cell with `Shift+Enter`
- [Quick start with jupyter notebook](http://cs231n.github.io/ipython-tutorial/)
- [Notebook 
basics](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb#Overview-of-the-Notebook-UI)


