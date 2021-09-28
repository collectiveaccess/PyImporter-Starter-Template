import subprocess
from pathlib import Path

base_path = Path(__file__).resolve().parent


def lint():
    _exec(f"black {Path(base_path, 'pyimporter_create.py')}")
    _exec(f"black {Path(base_path, 'template_files', 'scripts')}")
    _exec(f"black {Path(base_path, 'template_files', 'tests')}")
    _exec(f"flake8 {Path(base_path, 'pyimporter_create.py')}")
    _exec(f"flake8 {Path(base_path, 'template_files','scripts')}")
    _exec(f"flake8 {Path(base_path, 'template_files','tests')}")


def _exec(command):
    process = subprocess.Popen(command.split())
    output, error = process.communicate()


if __name__ == "__main__":
    lint()
