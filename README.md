# Data Science Project Structure

## Directory Structure

```
|- config/
  |- config.ini
  |- local_config.ini
|- data/
  |- raw/
    ...
  |- processed/
    ...
|- logs/
  ...
|- models/
  ...
|- notebooks/
  ...
|- src/
  |- modeling/
    ...
  |- processing/
    ...
  |- scoring/
    ...
  |- utils/
    ...
  |- __init__.py
  |- main.py
|- README.md
|- requirements.txt
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
