from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirement(file_path:str)->List[str]:
    '''
    this function returns a list of requirements
    '''
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name="Project-1",
    version="0.0.1",
    author="sumitkudale",
    author_email="sumitkudale@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)
