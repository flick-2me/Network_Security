from setuptools import find_packages,setup
from typing import List


def get_requirements() ->List  :
    try :
        with open("requirements.txt","r") as f :
            requirements = f.readlines()
            requirements = [r.replace("/n","").strip() for r in requirements if r!=""]

            requirements.remove("-e .")
            return requirements
    except  FileNotFoundError as e :
        raise e



setup(
    name= "Network Security",
    version='0.0.1',
    author='shubham',
    author_email='rawatshubham1801@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)