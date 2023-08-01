from setuptools import find_packages,setup
from typing import List

Const='-e .'
def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file :
          requirements=file.readlines()
          requirements=[i.replace('\n','')  for i in requirements]
    if Const in requirements :
         requirements.remove('-e .')
         
    return requirements

setup (
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Krish',
    author_email='lendalb123@gmail.com',
    install_requires=get_requirement('requirments.txt'),
    packages=find_packages()
)