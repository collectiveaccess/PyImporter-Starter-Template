# PyImporter-Starter-Template
Starter template for [PyImporter](https://github.com/collectiveaccess/PyImporter),
the CollectiveAccess Python-based importer.

This starter template:
- creates a new repo with a directory structure and environmental variables to use PyImporter.
- downloads the latest version of PyImporter as a git submodule
- includes a [demo import script](https://github.com/collectiveaccess/PyImporter-Starter-Template/blob/main/template_files/scripts/demo.py) and [demo data](https://github.com/collectiveaccess/PyImporter-Starter-Template/blob/main/template_files/data/demo.csv) to show how to use Pyimporter
- includes a [template](https://github.com/collectiveaccess/PyImporter-Starter-Template/blob/main/template_files/scripts/template.py) that you can use to create your own import script
- sets up pytest for testing
- sets up flake8 and black for code linting

## Installation part 1

1. Clone this repo

2. Run the `pyimporter_create.py` to create a new directory, download the latest version of PyImporter, and create the first commit.

```
python pyimporter_create.py
```

You can use absolute or relative paths when the prompt asks for a path for the new directory.

# Generated files and directories

`pyimporter_create.py` creates a new directory that you can use to import your data files.

## Installation part 2

1. Install the required packages for the directory created by `pyimporter_create.py`. You can use the virtual environment / package manager of your choice.

```bash
cd path/to/generated/directory
pip install -r requirements.txt
```

2. Setup environmental variables.

We are using [python-dotenv](https://github.com/theskumar/python-dotenv) to handle environmental variables. Copy `.env_example`, rename to `.env`, and fill in the envars.

Read [PyImporter environmental variables](https://github.com/collectiveaccess/PyImporter/wiki/Installing-PyImporter#pyimporter-environmental-variables) for more info the required envars.

3. Read the [PyImporter docs](https://github.com/collectiveaccess/PyImporter/wiki) for  instructions on how to use PyImporter. Examine the demo import script ([./scripts/demo.py](https://github.com/collectiveaccess/PyImporter-Starter-Template/blob/main/template_files/scripts/demo.py)) and data ([./data/demo.csv](https://github.com/collectiveaccess/PyImporter-Starter-Template/blob/main/template_files/data/demo.csv)) to see an example of how to use PyImporter.

4. Copy [./scripts/template.py](https://github.com/collectiveaccess/PyImporter-Starter-Template/blob/main/template_files/scripts/template.py) to serve as a starting point for your import scripts.


## Directories/Files

These are the files and directories generated by `pyimporter_create.py`.

* `/data` - Demo data to show how to use PyImporter. For your project, you can store the data files anywhere you want.
* `/logs` - Log files.
* `/PyImporter` - Git submodule for PyImporter.
* `/scripts` - Your scripts that will use PyImporter to import data. You should create a separate import script for each CollectiveAccess table and type.
  * `/bulk_import` - Bash script to run all the import scripts.
  * `config.py` - Setup paths and envars for `/scripts`.
  * `demo.py` - Demo import script to show how to use PyImporter.
  * `template.py` - A basic template you can copy to create your import scripts.
* `/tests` - Optional tests for `/scripts`. We are using [pytest](pytest.org).
* `.env_example` - Example .env file
* `.gitignore`
* `.gitmodules`
* `conftest.py` - Configuration for pytest.
* `linter.py` - Script to lint `/scripts` and `/tests` using [black](https://github.com/psf/black) and [flake8](https://flake8.pycqa.org).
* `requirements.txt` - List of packages required by the starter template and PyImporter.
* `secrets.json` - File created by PyImporter to store JWT tokens.
* `setup.cfg` - Configuration for the linters.


## Testing

Run tests using pytest.

```bash
pytest
```

Run linter (flake8) and code formatter (black).

```bash
python linter.py
```

## Updating PyImporter

To update the PyImporter submodule:

```
git submodule update --remote PyImporter
```
