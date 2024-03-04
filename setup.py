from setuptools import find_packages,setup
from typing import List

HYPEN_DOT = '-e .'
def get_requirements(file_path : str) -> List[str]:
    """
    Getting the requirements file from the path
    
    """
    req = []
    with open(file_path) as obj:
        req = obj.readlines()
        req = [r.replace("\n","") for r in req]

    if HYPEN_DOT in req:
        req.remove(HYPEN_DOT)

    return req

setup (
name='MLProject',
version= '0.0.1',
author='Abhishek Singh',
author_email='abhisheksinghbiet@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)