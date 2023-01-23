Template Data Science Project Repository
========================

## Python data science project structure
This template is meant for data science projects, e.g., where you explore data, 
train models, run experiments, optimize hyperparameters, that kind of thing.


## Not suited for minimalistic Python packages
If you're not doing a data science project, but just want a quick and dirty file structure for packaging your code as a
Python package, I suggest you use my other template: 
https://github.com/hviidhenrik/my-sample-package-structure


### Usage

1. Create a new repo on GitHub using this as a template.
2. Clone your new repo locally.
3. Write your code!

##### Note:

The template comes predefined with some helpful path definitions and a correctness test of these.
See them in: `src/config/definitions.py`

### Formatting
The files were formatted using isort and black. I recommend running isort to sort imports correctly 
and then format code nicely using black with a line length of 120.

    isort .
    black . -l 120

A template `.pre-commit-config.yaml` file is available. First install pre-commit 

    pip install pre-commit

Then run it by using 

    pre-commit run --all-files

Project Organization
------------
    ├── config             <- configuration files for path definitions and model config file
    ├── data               <- for storing data files
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── experiments        <- Scripts for running experiments on the data
    ├── models             <- Trained, serialized models
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── tests              <- Units tests and test fixtures - I recommend using pytest
        └── conftest.py    <- Constants, dataframes and pytest fixtures go in here
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pipreqs .`
    │
    ├── .pre-commit-config.yaml  <- template pre-commit configuration
    ├── pyproject.toml           <- config file for various formatters including black 
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── core               <- Source code for use in this project. The name you'll use to import stuff
        ├── __init__.py    <- Makes core a Python module
        └── models         <- Scripts to train models and then use trained models to make
            │                 predictions
            ├── predict_model.py
            └── train_model.py




--------

This template is inspired from the no-less awesome Cookiecutter template 
found at: https://github.com/drivendata/cookiecutter-data-science