from setuptools import setup, find_packages
import os


def get_requirements(file_path):
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


PROJECT_NAME = "Bare_Bones"
VERSION = "0.0.1"
DESCRIPTION = "The basic structure that ensures a systematic and reproducible approach to data science projects."
AUTHOR = "NarenBot"
AUTHOR_EMAIL = "narendas10@gmail.com"

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
)
