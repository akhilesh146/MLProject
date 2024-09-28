from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str)-> List[str]:
    """
    This function is used to read the requirements from the given file.
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','')  for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements



setup(
name='mlproject',
version='0.0.1',
author='Akhilesh',
author_email='akhileshsamarth9@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)