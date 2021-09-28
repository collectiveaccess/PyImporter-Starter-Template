# PyImporter Project

This project was creating using the [PyImporter Starter Template](https://github.com/collectiveaccess/PyImporter-Starter-Template).

## Setup

1. Install the required packages. You can use the virtual environment / package manager of your choice.

```bash
pip install -r requirements.txt
```

2. Setup environmental variables.

We are using [python-dotenv](https://github.com/theskumar/python-dotenv) to handle environmental variables. Copy `.env_example`, rename to `.env`, and fill in the envars.


- API_USERNAME: username for CollectiveAccess API
- API_PASSWORD: password for CollectiveAccess API
- API_URL: url for CollectiveAccess API
- JWT_AUDIENCE: audience for CollectiveAccess JWT
- JWT_ISSUER: issuer for CollectiveAccess JWT
- DATA_DIR: path for the data files
- BASE_DIR: path to this directory
- LOCALE: language settings for CollectiveAccess

## Directories/Files


* `/data` - Demo data to show how to use PyImporter. You can store the data files anywhere you want.
* `/logs` - Log files.
* `/PyImporter` - Git submodule for PyImporter.
* `/scripts` - Your scripts that will use PyImporter to import data. You should create a separate import script for each CollectiveAccess table and type.
  * `/bulk_import` - Bash script to run all the import scripts.
  * `config.py` - Setup paths and envars for `/scripts`.
  * `demo.py` - Demo import script to show how to use PyImporter.
  * `template.py` - A basic template to create your import scripts.
* `/tests` - Optional tests for `/scripts`. We are using [pytest](pytest.org).
* `.env` - File to store environmental variables.
* `.env_example` - Example file to fill out `.env`.
* `conftest.py` - Configuration for pytest.
* `linter.py` - Script to lint `/scripts` and `/tests` using [black](https://github.com/psf/black) and [flake8](https://flake8.pycqa.org).
* `reqyirements.txt` - List of packages required by the starter kit and PyImporter.
* `secrets.json` - File created by PyImporter to store JWT tokens.
* `setup.cfg` - Configuration.


## Run Scripts

We are using [Fire](https://github.com/google/python-fire) to run the import scripts.

```bash
python ./scripts/<file>.py <method>
```

Here are some prebuilt methods. You can add you own custom methods to each import script.

```bash
# perform basic data validation on the data files
python scripts/demo.py validation

# preview the graphql queries for the first metadata, first row of data
python scripts/demo.py preview_create 1

# send queries to api to create records for the first metadata
python scripts/demo.py create_records 1

# delete records for table, type, and id/idno.
python scripts/demo.py delete_records

# delete all records for table and type
python scripts/demo.py truncate_table

# delete all relationships for the second metadata
python scripts/demo.py delete_relationships 2
```

## Testing

Run tests. We are using [pytest](https://pytest.org) for testing.

```bash
pytest
```

Run linter (flake8) and code formatter (Black).

```bash
python linter.py
```

## Updating PyImporter

To update the PyImporter submodule.

```
git submodule update --remote PyImporter
```
