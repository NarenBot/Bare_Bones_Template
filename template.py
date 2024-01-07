import os
import logging
from pathlib import Path

logging.basicConfig(
    filename="temp.log",  # Upon initiating the project, remove the temporary log file.
    level=logging.INFO,
    format="[%(asctime)s | %(levelname)s | %(message)s]",
)


while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/predict_pipeline.py",
    "src/pipeline/train_pipeline.py",
    "tests/__init__.py",
    "tests/integration/__init__.py",
    "tests/integration/test_integration.py",
    "tests/unit/__init__.py",
    "tests/unit/test_unit.py",
    "requirements.txt",
    "setup.py",
    "init_setup.sh",
    # Additional Config Files:
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file:
            logging.info(f"Creating a new file: {filename} at path: {filepath}")

    else:
        logging.info(f"File already exists at: {filepath}")
