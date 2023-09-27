from distutils.core import setup

from setuptools import find_packages


with open("requirements.txt") as f:
    required_packages = f.read().splitlines()


setup(
    name="{{ cookiecutter.project_name }}",
    version="0.1.0",
    description="Feature extractors for OpaMind Recommender System",
    author='{{ cookiecutter.author_name }}',
    packages=find_packages(exclude=["tests", "test_data"]),
    install_requires=required_packages,
    include_package_data=True,
)