from setuptools import find_packages, setup
from typing import List 




requirements=[]
def get_requirements(file_path: str) -> List[str]:
    hyphen_e_dot= "-e ."
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n",'') for req in requirements]
    
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements





setup(
    name="MLProject",
    version="0.0.1",
    author="Jawad Parkar",
    author_email="trueajparker@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)


