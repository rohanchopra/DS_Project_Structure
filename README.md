# Data Science Project Structure

## Directory Structure

```
├── config/                     <- All project related config files
│  ├── config.ini               <- Configuration for the testing/production system
│  └── local_config.ini         <- Configuration for local development system
├── data/                       <- All project related data files
│  ├── external/                <- Data from third party sources
│  ├── raw/                     <- The original, immutable data dump
│  └── processed/               <- The final data sets for modeling
├── logs/                       <- Project logs
├── models/                     <- Trained models, predictions, and summaries
├── notebooks/                  <- Jupyter notebooks
├── references                  <- Data dictionaries, and all other explanatory material
├── src/                        <- Source code for the project
│  ├── modeling/                <- Scripts to train the modelS
│  ├── processing/              <- Scripts to process the data to create the final dataset
│  ├── scoring/                 <- Scripts to score the models
│  ├── utils/                   <- Scripts for utility functions
│    ├── custom_functions.py    <- Script for custom functions for the project
│    └── utils.py               <- Script for common utility functions
│  ├── __init__.py              <- Makes src a Python module
│  └── main.py                  <- Project's entry script
├── README.md                   <- The top-level README for developers using this project
└── requirements.txt            <- The requirements file for reproducing the environment
```

Populate the requirements.txt using

Python PIP
```
pip freeze > requirements.txt
```

Conda
```
conda list -e > requirements.txt
```

## Naming Conventions

### Jupyter Notebooks
```
yyyyMMdd-developer_initials-description_of_notebook.ipynb
```

### Log Files
```
yyyy-MM-ddTHHmm.log
```

### Model Files
```
yyyyMMdd-description_of_model.h5
```
