from setuptools import setup, find_packages
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list() -> List[str]:
    """
    This function returns a list of requirements
    excluding '-e .'
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirements = [
            line.strip()
            for line in requirement_file
            if line.strip() != "-e ."
        ]
    return requirements


setup(
    name="housing-predictor",
    version="0.0.1",
    author="kamalesh yadav",
    description="This is the first FSDS Nov batch Machine learning project",
    packages=find_packages(),
    install_requires=get_requirements_list(),
)
