# PyImporter Project

This project was creating using the [PyImporter Starter Template](https://github.com/collectiveaccess/PyImporter-Starter-Template).


## Installation

1. Install the required packages. You can use the virtual environment / package manager of your choice.

```bash
pip install -r requirements.txt
```

2. Setup environmental variables.

We are using [python-dotenv](https://github.com/theskumar/python-dotenv) to handle environmental variables. Copy `.env_example`, rename to `.env`, and fill in the envars.

Read [PyImporter environmental variables](https://github.com/collectiveaccess/PyImporter/wiki/Installing-PyImporter#pyimporter-environmental-variables) for more info the required envars.

3. Read the [PyImporter docs](https://github.com/collectiveaccess/PyImporter/wiki) for  instructions on how to use PyImporter. Examine the demo import script ([./script/demo.py](https://github.com/collectiveaccess/PyImporter-Starter-Template/blob/main/template_files/scripts/demo.py)) and data ([./data/demo.csv](https://github.com/collectiveaccess/PyImporter-Starter-Template/blob/main/template_files/data/demo.csv)) to see an example of how to use PyImporter.

4. Copy [./scripts/template.py](https://github.com/collectiveaccess/PyImporter-Starter-Template/blob/main/template_files/scripts/template.py) to serve as a starting point for your import scripts.



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

To update the PyImporter submodule:

```
git submodule update --remote PyImporter
```
