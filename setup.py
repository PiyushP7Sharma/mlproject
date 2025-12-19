from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''This function will return the list of requirements''' 
    requirements = []

    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements if req.strip()]
    
    return requirements




setup(
    name="ML_Project",
    version="0.0.1", 
    author="Piyush Sharma",
    author_email="piyushs0709@gmail.com",
    packages=find_packages(),
    install_requires=[get_requirements("requirements.txt")],
)