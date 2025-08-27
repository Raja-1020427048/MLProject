from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
 


setup(

name='MLProject',  # Replace with your package name        
version='0.1.0',  # Replace with your package version
author='Raja',  # Replace with your name
author_email='rmd241104@gmail.com',
packages=find_packages(),  # Automatically find packages in the directory
install_requires=get_requirements('requirements.txt')

)
















