Sample Module Repository
========================

## Python data science project structure
This template is meant for data science projects, e.g., where you explore data, train models, 
optimize hyperparameters that kind of thing.


## Not suited for minimalistic Python packages
If you're not doing a data science project, but just want a quick and dirty file structure for packaging your code as a
Python package, I suggest you use my other template: 
https://github.com/hviidhenrik/my-sample-package-structure


### Usage

1. Create a new repo on GitHub using this as a template.
2. Clone your new repo locally.
3. Change the name of the 'importname' directory to match your project.*
   Also change this name in the import in importname/config/\_\_init__.py and in setup.py
4. Write your code!

*This directory is sometimes called simply `src`, but this could cause problems if you have other custom-built packages
as this directory will house your source code and thus be used in imports in other projects.

##### Note:

The template comes predefined with some helpful path definitions. See them in: `importname/config/definitions.py`

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
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
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pipreqs .`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so importname can be imported
    ├── importname         <- Source code for use in this project. The name you'll use to import stuff
        ├── __init__.py    <- Makes importname a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py



--------

This template is adapted from the Cookiecutter template found at: 
https://github.com/drivendata/cookiecutter-data-science