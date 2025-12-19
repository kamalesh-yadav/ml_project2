from setuptools import setup
from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"




def get_requirements_list()->List[str]:
    """
    Description:This function is going to return the list of requirement mention in the requrement.txt
    
    return This function is going to return a list of libraries mention in 
    requirement.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
       return requirement_file.readlines()
setup(
    Name="Housing - Predictor",
    version="0.0.1",
    author="kamalesh yadav",
    description="This is the first FSDS Nov batch Machine learning project",
    packages=["housing"],
    install_requires=get_requirements_list()
)