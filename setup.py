from setuptools import setup, find_packages

with open("requirements.txt") as f:
  requirements = f.read().splitlines()

setup(
  name="MLOPS-PROJECT-1",
  version="0.1",
  author="Juan Palmeros",
  author_email= "palmerosjuanfrancisco@gmail.com",
  packages=find_packages(),
  install_requires = requirements,
  description="MLOPS full simple pipeline for hotel reservation behaviour prediction",
  long_description="MLOPS full simple pipeline for hotel reservation behaviour prediction: churn, targeted campaigns, etc."
)
