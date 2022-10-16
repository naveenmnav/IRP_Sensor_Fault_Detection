### If you need to share this project  outside, we need to create this file
import os
from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:

    """
        This function is used to list the requirements
        This reads the requiremnts.txt and append each requirement here

    """
    with open('requirements.txt') as file:
        required = file.read().splitlines()
    req_list: List[str] = required
    print("Installed Dependencies : " ,  req_list )
    return req_list

setup(

    name="Sensor-Fault-Project",
    version="0.0.1",
    author="naveenmnav",
    author_email="thenaveenm@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)