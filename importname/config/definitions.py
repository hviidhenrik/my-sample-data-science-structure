import os
from pathlib import Path

PATH_CONFIG = Path(__file__).parent
PATH_SRC = PATH_CONFIG.parent  # optionally, change this to reflect the name of the 'importname' directory
PATH_PROJECT_ROOT = PATH_SRC.parent
PATH_DATA = PATH_PROJECT_ROOT / "data"
PATH_DATA_RAW = PATH_PROJECT_ROOT / "data" / "raw"
PATH_DATA_INTERIM = PATH_PROJECT_ROOT / "data" / "interim"
PATH_DATA_PROCESSED = PATH_PROJECT_ROOT / "data" / "processed"
PATH_SAVED_MODELS = PATH_PROJECT_ROOT / "models"
PATH_NOTEBOOKS = PATH_PROJECT_ROOT / "notebooks"
PATH_REPORTS = PATH_PROJECT_ROOT / "reports"
PATH_TESTS = PATH_PROJECT_ROOT / "tests"

# if data outside the project, point an environment variable "DATASETS" to the dir and uncomment the line below
# PATH_DATA = os.environ["DATASETS"]


if __name__ == "__main__":
    try:
        print(PATH_CONFIG)
        print(PATH_SRC)
        print(PATH_PROJECT_ROOT)
        print(PATH_DATA)
        print(PATH_DATA_RAW)
        print(PATH_DATA_INTERIM)
        print(PATH_DATA_PROCESSED)
        print(PATH_SAVED_MODELS)
        print(PATH_NOTEBOOKS)
        print(PATH_REPORTS)
        print(PATH_TESTS)
    except FileNotFoundError:
        print("\nOne or more paths not configured properly - look in definitions.py in the config folder")
    else:
        print("\nPaths configured correctly!")
