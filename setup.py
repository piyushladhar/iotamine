from setuptools import setup, find_packages

setup(
    name="iotamine",
    version="0.1",
    description="Iotamine Cloud API SDK",
    author="Piyush Ladhar",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires='>=3.6',
)
