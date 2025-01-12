# Filename: setup.py
from setuptools import setup, find_packages

import dabdemo

setup(
  name = "dabdemo",
  version = dabdemo.__version__,
  author = dabdemo.__author__,
  url = "https://https://github.com/EfrainSO/databricksCICD",
  author_email = "efrain@gmail.com",
  description = "Un paquete de ejemplo para demostrar Databricks y DevOps",
  packages = find_packages(include = ["dabdemo"]),
  entry_points={"group_1": "run=dabdemo.__main__:main"},
  install_requires = ["setuptools"]
)
