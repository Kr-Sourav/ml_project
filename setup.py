from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements.
    """
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [package.replace('\n','') for package in requirements]
        
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = "ml_project",
    version ="0.0.1",
    author = "Sourav_Kumar",
    author_email="srv2503@gmail.com",
    packages = find_packages(),
    requires= get_requirements('requirements.txt')
)