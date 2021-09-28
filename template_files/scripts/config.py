import sys
from pathlib import Path
from dotenv import load_dotenv

project_path = Path(__file__).resolve().parent.parent
sys.path.append(str(project_path))

load_dotenv()
