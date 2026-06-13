# Thius setup.py is basically used to contains all the metadata/packaging or we can say all the information about the project is contained by setup.py file 
from setuptools import find_packages,setup
from typing import List

# Reading all the names of packages or lib from the requirements.txt and saving it in list requirements 
HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This func will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
name='mlproject',
version='0.0.1',
author_email = 'techayush009@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)