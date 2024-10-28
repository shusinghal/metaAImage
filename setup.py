from setuptools import setup, find_packages

setup(
    name="metaAI",
    version="0.1",
    packages=find_packages(),
    description="A simple greeting library",
    author="Shubham Singhal",
    author_email="masti.shyam@gmail.com",
    install_requires=[
        "selenium",
        "requests",
        "chromedriver"
    ],
)