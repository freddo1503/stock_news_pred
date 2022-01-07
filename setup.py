"""Module docstring."""
from setuptools import find_packages
from setuptools import setup

with open('requirements.txt',  encoding="utf-8") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='stock_news_pred',
      version="1.0",
      description="Project Description",
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True
      )
