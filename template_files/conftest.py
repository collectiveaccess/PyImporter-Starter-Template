import pytest
from pathlib import Path
import os
import sys

project_path = Path(__file__).resolve().parent
sys.path.append(str(project_path / 'scripts'))

os.environ['APP_ENV'] = 'testing'

@pytest.fixture(autouse=True)
def mock_env_var(monkeypatch):
    monkeypatch.setenv("PREVIEW_MODE", "False")
